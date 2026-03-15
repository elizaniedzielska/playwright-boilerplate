import re

import pytest
from playwright.sync_api import expect

from src.pages.home_page import HomePage


@pytest.mark.smoke
def test_homepage_loads_with_expected_url_and_title(home_page: HomePage) -> None:
    home_page.open_home()
    home_page.expect_loaded()
    expect(home_page.page).to_have_title(re.compile(r".+"))


@pytest.mark.smoke
def test_homepage_has_visible_heading(home_page: HomePage) -> None:
    home_page.open_home()
    expect(home_page.hero_heading()).to_be_visible()


@pytest.mark.parametrize("path", ["", "/blog"])
def test_basic_paths_are_reachable(home_page: HomePage, path: str) -> None:
    home_page.open(path)
    expect(home_page.page).to_have_title(re.compile(r".+"))
