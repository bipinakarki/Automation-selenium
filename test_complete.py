
import pytest
from pages.login import login
from pages.inventory import inventory
from pages.cart import cartpage
from pages.checkout import checkout
from pages.finish import finish
from pages.backhome import complete


  
@pytest.mark.parametrize("username,password",
    [
      ("standard_user","secret_sauce") ,
      ("locked_out_user","secret_sauce"),
      ("problem_user","secret_sauce"),
      ("performance_glitch_user", "secret_sauce"),
      ("error_user", "secret_sauce"),
      ("visual_user", "secret_sauce"),
      ("invalid_user","invalid_password"),
      ("wrong_user","password"),
      ("user","password")
     ])
    
def test_valid_login(driver,username,password):
    obj = login(driver)
    obj.open_url("https://www.saucedemo.com/")
    obj.enter_username(username)
    obj.enter_password(password)
    obj.click_login()
     
       # Check login result
    if "inventory.html" in driver.current_url:
      assert "inventory.html" in driver.current_url, "Login Failed"
      print("Login Successful")

      inv=inventory(driver)
      inv.click_backpack()
      inv.click_light()
      inv.click_jacket()
      inv.click_cart()
      
      assert"cart.html"in driver.current_url,"navigation to cart.html failed"
      print("cart page opened")

      cart=cartpage(driver)
      cart.click_checkout()

      assert"checkout-step-one.html" in driver.current_url,"navigation to checkout failed"
      print("navigation to checkout first successful")
      check=checkout(driver)
      check.first_name("Gita")
      check.last_name("Thapa")
      check.zip_code("1234")
      check.click_cont()

      assert"checkout-step-two.html" in driver.current_url,"navigation failed"
      print("successful navigation to finish page ")
      fin=finish(driver)
      fin.clickfinish()
      assert"checkout-complete.html" in driver.current_url,"navigation to complete page failed"
      print("successful navigation to complete")

      comp=complete(driver)
      comp.back_home()
      assert"inventory.html" in driver.current_url,"redirection to product failed"
      print(" successful redirection to product page")
    else:
       assert "inventory.html" not in driver.current_url
       print("Invalid Login Verified")