from selenium.webdriver.common.by import By
from selenium_generator.factories.page_factory import find_by


class LoginPage:

    _field_username = find_by(By.NAME, "username", cacheable=True)
    _field_password = find_by(By.NAME, "password", cacheable=True)
    _button_logout = find_by(By.XPATH, "//a/text()='Logout'", cacheable=True)
    _button_login = find_by(name="login", cacheable=True)

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("http://qualitypointtech.net/timesheetdemo/index.php")

    def login_positive(self, username, password):
        self.login(username, password)
        assert "report" in self._driver.current_url

    def login_negative(self, username, password):
        self.login(username, password)
        assert "report" not in self._driver.current_url

    def login(self, username, password):
        self._field_username().send_keys(username)
        self._field_password().send_keys(password)
        self._button_login().click()

    def logout(self):
        self._button_logout().click()
