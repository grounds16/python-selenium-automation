from target_automation.pages.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class SearchResultsPage(Base):
    search_results = (By.XPATH, "//div[@class='h-display-flex']/span")
    items = (By.XPATH, "//div[@class='h-display-flex h-flex-justify-space-between']")
    add_to_cart_button = (By.XPATH, f"//button[contains(@id, 'addToCartButton')]")
    close_button = (By.XPATH, "//button[@aria-label='close']")
    full_product_name = ''
    def verify_search_result(self, product):
        results = self.find_element(*self.search_results).text
        assert product in results, f"{product}, is not in {results}"
    def verify_serach_url(self, product):
        search_url = self.driver.current_url
        assert product in search_url, f"{product}, is not in {search_url}"

    def find_item_and_add_to_cart(self, product):
        items_list = self.find_elements(*self.items)
        add_to_cart = self.find_elements(*self.add_to_cart_button)
        counter = 0

        for item in items_list:
            if product in item.text:
                self.full_product_name = item.text
                add_to_cart[counter].click()
                break
            else:
                counter += 1

        self.driver.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h4[class*='StyledHeading']")),
            message="Product name not shown in side navigation")
        self.click(*self.close_button)