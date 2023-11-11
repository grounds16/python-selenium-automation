from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(6)


@then('Verify search worked for {product}')
def verify_search(context, product):
    search_results = context.driver.find_element(By.XPATH, "//h2[contains(@class,'styles__StyledHeading')]/span[@class='h-margin-r-x2']").text
    assert product in search_results , f"{product}, is not in {search_results}"
@then('Verify {product} in search result url')
def verify_search_url(context, product):
    search_url = context.driver.current_url
    assert product in search_url, f"{product}, is not in {search_url}"
