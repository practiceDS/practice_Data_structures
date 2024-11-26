from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoFindElement():
    def find_element(self):
        driver= webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        #driver.find_element(By.TAG_NAME,"input").send_keys("test@test.com")
        driver.find_element(By.CLASS_NAME, "email-login-box").send_keys("test@test.com")
        time.sleep(4)
        driver.close()



test = DemoFindElement()
test.find_element()