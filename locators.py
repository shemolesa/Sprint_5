from selenium.webdriver.common.by import By
class TestLocators:
    BUTTON_ENTRANCE_IN_ACCOUNT = By.XPATH, './/*[contains(@class,"button_button_size_large")]' # кнопка "Войти в аккаунт" на главной странице
    EMAIL_USER = (By.XPATH, ".//*[text()='Email']/following-sibling::input") # поле ввода логина
    PASSWORD_USER = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")   # поле ввода пароля
    NAME_USER = (By.XPATH, ".//*[text()='Имя']/following-sibling::input")  # поле ввода имени пользователя
    BUTTON_ENTRANCE = By.XPATH, './/*[contains(@class,"button_button_size_medium")]' # кнопка "Войти" на странице регистрации
    SEARCH_HEADER = By.XPATH, './/header[contains(@class, "AppHeader_header")]' # шапка главной страницы
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, './/a[@href="/account"]' # кнопка "Личный кабинет"
    LINK_REGISTER = By.XPATH, '.// a[contains( @ href, "/register")]' # ссылка "Зарегистрироваться"
    LINK_ENTRANCE_REGISTER = By.XPATH, '.// a[contains( @ href, "/login")]' # ссылка "Войти" со страницы регистрации
    RESTORE_PASSWORD = By.XPATH, '.// a[ @ href = "/forgot-password"]' # ссылка "Восстановить пароль"
    INSCRIPTION_RESTORE_PASSWORD = By.XPATH, '.// h2[text() = "Восстановление пароля"]' # надпись "Восстановление пароля" на странице восттановления пароля
    EMAIL_USER_PASSWORD_RECOVERY = By.XPATH, '.// input[contains( @class , "text_type_main-default")]' #поле ввода электронного адреса на странице восстановления пароля
    WARNING_INCORRECT_PASSWORD = By.XPATH, '.// p[text() = "Некорректный пароль"]' # сообщение "Некорректный пароль"
    BUTTON_REGISTER = By.XPATH, '.// button[text() = "Зарегистрироваться"]' # кнопка "Зарегистрироваться"
    INSCRIPTION_ENTRANCE = By.XPATH, '.// h2[text() = "Вход"]' # надпись "Вход" на странице входа
    TAB_PROFILE = By.XPATH, ' .// a[text() = "Профиль"]' # вкладка "Профиль"
    TAB_EXIT = By.XPATH, './/button[text()="Выход"]' # вкладка "Выход"
    BUTTON_CHECKOUT = By.XPATH, '.// button[text() = "Оформить заказ"]' # кнопка "Оформить заказ"
    BUTTON_CONSTRUCTOR = By.XPATH, '.// a[ @ href = "/"]' # кнопка "Конструктор"
    INSCRIPTION_ASSEMBLE_THE_BURGER = By.XPATH, './/h1[text() = "Соберите бургер"]' # надпись "Соберите бургер" на главной странице
    BUTTON_LOGO = By.XPATH, './/div[contains(@class, "AppHeader_header__logo")]' # логотип
    TAB_SAUCES = By.XPATH, '.// span[text() = "Соусы"]' #вкладка "Соусы"
    TAB_BUNS = By.XPATH, '.// span[text() = "Булки"]'  # вкладка "Булки"
    TAB_STUFFINGS = By.XPATH, '.// span[text() = "Начинки"]'  # вкладка "Начинки"
    MENU_SAUCES = By.XPATH, '.// span[text() = "Соусы"]' # меню "Соусы"
    MENU_BUNS = By.XPATH, '.// span[text() = "Булки"]'  # меню "Булки"
    MENU_STUFFINGS = By.XPATH, '.// span[text() = "Начинки"]'  # меню "Начинки"
    NAVIGATION_ACCOUNT = By.XPATH, '.// *[contains( @class , "Account_nav__Lgali")]' # раздел навигации в личном кабинете
    TAB_CURRENT = By.XPATH, '.// *[contains( @class , "tab_tab_type_current")]' # текущий раздел меню
