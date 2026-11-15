from playwright.sync_api import expect, Page
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_login_account(page: Page):
    # Create an instance of the LoginPage
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    # Navigate to the login page and click the login link
    page.goto("https://demowebshop.tricentis.com/")
    login_page.click_login_link()
    
    # Perform login
    login_page.login("saurabhkbasu@hotmail.com","password123")

    #Checking Account Information
    home_page.get_account_name()
    print("Account Name:", home_page.get_account_name())

