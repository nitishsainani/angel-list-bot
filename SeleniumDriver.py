from selenium import webdriver
from selenium.webdriver import ChromeOptions

import os

class SeleniumDriver:
    def __init__(self):
        self.seleniumPath = os.getenv('SELENIUM_DRIVER_PATH')
        if self.seleniumPath is None:
            raise Exception("SELENIUM_DRIVER_PATH is not in .env")

    def getDriver(self):
        isDevMode:bool = os.getenv('DEVELOPER_ENVIRONMENT') == 'TRUE'

        chromeOptions = ChromeOptions()
        chromeOptions.add_argument('--user-data-dir=chrome_user_data')

        return webdriver.Chrome(
            executable_path=self.seleniumPath,
            chrome_options=chromeOptions)