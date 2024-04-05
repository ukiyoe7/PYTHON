from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify your credentials
username = "your_username"
password = "your_password"

# Specify the path to the folder where you want to export the data
download_folder = "/path/to/your/download/folder"

# Configure Selenium WebDriver to use Chrome
chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_folder}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get("https://prepagos.alelo.com.br/")

# Find and fill in the username and password fields, then submit the form
username_field = driver.find_element_by_id("username")
password_field = driver.find_element_by_id("password")
username_field.send_keys(username)
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Wait until the page loads after login
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "menu-1")))

# Access the cartoes page
cartoes_link = driver.find_element_by_xpath("//a[contains(@href,'/cartoes')]")
cartoes_link.click()

# Wait until the cartoes page loads
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "page-cartoes")))

# Select menu "incentivo"
menu_incentivo = driver.find_element_by_xpath("//a[contains(text(), 'Incentivo')]")
menu_incentivo.click()

# Wait for the content to load
time.sleep(5)  # Adjust this delay as needed

# Locate the search button and click on it
search_button = driver.find_element_by_id("search-button")
search_button.click()

# Wait for the download to complete
time.sleep(10)  # Adjust this delay as needed

# Close the browser
driver.quit()
