import pytest
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class')
def setup(request):

    #driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    service = Service('D:\python\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    driver.get("https://courses.ultimateqa.com/users/sign_in")

    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
