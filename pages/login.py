from selenium.webdriver.common.by import By
import time
class login:
    def __init__(self,driver):
        self.driver=driver
        self.username=(By.ID,"user-name")
        self.password=(By.ID,"password")
        self.login_button=(By.ID,"login-button")
    def open_url(self,url):
        self.driver.get(url)
        time.sleep(1)
        
    def enter_username(self,username):
        self.driver.find_element(*self.username).send_keys(username)
        time.sleep(1)
    def enter_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)
        time.sleep(1)
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        time.sleep(1)