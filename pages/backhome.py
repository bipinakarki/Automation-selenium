from selenium.webdriver.common.by import By
import time

class complete:
     def __init__(self,driver):
          self.driver=driver
          self.home=(By.ID,"back-to-products")
     def back_home(self):
         '''self.driver.execute_script("window.scrollTo(0, 0);")
         time.sleep(1)'''
     
         self.driver.find_element(*self.home).click()
         time.sleep(2) 