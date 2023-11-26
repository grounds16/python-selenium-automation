from target_automation.pages.base import Base
from selenium.webdriver.common.by import By
class CartPage(Base):
    actual_message = (By.XPATH, "//div[@data-test='boxEmptyMsg']")

    def cart_empty(self):
        actual_text = self.find_element(*self.actual_message).text
        expected_text = "Your cart is empty"
        assert actual_text == expected_text, f"Cart is not empty, actual message is {actual_text}"