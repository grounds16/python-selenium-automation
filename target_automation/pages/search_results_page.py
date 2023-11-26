from target_automation.pages.base import Base
from selenium.webdriver.common.by import By
class SearchResultsPage(Base):
    search_results = (By.XPATH, "//div[@class='h-display-flex']/span")
    def verify_search_result(self, product):
        results = self.find_element(*self.search_results).text
        assert product in results, f"{product}, is not in {results}"
    def verify_serach_url(self, product):
        search_url = self.driver.current_url
        assert product in search_url, f"{product}, is not in {search_url}"
