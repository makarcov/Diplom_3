import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик на Личный кабинет")
    def open_profile(self):
        self.click_element(ProfilePageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Клик на раздел История заказов")
    def open_order_history(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY)

    @allure.step("Клик на Выход")
    def logout(self):
        self.click_element(ProfilePageLocators.EXIT_BUTTON)