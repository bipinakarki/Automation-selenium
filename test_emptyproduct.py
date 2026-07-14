from pages.login import login
from pages.inventory import inventory
from pages.cart import cartpage


def test_emptyproduct(driver):
    obj = login(driver)
    obj.open_url("https://www.saucedemo.com/")
    obj.enter_username("standard_user")
    obj.enter_password("secret_sauce")
    obj.click_login()

    
    inv = inventory(driver)
    inv.click_cart()
    
    cart=cartpage(driver)
    cart.click_checkout()

    # Verify checkout page opens
    assert "checkout-step-one.html" not in driver.current_url,"navigation without product on cart"
    