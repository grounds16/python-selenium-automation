from target_automation.pages.base import Base
from selenium.webdriver.common.by import By
class LoginPage(Base):
    terms_and_conditions = (By.XPATH, "//a[@aria-label='terms & conditions - opens in a new window']")
    def open_login_page(self):
        self.open_url('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')

    def select_terms_and_conditions(self):
        self.click(*self.terms_and_conditions)