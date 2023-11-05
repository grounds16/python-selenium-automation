from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.ID, "nav-orders").click()
sleep(2)
signin_header = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
email_field = driver.find_element(By.ID, "ap_email")
assert signin_header.is_displayed(), "Sign in is not displayed"
assert email_field.is_displayed(), "Email Field is not displayed"
