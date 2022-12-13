import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestDemoQA(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_Text_Box(self):
        #steps
        web = self.browser
        web.get("https://demoqa.com/text-box")
        web.maximize_window()
        time.sleep(1)
        web.find_element(By.ID,"userName").send_keys("test")
        time.sleep(1)
        web.find_element(By.ID,"userEmail").send_keys("test@gmail.com")
        time.sleep(1)
        web.find_element(By.ID,"currentAddress").send_keys("Jalan Test")
        time.sleep(1)
        web.find_element(By.ID,"permanentAddress").send_keys("Kota Test")
        web.find_element(By.ID,"submit").send_keys(Keys.ENTER)
        time.sleep(5)
    
    def test_links(self):
        #steps
        web = self.browser
        web.get("https://demoqa.com/links")
        web.maximize_window()
        time.sleep(1)
        web.find_element(By.XPATH,"//a[@id='simpleLink']").click
        time.sleep(2)

    def test_new_tab_and_window(self):
        #steps
        web = self.browser
        web.get("https://demoqa.com/browser-windows")
        web.maximize_window()
        time.sleep(1)
        web.find_element(By.ID,"tabButton").send_keys(Keys.ENTER)
        time.sleep(2)
        web.find_element(By.ID,"windowButton").send_keys(Keys.ENTER)
        time.sleep(2)
    
    def test_alert(self):
        #steps
        web = self.browser
        web.get("https://demoqa.com/alerts")
        web.maximize_window()
        time.sleep(1)
        web.find_element(By.ID,"alertButton").send_keys(Keys.ENTER)
        time.sleep(2)
    
    def test_login_wrong(self):
        web = self.browser
        web.get("https://demoqa.com/login")
        web.maximize_window()
        time.sleep(1)
        web.find_element(By.ID,"userName").send_keys("test")
        web.find_element(By.ID,"password").send_keys("test123")
        web.find_element(By.ID,"login").send_keys(Keys.ENTER)
        time.sleep(5)
    
    def tearDown(self):
        self.browser.close()
    
if __name__ == "__main__": 
    unittest.main()







