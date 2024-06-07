from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators

class TestRegistration:

# проверка успешной регистрации
    def test_successful_registration(self, driver, generated_login):
       driver.find_element(*TestLocators.BUTTON_ENTRANCE_IN_ACCOUNT).click() # найти и нажать кнопку "Войти в аккаунт"
       WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, '.// a[contains( @ href, "/register")]'))) #ждем, пока не будет кликабельна ссылка "Зарегистрироваться"
       driver.find_element(*TestLocators.LINK_REGISTER).click() # ищем и нажимаем ссылку "Зарегистрироваться"
       driver.find_element(*TestLocators.NAME_USER).send_keys(generated_login) # ищем и вводим имя
       driver.find_element(*TestLocators.EMAIL_USER).send_keys(generated_login) # ищем и вводим логин
       driver.find_element(*TestLocators.PASSWORD_USER).send_keys('1234567') # ищем и вводим пароль
       driver.find_element(*TestLocators.BUTTON_REGISTER).click() # ищем и нажимаем кнопку "Зарегистрироваться"
       driver.implicitly_wait(3)
       assert driver.find_element(*TestLocators.INSCRIPTION_ENTRANCE) # проверяем наличие надпии "Вход"


# проверка обработки ошибки для некорректного пароля (1-5 символов)
    def test_entering_incorrect_password(self, driver):
       driver.find_element(*TestLocators.BUTTON_ENTRANCE_IN_ACCOUNT).click() # найти и нажать кнопку "Войти в аккаунт"
       WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.LINK_REGISTER))) #ждем, пока не будет кликабельна ссылка "Зарегистрироваться"
       element = driver.find_element(*TestLocators.LINK_REGISTER)
       driver.execute_script("arguments[0].scrollIntoView();", element) # прокручиваем до ссылки "Зарегистрироваться"
       driver.find_element(*TestLocators.LINK_REGISTER).click() # ищем и нажимаем ссылку "Зарегистрироваться"
       driver.find_element(*TestLocators.PASSWORD_USER).send_keys('123') # вводим пароль с символами <6
       driver.find_element(*TestLocators.BUTTON_REGISTER).click() # ищем и нажимаем кнопку "Зарегистрироваться"
       assert driver.find_element(*TestLocators.WARNING_INCORRECT_PASSWORD).text == 'Некорректный пароль' # ищем и проверяем текст сообщения
