from SeleniumDriver import SeleniumDriver
import time
from selenium.webdriver.common.keys import Keys


MESSAGE_TO_RECRUITER = "Hi {},\nI hope this email finds you well."\
    "\nReading your job posting on Angel for this position excites me to work in the company."\
    "Your description of the work responsibilities closely matches my experience and skills, and so I am excited to submit my resume to you for your consideration."\
    "\nMy Website - http://nitishsainani.github.io/"\
    "\nMy resume - http://bit.ly/2QbwnNl"\
    "\nBest,"\
    "\nNitish"\
    "\n+91 9644354203"


class AngelBot:
    def __init__(self):
        self.driver = SeleniumDriver().getDriver()
        self.driver.implicitly_wait(10)

    def __del__(self):
        if self.driver:
            self.driver.quit()

    def startAutomation(self):
        self.driver.get('https://angel.co/')
        applyButtonsNeeded = 100
        applyButtons = self.driver.find_elements_by_xpath('//*[@id="main"]/div[4]/div[2]/div[2]/div/div/div[2]/div/div/div/button')
        while len(applyButtons) < applyButtonsNeeded:
            # Scroll to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait for loading
            time.sleep(3)
            # Get new apply buttons
            applyButtons = self.driver.find_elements_by_xpath('//*[@id="main"]/div[4]/div[2]/div[2]/div/div/div[2]/div/div/div/button')
        
        # Scroll to top
        self.driver.execute_script("window.scrollTo(0, 0);")
        applyButtons = self.driver.find_elements_by_xpath('//*[@id="main"]/div[4]/div[2]/div[2]/div/div/div[2]/div/div/div/button')
        for button in applyButtons:
            time.sleep(2)
            try:
                button.click()
                time.sleep(2)
                try:
                    recruiterName = self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/form//div[1]/h4').text.split()[4]
                except:
                    recruiterName = "Hiring Manager"
                textBox = self.driver.find_element_by_xpath('//*[@id="form-input--userNote"]')
                textBox.send_keys(MESSAGE_TO_RECRUITER.format(recruiterName))

                # send Application button
                sendApplicationButton = self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/form//button[2]')
                sendApplicationButton.click()
            except Exception as e:
                print(e)
                try:
                    self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/form//button[1]').click()
                except:
                    pass
