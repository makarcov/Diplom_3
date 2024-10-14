import allure
from selenium.common import NoSuchWindowException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # переход по заданному адресу
    @allure.step("Переход по заданному адресу")
    def open_url(self, url):
        return self.driver.get(url)

    @allure.step("Найти элемент с использованием ожидания")
    def find_element_with_wait(self, locator, time=30):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # найти кликабельный элемент с использованием ожидания
    @allure.step("Найти кликабельный элемент с использованием ожидания")
    def find_element_to_click_with_wait(self, locator, time=30):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    # кликнуть по элементу
    @allure.step("Кликнуть по элементу")
    def click_element(self, locator):
        element = self.find_element_to_click_with_wait(locator)
        return element.click()

    # получить текст элемента
    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    # получить атрибут элемента
    @allure.step("Получить атрибут class элемента")
    def get_element_attribute_class(self, locator):
        element = self.find_element_with_wait(locator)
        return element.get_attribute('class')

    # ввести текст в элемент
    @allure.step("Ввести текст в элемент")
    def set_text(self, locator, text):
        element = self.find_element_with_wait(locator)
        return element.send_keys(text)

    # скролл до элемента
    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # кликнуть на элемент с использованием JavaScript
    @allure.step("Кликнуть на элемент с использованием JavaScript")
    def click_element_with_js(self, locator):
        element = self.find_element_to_click_with_wait(locator)
        return self.driver.execute_script("arguments[0].click();", element)

    # получить url текущей страницы
    @allure.step("Получить url текущей страницы")
    def get_current_url(self, time=None):
        if time:
            WebDriverWait(self.driver, time).until(EC.url_changes(self.driver.current_url))
        else:
            pass
        return self.driver.current_url

    # переключиться на новое окно
    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self, time=10):
        WebDriverWait(self.driver, time).until(lambda browser: len(browser.window_handles) > 1)
        new_window = self.driver.window_handles[-1]
        try:
            self.driver.switch_to.window(new_window)
        except NoSuchWindowException:
            WebDriverWait(self.driver, 10).until(lambda browser: len(browser.window_handles) > 1)
            self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Задаем ожидание для изменения текста элементе")
    def get_expectation_for_element(self, locator, old_value, time=10):
        return WebDriverWait(self.driver, time).until(lambda browser: self.find_element_with_wait(locator, time).text.strip() != old_value)
