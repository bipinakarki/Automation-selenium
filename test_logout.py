from pages.menu import menubar
from pages.login import login
from pages.inventory import inventory

def test_logout(driver):
    obj=login(driver)
    obj.open_url("https://www.saucedemo.com/")
    obj.enter_username("standard_user")
    obj.enter_password("secret_sauce")
    obj.click_login()

    assert"inventory.html" in driver.current_url


    inv=inventory(driver)
    
    menu=menubar(driver)
    
    menu.menu_button()
    menu.click_logout()
    assert"https://www.saucedemo.com/" in driver.current_url
    obj.click_login()
    assert"inventory.html" not in driver.current_url