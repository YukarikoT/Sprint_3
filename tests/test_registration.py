from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls
from data import TestData

class TestRegistration:

    def test_registration_success(self, browser):
        browser.get(TestUrls.reg_url)
        browser.find_element(*TestLocators.NAME_INPUT_REG).send_keys(TestData.new_name)
        browser.find_element(*TestLocators.EMAIL_INPUT_REG).send_keys(TestData.new_email)
        browser.find_element(*TestLocators.PASSWORD_INPUT_REG).send_keys(TestData.password)
        browser.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.LOGIN_BUTTON_LOGIN))
        assert browser.current_url != TestUrls.reg_url, 'При валидных данных не выполнен переход к логину!'

    def test_registration_pass_error(self, browser):
        browser.get(TestUrls.reg_url)
        browser.find_element(*TestLocators.NAME_INPUT_REG).send_keys(TestData.new_name)
        browser.find_element(*TestLocators.EMAIL_INPUT_REG).send_keys(TestData.new_email)
        browser.find_element(*TestLocators.PASSWORD_INPUT_REG).send_keys(TestData.error_password)
        browser.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.PASSWORD_INPUT_ERROR_REG))
        assert browser.current_url == TestUrls.reg_url, 'При ошибке в пароле выполнен переход со страницы регистрации!'