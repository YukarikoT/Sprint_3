from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls
from data import TestData

class TestLogOut:

    def test_logout_from_account(self, get_driver):
        self.driver.get(TestUrls.main_url)
        self.driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        self.driver.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(TestData.valid_email)
        self.driver.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(TestData.valid_password)
        self.driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        self.driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.LOGOUT_BUTTON)).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_LOGIN))
        assert self.driver.current_url == TestUrls.log_url
        self.driver.quit()

