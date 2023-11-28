from target_automation.pages.base import Base
from selenium.webdriver.common.by import By

class TermsAndConditions(Base):
    title = (By.XPATH, "//h1[@data-test='page-title']")
    expected_title_text = "Terms & Conditions"
    def verify_tc_page(self):
        self.assert_text(self.expected_title_text, *self.title)