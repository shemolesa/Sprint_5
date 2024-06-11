import pytest
import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators

class TestWorkingWithTheApplication:

# проверка перехода в личный кабинет
    def test_go_to_personal_account(self, driver, url):
        driver.get(url) # открыть главную страницу под пользователем
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click() # найти и нажать кнопку "Личный кабинет"
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.TAB_PROFILE))) #ждем, пока не будет кликабельна вкладка "Профиль"
        assert driver.find_element(*TestLocators.TAB_PROFILE) # проверяем наличие вкладки "Профиль"

# проверка перехода из личного кабинета на главную страницу по клику на логтипе/конструкторе
    @pytest.mark.parametrize('locator', [TestLocators.BUTTON_LOGO, TestLocators.BUTTON_CONSTRUCTOR])
    def test_going_the_main_page_for_constructor_and_logo(self, driver, url, locator):
        driver.get(url)
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click() # найти и нажать кнопку "Личный кабинет"
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.TAB_PROFILE))) #ждем, пока не будет кликабельна вкладка "Профиль"
        driver.find_element(*locator).click() # найти и нажать кнопку "Конструктор"
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((TestLocators.BUTTON_CHECKOUT)))  # ждем, пока не будет кликабельна кнопка "Оформить заказ"
        assert driver.find_element(*TestLocators.INSCRIPTION_ASSEMBLE_THE_BURGER) # проверяем наличие надписи "Соберите Бургер"

# проверка перехода к разделу "Соусы" из разделов "Булки" и "Начинки"
    @pytest.mark.parametrize('locator_source', [TestLocators.TAB_BUNS, TestLocators.TAB_STUFFINGS])
    def test_transition_to_sauces(self, driver, locator_source):
        driver.get(data.url_main_page)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.INSCRIPTION_ASSEMBLE_THE_BURGER))) #ждем отображения надписи "Соберите бургер"
        if driver.find_element(*locator_source).text != 'Булки':
            driver.find_element(*locator_source).click() # найти и нажать исходную вкладку меню
        driver.find_element(*TestLocators.TAB_SAUCES).click() # найти и нажать вкладку "Соусы"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.MENU_SAUCES))) #ждем, пока не отобразится меню с соусами
        assert driver.find_element(*TestLocators.MENU_SAUCES) # проверяем наличие надписи меню "Соусы"

# проверка перехода к разделу "Начинки" из разделов "Булки" и "Соусы"
    @pytest.mark.parametrize('locator_source', [TestLocators.TAB_BUNS, TestLocators.TAB_SAUCES])
    def test_transition_to_stuffings(self, driver, locator_source):
        driver.get(data.url_main_page)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.INSCRIPTION_ASSEMBLE_THE_BURGER))) #ждем отображения надписи "Соберите бургер"
        if driver.find_element(*locator_source).text != 'Булки':
            driver.find_element(*locator_source).click() # найти и нажать исходную вкладку меню
        driver.find_element(*TestLocators.TAB_STUFFINGS).click() # найти и нажать вкладку "Начинки"
        assert driver.find_element(*TestLocators.MENU_STUFFINGS) # проверяем наличие надписи меню "Начинки"

# проверка перехода к разделу "Булки" из разделов "Начинки" и "Соусы"
    @pytest.mark.parametrize('locator_source', [TestLocators.TAB_STUFFINGS, TestLocators.TAB_SAUCES])
    def test_transition_to_buns(self, driver, locator_source):
        driver.get(data.url_main_page)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.INSCRIPTION_ASSEMBLE_THE_BURGER))) #ждем отображения надписи "Соберите бургер"
        driver.find_element(*locator_source).click() # найти и нажать исходную вкладку меню
        driver.find_element(*TestLocators.TAB_BUNS).click() # найти и нажать вкладку "Начинки"
        assert driver.find_element(*TestLocators.MENU_BUNS) # проверяем наличие надписи меню "Начинки"
