from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoCheckElementState():
    def demo_check_element_state(self):
        driver= webdriver.Chrome()
        driver.get("https://training.openspan.com/login")
        driver.maximize_window()
        state = driver.find_element(By.ID,"login_button").is_enabled()
        print(state)
        driver.find_element(By.NAME,"user_name").send_keys("test")
        time.sleep(2)
        driver.find_element(By.NAME,"user_pass").send_keys("test")
        time.sleep(2)
        state = driver.find_element(By.ID, "login_button").is_enabled()
        print(state)
        
test = DemoCheckElementState()
test.demo_check_element_state()