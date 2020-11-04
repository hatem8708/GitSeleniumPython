from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    countryBox = (By.ID, "country")

    selectedCountry = (By.CSS_SELECTOR, "div.suggestions ul:nth-child(2) li a")

    checkbox = (By.CSS_SELECTOR, "label[for='checkbox2']")

    submitButton = (By.CSS_SELECTOR, "input[type='submit']")

    def getCountryBox(self):
        return self.driver.find_element(*ConfirmPage.countryBox)

    def getSelectedCountry(self):
        return self.driver.find_element(*ConfirmPage.selectedCountry)

    def getCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.submitButton)