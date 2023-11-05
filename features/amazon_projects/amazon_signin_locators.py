from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/ap/signin')

logo = driver.find_element(By.XPATH, "//i[@role='img']")
email = driver.find_element(By.ID, "ap_email")
continue_button = driver.find_element(By.ID, 'continue')
conditions = driver.find_element(By.LINK_TEXT, 'Conditions of Use')
privacy = driver.find_element(By.LINK_TEXT, ' Privacy Notice')
help_link = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
forgot_pw = driver.find_element(By.ID, "auth-fpp-link-bottom")
other_issues = driver.find_element(By.ID, "ap-other-signin-issues-link")
create_account_button = driver.find_element(By.ID, "createAccountSubmit")
