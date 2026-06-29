from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver, locators):
        super().__init__(driver)
        self.locators = locators

    def accept_cookies(self):
        self.click(self.locators.COOKIE_BUTTON)

    def scroll_to_faq_block(self):
        element = self.find_element(self.locators.FAQ_BLOCK)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_question(self, index):
        locator = (self.locators.QUESTION[0], self.locators.QUESTION[1].format(index))
        self.click(locator)

    def get_answer_text(self, index):
        locator = (self.locators.ANSWER[0], self.locators.ANSWER[1].format(index))
        return self.get_text(locator)

    def is_answer_visible(self, index):
        locator = (self.locators.ANSWER[0], self.locators.ANSWER[1].format(index))
        return self.is_element_visible(locator)
    
    def click_yandex_logo(self):
        self.click(self.locators.YANDEX_LOGO)