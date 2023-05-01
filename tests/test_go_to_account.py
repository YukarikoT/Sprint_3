from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls

class TestGoToAccount:

    def test_go_to_account(self, get_driver):
        self.driver.get(TestUrls.main_url)
        self.driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_LOGIN))
        assert self.driver.current_url == TestUrls.log_url
        self.driver.quit()