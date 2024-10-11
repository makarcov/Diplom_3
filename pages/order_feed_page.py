import allure

from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик на Ленту заказов")
    def open_order_feed(self):
        self.click_element(OrderFeedLocators.ORDER_FEED_BUTTON)

    @allure.step("Клик на заказ")
    def open_order_info(self):
        self.click_element(OrderFeedLocators.ORDER_1)

    @allure.step("Получить статус видимости всплывающего окна заказа")
    def popup_order_info_visibility(self):
        return self.find_element_with_wait(OrderFeedLocators.ORDER_POPUP_WINDOW_OPENED).is_displayed()

    @allure.step("Закрыть всплывающее окно заказа")
    def close_popup_order_info(self):
        self.click_element(OrderFeedLocators.CLOSE_POPUP_ORDER_WINDOW)

    @allure.step("Получить номер заказа на вкладке История заказов")
    def get_order_number_in_order_history(self):
        number = self.find_element_with_wait(OrderFeedLocators.USER_ORDER_1_NUMBER)
        return number.text

    @allure.step("Получить номер заказа с Ленты заказов")
    def get_order_number_in_order_feed(self):
        number = self.find_element_with_wait(OrderFeedLocators.ORDER_1_NUMBER)
        return number.text

    @allure.step("Получить количество заказов за все время")
    def get_counter_all_time(self):
        number = self.find_element_with_wait(OrderFeedLocators.COUNTER_ALL_TIME)
        return number.text

    @allure.step("Получить количество заказов за сегодня")
    def get_counter_today(self):
        number = self.find_element_with_wait(OrderFeedLocators.COUNTER_TODAY)
        return number.text

    @allure.step("Получить количество заказов в работе")
    def get_counter_order_in_process(self):
        number = self.find_element_with_wait(OrderFeedLocators.ORDERS_IN_PROCESS)
        return number.text