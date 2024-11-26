from selenium import webdriver
import time
class Demo_JavaScript():
    def demo_javascript(self):
        driver = webdriver.Chrome()
        # NOte this _self is used to open the URL in the same tab
        driver.execute_script("window.open('https://training.rcvacademy.com/courses', '_self');")
        time.sleep(3)
        demo_elem = driver.execute_script("return document.getElementsByTagName('p')[1];")
        print(demo_elem)
        time.sleep(4)
        driver.execute_script("arguments[0].click();", demo_elem)
        time.sleep(4)



obj = Demo_JavaScript()
obj.demo_javascript()