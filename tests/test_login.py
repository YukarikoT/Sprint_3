from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls
from data import TestData


class TestLogin:

    def test_login_from_main(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        browser.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(TestData.valid_email)
        browser.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(TestData.valid_password)
        browser.find_element(*TestLocators.LOGIN_BUTTON_LOGIN).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        assert browser.current_url == TestUrls.main_url, 'Логин с главной страницы не выполнен!'

    def test_login_from_account(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        browser.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(TestData.valid_email)
        browser.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(TestData.valid_password)
        browser.find_element(*TestLocators.LOGIN_BUTTON_LOGIN).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        assert browser.current_url == TestUrls.main_url, 'Логин из Личного кабинета не выполнен!'

    def test_login_from_registration_form(self, browser):
        browser.get(TestUrls.reg_url)
        browser.find_element(*TestLocators.LOGIN_BUTTON_REG).click()
        browser.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(TestData.valid_email)
        browser.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(TestData.valid_password)
        browser.find_element(*TestLocators.LOGIN_BUTTON_LOGIN).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        assert browser.current_url == TestUrls.main_url, 'Логин со страницы регистрации не выполнен!'

    def test_login_from_recovery_form(self, browser):
        browser.get(TestUrls.rec_url)
        browser.find_element(*TestLocators.LOGIN_BUTTON_RECOVERY).click()
        browser.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(TestData.valid_email)
        browser.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(TestData.valid_password)
        browser.find_element(*TestLocators.LOGIN_BUTTON_LOGIN).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        assert browser.current_url == TestUrls.main_url, 'Логин со страницы восстановления не выполнен!'

