# UI тесты

## Тестирование сайтa Stellar Burgers

### Описание файлов и директорий:
#### Файлы

*conftest.py* - файл с настройками (фикстурами)

*burgers_api.py* - файл с методами запросов ручек

*helpers.py* - файл с вспомогательными функциями

*data.py* - файл с вспомогательной информацией

*requirements.txt* - файл с зависимостями

#### Directory "tests":

*test_login_page.py* - тест страницы авторизации и восстановления пароля

*test_main_page.py* - тест главной страницы

*test_order_feed_page.py* - тест страницы Лента заказов

*test_profile_page.py* - тест страницы профиля пользователя

#### Directory "pages":

*base_page.py* - базовый класс страницы с общими методами для всех страниц

*login_page.py* - страница авторизации и восстановления пароля

*main_page.py* - главная страница

*order_feed_page.py* - страница Лента заказов

*profile_page.py* - страница профиля пользователя

#### Directory "locators":

*forgot_password_locators.py* - локаторы страницы восстановления пароля

*login_page_locators.py* - локаторы страницы авторизации и восстановления пароля

*main_page_locators.py* - локаторы главной страницы

*order_feed_locators.py* - локаторы страницы Лента заказов

*profile_page_locators.py* - локаторы страницы профиля пользователя

#### Directory "allure_results":
отчет о тестах

#### **Для запуска тестов**: pytest
#### **Установка зависимостей**: pip install -r requirements.txt`

