from target_automation.pages.base import Base
from selenium.webdriver.common.by import By
class CartPage(Base):
    actual_message = (By.XPATH, "//div[@data-test='boxEmptyMsg']")
    items_in_cart = (By.XPATH, "//div[@data-test='cartItem-title']")
    def cart_empty(self):
        actual_text = self.find_element(*self.actual_message).text
        expected_text = "Your cart is empty"
        assert actual_text == expected_text, f"Cart is not empty, actual message is {actual_text}"

    def verify_item_is_in_cart(self, full_product_name):
        item_in_cart = self.find_element(*self.items_in_cart)
        assert full_product_name in item_in_cart.text, f"item in cart ('{item_in_cart}') does not match products name ('{full_product_name}')"