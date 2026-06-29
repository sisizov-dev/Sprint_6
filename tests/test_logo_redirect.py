from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.feature("Переходы по логотипам")
class TestLogoRedirect:

    @allure.title("Переход по логотипу Яндекса")
    @allure.description("При клике на логотип Яндекса открывается Дзен в новой вкладке")
    @allure.story("Логотип Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver, MainPageLocators)

        @allure.step("Принять куки")
        def step_accept_cookies():
            main_page.accept_cookies()

        @allure.step("Кликнуть по логотипу Яндекса")
        def step_click_yandex_logo():
            main_page.click_yandex_logo()

        @allure.step("Переключиться на новую вкладку")
        def step_switch_to_new_window():
            driver.switch_to.window(driver.window_handles[1])

        @allure.step("Дождаться загрузки страницы Дзена")
        def step_wait_for_dzen():
            WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))

        @allure.step("Проверить, что открылся Дзен")
        def step_check_url():
            assert "dzen.ru" in driver.current_url

        step_accept_cookies()
        step_click_yandex_logo()
        step_switch_to_new_window()
        step_wait_for_dzen()
        step_check_url()

    @allure.title("Переход по логотипу Самоката")
    @allure.description("При клике на логотип Самоката открывается главная страница")
    @allure.story("Логотип Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver, MainPageLocators)

        @allure.step("Принять куки")
        def step_accept_cookies():
            main_page.accept_cookies()

        @allure.step("Открыть страницу заказа")
        def step_open_order_page():
            order_page = OrderPage(driver, OrderPageLocators)
            order_page.click_order_button_top()
            return order_page

        @allure.step("Кликнуть по логотипу Самоката")
        def step_click_scooter_logo(order_page):
            order_page.click_scooter_logo()

        @allure.step("Проверить, что открылась главная страница")
        def step_check_url():
            assert "qa-scooter.praktikum-services.ru" in driver.current_url

        step_accept_cookies()
        order_page = step_open_order_page()
        step_click_scooter_logo(order_page)
        step_check_url()