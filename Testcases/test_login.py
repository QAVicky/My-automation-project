import pytest

from Pages.Loginpage import Login

@pytest.mark.usefixtures("setup")

class Testlogin():


    def test_email(self):
        s = Login(self.driver)
        s.Email("vickydce1992@gmail.com")

    def test_password(self):
        s = Login(self.driver)
        s.Password("Vickyqa@22")

    def test_submit(self):
        s = Login(self.driver)
        s.Submit()
