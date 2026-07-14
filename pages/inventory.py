from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
class inventory:
 def __init__(self,driver):
  self.driver=driver
  self.backpack=(By.ID,"add-to-cart-sauce-labs-backpack")
  self.light=(By.ID,"add-to-cart-sauce-labs-bike-light")
  self.jacket=(By.ID,"add-to-cart-sauce-labs-fleece-jacket")
  self.cart=(By.CLASS_NAME,"shopping_cart_link")

#for test_inventory.py added later
  self.removebackpack=(By.ID,"remove-sauce-labs-backpack")
  self.removelight=(By.ID,"remove-sauce-labs-bike-light")
  self.removejacket=(By.ID,"remove-sauce-labs-fleece-jacket")
  self.cartbadge=(By.CLASS_NAME,"shopping_cart_badge")
  self.sort=(By.CLASS_NAME,"product_sort_container")

 def  click_backpack(self):
   self.driver.find_element(*self.backpack).click()
   time.sleep(2)
 def click_light(self):
    self.driver.find_element(*self.light).click()
    time.sleep(1)
 def click_jacket(self):
    self.driver.find_element(*self.jacket).click()
    time.sleep(2)

 def click_cart(self):
    self.driver.find_element(*self.cart).click()
    time.sleep(1)

 #remove function added later
 def remove_backpack(self):
   self.driver.find_element(*self.removebackpack).click()
   time.sleep(1)
 def remove_light(self):
   self.driver.find_element(*self.removelight).click()

 def remove_jacket(self):
   self.driver.find_element(*self.removejacket).click()
   
 def see_cartbadge(self):
   return self.driver.find_element(*self.cartbadge).text
   time.sleep(2)
 def select_sort(self,option):
   dropdown=Select(self.driver.find_element(*self.sort))
   dropdown.select_by_visible_text(option)
   time.sleep(2)
 def get_selected_sort(self):
    dropdown = Select(self.driver.find_element(*self.sort))
    return dropdown.first_selected_option.text
