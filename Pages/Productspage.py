import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Locators.locators import locatorspage

driver = webdriver.Chrome()

class product():
    def __init__(self, driver):
        self.driver = driver

    def search(self, c):
        s = self.driver.find_element(By.NAME, locatorspage.Searchbar)
        s.click()
        time.sleep(2)
        s.send_keys(c)
        s.send_keys(Keys.ENTER)
        time.sleep(5)

    def Product(self):
        pr = self.driver.find_element(By.XPATH, locatorspage.Product)
        pr.click()
        time.sleep(5)

    def Product1(self):
        pr1 = self.driver.find_element(By.XPATH, locatorspage.Resume)
        self.driver.save_screenshot('ss.png')
        image = Image.open('ss.png')
        image.show()
        pr1.click()
        time.sleep(20)

''' 
    def complete(self):
        comp = self.driver.find_element(By.XPATH, locatorspage.complete)
        comp.click()
        time.sleep(3)
'''



























































