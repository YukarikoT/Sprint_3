from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls


class TestFromAccountToConst:

    def test_click_const_button(self, get_driver):
        self.driver.get(TestUrls.log_url)
        self.driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_BURGER_BANNER))
        assert self.driver.current_url == TestUrls.main_url
        self.driver.quit()

    def test_click_logo(self, get_driver):
        self.driver.get(TestUrls.log_url)
        self.driver.find_element(*TestLocators.LOGO_MAIN).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_BURGER_BANNER))
        assert self.driver.current_url == TestUrls.main_url
        self.driver.quit()
