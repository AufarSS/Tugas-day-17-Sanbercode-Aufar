import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class testday17(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_edit_activity(self):
        #steps
        web = self.browser
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        web.maximize_window()
        time.sleep(5)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(3)
    
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
