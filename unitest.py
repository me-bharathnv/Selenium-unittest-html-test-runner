from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import HtmlTestRunner

class GoogleSearchEngine(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome("C:/Users/Bharath/Desktop/chromedriver.exe")


    def setUp(self) -> None:
        self.browser.get("https://www.google.com")
        time.sleep(5)

    def testcase1SearchYoutube(self):
        self.browser.find_element(By.NAME, "q").send_keys("youtube")
        time.sleep(5)
        self.browser.find_element(By.NAME, "btnK").click()


    def testcase2searchMicrodegree(self):
        self.browser.find_element(By.NAME, "q").send_keys("Microdegree")
        time.sleep(5)
        self.browser.find_element(By.NAME, "btnK").click()

    def testcase3searchWin11(self):
        self.browser.find_element(By.NAME, "q").send_keys("windows11")
        time.sleep(5)
        self.browser.find_element(By.NAME, "btnK").click()

    def testcase4searchNetflix(self):
        self.browser.find_element(By.NAME, "q").send_keys("Netflix")
        time.sleep(5)
        self.browser.find_element(By.NAME, "btnK").click()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./reports/"))
