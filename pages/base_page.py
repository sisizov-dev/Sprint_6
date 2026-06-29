from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Базовый класс для всех Page Object'ов."""

    def __init__(self, driver):
        """Инициализация базовой страницы с драйвером и ожиданием."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Находит элемент с ожиданием его видимости."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Кликает по элементу."""
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        """Вводит текст в элемент."""
        self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        """Возвращает текст элемента."""
        return self.find_element(locator).text

    def is_element_visible(self, locator):
        """Проверяет, видим ли элемент на странице."""
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False