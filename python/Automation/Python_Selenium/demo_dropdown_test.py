from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class DemoDropDown():
    def demo_dropdown_test(self):
        driver = webdriver.Chrome()
        driver.get("https://www.salesforce.com/form/signup/freetrial-elf-v2/?d=70130000000EqoP")
        driver.maximize_window()
        driver.find_element(By.NAME,"UserFirstName").send_keys("test")
        time.sleep(2)
        driver.find_element(By.NAME, "UserLastName").send_keys("test")
        time.sleep(2)
        driver.find_element(By.NAME, "UserTitle").send_keys("test")
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[normalize-space(text())='Next']").click()
        time.sleep(2)
        select = driver.find_element(By.NAME,"CompanyCountry")
        select_element = Select(select)
        time.sleep(2)
        select_element.select_by_visible_text("India")
        time.sleep(2)

test = DemoDropDown()
test.demo_dropdown_test()