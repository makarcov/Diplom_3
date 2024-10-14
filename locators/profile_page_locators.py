from selenium.webdriver.common.by import By


class ProfilePageLocators:

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[starts-with(@class, 'AppHeader_header__link') and @href = '/account']")  # кнопка "Личный кабинет"
    PROFILE_LOGIN = (By.XPATH, "//input[@name = 'name' and @type = 'text']")
    SAVE_BUTTON = (By.XPATH, "//button[text() = 'Сохранить']")  # кнопка "Сохранить"
    EXIT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")  # кнопка "Выход"
    ORDER_HISTORY = (By.XPATH, "//a[@href='/account/order-history']")  # кнопка "История заказов"