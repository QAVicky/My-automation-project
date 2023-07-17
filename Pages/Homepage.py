import time

from selenium.webdriver.common.by import By
from Locators.locators import locatorspage

class homepage1():
    def __init__(self, driver):
        self.driver = driver

    def Email(self,a):

        em = self.driver.find_element(By.ID, locatorspage.Email)
        em.click()
        time.sleep(2)
        em.send_keys(a)
        time.sleep(2)


    def Password(self,b):

        pwd = self.driver.find_element(By.ID, locatorspage.Password)
        pwd.click()
        time.sleep(2)
        pwd.send_keys(b)
        time.sleep(2)


    def Submit(self):
        bt = self.driver.find_element(By.XPATH, locatorspage.Submit)
        bt.click()
        time.sleep(10)

    def viewmore(self):
        vm = self.driver.find_element(By.XPATH, locatorspage.Viewmore)
        vm.click()
        time.sleep(5)

    def Pagenation(self):
        pn = self.driver.find_element(By.XPATH, locatorspage.pagenation)
        pn.click()
        time.sleep(5)

    def Pagenation1(self):
        pn1 = self.driver.find_element(By.XPATH, locatorspage.pagination1)
        pn1.click()
        time.sleep(5)





