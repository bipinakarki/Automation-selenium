from selenium.webdriver.common.by import By
import time

class finish:
    def __init__(self,driver):
        self.driver=driver
        self.click_finish=(By.ID,"finish")
    def clickfinish(self):

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.find_element(*self.click_finish).click()
       # time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        