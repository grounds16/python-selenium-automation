from behave import given, when, then

@then('Verify Cart is empty')
def verify_empty_cart(context):
    context.app.cart_page.cart_empty()
