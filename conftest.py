import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture
def get_driver(request):
    options = ChromeOptions()
    options.add_argument("--window-size=1200,900")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver