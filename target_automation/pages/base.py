from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Base:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)
    def input(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def assert_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f"Actual text: '{actual_text}' does not match Expected text: '{expected_text}'"

    def store_windows(self):
        return self.driver.window_handles

    def switch_tabs(self, windows, tab_index):
        self.driver.switch_to.window(windows[tab_index])

    def close_tab(self):
        self.driver.close()