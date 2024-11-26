from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoFindElement():
    def find_element(self):
        driver= webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.XPATH,"//input[@placeholder='Email ID / Mobile Number']").send_keys("test@test.com")
        time.sleep(4)
        driver.close()



test = DemoFindElement()
test.find_element()