import pytest
from pages.login import login

@pytest.mark.parametrize("username,password,expected",
  [
     ("standard_user","secret_sauce","pass") ,
      ("locked_out_user","secret_sauce","fail"),
      ("problem_user","secret_sauce","pass"),
      ("performance_glitch_user", "secret_sauce","pass"),
      ("error_user", "secret_sauce","pass"),
      ("visual_user", "secret_sauce","pass"),
      ("invalid_user","invalid_password","fail"),
      ("wrong_user","password","fail"),
      ("user","password","fail") ,
      ("","","fail"),
      ("standard_user","","fail;"),
      ("","secret_sauce","fail")          

  ])
def test_login(driver, username, password, expected):
    objc=login(driver)
    objc.open_url("https://www.saucedemo.com/")
    objc.enter_username(username)
    objc.enter_password(password)
    objc.click_login()

    if expected=="pass":
       assert "inventory.html" in driver.current_url,"login failed"
       print("login successful")
    else:
        assert"inventory.html" not in driver.current_url
        print("login failed")