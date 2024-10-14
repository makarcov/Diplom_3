import time

import allure

from seletools.actions import drag_and_drop

from data import ExpextedText
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик на Конструктор")
    def open_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик на Ленту заказов")
    def open_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Клик на ингредиент")
    def click_ingredient(self):
        self.click_element(MainPageLocators.BUN_1)

    @allure.step("Закрытие всплывающего окна ингредиента")
    def close_popup_ingredient_window(self):
        self.click_element(MainPageLocators.POPUP_WINDOW_CLOSE)

    @allure.step("Добавление булочки в заказ")
    def add_bun_to_order(self):
        source = self.find_element_with_wait(MainPageLocators.BUN_1)
        target = self.find_element_with_wait(MainPageLocators.ORDER_BASKET)
        drag_and_drop(self.driver, source, target)

    @allure.step("Добавление соуса в заказ")
    def add_sauce_to_order(self):
        source = self.find_element_with_wait(MainPageLocators.SAUCE_3)
        target = self.find_element_with_wait(MainPageLocators.ORDER_BASKET)
        drag_and_drop(self.driver, source, target)

    @allure.step("Добавление начинки в заказ")
    def add_filling_to_order(self):
        source = self.find_element_with_wait(MainPageLocators.FILLING_2)
        target = self.find_element_with_wait(MainPageLocators.ORDER_BASKET)
        drag_and_drop(self.driver, source, target)

    @allure.step("Сделать заказ бургера")
    def create_burger_order(self):
        self.open_constructor()
        self.add_bun_to_order()
        self.add_sauce_to_order()
        self.add_filling_to_order()
        self.make_order_click()
        number = self.get_order_number_from_popup()
        if number == ExpextedText.ORDER_NUMBER:
            self.get_expectation_for_element(MainPageLocators.POPUP_WINDOW_ORDER_NUMBER, number)
            new_number = self.get_text(MainPageLocators.POPUP_WINDOW_ORDER_NUMBER).strip()
        self.close_popup_order_number()
        return new_number

    @allure.step("Получение значение счетчика ингредиента при добавлении в заказ")
    def get_bun_counter(self):
        counter = self.find_element_with_wait(MainPageLocators.BUN_1_COUNTER)
        return counter.text

    @allure.step("Клик на Оформить заказ")
    def make_order_click(self):
        self.click_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step("Получить номер заказа")
    def get_order_number_from_popup(self):
        return self.find_element_with_wait(MainPageLocators.POPUP_WINDOW_ORDER_NUMBER).text

    @allure.step("Закрыть всплывающее окно заказа")
    def close_popup_order_number(self):
        self.click_element(MainPageLocators.CLOSE_POPUP_ORDER_WINDOW)
