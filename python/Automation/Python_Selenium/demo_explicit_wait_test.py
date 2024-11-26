from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
class DemoFindElement():
    def find_element(self):
        driver= webdriver.Chrome()
        # Explicit wait and Fluent wait ans same, it just Fluent have polling functionailty.
        wait = WebDriverWait(driver,10,2)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Email ID / Mobile Number']"))).send_keys("test@test.com")
        driver.close()



test = DemoFindElement()
test.find_element()