from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class DemoSlider():
    def demo_slider(self):
        driver = webdriver.Chrome()
        driver.get("https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3DMax")
        driver.maximize_window()
        time.sleep(10)
        elem1 = driver.find_element(By.XPATH,"//*[@class='iToJ4v Kaqq1s']")
        ActionChains(driver).drag_and_drop_by_offset(elem1,120,0).perform()
        time.sleep(10)


obj = DemoSlider()
obj.demo_slider()
