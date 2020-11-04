from selenium.webdriver.common.by import By
from PageObjects.CheckoutPage import CheckOutPage


class HomePage():

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    email = (By.CSS_SELECTOR, "input[name ='email']")
    name = (By.XPATH, "//div[@class='container']/form[1]/div[1]/input")
    checkMe = (By.ID, "exampleCheck1")
    genderList = (By.ID, "exampleFormControlSelect1")
    submitButton = (By.XPATH, "//input[@type='submit']")
    successMessage = (By.CLASS_NAME, "alert-success")

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
        #  driver.find_element_by_css_selector("a[href*='shop']")

    def getNameField(self):
        return self.driver.find_element(*HomePage.name)

    def getEmailField(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckMe(self):
        return self.driver.find_element(*HomePage.checkMe)

    def getGender(self):
        return self.driver.find_element(*HomePage.genderList)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submitButton)

    def displaySuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage).text
