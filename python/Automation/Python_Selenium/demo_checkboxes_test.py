from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DemoCheckbox():
    def demo_checkbox_test(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        checkbox = driver.find_element(By.XPATH,"//*[@type='checkbox']")
        time.sleep(2)
        print(checkbox.is_selected())
        time.sleep(2)
        checkbox.click()
        time.sleep(2)
        print(checkbox.is_selected())


test = DemoCheckbox()
test.demo_checkbox_test()