import re
from conftest import page
from playwright.sync_api import expect, sync_playwright

def test_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
    
        page.goto("https://www.google.com")
        page.wait_for_timeout(2000)
        #expect(page).to_have_title(re.compile("Google"))

        #page.get_by_role("combobox", name="q").click()
        #page.get_attribute("name", "q").click()
        page.get_by_role("combobox", name="Search").fill("Playwright Python")
        page.wait_for_timeout(2000)
        page.keyboard.press("Enter")
        page.wait_for_timeout(2000)

       #expect(page).to_have_title(re.compile("Playwright Python",re.IGNORECASE))

try:
        page.get_by_role("button", name="Accept all").click(timeout=5000)
except:
        print("No Pop up Found")






