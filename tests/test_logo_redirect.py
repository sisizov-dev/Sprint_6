import pytest
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
        main_page.accept_cookies()
        main_page.click_yandex_logo()
        
        driver.switch_to.window(driver.window_handles[1])
        
        WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))   

        assert "dzen.ru" in driver.current_url

    @allure.title("Переход по логотипу Самоката")
    @allure.description("При клике на логотип Самоката открывается главная страница")
    @allure.story("Логотип Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver, MainPageLocators)
        main_page.accept_cookies()
        
        order_page = OrderPage(driver, OrderPageLocators)
        order_page.click_order_button_top()
        order_page.click_scooter_logo()
        
        assert "qa-scooter.praktikum-services.ru" in driver.current_url