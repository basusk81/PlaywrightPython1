import re
from playwright.sync_api import Page, expect

import yaml

with open("config/user.yaml", "r") as file:
       user_data = yaml.safe_load(file)
       print(user_data)

def test_example(page: Page) -> None:
    page.goto("https://demowebshop.tricentis.com/")

    #print(user_data["test_env"]["username"])
    #print(user_data["test_env"]["password"])
    print("Test Started")


    username= user_data["test_env"]["username"]
    password= user_data["test_env"]["password"]

    print("Username:", username)
    print("Password:", password)

   
    page.get_by_role("link", name="Log in").click()
    page.get_by_role("textbox", name="Email:").click()
    page.get_by_role("textbox", name="Email:").fill(username)
    page.wait_for_timeout(3000)
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill(password)
    page.get_by_role("button", name="Log in").click()
    page.get_by_role("link", name="Apparel & Shoes").first.click()
    page.get_by_role("link", name="Casual Golf Belt", exact=True).click()
    page.get_by_role("textbox", name="Qty:").click()
    page.get_by_role("textbox", name="Qty:").press("Delete")
    page.get_by_role("textbox", name="Qty:").fill("5")
    page.locator("#add-to-cart-button-40").click()
    page.get_by_role("link", name="Shopping cart (5)").click()
    page.get_by_label("State / province:").select_option("15")
    page.get_by_role("textbox", name="Zip / postal code:").click()
    page.get_by_role("textbox", name="Zip / postal code:").fill("33624")
    page.get_by_role("button", name="Estimate shipping").click()
    page.locator("#termsofservice").check()
    #page.get_by_role("button", name="Checkout").click()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_label("Select a billing address from").select_option("5198969")
    page.wait_for_timeout(3000)
    #expect(page.get_by_label("Select a billing address from")).to_contain_text("Saurabh Basu, 1 Main Street, Tampa, Florida 33624, United States")
    page.get_by_role("button", name="Continue").click()
    page.get_by_label("Select a shipping address").select_option("5198969")
    page.wait_for_timeout(3000)
    #expect(page.get_by_label("Select a shipping address")).to_contain_text("Saurabh Basu, 1 Main Street, Tampa, Florida 33624, United States")
    page.get_by_role("button", name="Continue").click()
    expect(page.locator("#checkout-shipping-method-load")).to_contain_text("Ground (10.00)")
    expect(page.locator("#checkout-shipping-method-load")).to_contain_text("Next Day Air (40.00)")
    expect(page.locator("#checkout-shipping-method-load")).to_contain_text("2nd Day Air (20.00)")
    page.get_by_role("radio", name="2nd Day Air (20.00)").check()
    page.get_by_role("radio", name="Ground (10.00)").check()
    page.wait_for_timeout(3000)
    page.get_by_role("button", name="Continue").click()
    expect(page.locator("#checkout-payment-method-load")).to_contain_text("Cash On Delivery (COD) (7.00)")
    expect(page.locator("#checkout-payment-method-load")).to_contain_text("Check / Money Order (5.00)")
    expect(page.locator("#checkout-payment-method-load")).to_contain_text("Credit Card")
    expect(page.locator("#checkout-payment-method-load")).to_contain_text("Purchase Order")
    page.get_by_role("radio", name="Purchase Order Purchase Order").check()
    page.get_by_role("radio", name="Cash On Delivery (COD) (7.00").check()
    page.wait_for_timeout(3000)
    page.get_by_role("button", name="Continue").click()
    expect(page.get_by_role("cell")).to_contain_text("You will pay by COD")
    page.wait_for_timeout(3000)
    page.get_by_role("button", name="Continue").click()
    page.wait_for_timeout(3000)
    page.get_by_role("button", name="Confirm").click()
    #expect(page.get_by_role("strong")).to_contain_text("Your order has been successfully processed!").to_be_visible()
    expect(page.locator("text=Your order has been successfully processed!")).to_be_visible()
    #expect(page.get_by_role("strong")).to_contain_text("Your order has been successfully processed!")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("link", name="Log out").click()


    page.close()