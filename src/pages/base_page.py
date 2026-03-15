from __future__ import annotations

import re

from playwright.sync_api import Locator, Page, expect


class BasePage:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")

    def open(self, path: str = "") -> None:
        normalized_path = path if path.startswith("/") or not path else f"/{path}"
        self.page.goto(f"{self.base_url}{normalized_path}")

    def locator(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def xpath(self, selector: str) -> Locator:
        return self.page.locator(f"xpath={selector}")

    def click(self, selector: str) -> None:
        self.page.locator(selector).click()

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).first.is_visible()

    def get_attribute(self, selector: str, attribute: str) -> str | None:
        return self.page.locator(selector).first.get_attribute(attribute)

    def expect_url_contains(self, value: str) -> None:
        expect(self.page).to_have_url(re.compile(re.escape(value)))
