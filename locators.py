from selenium.webdriver.common.by import By

class TestLocators:

# верхний блок
Constructor_Button = By.XPATH, ".//p[text()='Конструктор']" # кнопка «Конструктор»
Logo = By.CLASS_NAME, "AppHeader_header__logo__2D0X2" # логотип Stellar Burgers
Account_Button = By.XPATH, ".//p[text()='Личный Кабинет']" # кнопка «Личный Кабинет»

# главная
Login_Account_Button = By.XPATH, ".//button[text()='Войти в аккаунт']" # кнопка «Войти в аккаунт»
Make_Order_Button = By.XPATH, ".//button[text()='Оформить заказ']" # кнопка «Оформить Заказ»
Make_Burger_Banner = By.XPATH, ".//h1[text()='Соберите бургер']" # заголовок «Соберите бургер»
Buns_Button = By.XPATH, ".//span[text()='Булки']" # кнопка раздела «Булки»
Buns_Banner = By.XPATH, ".//h2[text()='Булки']" # заголовок «Булки»
Sauces_Button = By.XPATH, ".//span[text()='Соусы']" # кнопка раздела «Соусы»
Sauces_Banner = By.XPATH, ".//h2[text()='Соусы']" # заголовок «Соусы»
Toppings_Button = By.XPATH, ".//span[text()='Начинки']" # кнопка раздела «Начинки»
Toppings_Banner = By.XPATH, ".//h2[text()='Начинки']" # заголовок «Начинки»

# страница регистрации
Name_Input_Reg = By.XPATH,".//fieldset[1]//input" # поле ввода «Имя»
Email_Input_Reg = By.XPATH,".//fieldset[2]//input" # поле ввода «Email»
Password_Input_Reg = By.NAME, "Пароль" # поле ввода «Пароль»
Registration_Button = By.TAG_NAME,"button" # кнопка «Зарегистрироваться»
Password_Input_Reg_Error = By.XPATH, ".//p[text()='Некорректный пароль']" # поле «Пароль» с ошибкой «Некорректный пароль»
Login_Button_Reg = By.XPATH, ".//a[text()='Войти']" #кнопка «Войти»

# страница входа
Email_Input_Login = By.XPATH, ".//fieldset[1]//input" # поле ввода «Email»
Password_Input_Login = By.NAME, "Пароль" # поле ввода «Пароль»
Login_Button_Login = By.XPATH, ".//button[text()='Войти']" # кнопка «Войти»

# страница восстановления
Login_Button_Rec = By.XPATH, ".//a[text()='Войти']" # кнопка «Войти»

# личный кабинет
Logout_Button = By.XPATH, ".//button[text()='Выход']" # кнопка «Выход»