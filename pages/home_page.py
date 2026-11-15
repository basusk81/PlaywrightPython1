from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.account_name = page.locator("a.account").first
        
    def get_account_name(self):
        return self.account_name.text_content()
    