from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then



@then('Verify search worked for {product}')
def verify_search(context, product):
    context.app.search_results_page.verify_search_result(product)


@then('Verify {product} in search result url')
def verify_search_url(context, product):
    context.app.search_results_page.verify_serach_url(product)


@then('Verify item is found and select cart')
def find_item_and_add_to_cart(context):
    context.app.search_results_page.find_item_and_add_to_cart(context.app.home_page.product)



@then('Verify colors matches title')
def verify_colors_are_matching_titles(context):
    expected_colors = ["Brown", "Oatmeal", "Gray", "Black"]
    actual_color = context.driver.find_element(By.XPATH, '//div[contains(@class, "styles__BaseVariationSelectorWrapper")][2]/div[1]')
    color_checkbox = context.driver.find_elements(By.XPATH, "//div[contains(@class, 'styles__ButtonWrapper')]/a/img")

    for counter in range(0, len(color_checkbox) - 1):
        color_checkbox[counter].click()
        assert expected_colors[counter] in actual_color.text, f"Actual Color: '{actual_color.text}' does not match Expected Color: '{expected_colors[counter]}'"
