from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    """Класс для главной страницы."""

    def __init__(self, driver, locators):
        """Инициализация главной страницы."""
        super().__init__(driver)
        self.locators = locators

    @allure.step("Принять куки")
    def accept_cookies(self):
        """Нажимает кнопку принятия куки."""
        self.click(self.locators.COOKIE_BUTTON)

    @allure.step("Прокрутить до блока 'Вопросы о важном'")
    def scroll_to_faq_block(self):
        """Прокручивает страницу до блока 'Вопросы о важном'."""
        self.scroll_to_element(self.locators.FAQ_BLOCK)

    @allure.step("Кликнуть по вопросу с индексом {index}")
    def click_question(self, index):
        """Кликает по вопросу с указанным индексом."""
        locator = (self.locators.QUESTION[0], self.locators.QUESTION[1].format(index))
        self.click(locator)

    @allure.step("Получить текст ответа на вопрос с индексом {index}")
    def get_answer_text(self, index):
        """Возвращает текст ответа на вопрос с указанным индексом."""
        locator = (self.locators.ANSWER[0], self.locators.ANSWER[1].format(index))
        return self.get_text(locator)

    @allure.step("Проверить, видим ли ответ на вопрос с индексом {index}")
    def is_answer_visible(self, index):
        """Проверяет, видим ли ответ на вопрос с указанным индексом."""
        locator = (self.locators.ANSWER[0], self.locators.ANSWER[1].format(index))
        return self.is_element_visible(locator)

    @allure.step("Кликнуть по логотипу Яндекса")
    def click_yandex_logo(self):
        """Кликает по логотипу Яндекса."""
        self.click(self.locators.YANDEX_LOGO)