ПРОЕКТ АВТОМАТИЗАЦИИ ТЕСТИРОВАНИЯ ДЛЯ СЕРВИСА Stellar Burgers

Stellar Burgers - это космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.

1. Основа для написания автотестов — фреймворк pytest
2. Используемые библиотеки: selenium, names, random
3. Главная страница сервиса - https://stellarburgers.nomoreparties.site/

Содержание:

1. readme.md - файл с описанием тестов

2. conftest.py - файл с фикстурами:
  2.1. фикстура url содержит адреса сервиса
  2.2. фикстура data содержит данные для аккаунтов, 
  где переменые new_name, new_email и password генерируются для каждого теста рандомно с помощью функций
  
3. locators.py - файл со списком элементов-локаторов, используемых в тестах

4. tests - папка с автоматизированными тестами для проверки основного функционала stellarburgers:

  4.1. test_registration.py - тесты проверяющие регистрацию: 
         test_registration_success - положительная проверка, все данные корректны
		 test_registration_pass_error - отрицательная проверка, ошибка "некорректный пароль"
		 
  4.2. test_login.py - тесты проверяющие вход в учётную записью:
         test_login_from_main - проверка входа по кнопке «Войти в аккаунт» на главной странице
		 test_login_from_account - проверка входа через кнопку «Личный кабинет»
		 test_login_from_registration_form - проверка входа через кнопку в форме регистрации
		 test_login_from_recovery_form - проверка входа через кнопку в форме восстановления пароля
		
  4.3. test_go_to_account.py - тесты проверяющие переход в личный кабинет
         test_go_to_account - проверка перехода по клику на «Личный кабинет»
		
  4.4. test_from_account_to_const.py - тесты проверяющие переход из личного кабинета в конструктор
         test_click_const_button - проверка перехода по клику на «Конструктор»
		 test_click_logo - проверка перехода по клику на на логотип Stellar Burgers
		
  4.5. test_logout.py - тесты проверяющие выход из учётной записи
         test_logout_from_account - проверка выхода по кнопке «Выйти» в личном кабинете
		 
  4.6. test_constructor.py - тесты проверяющие раздел "Конструктор"
         test_const_go_to_toppings - проверка перехода к разделу "Начинки"
		 test_const_go_to_sauces - проверка перехода к разделу "Соусы"
		 test_const_go_to_buns - проверка перехода к разделу "Булки"
