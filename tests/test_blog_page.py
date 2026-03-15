import pytest
from playwright.sync_api import expect

from src.pages.blog_page import BlogPage
from src.pages.home_page import HomePage


@pytest.mark.blog
@pytest.mark.smoke
def test_navigation_to_blog_from_home(home_page: HomePage, blog_page: BlogPage) -> None:
    home_page.open_home()
    home_page.go_to_blog()
    blog_page.expect_blog_loaded()


@pytest.mark.blog
def test_blog_contains_cat_gif(blog_page: BlogPage) -> None:
    blog_page.open_known_gif_article()
    gif = blog_page.gif_image()
    assert gif.count() > 0, "Expected at least one GIF image on the blog subpage."

    source = gif.get_attribute("src") or ""
    assert ".gif" in source.lower() or "giphy" in source.lower()
