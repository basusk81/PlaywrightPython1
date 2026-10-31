import pytest
from playwright.sync_api import sync_playwright

def test_get_page_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://demowebshop.tricentis.com")
        title = page.title()

        page.wait_for_load_state("load")

        print("Page title:", title)
        assert title == "Demo Web Shop"

        browser.close()
