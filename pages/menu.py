from selenium.webdriver.common.by import By
import time
class menubar:
    def __init__(self,driver):
        self.driver=driver
        self.menubutton=(By.ID,"react-burger-menu-btn")
        self.allitems=(By.ID,"inventory_sidebar_link")
        self.about=(By.ID,"about_sidebar_link")
        self.logout=(By.ID,"logout_sidebar_link")
        self.resetapp=(By.ID,"reset_sidebar_link")
        self.closemenu=(By.ID,"react-burger-cross-btn")

    def menu_button(self):
            self.driver.find_element(*self.menubutton).click()
            time.sleep(2)

    def all_items(self):
            self.driver.find_element(*self.allitems).click()
            time.sleep(2)
    def click_about(self):
            self.driver.find_element(*self.about).click()
            time.sleep(2)
        
    def click_reset(self):
            self.driver.find_element(*self.resetapp).click()
            time.sleep(3)
    def click_logout(self):
            self.driver.find_element(*self.logout).click()
            time.sleep(3)

    def close_menu(self):
            self.driver.find_element(*self.closemenu).click()
            time.sleep(2)