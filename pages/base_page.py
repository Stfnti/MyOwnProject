from selenium.webdriver.chrome.webdriver import WebDriver
from metaclasses.meta_locators import MetaLocator


class BasePage(metaclass=MetaLocator):

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open_page(self):
        self.driver.get(self._PAGE_URL)