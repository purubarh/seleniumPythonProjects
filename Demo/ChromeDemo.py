from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#from selenium.webdriver.chrome.options import Options
#chrome_options = Options()

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="../Drivers/chromedriver")

driver.get("https://www.google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
print(driver.title)
driver.close()
driver.quit()
print("Run successfully completed")
