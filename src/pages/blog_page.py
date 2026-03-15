import re

from playwright.sync_api import Locator, expect

from src.pages.base_page import BasePage


class BlogPage(BasePage):
    blog_header_css = "main h1, article h1, h1"
    gif_xpath = "//img[contains(@src, '.gif') or contains(@src, 'giphy')]"
    cat_gif_css = "img[src*='.gif'], img[src*='giphy'], img[alt*='cat' i], img[alt*='kot' i]"
    rebranding_story_path = "/blog/its-time-for-widelab-rebranding-and-story"

    def open_blog(self) -> None:
        self.open("/blog")

    def open_known_gif_article(self) -> None:
        self.open(self.rebranding_story_path)

    def heading(self) -> Locator:
        return self.locator(self.blog_header_css).first

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
