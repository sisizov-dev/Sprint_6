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
    @pytest.mark.parametrize("button_position, name, surname, address, station, phone, date, period, color", [
        ("top", "Олег", "Кузин", "г. Москва, ул. Зорге, д. 5", "Фрунзенская", "+79995554444", "15", "двое суток", "black"),
        ("bottom", "Ольга", "Михеева", "Московская обл., г. Красногорск, ул. Витте, д. 7", "Митино", "+79998882233", "20", "семеро суток", "grey")
    ])
    def test_order_flow(self, driver, button_position, name, surname, address, station, phone, date, period, color):
        order_page = OrderPage(driver, OrderPageLocators)

        @allure.step("Открыть главную страницу и принять куки")
        def step_accept_cookies():
            main_page = MainPage(driver, MainPageLocators)
            main_page.accept_cookies()

        @allure.step(f"Нажать кнопку 'Заказать' ({button_position})")
        def step_click_order_button():
            if button_position == "top":
                order_page.click_order_button_top()
            else:
                order_page.click_order_button_bottom()

        @allure.step("Заполнить первую часть формы")
        def step_fill_first_form():
            order_page.fill_name(name)
            order_page.fill_surname(surname)
            order_page.fill_address(address)
            order_page.select_metro(station)
            order_page.fill_phone(phone)

        @allure.step("Нажать 'Далее'")
        def step_click_next():
            order_page.click_next()

        @allure.step("Заполнить вторую часть формы")
        def step_fill_second_form():
            order_page.select_date(date)
            order_page.select_rental_period(period)
            if color == "black":
                order_page.select_color_black()
            else:
                order_page.select_color_grey()

        @allure.step("Нажать 'Заказать'")
        def step_click_order():
            order_page.click_order()

        @allure.step("Подтвердить заказ (кнопка 'Да')")
        def step_click_yes():
            order_page.click_yes()

        @allure.step("Проверить сообщение об успешном заказе")
        def step_check_success():
            assert order_page.is_success_displayed(), "Сообщение об успешном заказе не отображается"

        step_accept_cookies()
        step_click_order_button()
        step_fill_first_form()
        step_click_next()
        step_fill_second_form()
        step_click_order()
        step_click_yes()
        step_check_success()