from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

class Dragdrop():
    def demo_drag_and_drop(self):
        driver = webdriver.Chrome()
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        time.sleep(5)
        driver.switch_to.frame(driver.find_element(By.XPATH,"//*[@class='demo-frame']"))
        time.sleep(3)
        elem1 = driver.find_element(By.XPATH,"//*[normalize-space(text())='Drag me to my target']")
        elem2 = driver.find_element(By.XPATH, "//*[normalize-space(text())='Drop here']")
        ActionChains(driver).drag_and_drop(elem1,elem2).perform()
        time.sleep(10)


obj = Dragdrop()
obj.demo_drag_and_drop()


