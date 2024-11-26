from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoFindElement():
    def find_element(self):
        driver= webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(8)
        text = driver.find_element(By.XPATH, "(//span[normalize-space(text())='Flights'])[1]").text
        print(text)
        time.sleep(4)
        driver.close()



test = DemoFindElement()
test.find_element()