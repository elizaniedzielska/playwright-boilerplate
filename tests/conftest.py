from __future__ import annotations

import os
from pathlib import Path

import pytest
from playwright.sync_api import Page

from src.pages.blog_page import BlogPage
from src.pages.home_page import HomePage


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "smoke: Quick smoke checks for critical flows")
    config.addinivalue_line("markers", "blog: Tests focused on blog page behavior")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "https://widelab.co")


@pytest.fixture(autouse=True)
def screenshot_on_failure(page: Page, request: pytest.FixtureRequest) -> None:
    yield
    report = getattr(request.node, "rep_call", None)
    if report and report.failed:
        screenshots_dir = Path("artifacts") / "screenshots"
        screenshots_dir.mkdir(parents=True, exist_ok=True)
        file_name = f"{request.node.name}.png".replace("/", "_").replace("\\", "_")
        page.screenshot(path=str(screenshots_dir / file_name), full_page=True)


@pytest.fixture()
def home_page(page: Page, base_url: str) -> HomePage:
    return HomePage(page=page, base_url=base_url)


@pytest.fixture()
def blog_page(page: Page, base_url: str) -> BlogPage:
    return BlogPage(page=page, base_url=base_url)
