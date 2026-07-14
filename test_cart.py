import pytest
from pages.cart import cartpage
from pages.login import login
from pages.inventory import inventory

def test_cart(driver):
    obj=login(driver)
    obj.open_url("https://www.saucedemo.com/")
    obj.enter_username("standard_user")
    obj.enter_password("secret_sauce")
    obj.click_login()
    assert"inventory.html" in driver.current_url
    print("successful login")
    
    inv=inventory(driver)
    inv.click_backpack()
    inv.click_jacket()
    inv.click_light()
    inv.click_cart()
    assert "cart.html" in driver.current_url
    print("navigation to cart page")

    cart=cartpage(driver)
    products=cart.get_product_names()
    assert"Sauce Labs Backpack" in products
    print("backpack added")
    assert"Sauce Labs Fleece Jacket" in products
    print("Jacket added")
    assert"Sauce Labs Bike Light" in products
    print("light added")
    

    before=cart.get_product_count()
    print("product count added:",before)

    cart.remove_backpack()
    products=cart.get_product_names()
    assert"Sauce Labs Backpack"not in products
    print("backpack removed")
    after=cart.get_product_count()
    assert after == before - 1

    print("product count after removal:",after)
    cart.continue_shopping()
    
    assert"inventory.html" in driver.current_url
    print("redirection to inventory page ")
    
    