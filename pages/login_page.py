from pages.base_page import BasePage


class LoginPage(BasePage):
    _PAGE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    _USER_NAME_FIELD = "//input[@placeholder='Username']"
    _PASSWORD_FIELD = "//input[@placeholder='Password']"
    _LOGIN_BUTTON = "//button[contains(@class, 'orangehrm-login-button')]"

    def fill_username_field(self, username) -> None:
        field = self.driver.find_element(*self._USER_NAME_FIELD)
        field.send_keys(username)

    def fill_password(self, password) -> None:
        field = self.driver.find_element(*self._PASSWORD_FIELD)
        field.send_keys(password)

    def click_login_button(self) -> None:
        self.driver.find_element(*self._LOGIN_BUTTON).click()
