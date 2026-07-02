from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    """Базовый класс для всех Page Object'ов."""

    def __init__(self, driver):
        """Инициализация базовой страницы с драйвером и ожиданием."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Прокрутить страницу к элементу: {locator}")
    def scroll_to_element(self, locator):
        """Прокручивает страницу до указанного элемента."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element    

    @allure.step("Найти элемент по локатору: {locator}")
    def find_element(self, locator):
        """Находит элемент с ожиданием его видимости."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть по элементу: {locator}")
    def click(self, locator):
        """Кликает по элементу."""
        self.find_element(locator).click()

    @allure.step("Ввести текст '{text}' в элемент: {locator}")
    def send_keys(self, locator, text):
        """Вводит текст в элемент."""
        self.find_element(locator).send_keys(text)

    @allure.step("Получить текст из элемента: {locator}")
    def get_text(self, locator):
        """Возвращает текст элемента."""
        return self.find_element(locator).text

    @allure.step("Проверить, видим ли элемент: {locator}")
    def is_element_visible(self, locator):
        """Проверяет, видим ли элемент на странице."""
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False
        
    @allure.step("Ожидать, что URL содержит '{expected_url}'")
    def wait_url_contains(self, expected_url):
        """Ожидает, что текущий URL содержит указанную строку."""
        self.wait.until(EC.url_contains(expected_url))

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_window(self):
        """Переключается на последнюю открытую вкладку."""
        self.driver.switch_to.window(self.driver.window_handles[-1])