import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class MouseActions():
    def test_mouse_actions(self):
        driver = webdriver.Chrome()
        driver.get('https://www.yatra.com/')
        time.sleep(5)
        ActionChains(driver).click(driver.find_element(By.XPATH,"//*[normalize-space(text())='Login']")).perform()
        time.sleep(10)



obj = MouseActions()
obj.test_mouse_actions()

