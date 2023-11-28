from selenium.webdriver.common.by import By
from behave import given, when, then


@then("Verify Terms and Conditions page is opened")
def verify_tc_page(context):
    context.app.tc_page.verify_tc_page()


@when("Switch to the newly opened window")
def switch_to_tc_window(context):
    context.app.base.switch_tabs(context.app.base.store_windows(), 1)
