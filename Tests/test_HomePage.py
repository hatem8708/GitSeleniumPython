import pytest

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        homepage= HomePage(self.driver)
        homepage.getNameField().send_keys(getData["firstname"])
        homepage.getEmailField().send_keys(getData["email"])
        homepage.getCheckMe().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])

        homepage.getSubmitButton().click()

        alertText = homepage.displaySuccessMessage()

        assert "Success" in alertText
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param


