import allure

from data import Url
from pages.login_page import LoginPage


class TestLoginPage:

    @allure.title("Проверяем переход по клику на кнопку Восстановить пароль")
    def test_click_forgot_password_button(self, driver):
        login_page = LoginPage(driver)
        login_page.click_forgot_password()
        url = login_page.get_current_url()
        assert url == Url.FORGOT_PASSWORD_URL

    @allure.title("Проверяем ввод почты и клик на кнопку Восстановить")
    def test_insert_email_click_restore_password(self, driver):
        login_page = LoginPage(driver)
        login_page.click_forgot_password()
        login_page.insert_email_and_click_restore_password_button()
        url = login_page.get_current_url(time=2)
        assert url == Url.RESET_PASSWORD_URL

    @allure.title("Проверяем клик по кнопке показать/скрыть пароль")
    def test_show_hide_password_button(self, driver):
        login_page = LoginPage(driver)
        login_page.click_forgot_password()
        login_page.insert_email_and_click_restore_password_button()
        login_page.insert_new_password()
        login_page.click_show_hide_password_button()
        field_status = login_page.get_status_password_field()
        light_status = login_page.get_light_status_password_field()
        assert "status_active" in field_status and "focused" in light_status
