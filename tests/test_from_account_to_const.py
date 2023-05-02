from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls


class TestFromAccountToConst:

    def test_click_const_button(self, browser):
        browser.get(TestUrls.log_url)
        browser.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_BURGER_BANNER))
        assert browser.current_url == TestUrls.main_url, 'Переход по кнопке "Конструктор" не выполнен!'

    def test_click_logo(self, browser):
        browser.get(TestUrls.log_url)
        browser.find_element(*TestLocators.LOGO_MAIN).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_BURGER_BANNER))
        assert browser.current_url == TestUrls.main_url, 'Переход по логотипу не выполнен!'
