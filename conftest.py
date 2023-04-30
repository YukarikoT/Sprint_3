import pytest
import names
import random


@pytest.fixture
def url():
    main_url = 'https://stellarburgers.nomoreparties.site/'
    reg_url = 'https://stellarburgers.nomoreparties.site/register'
    log_url = 'https://stellarburgers.nomoreparties.site/login'
    rec_url = 'https://stellarburgers.nomoreparties.site/forgot-password'
    return main_url, reg_url, log_url, rec_url


@pytest.fixture
def data():
    new_name = names.get_first_name(gender='female')
    new_email = f"kalinovskaya_9{random.randint(100,999)}@ya.ru"
    password = f"{random.randint(100000, 999999)}"
    error_password = f"{random.randint(10000, 99999)}"
    old_email = 'kalinovskaya_9199@ya.ru'
    old_password = 123456
    return new_name, new_email, password, error_password, old_email, old_password

