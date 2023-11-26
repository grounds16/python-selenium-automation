from behave import given, when, then

@then('Verify Cart is empty')
def verify_empty_cart(context):
    context.app.cart_page.cart_empty()

@then('Verify item is in cart')
def verify_item_is_in_cart(context):
    context.app.cart_page.verify_item_is_in_cart(context.app.search_results_page.full_product_name)
