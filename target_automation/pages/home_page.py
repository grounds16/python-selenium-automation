from target_automation.pages.base import Base
from selenium.webdriver.common.by import By
class HomePage(Base):

    cart_button = (By.XPATH, "//div[@data-test='@web/CartIcon']")
    search_field = (By.ID, 'search')
    search_button = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    signin = (By.XPATH, "//span[contains(@class, 'styles__LinkText')]")
    signin_side_menu = (By.XPATH, "//a[@data-test='accountNav-signIn']")
    signin_text = (By.XPATH, "//h1[contains(@class,'styles__StyledHeading')]/span")
    product = ''


    def open_main(self):
        self.open_url('https://www.target.com/')

    def search(self, product):
        self.product = product
        self.input(product, *self.search_field)
        self.click(*self.search_button)

    def cart(self):
        self.click(*self.cart_button)

    def click_signin(self):
        self.click(*self.signin)

    def click_signin_from_account_menu(self):
        self.click(*self.signin_side_menu)

    def verify_signin_form(self):
        actual_message = self.find_element(*self.signin_text).text
        expected_message = "Sign into your Target account"
        assert actual_message == expected_message, f"Sign in message does match, actual message = {actual_message}"

