import time


class basepage():
    def __init__(self,driver):
        self.driver = driver

    #Scrolling Purpose

    def page_scroll(self):
        pagelenth = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var pagelenth = document.body.scrollHeight; return pagelenth;")
        match = False
        while (match == False):
            lastcount = pagelenth
            time.sleep(2)
            pagelenth = self.driver.execute_script( "window.scrollTo(0, document.body.scrollHeight);var pagelenth = document.body.scrollHeight; return pagelenth;")
            if lastcount == pagelenth:
                match = True
        time.sleep(3)





