import pytest
import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture() # инициация вебдрайвера
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options)
    driver.get(data.url_main_page)
    yield driver
    driver.quit()


@pytest.fixture() # авторизация пользователя с главной страницы
def url(driver):
    driver.find_element(*TestLocators.BUTTON_ENTRANCE_IN_ACCOUNT).click() # найти и нажать кнопку "Войти в аккаунт"
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.INSCRIPTION_ENTRANCE))) #ждем, пока не отобразится надпись "Вход"
    driver.find_element(*TestLocators.EMAIL_USER).send_keys(data.my_login) # ищем и вводим логин
    driver.find_element(*TestLocators.PASSWORD_USER).send_keys(data.my_password) # ищем и вводим пароль
    driver.find_element(*TestLocators.BUTTON_ENTRANCE).click() # ищем и нажимаем кнопку "Войти"
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.BUTTON_CHECKOUT)))  # ждем, пока не будет кликабельна кнопка "Оформить заказ"
    url = driver.current_url # получаем url текущей страницы
    return url

