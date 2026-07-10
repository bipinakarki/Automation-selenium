from selenium.webdriver.common.by import By
import time
class cartpage:
    def __init__(self,driver):
     self.driver=driver
     self.check_out=(By.ID,"checkout")
     
    def click_checkout(self):
      self.driver.find_element(*self.check_out).click()
      time.sleep(2)
