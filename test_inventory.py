from pages.login import login
from pages.inventory import inventory


def test_inventory(driver):

  
    obj = login(driver)
    obj.open_url("https://www.saucedemo.com/")
    obj.enter_username("standard_user")
    obj.enter_password("secret_sauce")
    obj.click_login()

    assert "inventory.html" in driver.current_url
    print("Login Successful")
    

    inv = inventory(driver)
    inv.click_backpack()
    inv.click_jacket()
    inv.click_light()
    inv.remove_backpack()
    inv.remove_light()
   
     #sorting

    sorting_options = [
    "Name (A to Z)",
    "Name (Z to A)",
    "Price (low to high)",
    "Price (high to low)"
    ]


    for option in sorting_options:
     inv.select_sort(option)
 
   
    assert inv.get_selected_sort() == option

    print(f" {option} Selected")


    inv.click_cart()
    assert"cart.html"in driver.current_url,"navigation to cart.html failed"
    print("cart page opened")