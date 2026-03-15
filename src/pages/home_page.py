import re

from playwright.sync_api import Locator, expect

from src.pages.base_page import BasePage


class HomePage(BasePage):
    blog_link_css = "a[href*='blog']"
    hero_heading_xpath = "(//h1 | //h2)[1]"
    nav_relative_xpath = (
        ".//a[contains(translate(normalize-space(.),"
        "'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'BLOG')]"
    )

    def open_home(self) -> None:
        self.open("")

    def blog_link(self) -> Locator:
        return self.locator(self.blog_link_css).first

    def hero_heading(self) -> Locator:
        return self.xpath(self.hero_heading_xpath).first

    def blog_link_in_nav_relative(self) -> Locator:
        nav = self.locator("header nav, nav").first
        return nav.locator(f"xpath={self.nav_relative_xpath}").first

    def go_to_blog(self) -> None:
        relative_blog_link = self.blog_link_in_nav_relative()
        if relative_blog_link.count() > 0:
            relative_blog_link.click()
        else:
            self.blog_link().click()

    def expect_loaded(self) -> None:
        expect(self.page).to_have_url(re.compile(r"^https://(www\.)?widelab\.co/?$"))
