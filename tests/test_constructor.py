from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:

    def test_const_go_to_toppings(self, url):
        driver = webdriver.Chrome()
        driver.get(url[0])
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Начинки']")))
        driver.quit()

    def test_const_go_to_sauces(self, url):
        driver = webdriver.Chrome()
        driver.get(url[0])
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Соусы']")))
        driver.quit()

    def test_const_go_to_buns(self, url):
        driver = webdriver.Chrome()
        driver.get(url[0])
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
        driver.find_element(By.XPATH, ".//span[text()='Булки']").click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Булки']")))
        driver.quit()
