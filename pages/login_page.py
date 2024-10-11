import allure

from helpers import Helpers
from locators.forgot_password_locators import ForgotPasswordLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик на кнопку Восстановить пароль")
    def click_forgot_password(self):
        self.click_element(MainPageLocators.ENTER_ACCOUNT_BUTTON)
        self.click_element(ForgotPasswordLocators.ENTER_FORGOT_PASSWORD_BUTTON)

    @allure.step("Ввести адрес почты на странице восстановления пароля и клик на кнопку Восстановить")
    def insert_email_and_click_restore_password_button(self):
        email = Helpers.fake_email()
        self.set_text(ForgotPasswordLocators.ENTER_EMAIL_FIELD, email)
        self.click_element(ForgotPasswordLocators.RESTORE_PASSWORD_BUTTON)

    @allure.step("Клик на кнопку показать/скрыть пароль")
    def click_show_hide_password_button(self):
        self.click_element(ForgotPasswordLocators.SHOW_HIDE_PASSWORD_BUTTON)

    @allure.step("Заполнить поле Пароль")
    def insert_new_password(self):
        password = Helpers.fake_password()
        self.set_text(ForgotPasswordLocators.PASSWORD_FIELD, password)

    @allure.step("Получить статус поля Пароль для проверки скрыть/показать пароль")
    def get_status_password_field(self):
        locator = self.find_element_with_wait(ForgotPasswordLocators.PASSWORD_FIELD_STATUS, 15)
        return locator.get_attribute('class')

    @allure.step("Получить статус подсветки поля Пароль для проверки скрыть/показать пароль")
    def get_light_status_password_field(self):
        locator = self.find_element_with_wait(ForgotPasswordLocators.PASSWORD_FIELD_LIGHT, 15)
        return locator.get_attribute('class')
