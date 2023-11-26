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
def select_cart(context):
    items = context.driver.find_elements(By.XPATH, "//div[@class='h-display-flex h-flex-justify-space-between']")
    add_to_cart = context.driver.find_elements(By.XPATH, f"//button[contains(@id, 'addToCartButton')]")
    counter = 0
    for item in items:
        if context.product in item.text:
            context.fullProductsName = item.text
            add_to_cart[counter].click()
            break
        else:
            counter += 1
    context.driver.wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h4[class*='StyleHeading']")),
        message="Product name not shown in side navigation")
    context.driver.find_element(By.XPATH, "//button[@aria-label='close']").click()


@then('Verify item is in cart')
def verify_item_is_in_cart(context):
    item_in_cart = context.driver.find_element(By.XPATH, "//div[@data-test='cartItem-title']").text
    assert item_in_cart == context.fullProductsName, f"item in cart ('{item_in_cart}') does not match products name ('{context.fullProductsName}')"


@then('Verify colors matches title')
def verify_colors_are_matching_titles(context):
    expected_colors = ["Brown", "Oatmeal", "Gray", "Black"]
    actual_color = context.driver.find_element(By.XPATH, '//div[contains(@class, "styles__BaseVariationSelectorWrapper")][2]/div[1]')
    color_checkbox = context.driver.find_elements(By.XPATH, "//div[contains(@class, 'styles__ButtonWrapper')]/a/img")

    for counter in range(0, len(color_checkbox) - 1):
        color_checkbox[counter].click()
        assert expected_colors[counter] in actual_color.text, f"Actual Color: '{actual_color.text}' does not match Expected Color: '{expected_colors[counter]}'"
