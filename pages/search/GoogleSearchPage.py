from selenium.webdriver.common.by import By
from selenium_generator.factories.page_factory import find_by
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage:

    _field_search = find_by(By.NAME, "q", cacheable=True)
    _button_search = find_by(name="btnK", cacheable=True)

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.google.com/")

    def search_positive(self, search_text):
        self._field_search().send_keys(search_text)
        self._field_search().send_keys(Keys.RETURN)
        assert "search" in self._driver.current_url

    def search_negative(self, search_text):
        self._field_search().send_keys(search_text)
        self._field_search().send_keys(Keys.RETURN)
        assert "search" not in self._driver.current_url
