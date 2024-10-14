import allure
import pytest

from selenium import webdriver

from burgers_api import BurgersApi
from data import Url
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage


@allure.step("Запуск браузера")
# @pytest.fixture(params=['chrome', 'firefox'])
@pytest.fixture(params=['chrome'])
def driver(request):
    browser = None
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    elif request.param == 'firefox':
        browser = webdriver.Firefox()

    browser.get(Url.BASE_URL)
    yield browser
    browser.quit()


@allure.step("Создание и авторизация пользователя")
@pytest.fixture()
def create_and_login_user(driver):
    main_page = MainPage(driver)
    create_user = BurgersApi.create_user()
    user_data, token = create_user
    email = user_data.get("email")
    password = user_data.get("password")
    main_page.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    main_page.set_text(LoginPageLocators.ENTER_EMAIL_INPUT_FIELD, email)
    main_page.set_text(LoginPageLocators.ENTER_PASSWORD_INPUT_FIELD, password)
    main_page.click_element(LoginPageLocators.ENTER_BUTTON)

    yield user_data

    BurgersApi.delete_user(token)


@allure.step("Создание бургера авторизированным пользователем")
@allure.description("Возвращаем номер заказа из Истории заказов")
@pytest.fixture()
def create_burger_with_history_number(driver, create_and_login_user):
    main_page = MainPage(driver)
    main_page.create_burger_order()
    profile_page = ProfilePage(driver)
    profile_page.open_profile()
    profile_page.open_order_history()
    order_feed_page = OrderFeedPage(driver)
    order_number = order_feed_page.get_order_number_in_order_history()

    yield order_number


@allure.step("Создание бургера авторизированным пользователем")
@allure.description("Возвращаем номер заказа из всплывающего окна")
@pytest.fixture()
def create_burger_with_popup_number(driver, create_and_login_user):
    main_page = MainPage(driver)
    popup_number = main_page.create_burger_order()

    yield popup_number

@allure.step("Создание бургера авторизированным пользователем, возврат номера заказа и страницы Лента заказов")
@allure.description("Возвращаем номер заказа из Истории заказов")
@pytest.fixture()
def create_burger_with_number_and_page(driver, create_and_login_user):
    main_page = MainPage(driver)
    main_page.create_burger_order()
    popup_number = main_page.create_burger_order()
    order_feed_page = OrderFeedPage(driver)
    order_feed_page.open_order_feed()

    yield popup_number, order_feed_page
