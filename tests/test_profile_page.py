import time

import allure

from data import Url
from locators.profile_page_locators import ProfilePageLocators
from pages.profile_page import ProfilePage


class TestProfilePage:

    @allure.title("Проверяем переход по клику на Личный кабинет")
    def test_open_profile(self, driver, create_and_login_user):
        email = create_and_login_user.get("email")
        profile_page = ProfilePage(driver)
        profile_page.open_profile()
        time.sleep(1)
        login = profile_page.find_element_with_wait(ProfilePageLocators.PROFILE_LOGIN).get_attribute('value')
        assert login == email

    @allure.title("Проверяем переход в раздел История заказов")
    def test_open_order_history(self, driver, create_and_login_user):
        profile_page = ProfilePage(driver)
        profile_page.open_profile()
        profile_page.open_order_history()
        url = profile_page.get_current_url()
        assert "/account/order-history" in url

    @allure.title("Проверяем выход из аккаунта")
    def test_logout_profile(self, driver, create_and_login_user):
        profile_page = ProfilePage(driver)
        profile_page.open_profile()
        old_url = profile_page.get_current_url()
        profile_page.logout()
        new_url = profile_page.get_current_url()
        if old_url == new_url:
            profile_page.get_current_url(10)
        else:
            pass
        assert profile_page.get_current_url(10) == Url.LOGIN_URL
