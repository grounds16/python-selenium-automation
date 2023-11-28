from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open sign in page')
def open_login(context):
    context.app.login_page.open_login_page()

@when('Store original windows')
def store_windows(context):
    context.app.base.store_windows()

@when("Click on Target terms and conditions link")
def click_tc(context):
    context.app.login_page.select_terms_and_conditions()



@then ("User can close new window and switch back to original")
def close_tc_window(context):
    context.app.base.close_tab()
    context.app.base.switch_tabs(context.app.base.store_windows(), 0)
    context.app.home_page.verify_signin_form()
