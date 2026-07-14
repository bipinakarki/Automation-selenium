from selenium.webdriver.common.by import By
import time

class complete:
     def __init__(self,driver):
          self.driver=driver
          self.home=(By.ID,"back-to-products")
     def back_home(self):
         self.driver.find_element(*self.home).click()
         time.sleep(2) 