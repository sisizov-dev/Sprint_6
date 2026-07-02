from locators.main_page_locators import MainPageLocators


@allure.feature("Вопросы о важном")
class TestFaq:

    @allure.title("Проверка открытия текста ответа на вопрос")
    @allure.description("При клике на вопрос должен открываться соответствующий текст")
    @allure.story("Аккордеон")
    @pytest.mark.parametrize("index, expected_part", [
        (0, "400 рублей"),
        (1, "один заказ — один самокат"),
        (2, "8 мая"),
        (3, "завтрашнего дня"),
        (4, "1010"),
        (5, "восемь суток"),
        (6, "Штрафа не будет"),
        (7, "Москве")
    ])
    def test_faq_answers(self, driver, index, expected_part):
        main_page = MainPage(driver, MainPageLocators)

        main_page.accept_cookies()
        main_page.scroll_to_faq_block()
        main_page.click_question(index)

        assert main_page.is_answer_visible(index), f"Ответ на вопрос {index} не видим"

        actual_text = main_page.get_answer_text(index)
        assert expected_part in actual_text, f"'{expected_part}' не найдено в тексте: {actual_text}"