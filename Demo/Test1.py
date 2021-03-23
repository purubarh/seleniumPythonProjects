import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("../Drivers/chromedriver")
driver.set_page_load_timeout(10)
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
time.sleep(2)
driver.close()
driver.quit()
print("First Selenium Python Script Completed Successfully")
