import re
import time

from playwright.sync_api import Locator, expect

from src.pages.base_page import BasePage


class BlogPage(BasePage):
    blog_header_css = "main h1, article h1, h1"
    hero_cat_video_css = "video#heroVideoSpan:visible"
    gif_xpath = "//img[contains(@src, '.gif') or contains(@src, 'giphy')]"
    cat_gif_css = "img[src*='.gif'], img[src*='giphy'], img[alt*='cat' i], img[alt*='kot' i]"

    def open_blog(self) -> None:
        self.open("/blog")

    def heading(self) -> Locator:
        return self.locator(self.blog_header_css).first

    def hero_cat_video(self) -> Locator:
        return self.locator(self.hero_cat_video_css).first

    def wait_for_hero_media_source(self, timeout_ms: int = 8000) -> str:
        video = self.hero_cat_video()
        assert video.count() > 0, "Expected visible blog hero video."

        deadline = time.monotonic() + (timeout_ms / 1000)
        while time.monotonic() < deadline:
            source = (
                video.get_attribute("src")
                or video.get_attribute("data-src")
                or video.evaluate("el => el.currentSrc || ''")
            )
            if source:
                return source

            source_tag = video.locator("source").first
            if source_tag.count() > 0:
                source = source_tag.get_attribute("src") or source_tag.get_attribute("data-src")
                if source:
                    return source

            self.page.wait_for_timeout(250)

        raise AssertionError("Expected blog hero video source to be available.")

    def gif_image(self) -> Locator:
        visible_gif = self.locator("img[src*='.gif']:visible, img[src*='giphy']:visible").first
        if visible_gif.count() > 0:
            return visible_gif

        xpath_gif = self.xpath(self.gif_xpath).first
        if xpath_gif.count() > 0:
            return xpath_gif
        return self.locator(self.cat_gif_css).first

    def expect_blog_loaded(self) -> None:
        expect(self.page).to_have_url(re.compile(r"^https://(www\.)?widelab\.co/blog/?$"))
