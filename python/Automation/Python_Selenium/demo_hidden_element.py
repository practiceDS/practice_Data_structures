from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DemoHiddenElement():
    def demo_hidden_element(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        driver.maximize_window()
        state = driver.find_element(By.XPATH, "//*[normalize-space(text())='Click the button!']").is_displayed()
        print(state)
        driver.find_element(By.XPATH, "//*[normalize-space(text())='Toggle Hide and Show']").click()
        time.sleep(2)
        state = driver.find_element(By.XPATH, "//*[normalize-space(text())='Click the button!']").is_displayed()
        print(state)


test = DemoHiddenElement()
test.demo_hidden_element()