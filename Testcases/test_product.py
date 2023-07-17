import time

import pytest
from selenium.webdriver import Keys

from Pages.Loginpage import Login
from Pages.Homepage import homepage1
from Pages.Productspage import product
from Basefile.base_driver import basepage

@pytest.mark.usefixtures("setup")
class Test_home():
    def test_email(self):
        s = Login(self.driver)
        s.Email("vickydce1992@gmail.com")

    def test_password(self):
        s = Login(self.driver)
        s.Password("Vickyqa@22")

    def test_submit(self):
        s = Login(self.driver)
        s.Submit()

    def test_home(self):
        v = homepage1(self.driver)
        v.viewmore()

    def test_base(self):
        bp = basepage(self.driver)
        bp.page_scroll()

    def test_page(self):
        p = homepage1(self.driver)
        p.Pagenation()

    def test_base1(self):
        bp1 = basepage(self.driver)
        bp1.page_scroll()

    def test_page1(self):
        p1 = homepage1(self.driver)
        p1.Pagenation1()

    def test_search1(self):
        se = product(self.driver)
        se.search("Browser stack")

    def test_base2(self):
        bp1 = basepage(self.driver)
        bp1.page_scroll()

    def test_product(self):
        pr1 = product(self.driver)
        pr1.Product()

    def test_product1(self):
        pr2 = product(self.driver)
        pr2.Product1()
'''
    def test_comp(self):
        con = product(self.driver)
        con.complete()
'''


































































