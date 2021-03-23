import time
import unittest

import HtmlTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POMDemo.Pages.homePage import HomePage
from POMDemo.Pages.loginPage import LoginPage


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/purushottamkumar/PycharmProjects/seleniumProjects/Reports'), verbosity=0)
