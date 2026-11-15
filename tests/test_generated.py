from playwright.sync_api import Page, Playwright, sync_playwright, expect


def example(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demowebshop.tricentis.com")
    page.wait_for_timeout(3000)
    
    # Recorded actions & locators
    page.get_by_role("link", name="Books").first.click()
    page.wait_for_timeout(3000)
    expect(page).to_have_url("https://demowebshop.tricentis.com/books")
    print(page.url)
    context.close()
    browser.close()


with sync_playwright() as playwright:
    example(playwright)