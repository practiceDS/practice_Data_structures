from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JavascriptAlerts():
    def handle_javascript_alert(self):
        driver = webdriver.Chrome()
        driver.get('https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt')
        driver.maximize_window()
        time.sleep(5)
        driver.switch_to.frame(driver.find_element(By.ID,'iframeResult'))
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[normalize-space(text())='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.send_keys("Hello")
        time.sleep(5)
        driver.switch_to.alert.accept()
        time.sleep(5)


obj = JavascriptAlerts()
obj.handle_javascript_alert()
