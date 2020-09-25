from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    AUTH_CODE = (By.ID, "code")
    HEADER = (By.XPATH, "//html//body//div//div//div//div//div//div//h1//i18n-string")
    # ACCOUNT_NAME = (By.CSS_SELECTOR, "account-name")
    # SETTINGS_ICON = (By.ID,"navSetting")

    def __init__(self,driver):
        super().__init__(driver)
        # While we are calling super() class constructor, it's calling its base class constructor
        # Providing the same driver here

    def get_home_page_title(self, pageTitle):
        return self.get_title(pageTitle)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_elemet_text(self.HEADER)

    def get_login_auth_code_visible(self):
        return self.is_visible(self.AUTH_CODE)
