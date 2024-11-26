from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoFindElement():
    def find_element(self):
        driver= webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        elements = driver.find_elements(By.TAG_NAME,"a")
        for i in elements:
            print(i.text)
        time.sleep(4)
        driver.close()



test = DemoFindElement()
test.find_element()