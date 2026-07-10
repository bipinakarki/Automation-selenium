from selenium.webdriver.common.by import By
import time
class inventory:
 def __init__(self,driver):
  self.driver=driver
  self.backpack=(By.ID,"add-to-cart-sauce-labs-backpack")
  self.light=(By.ID,"add-to-cart-sauce-labs-bike-light")
  self.jacket=(By.ID,"add-to-cart-sauce-labs-fleece-jacket")
  self.cart=(By.CLASS_NAME,"shopping_cart_link")

 def  click_backpack(self):
   self.driver.find_element(*self.backpack).click()
   time.sleep(1)
 def click_light(self):
    self.driver.find_element(*self.light).click()
    time.sleep(1)
 def click_jacket(self):
    self.driver.find_element(*self.jacket).click()
    time.sleep(1)

 def click_cart(self):
    self.driver.find_element(*self.cart).click()
    time.sleep(1)

 