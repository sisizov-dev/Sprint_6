import pytest
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
import allure

@allure.feature("Заказ самоката")
class TestOrder:
    
    @allure.title("Позитивный сценарий заказа самоката")
    @allure.description("Проверка полного флоу заказа с двумя наборами данных")
    @allure.story("Оформление заказа")
    @pytest.mark.parametrize("button_position, name, surname, address, station, phone, date, period, color", [
        ("top", "Олег", "Кузин", "г. Москва, ул. Зорге, д. 5", "Фрунзенская", "+79995554444", "15", "двое суток", "black"),
        ("bottom", "Ольга", "Михеева", "Московская обл., г. Красногорск, ул. Витте, д. 7", "Митино", "+79998882233", "20", "семеро суток", "grey")
    ])
    def test_order_flow(self, driver, button_position, name, surname, address, station, phone, date, period, color):
        order_page = OrderPage(driver, OrderPageLocators)

        
        from pages.main_page import MainPage
        from locators.main_page_locators import MainPageLocators
        main_page = MainPage(driver, MainPageLocators)
        main_page.accept_cookies()

        if button_position == "top":
            order_page.click_order_button_top()
        else:
            order_page.click_order_button_bottom()

        order_page.fill_name(name)
        order_page.fill_surname(surname)
        order_page.fill_address(address)
        order_page.select_metro(station)
        order_page.fill_phone(phone)
        order_page.click_next()

        order_page.select_date(date)
        order_page.select_rental_period(period)

        if color == "black":
            order_page.select_color_black()
        else:
            order_page.select_color_grey()

        order_page.click_order()
        order_page.click_yes()

        assert order_page.is_success_displayed(), "Сообщение об успешном заказе не отображается"