"""This is the Parent class for all Test Classes"""

import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass