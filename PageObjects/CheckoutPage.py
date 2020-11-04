from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    chceckOutButton = (By.XPATH, "//button[@class ='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def CheckOutItems(self):
        self.driver.find_element(*CheckOutPage.chceckOutButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage