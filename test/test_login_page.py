import time
from base.base_test import BaseTest

class TestLoginPage(BaseTest):

    def test_login_page(self):
        self.login_page.open_page()
        time.sleep(5)
        self.login_page.fill_username_field("Admin")
        self.login_page.fill_password("admin123")
        self.login_page.click_login_button()
        time.sleep(5)
        self.dashboard_page.click_helper_icon()
        time.sleep(5)