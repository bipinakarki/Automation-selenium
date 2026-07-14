from selenium.webdriver.common.by import By
import time
class cartpage:
    def __init__(self,driver):
     self.driver=driver
     self.check_out=(By.ID,"checkout")
     # added after
     self.removebackpack=(By.ID,"remove-sauce-labs-backpack")
     self.removelight=(By.ID,"remove-sauce-labs-bike-light")
     self.removejacket=(By.ID,"remove-sauce-labs-fleece-jacket")
     self.continueshopping=(By.ID,"continue-shopping")
     self.product_names=(By.CLASS_NAME,"inventory_item_name")

    def remove_backpack(self):
      self.driver.find_element(*self.removebackpack).click()
      time.sleep(2)
    
    def continue_shopping(self):
      self.driver.find_element(*self.continueshopping).click()

    def click_checkout(self):
      self.driver.find_element(*self.check_out).click()
      time.sleep(2)
    def get_product_names(self):
      products=self.driver.find_elements(*self.product_names)
      return[product.text for product in products]
    def get_product_count(self):
     return len(self.driver.find_elements(*self.product_names))