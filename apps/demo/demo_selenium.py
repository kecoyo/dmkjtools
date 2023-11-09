from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.ljlx.com/"
driver = webdriver.Chrome()
driver.get(url)

for quote in driver.find_elements(By.CSS_SELECTOR, ".img-bg img"):
    print(quote.get_attribute("src"))

driver.quit()
