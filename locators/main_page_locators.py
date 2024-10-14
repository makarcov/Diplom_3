from selenium.webdriver.common.by import By


class MainPageLocators:

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[starts-with(@class, 'AppHeader_header__link') and @href = '/account']")  # кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[starts-with(@class, 'AppHeader_header__link') and @href = '/']")  # кнопка "Конструктор"
    ORDER_FEED_BUTTON = (By.XPATH, "//a[starts-with(@class, 'AppHeader_header__link') and @href = '/feed']")  # кнопка "Лента заказов"
    LOGO_BUTTON = (By.XPATH, "//div[starts-with(@class, 'AppHeader_header__logo')]/a[@href = '/']")  # Логотип
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")  # кнопка "Оформить заказ"

    CONSTRUCTOR_TITLE = (By.XPATH, "//section/h1")  # надпись "Соберите бургер"
    BUNS_BUTTON = (By.XPATH, "//span[text() = 'Булки']/parent::div")  # кнопка "Булки"
    SAUCES_BUTTON = (By.XPATH, "//span[text() = 'Соусы']/parent::div")  # кнопка "Соусы"
    FILLINGS_BUTTON = (By.XPATH, "//span[text() = 'Начинки']/parent::div")  # кнопка "Начинки"

    BUN_HEADER = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][text()='Булки']")  # заголовок "Булки"
    SAUCE_HEADER = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][text()='Соусы']")  # заголовок "Соусы"
    FILLING_HEADER = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][text()='Начинки']")  # заголовок "Начинки"

    BUN_1 = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a")  # Флюоресцентная булка
    BUN_1_COUNTER = (By.XPATH, "//img[contains(@alt, 'Флюоресцентная булка R2-D3')]/preceding-sibling::div/p") # счетчик Флюоресцентная булка

    SAUCE_3 = (By.XPATH, "//p[text()='Соус традиционный галактический']/parent::a")  # Соус традиционный галактический

    FILLING_2 = (By.XPATH, "//p[text()='Говяжий метеорит (отбивная)']/parent::a")  # Говяжий метеорит (отбивная)

    ORDER_BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket')]")  # Конструктор бургера

    POPUP_WINDOW_OPENED = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened') and contains(@class, 'Modal_modal')]")
    POPUP_WINDOW_HIDDEN = (By.XPATH, "//section[contains(@class, 'Modal_modal') and contains(@class, 'Modal_modal')][1]")
    POPUP_WINDOW_CLOSE = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//*[name()='svg']")  # кнопка закрытия всплывающего окна ингредиента
    POPUP_WINDOW_ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]")  # Номера заказа из всплывающего окна
    CLOSE_POPUP_ORDER_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button")  # Закрыть попап окно

    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']")  # кнопка "Войти в аккаунт"
