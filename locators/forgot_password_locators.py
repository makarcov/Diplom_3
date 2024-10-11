from selenium.webdriver.common.by import By


class ForgotPasswordLocators:

    ENTER_FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[contains(@class, 'Auth_link') and @href = '/forgot-password']")  # кнопка "Восстановить пароль"
    FORGOT_PASSWORD_ENTER_BUTTON = (By.XPATH, "//a[text() = 'Войти']")  # кнопка "Войти" рядом с надписью "Вспомнили пароль?"
    ENTER_EMAIL_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")  # поле Email
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")  # кнопка "Восстановить"
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class,'input')]/*[name()='svg']")  # кнопка "Показать/Скрыть пароль"
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")  # поле "Пароль"
    PASSWORD_FIELD_STATUS = (By.XPATH, "//div[contains(@class, 'input') and contains(@class, 'input_status_active')]")  # статус поля "Пароль"
    PASSWORD_FIELD_LIGHT = (By.XPATH, "//div[contains(@class, 'input') and contains(@class, 'input_status_active')]/label")  # статус подсветки поля "Пароль"
