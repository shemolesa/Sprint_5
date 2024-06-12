# Sprint_5

## conftest.py 
файл с фикстурами
_driver_ - инициация вебдрайвера
_generated_login_ - генерация логина пользователя
_url_ - авторизация пользователя с главной страницы


## data.py
файл с тестовыми данными


## test_extrance_and_exit_account.py
файл с положительными тестами входа в аккаунт пользователя
_test_successful_login_from_home_page_ - проверка входа по кнопке «Войти в аккаунт»/"Личный кабинет" на главной странице
_test_successful_login_from_your_personal_account_page_ - проверка входа по ссылке со страницы регистрации/восстановления пароля
_test_successful_login_from_registration_and_recovery_pages_ - проверка входа по ссылке со страницы регистрации/восстановления пароля
_test_logout_from_account_ - проверка выхода из профиля


## test_registration.py
файл с тестами регистрации
_test_successful_registration_ - проверка успешной регистрации
_test_entering_incorrect_password_ - проверка обработки ошибки для некорректного пароля (1-5 символов)


## test_transitions.py
файл с тестами остальных действий на странице
_test_go_to_personal_account_ - проверка перехода в личный кабинет
_test_going_the_main_page_for_constructor_and_logo_ - проверка перехода из личного кабинета на главную страницу по клику на логтипе/конструкторе
_test_transition_to_stuffings_and_sauces_ - проверка перехода к разделу "Начинки"/"Соусы" из разделов "Соусы" и "Начинки"
_test_transition_from_buns_to_stuffings_and_sauces_ - проверка перехода к разделу "Начинки"/"Соусы" из раздела "Булки"
_test_transition_to_buns_ - проверка перехода к разделу "Булки" из разделов "Начинки" и "Соусы"