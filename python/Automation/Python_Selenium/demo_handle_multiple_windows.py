from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class MultipleWindows():
    def multiple_windows(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        curr_win_handle = driver.window_handles
        time.sleep(5)
        driver.find_element(By.XPATH,"//*[normalize-space(text())='For Business']").click()
        time.sleep(5)
        handles = driver.window_handles
        for handle in handles:
            if handle != curr_win_handle:
                driver.switch_to.window(handle)

        time.sleep(5)
        driver.switch_to.window(curr_win_handle[0])
        time.sleep(5)




obj = MultipleWindows()
obj.multiple_windows()
