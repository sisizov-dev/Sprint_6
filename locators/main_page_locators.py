from selenium.webdriver.common.by import By


class MainPageLocators:

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    FAQ_BLOCK = (By.CLASS_NAME, "accordion")
    QUESTION = (By.ID, "accordion__heading-{}")
    ANSWER = (By.ID, "accordion__panel-{}")

    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex__')]")