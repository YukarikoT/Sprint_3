from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls
from data import TestData

class TestRegistration:

    def test_registration_success(self, get_driver):
        self.driver.get(TestUrls.reg_url)
        self.driver.find_element(*TestLocators.NAME_INPUT_REG).send_keys(TestData.new_name)
        self.driver.find_element(*TestLocators.EMAIL_INPUT_REG).send_keys(TestData.new_email)
        self.driver.find_element(*TestLocators.PASSWORD_INPUT_REG).send_keys(TestData.password)
        self.driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.LOGIN_BUTTON_LOGIN))
        assert self.driver.current_url != TestUrls.reg_url
        self.driver.quit()

    def test_registration_pass_error(self, get_driver):
        self.driver.get(TestUrls.reg_url)
        self.driver.find_element(*TestLocators.NAME_INPUT_REG).send_keys(TestData.new_name)
        self.driver.find_element(*TestLocators.EMAIL_INPUT_REG).send_keys(TestData.new_email)
        self.driver.find_element(*TestLocators.PASSWORD_INPUT_REG).send_keys(TestData.error_password)
        self.driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.PASSWORD_INPUT_ERROR_REG))
        assert self.driver.current_url == TestUrls.reg_url
        self.driver.quit()