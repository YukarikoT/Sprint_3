from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogOut:

    def test_logout_from_account(self, url, data):
        driver = webdriver.Chrome()
        driver.get(url[0])
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(data[4])
        driver.find_element(By.NAME, "Пароль").send_keys(data[5])
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        driver.find_element(By.XPATH, ".//button[text()='Выход']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
        assert driver.current_url == url[2]
        driver.quit()


