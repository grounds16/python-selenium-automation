from target_automation.pages.base import Base
from selenium.webdriver.common.by import By
class HomePage(Base):

    search_field = (By.ID, 'search')
    search_button = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    cart_button = (By.XPATH, "//div[@data-test='@web/CartIcon']")
    def open_main(self):
        self.open_url('https://www.target.com/')

    def search(self, product):
        self.input(product, *self.search_field)
        self.click(*self.search_button)

    def cart(self):
        self.click(*self.cart_button)
