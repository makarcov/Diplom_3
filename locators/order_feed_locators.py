from selenium.webdriver.common.by import By


class OrderFeedLocators:

    ORDER_FEED_BUTTON = (By.XPATH, "//a[starts-with(@class, 'AppHeader_header__link') and @href = '/feed']")  # кнопка "Лента заказов"
    ORDER_1 = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]")  # Верхний заказ
    ORDER_1_NUMBER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]//p[@class = 'text text_type_digits-default']")  # Номер верхнего заказа в ленте
    ORDER_POPUP_WINDOW_OPENED = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")   # Попап окно заказа
    CLOSE_POPUP_ORDER_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//*[name()='svg']")  # Закрыть попап окно заказа
    COUNTER_ALL_TIME = (By.XPATH, "//p[contains(text(), 'Выполнено за все время:')]//following-sibling::p")  # Счетчик Выполнено за все время
    COUNTER_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]//following-sibling::p")  # Счетчик за сегодня

    USER_ORDER_1_NUMBER = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]/li[1]//p[1]")  # Номер верхнего заказа в истории пользователя

    ORDERS_IN_PROCESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")  # Номера заказов в работе
