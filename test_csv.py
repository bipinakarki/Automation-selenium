import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

LOGIN_URL = "https://www.saucedemo.com/"

USERNAME = (By.ID, "user-name")
PASSWORD = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login-button")

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()


def login_test(username, password):

    driver.get(LOGIN_URL)
    time.sleep(2)

    # Enter Username
    driver.find_element(*USERNAME).clear()
    driver.find_element(*USERNAME).send_keys(username)

    # Enter Password
    driver.find_element(*PASSWORD).clear()
    driver.find_element(*PASSWORD).send_keys(password)

    # Click Login
    driver.find_element(*LOGIN_BUTTON).click()
    time.sleep(2)

    # Verify Login
    if "inventory.html" in driver.current_url:
        print(f"✅ Login Successful : {username}")

    else:
        print(f"❌ Login Failed : {username}")


# Read CSV File
with open(r"C:\Users\Dell\Desktop\framework\data\login.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        username = row["username"]
        password = row["password"]

        login_test(username, password)

driver.quit()