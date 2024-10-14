from selenium.webdriver.common.by import By


class LoginPageLocators:

    ENTER_EMAIL_INPUT_FIELD = (By.XPATH, "//input[@name = 'name']") # поле ввода "Email"
    ENTER_PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@name = 'Пароль']") # поле ввода "Пароль"
    ENTER_BUTTON = (By.XPATH, "//button[text() = 'Войти']")  # кнопка "Войти"
    ENTER_REGISTRATION_BUTTON = (By.XPATH, "//a[@class = 'Auth_link__1fOlj' and @href = '/register']")  # кнопка "Зарегистрироваться"
    ENTER_FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[@class = 'Auth_link__1fOlj' and @href = '/forgot-password']")  # кнопка "Восстановить пароль"