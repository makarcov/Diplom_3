import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedPage:

    @allure.title("Проверяем появление всплывающего окна при клике на заказ")
    def test_click_order_popup_window(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed()
        order_feed_page.open_order_info()
        assert order_feed_page.popup_order_info_visibility() is True

    @allure.title("Проверяем, что заказ пользователя из Истории заказов отображается в Ленте заказов")
    def test_order_in_history_present_in_feed(self, driver, create_burger_with_history_number):
        number_in_history = create_burger_with_history_number
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed()
        number_in_feed = order_feed_page.get_order_number_in_order_feed()
        assert number_in_history == number_in_feed

    @allure.title("Проверяем увеличение счетчика Выполнено за все время при создании нового заказа")
    def test_counter_all_time(self, driver, create_burger_with_popup_number):
        order_number = create_burger_with_popup_number
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed()
        counter_all_time = order_feed_page.get_counter_all_time()
        assert int(order_number) >= int(counter_all_time)

    @allure.title("Проверяем увеличение счетчика Выполнено за сегодня при создании нового заказа")
    def test_counter_today(self, driver, create_and_login_user):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed()
        counter_today_start = order_feed_page.get_counter_today()
        main_page = MainPage(driver)

        main_page.create_burger_order()
        order_feed_page.open_order_feed()
        counter_today_finish = order_feed_page.get_counter_today()

        assert int(counter_today_finish) > int(counter_today_start)

    @allure.title("Проверяем появление номера заказа в разделе В работе")
    def test_order_in_process_section(self, driver, create_and_login_user):
        main_page = MainPage(driver)
        order_number = main_page.create_burger_order()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed()
        order_in_process = order_feed_page.get_counter_order_in_process()

        assert order_number in order_in_process
