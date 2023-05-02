from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls
from data import TestTexts

class TestConstructor:

    def test_const_go_to_toppings(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.TOPPINGS_BUTTON).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.TOPPINGS_BANNER))
        current_tab_text = browser.find_element(*TestLocators.CURRENT_TAB).text
        assert TestTexts.toppings_tab_text == current_tab_text, 'Переход к вкладке "Начинки" не выполнен!'

    def test_const_go_to_sauces(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.SAUCES_BUTTON).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SAUCES_BANNER))
        current_tab_text = browser.find_element(*TestLocators.CURRENT_TAB).text
        assert TestTexts.sauces_tab_text == current_tab_text, 'Переход к вкладке "Соусы" не выполнен!'

    def test_const_go_to_buns(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.TOPPINGS_BUTTON).click()
        browser.find_element(*TestLocators.BUNS_BUTTON).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUNS_BANNER))
        current_tab_text = browser.find_element(*TestLocators.CURRENT_TAB).text
        assert TestTexts.buns_tab_text == current_tab_text, 'Переход к вкладке "Булки" не выполнен!'
