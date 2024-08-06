from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the webdriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://shopee.co.id/search?keyword=Earphone%20Wireless")
driver.execute_script("window.scrollTo(0, 1000);")
time.sleep(15)

# Find the div element you want to click by its text content using By.XPATH
div_element = driver.find_element(By.XPATH, "//div[text()='Terlaris']")
time.sleep(15)
# Click the div element
div_element.click()
time.sleep(15)
# Close the browser
driver.quit()