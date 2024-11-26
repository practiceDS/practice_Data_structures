from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoFindElement():
    def find_element(self):
        driver= webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        #driver.find_element(By.LINK_TEXT,"For Business").click()
        driver.find_element(By.PARTIAL_LINK_TEXT, "Business").click()
        time.sleep(4)
        driver.close()



test = DemoFindElement()
test.find_element()