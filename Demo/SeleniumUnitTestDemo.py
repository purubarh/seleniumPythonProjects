#https://pypi.org/project/html-testRunner/

import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../Drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Automation step by step - Google Search")

    def test_search_2(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Raghav Pal")
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Raghav Pal - Google Search")

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/purushottamkumar/PycharmProjects/seleniumProjects/Reports'), verbosity=0)
