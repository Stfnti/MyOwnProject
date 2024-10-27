from pages.base_page import BasePage


class DashboardPage(BasePage):
    _PAGE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    _HELPER_ICON = "//i[@class='oxd-icon bi-question-lg']"

    def click_helper_icon(self) -> None:
        self.driver.find_element(*self._HELPER_ICON).click()