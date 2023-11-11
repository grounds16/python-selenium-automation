from selenium.webdriver.common.by import By
from behave import given, when, then


@given('User navigates to target circle')
def navigate_to_target_circle(context):
    context.driver.get('https://www.target.com/circle')


@when('User selects the cart button')
def selects_cart(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()


@then('Verify Cart is empty')
def verify_empty_cart(context):
    actual_message = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    expected_message = "Your cart is empty"
    assert actual_message == expected_message, f"Cart is not empty, actual message is {actual_message}"


@when('User selects Signin')
def user_selects_signin(context):
    context.driver.find_element(By.XPATH, "//span[contains(@class, 'styles__LinkText')]").click()


@when('User selects Signin from the sign menu')
def user_selects_signin_from_side_menu(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()


@then('Verify Signin Form is displayed')
def verify_signin_is_displayed(context):
    actual_message = context.driver.find_element(By.XPATH, "//h1[contains(@class,'styles__StyledHeading')]/span").text
    expected_message = "Sign into your Target account"
    assert actual_message == expected_message, f"Sign in message does match, actual message = {actual_message}"


@then('Verify there {number} benefit cards are displayed')
def verify_the_amount_of_benefits(context, number):
    amount_benefit_cards = len(context.driver.find_elements(By.XPATH, "//li[contains(@class, 'styles__BenefitCard')]"))
    assert amount_benefit_cards == int(number), f"Amount of benefit cards ({amount_benefit_cards}) does not match the expected ({number})"
