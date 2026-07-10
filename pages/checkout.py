from selenium.webdriver.common.by import By
import time

class checkout:
    def __init__(self,driver):
        self.driver=driver
        self.firstname=(By.ID,"first-name")
        self.lastname=(By.ID,"last-name")
        self.zipcode=(By.ID,"postal-code")
        self.cont=(By.ID,"continue")
    def first_name(self,firstname):
        self.driver.find_element(*self.firstname).send_keys(firstname)
        time.sleep(1)
    def last_name(self,lastname):
        self.driver.find_element(*self.lastname).send_keys(lastname)
        time.sleep(1)
    def zip_code(self,zipcode):
        self.driver.find_element(*self.zipcode).send_keys(zipcode)
        time.sleep(1)
    def click_cont(self):
        self.driver.find_element(*self.cont).click()
        time.sleep(1)
