from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page1: Page):
        self.page = page1
        self.email_input = page1.get_by_role("textbox", name="Email:")
        self.password_input = page1.get_by_role("textbox", name="Password:")
        self.login_button = page1.get_by_role("button", name="Log in")

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def click_login_link(self):
        self.page.get_by_role("link", name="Log in").click()

    def enter_email(self, email):
        self.email_input.fill(email)

    def enter_password(self, password):
        self.password_input.fill(password)

    def click_login_button(self):
            self.login_button.click()