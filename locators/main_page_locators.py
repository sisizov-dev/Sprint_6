from selenium.webdriver.common.by import By

#Локаторы для главной страницы
class MainPageLocators:

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button") # Кнопка принятия куки
    FAQ_BLOCK = (By.CLASS_NAME, "accordion")  # Блок с вопросами (аккордеон)
    QUESTION = (By.ID, "accordion__heading-{}") # Вопросы в аккордеоне (подставляется индекс: 0, 1, 2...)
    ANSWER = (By.ID, "accordion__panel-{}") # Ответы в аккордеоне (подставляется индекс: 0, 1, 2...)

    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex__')]") # Логотип Яндекса