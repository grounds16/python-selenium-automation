from target_automation.pages.base import Base
from target_automation.pages.home_page import HomePage
from target_automation.pages.search_results_page import SearchResultsPage
from target_automation.pages.cart_page import CartPage
from target_automation.pages.login_page import LoginPage
from target_automation.pages.terms_and_conditions_page import TermsAndConditions

class Application:
    def __init__(self, driver):
        self.base = Base(driver)
        self.home_page = HomePage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.login_page = LoginPage(driver)
        self.tc_page = TermsAndConditions(driver)