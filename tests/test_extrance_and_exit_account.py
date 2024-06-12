import pytest
import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators

class TestExtranceAccount:

# проверка входа по кнопке «Войти в аккаунт»/"Личный кабинет" на главной странице
    @pytest.mark.parametrize('locator', [TestLocators.BUTTON_ENTRANCE_IN_ACCOUNT, TestLocators.BUTTON_PERSONAL_ACCOUNT])
    def test_successful_login_from_home_page(self, driver, locator):
        driver.find_element(*locator).click() # ищем и нажимаем кнопку "Войти в аккаунт"/"Личный кабинет"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.INSCRIPTION_ENTRANCE))
        driver.find_element(*TestLocators.EMAIL_USER).send_keys(data.my_login) # ищем и вводим логин
        driver.find_element(*TestLocators.PASSWORD_USER).send_keys(data.my_password) # ищем и вводим пароль
        driver.find_element(*TestLocators.BUTTON_ENTRANCE).click()  # ищем и нажимаем кнопку "Войти"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.BUTTON_ENTRANCE_IN_ACCOUNT)))  # ждем, пока не отобразится кнопка "Оформить заказ"
        assert driver.find_element(*TestLocators.BUTTON_ENTRANCE_IN_ACCOUNT).text == 'Оформить заказ' # проверка кнопки "Оформить заказ" на главной странице

#проверка входа по ссылке со страницы регистрации/восстановления пароля
    @pytest.mark.parametrize('locator', [TestLocators.LINK_REGISTER, TestLocators.RESTORE_PASSWORD])
    def test_successful_login_from_registration_and_recovery_pages(self, driver, locator):
        driver.find_element(*TestLocators.BUTTON_ENTRANCE_IN_ACCOUNT).click() # ищем и нажимаем кнопку "Войти в аккаунт"
        element = driver.find_element(*locator)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.find_element(*locator).click() # ищем и кликаем ссылку "Зарегистрироваться"/"Восстановить пароль"
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
          (TestLocators.LINK_ENTRANCE_REGISTER)))  # ждем, пока не будет кликабельна ссылка "Войти"
        driver.find_element(*TestLocators.LINK_ENTRANCE_REGISTER).click() # ищем и кликаем ссылка "Войти"
        driver.find_element(*TestLocators.EMAIL_USER).send_keys(data.my_login) # ищем и вводим логин
        driver.find_element(*TestLocators.PASSWORD_USER).send_keys(data.my_password) # ищем и вводим пароль
        driver.find_element(*TestLocators.BUTTON_ENTRANCE).click() # ищем и нажимаем кнопку "Войти"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.BUTTON_ENTRANCE_IN_ACCOUNT)))  # ждем, пока не отобразится кнопка "Оформить заказ"
        assert driver.find_element(*TestLocators.BUTTON_ENTRANCE_IN_ACCOUNT).text == 'Оформить заказ' # проверка кнопки "Оформить заказ" на главной странице

# проверка выхода из профиля
    def test_logout_from_account(self, driver, url):
        driver.get(url)
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click() # найти и нажать кнопку "Личный кабинет"
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.TAB_PROFILE))) #ждем, пока не будет кликабельна вкладка "Профиль"
        driver.find_element(*TestLocators.TAB_EXIT).click() # найти и нажать кнопку "Выход"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.INSCRIPTION_ENTRANCE))) #ждем, пока не будет отображена надпись "Вход"
        assert driver.find_element(*TestLocators.INSCRIPTION_ENTRANCE) # проверяем наличие надписи "Вход" на странице входа
