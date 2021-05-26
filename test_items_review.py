import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_assert_button_diff_language(browser):
    browser.get(link)
    time.sleep(5)
    # Проверяем, что элемент присутствует на странице
    button = browser.find_elements_by_id("add_to_basket_form")
    assert button, "Кнопка не найдена"