import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")

class BaseClass:
    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):

        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def selectOptionByIndex(self, locator, index):

        dropdown = Select(locator)
        dropdown.select_by_index(index)


    def test_getLogger(self):
        loggerName = inspect.stack()[1][3]

        logger = logging.getLogger(loggerName)  # __name__ : catches the file name and display it in the logs

        fileHandler = logging.FileHandler('../Utilities/logfile.log')

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s ")

        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)

        return logger