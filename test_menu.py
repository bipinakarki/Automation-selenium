from pages.menu import menubar
from pages.login import login
from pages.inventory import inventory

def test_menu(driver):
    obj=login(driver)
    obj.open_url("https://www.saucedemo.com/")
    obj.enter_username("standard_user")
    obj.enter_password("secret_sauce")
    obj.click_login()

    inv=inventory(driver)
    
    menu=menubar(driver)

    products=[
    inv.click_backpack,
    inv.click_jacket,
    inv.click_light
    ]
    for count,product in enumerate(products,start=1):
        product()
        assert inv.see_cartbadge() == str(count)


    menu.menu_button()
    menu.click_reset()
    assert len(driver.find_elements(*inv.cartbadge)) == 0
    print("cart count reset auttomatically")
    
    remove_buttons = [
    ("Backpack", inv.removebackpack),
    ("Bike Light", inv.removelight),
    ("Fleece Jacket", inv.removejacket)
    ]
 
    for name, button in remove_buttons:
     assert len(driver.find_elements(*button)) == 0, \
        f" {name}: automatic reset failed"
