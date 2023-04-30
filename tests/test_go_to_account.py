from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestGoToAccount:

    def test_go_to_account(self, url):
        driver = webdriver.Chrome()
        driver.get(url[0])
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
        assert driver.current_url == url[2]
        driver.quit()