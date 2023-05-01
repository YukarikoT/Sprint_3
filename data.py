import names
import random

class TestUrls:
    main_url = 'https://stellarburgers.nomoreparties.site/'
    reg_url = 'https://stellarburgers.nomoreparties.site/register'
    log_url = 'https://stellarburgers.nomoreparties.site/login'
    rec_url = 'https://stellarburgers.nomoreparties.site/forgot-password'

class TestData:
    new_name = names.get_first_name(gender='female')
    new_email = f"kalinovskaya_9{random.randint(100,999)}@ya.ru"
    password = f"{random.randint(100000, 999999)}"
    error_password = f"{random.randint(10000, 99999)}"
    valid_email = 'kalinovskaya_9199@ya.ru'
    valid_password = 123456

class TestTexts:
    buns_tab_text = 'Булки'
    sauces_tab_text = 'Соусы'
    toppings_tab_text = 'Начинки'