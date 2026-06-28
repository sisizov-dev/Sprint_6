from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы для страницы заказа."""

    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button') and contains(text(), 'Заказать')]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Middle') and contains(text(), 'Заказать')]")
    
    # Поля формы
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    
    # Метро (выпадающий список)
    METRO_DROPDOWN = (By.CLASS_NAME, "select-search__select")
    METRO_OPTION = (By.XPATH, "//button[contains(@class, 'Order_SelectOption__') and contains(text(), '{}')]")
    
    # Дата аренды
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER = ((By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='{}']"))
    DATE_PICKER_SELECTED = (By.CLASS_NAME, "react-datepicker__day--selected")
    
    # Сроки аренды
    INPUT_RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{}']")
    
    # Цвет
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    
    # Кнопки навигации
    BUTTON_NEXT = (By.XPATH, "//button[contains(text(), 'Далее')]")
    BUTTON_ORDER = (By.XPATH, "//button[contains(@class, 'Button_Middle') and contains(text(), 'Заказать')]")
    BUTTON_YES = (By.XPATH, "//button[contains(text(), 'Да')]")
    
    
    # Сообщение об успехе
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")