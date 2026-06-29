from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):
    """Класс для страницы заказа самоката."""

    def __init__(self, driver, locators):
        """Инициализация страницы заказа."""
        super().__init__(driver)
        self.locators = locators

    def click_order_button_top(self):
        """Кликает по кнопке 'Заказать' в верхней части страницы."""
        self.click(self.locators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        """Кликает по кнопке 'Заказать' в нижней части страницы."""
        self.click(self.locators.ORDER_BUTTON_BOTTOM)

    def fill_name(self, name):
        """Заполняет поле 'Имя'."""
        self.send_keys(self.locators.INPUT_NAME, name)

    def fill_surname(self, surname):
        """Заполняет поле 'Фамилия'."""
        self.send_keys(self.locators.INPUT_SURNAME, surname)

    def fill_address(self, address):
        """Заполняет поле 'Адрес'."""
        self.send_keys(self.locators.INPUT_ADDRESS, address)

    def fill_phone(self, phone):
        """Заполняет поле 'Телефон'."""
        self.send_keys(self.locators.INPUT_PHONE, phone)

    def select_metro(self, station):
        """Выбирает станцию метро из выпадающего списка."""
        self.click(self.locators.INPUT_METRO)
        self.click(self.locators.metro_station(station))

    def select_date(self, day):
        """Выбирает дату в календаре."""
        self.click(self.locators.INPUT_DATE)
        locator = (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']")
        self.click(locator)

    def select_rental_period(self, period):
        """Выбирает срок аренды из выпадающего списка."""
        self.click(self.locators.INPUT_RENTAL_PERIOD)
        locator = (self.locators.RENTAL_OPTION[0], self.locators.RENTAL_OPTION[1].format(period))
        self.click(locator)

    def select_color_black(self):
        """Выбирает чёрный цвет самоката."""
        self.click(self.locators.COLOR_BLACK)

    def select_color_grey(self):
        """Выбирает серый цвет самоката."""
        self.click(self.locators.COLOR_GREY)

    def click_next(self):
        """Нажимает кнопку 'Далее' для перехода ко второй части формы."""
        self.click(self.locators.BUTTON_NEXT)

    def click_order(self):
        """Нажимает кнопку 'Заказать' для оформления заказа."""
        self.click(self.locators.BUTTON_ORDER)

    def click_yes(self):
        """Подтверждает заказ в модальном окне (кнопка 'Да')."""
        self.click(self.locators.BUTTON_YES)

    def get_success_message(self):
        """Возвращает текст сообщения об успешном оформлении заказа."""
        return self.get_text(self.locators.SUCCESS_MESSAGE)

    def is_success_displayed(self):
        """Проверяет, отображается ли сообщение об успешном заказе."""
        return self.is_element_visible(self.locators.SUCCESS_MESSAGE)

    def click_scooter_logo(self):
        """Кликает по логотипу Самоката для перехода на главную страницу."""
        self.click(self.locators.SCOOTER_LOGO)