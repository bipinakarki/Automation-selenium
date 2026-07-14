'''from selenium import webdriver
import pytest
@pytest.fixture()

def driver():
  driver=webdriver.Chrome()
  driver.maximize_window()
  yield driver
  driver.quit()
  '''

import pytest
from selenium import webdriver
@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()

    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    )


    driver = webdriver.Chrome(options=options)

    driver.maximize_window()

    yield driver

    driver.quit()