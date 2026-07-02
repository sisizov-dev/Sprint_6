
import pytest
import allure
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Позитивный сценарий заказа самоката")
    @allure.description("Проверка полного флоу заказа с двумя наборами данных")
    @allure.story("Оформление заказа")
    @pytest.mark.parametrize("button_method, color_method, name, surname, address, station, phone, date, period", [
        (OrderPage.click_order_button_top, OrderPage.select_color_black, "Олег", "Кузин", "г. Москва, ул. Зорге, д. 5", "Фрунзенская", "+79995554444", "15", "двое суток"),
        (OrderPage.click_order_button_bottom, OrderPage.select_color_grey, "Ольга", "Михеева", "Московская обл., г. Красногорск, ул. Витте, д. 7", "Митино", "+79998882233", "20", "семеро суток")
    ])
    def test_order_flow(self, driver, button_method, color_method, name, surname, address, station, phone, date, period):
        main_page = MainPage(driver, MainPageLocators)
        main_page.accept_cookies()

        order_page = OrderPage(driver, OrderPageLocators)

        button_method(order_page)
        order_page.fill_name(name)
        order_page.fill_surname(surname)
        order_page.fill_address(address)
        order_page.select_metro(station)
        order_page.fill_phone(phone)
        order_page.click_next()

        order_page.select_date(date)
        order_page.select_rental_period(period)
        color_method(order_page)

        order_page.click_order()
        order_page.click_yes()

        assert order_page.is_success_displayed(), "Сообщение об успешном заказе не отображается"