import allure

from data import Url
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestMainPage:

    @allure.title("Проверяем переход по клику на Конструктор")
    def test_open_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Url.LOGIN_URL)
        main_page.open_constructor()
        assert main_page.find_element_with_wait(MainPageLocators.CONSTRUCTOR_BUTTON).is_displayed()

    @allure.title("Проверяем переход по клику на Ленту заказов")
    def test_open_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_order_feed()
        assert "/feed" in main_page.get_current_url()

    @allure.title("Проверяем появление всплывающего окна по клику на ингредиент")
    def test_ingredient_popup_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.find_element_with_wait(MainPageLocators.POPUP_WINDOW_OPENED).is_displayed()
        assert main_page.find_element_with_wait(MainPageLocators.POPUP_WINDOW_OPENED).is_displayed()

    @allure.title("Проверяем закрытие всплывающего окна ингредиента")
    def test_close_ingredient_popup_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_popup_ingredient_window()
        text_class_popup_window_close = main_page.get_element_attribute_class(MainPageLocators.POPUP_WINDOW_HIDDEN)
        assert "opened" not in text_class_popup_window_close

    @allure.title("Проверяем изменение счетчика при добавлении ингредиента в заказ")
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        start_counter = main_page.get_bun_counter()
        main_page.add_bun_to_order()
        finish_counter = main_page.get_bun_counter()
        assert finish_counter == str(int(start_counter) + 2)

    @allure.title("Проверяем, что залогиненный пользователь может создать заказ")
    def test_create_order_login_user(self, driver, create_and_login_user):
        main_page = MainPage(driver)
        main_page.create_burger_order()
        order_number = main_page.find_element_with_wait(MainPageLocators.POPUP_WINDOW_ORDER_NUMBER).is_displayed()
        assert order_number is True
