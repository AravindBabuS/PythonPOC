"""Write the Test Cases for Login"""

import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Test.test_base import BaseTest

"""from Config.config import TestData
from Pages.LoginPage import LoginPage
from Test.test_base import BaseTest
"""


class Test_Login(BaseTest):

    def test_signup_link_visible(self):
        # Create the Object of LoginPage Class
        self.loginPage = LoginPage(self.driver)

        # With the help of self.loginPage, call all the methods in LoginPage Class
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
