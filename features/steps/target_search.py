from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[data-test='@web/Search/SearchButton']").click()
    sleep(6)

@then('Verify search worked')
def verify_search(context):
    search_results_header = context.driver.find_element(By.XPATH, "//h2[@class='styles__StyledHeading']/span")