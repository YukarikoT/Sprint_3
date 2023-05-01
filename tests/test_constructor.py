from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls
from data import TestTexts

class TestConstructor:

    def test_const_go_to_toppings(self, get_driver):
        self.driver.get(TestUrls.main_url)
        self.driver.find_element(*TestLocators.TOPPINGS_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.TOPPINGS_BANNER))
        current_tab_text = self.driver.find_element(*TestLocators.CURRENT_TAB).text
        assert TestTexts.toppings_tab_text == current_tab_text
        self.driver.quit()

    def test_const_go_to_sauces(self, get_driver):
        self.driver.get(TestUrls.main_url)
        self.driver.find_element(*TestLocators.SAUCES_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SAUCES_BANNER))
        current_tab_text = self.driver.find_element(*TestLocators.CURRENT_TAB).text
        assert TestTexts.sauces_tab_text == current_tab_text
        self.driver.quit()

    def test_const_go_to_buns(self, get_driver):
        self.driver.get(TestUrls.main_url)
        self.driver.find_element(*TestLocators.TOPPINGS_BUTTON).click()
        self.driver.find_element(*TestLocators.BUNS_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUNS_BANNER))
        current_tab_text = self.driver.find_element(*TestLocators.CURRENT_TAB).text
        assert TestTexts.buns_tab_text == current_tab_text
        self.driver.quit()
