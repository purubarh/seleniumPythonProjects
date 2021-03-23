from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://www.google.com")
print(driver.title)
driver.close()
driver.quit()
print("Run completed successfully")
