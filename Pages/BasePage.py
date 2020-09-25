"""This is the Super Class for all the Pages"""
from py._builtin import text
# from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""It contains all generic methods and utilities for all the pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    """Function to click on a specific element"""

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        """
        WebDriverWait(self.driver, 10) - This will wait for 10 sec to identify the locator,
        until(EC.visibility_of_element_located(by_locator)) -  We'll wait until identifying the specified locator
        click() - We'll click on the element
        Waiting for 10 seconds to identify the element and then clicking on the element
        """

    """This function to perform sendKeys action"""

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_elemet_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text
        # Wait till the element to be loaded, once it is located, store it in a variable
        # It is returning an element

    """To verify whether the element is visible or not"""

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
        # Whether the element is visible or not, it'll return a boolean value

    """For verifying the Title of the Page"""

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
