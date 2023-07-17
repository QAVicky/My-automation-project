import pytest
from Pages.Loginpage import Login
from Pages.Homepage import homepage1
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














