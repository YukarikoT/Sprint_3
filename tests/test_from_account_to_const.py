from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestFromAccountToConst:

    def test_click_const_button(self, url):
        driver = webdriver.Chrome()
        driver.get(url[2])
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))
        assert driver.current_url == url[0]
        driver.quit()

    def test_click_logo(self, url):
        driver = webdriver.Chrome()
        driver.get(url[2])
        driver.implicitly_wait(5)
        driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))
        assert driver.current_url == url[0]
        driver.quit()
