from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshot():
    def screenshot_page(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.ID,"login-continue-btn").screenshot('Continue_button.png')
        time.sleep(2)
        driver.find_element(By.ID,"login-input").send_keys("7838574602")
        time.sleep(2)
        driver.find_element(By.ID,"login-continue-btn").click()
        time.sleep(2)
        driver.save_screenshot("Full_page.png")

obj = Screenshot()
obj.screenshot_page()
