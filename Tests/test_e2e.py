
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckoutPage import CheckOutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):

        logger = self.test_getLogger()

        homePage = HomePage(self.driver)

        checkOutPage = homePage.shop_items()

        logger.info("Getting all card titles")

        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i+1
            cardText = card.text
            logger.info(cardText)

            if cardText == "BlackBerry":
                checkOutPage.getCardFooter()[i].click()

        self.driver.find_element_by_partial_link_text("Checkout").click()

        confirmPage = checkOutPage.CheckOutItems()

        logger.info("Entering country name")

        confirmPage.getCountryBox().send_keys("F")

        self.verifyLinkPresence("France")

        confirmPage.getSelectedCountry().click()

        confirmPage.getCheckbox().click()

        confirmPage.getSubmitButton().click()

        Message = self.driver.find_element_by_class_name("alert-success").text

        logger.info("Message received from application is" +Message)

        assert "Success!" in Message

        self.driver.get_screenshot_as_file("../Screenshots/screen.png")

        self.driver.quit()


