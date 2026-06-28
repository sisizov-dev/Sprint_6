from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):

    def __init__(self, driver, locators):
        super().__init__(driver)
        self.locators = locators

    def click_order_button_top(self):
        self.click(self.locators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click(self.locators.ORDER_BUTTON_BOTTOM)

    def fill_name(self, name):
        self.send_keys(self.locators.INPUT_NAME, name)

    def fill_surname(self, surname):
        self.send_keys(self.locators.INPUT_SURNAME, surname)

    def fill_address(self, address):
        self.send_keys(self.locators.INPUT_ADDRESS, address)

    def fill_phone(self, phone):
        self.send_keys(self.locators.INPUT_PHONE, phone)

    def select_metro(self, station):
        self.click(self.locators.INPUT_METRO)
        locator = (self.locators.METRO_OPTION[0], self.locators.METRO_OPTION[1].format(station))
        self.click(locator)

    def select_date(self, day):
        self.click(self.locators.INPUT_DATE)
        locator = (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']")
        self.click(locator)

    def select_rental_period(self, period):
        self.click(self.locators.INPUT_RENTAL_PERIOD)
        locator = (self.locators.RENTAL_OPTION[0], self.locators.RENTAL_OPTION[1].format(period))
        self.click(locator)

    def select_color_black(self):
        self.click(self.locators.COLOR_BLACK)

    def select_color_grey(self):
        self.click(self.locators.COLOR_GREY)

    def click_next(self):
        self.click(self.locators.BUTTON_NEXT)

    def click_order(self):
        self.click(self.locators.BUTTON_ORDER)

    def click_yes(self):
        self.click(self.locators.BUTTON_YES)

    def get_success_message(self):
        return self.get_text(self.locators.SUCCESS_MESSAGE)

    def is_success_displayed(self):
        return self.is_element_visible(self.locators.SUCCESS_MESSAGE)