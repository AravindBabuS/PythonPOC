from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    """The list of By locator - Object Repository"""
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")


    """Create the Constructors and Page Class"""
    """Initializing the Driver"""

    def __init__(self, driver):
        super().__init__(driver)
        # super keyword is used to call the parent class constructor
        # In supre class (BasePage.py) we've initialized "__init__()"and passed the parameter "driver"
        self.driver.get(TestData.BASE_URL)

    """Page Actions for Login Page"""
    """Get the Login page Title"""

    def get_login_page_title(self, title):
        return self.get_title(title)

    """Verifying for signup link visibility"""

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    """Login into the Application"""

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        # After entering the credentials and by clicking on Login button, it's navigating to Authentication page
        # This method should return the object of next landing page
        return HomePage(self.driver)
