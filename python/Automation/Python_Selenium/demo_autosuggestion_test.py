from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class DemoAutoSuggestions():
    def demo_autosuggestion_test(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        get_element = driver.find_element(By.XPATH,"(//*[@class ='MuiTypography-root MuiTypography-body1  css-17kn1z8'])[1]")
        time.sleep(2)
        get_element.click()
        time.sleep(2)
        type_text = driver.find_element(By.XPATH,"(//*[@type='text'])[1]")
        type_text.send_keys("New")
        time.sleep(2)
        suggestions = driver.find_elements(By.XPATH,"//*[@class='MuiBox-root css-134xwrj']")
        time.sleep(2)
        for  text in suggestions:
            print(text.text)
            if "New York" in text.text:
                driver.find_element(By.XPATH,"//*[contains(normalize-space(text()),'New York')]").click()

        time.sleep(4)

test = DemoAutoSuggestions()
test.demo_autosuggestion_test()