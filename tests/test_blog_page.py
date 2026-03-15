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
    blog_page.open_blog()
    blog_page.expect_blog_loaded()

    hero_video = blog_page.hero_cat_video()
    assert hero_video.count() > 0, "Expected cat hero media on /blog."

    source = blog_page.wait_for_hero_media_source()
    assert "blog.mp4" in source.lower() or "blog.webm" in source.lower()
