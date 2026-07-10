from selenium import webdriver
import pytest
from pages.login import login
import random

@pytest.fixture()

def driver():
  driver=webdriver.Chrome()
  driver.maximize_window()
  yield driver
  driver.quit()
  
usernames=[
    "standard_user",
    "locked_out_user",
    "error_user",
    "visual_user",
    "problem_user",
    "performance_glitch_user",
    "invalid_user",
    "wrong_user",
    "user"
]

passwords=[
    "invalid_password",
    "secret_sauce",
    "password"
]
def get_random():
    username=random.choice(usernames)
    password=random.choice(passwords)
    return username,password
def test_random(driver):
   username, password=get_random()
   obj = login(driver)
   obj.open_url("https://www.saucedemo.com/")
   obj.enter_username(username)
   obj.enter_password(password)
   obj.click_login()
  
   if "inventory.html" in driver.current_url:
      assert "inventory.html" in driver.current_url,"login failed"
      print("login successful")
   else:
      assert "inventory.html" not in driver.current_url
      print("❌ Login Failed")