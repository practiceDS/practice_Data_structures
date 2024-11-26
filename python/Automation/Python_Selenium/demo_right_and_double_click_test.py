from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class RightandDoubleClick():
    def right_and_double_click(self):
        driver = webdriver.Chrome()
        driver.get('https://demo.guru99.com/test/simple_context_menu.html')
        time.sleep(2)
        driver.maximize_window()
        actions = ActionChains(driver)
        actions.context_click(driver.find_element(By.XPATH,"//*[normalize-space(text())='right click me']")).perform()
        driver.find_element(By.XPATH,"//*[normalize-space(text())='Copy']").click()
        driver.switch_to.alert.accept()
        actions.double_click(driver.find_element(By.XPATH,"//*[normalize-space(text())='Double-Click Me To See Alert']")).perform()
        driver.switch_to.alert.accept()


obj = RightandDoubleClick()
obj.right_and_double_click()

