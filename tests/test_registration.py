from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

    def test_registration_success(self, url, data):
        driver = webdriver.Chrome()
        driver.get(url[1])
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,".//fieldset[1]//input").send_keys(data[0])
        driver.find_element(By.XPATH,".//fieldset[2]//input").send_keys(data[1])
        driver.find_element(By.NAME, "Пароль").send_keys(data[2])
        driver.find_element(By.TAG_NAME,"button").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
        assert driver.current_url != url[1]
        driver.quit()

    def test_registration_pass_error(self, url, data):
        driver = webdriver.Chrome()
        driver.get(url[1])
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(data[0])
        driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(data[1])
        driver.find_element(By.NAME, "Пароль").send_keys(data[3])
        driver.find_element(By.TAG_NAME, "button").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//p[text()='Некорректный пароль']")))
        assert driver.current_url == url[1]
        driver.quit()