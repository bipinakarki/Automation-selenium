from pages.login import login
from pages.inventory import inventory
from pages.cart import cartpage
from pages.checkout import checkout
import pytest

@pytest.mark.parametrize(
    "firstname, lastname, zipcode, expected",
    [
        
        ("Bipina", "Karki", "00342", "pass"),
        ("", "Karki", "00342", "error"),
        ("Bipina", "", "00342", "error"),
        ("Bipina", "Karki", "", "error"),
        ("76856", "Karki", "11180", "bug"),
        ("@##&", "Karki", "67540", "bug"),
        ("Bipina", "12345", "98300", "bug"),
        ("Bipina", "@@@###", "65111", "bug"),
        ("Bipina", "Karki", "abcd", "bug"),
        ("Bipina", "Karki", "#####", "bug"),
    ]
)
def test_checkout(driver,firstname,lastname,zipcode,expected):
    obj=login(driver)
    obj.open_url("https://www.saucedemo.com/")
    obj.enter_username("standard_user")
    obj.enter_password("secret_sauce")
    obj.click_login()
    assert"inventory.html" in driver.current_url
    print("successful login")
    
    inv=inventory(driver)
    inv.click_backpack()
    inv.click_cart()
    assert"cart.html"in driver.current_url,"navigation to cart.html failed"
    print("cart page opened")

    cart=cartpage(driver)
    cart.click_checkout()
    assert"checkout-step-one.html" in driver.current_url
    print("navigation to checkout first page")

    check=checkout(driver)
  

    check.first_name(firstname)
    check.last_name(lastname)
    check.zip_code(zipcode)
    check.click_cont()

    
    if expected == "pass":

        assert "checkout-step-two.html" in driver.current_url

        print("valid checkout")
    elif expected =="error":

        assert check.get_error_message() == expected

        print("invalid checkout")
        print(expected)

    elif expected == "bug":

        if "checkout-step-two.html" in driver.current_url:

            print("BUG FOUND")
            print("Application accepted invalid input.")
            print(f"First Name : {firstname}")
            print(f"Last Name  : {lastname}")
            print(f"Zip Code   : {zipcode}")

        else:

            print("Invalid input rejected.")