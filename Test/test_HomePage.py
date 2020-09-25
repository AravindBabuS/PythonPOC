
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Test.test_base import BaseTest


class Test_Home(BaseTest):

    def test_home_page_titele(self):
        """
        For verifying the Home Page Title, first we need to login into application
        For logging in, already defined the credentials and required methods, we need to call the same
        We need to create the instance of Login Class and make use of it
        """

        self.logiPage = LoginPage(self.driver)
        # Login page constructor will be called and request for the driver
        # The driver will be provided to the Parent class constructor
        # After getting the login page reference, we can call all the methods of Login page

        homePage = self.logiPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        pageTitle = homePage.get_home_page_title(TestData.AUTH_PAGE_TITLE)
        assert pageTitle == TestData.AUTH_PAGE_TITLE

    def test_loging_auth_code_validate(self):
        self.logiPage = LoginPage(self.driver)
        homePage = self.logiPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header = homePage.get_header_value()
        assert header == TestData.AUTH_PAGE_HEADER
