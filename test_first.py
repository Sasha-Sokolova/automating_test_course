from selenium import webdriver
import time
import unittest


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        self.browser.get(link)


    # Ваш код, который заполняет обязательные поля
    def test_search_in_python_org(self):

        browser = self.browser

    # Отправляем заполненную форму
        button = browser.find_element_by_css_selector(".first:required").send_keys("Van")

        button2 = browser.find_element_by_css_selector(".second:required").send_keys("Ivanov")

        button3 = browser.find_element_by_css_selector(".third:required").send_keys("test@test.ru")

        button4 = browser.find_element_by_xpath("//button[@type='submit']").click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(1)

    # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text


    # ожидание чтобы визуально оценить результаты прохождения скрипта

    # закрываем браузер после всех манипуляций
    def tearDown(self):
       self.browser.quit()

class PythonOrgSearch2(unittest.TestCase):

    def setUp(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        self.browser.get(link)

        # Ваш код, который заполняет обязательные поля
    def test_search_in_python_org(self):
        browser = self.browser

            # Отправляем заполненную форму
        button5 = browser.find_element_by_css_selector(".first:required").send_keys("Van")

        button6 = browser.find_element_by_css_selector(".second:required").send_keys("Ivanov")

        button7 = browser.find_element_by_css_selector(".third:required").send_keys("test@test.ru")
        button8 = browser.find_element_by_xpath("//button[@type='submit']").click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
        time.sleep(1)

            # находим элемент, содержащий текст
        welcome_text_elt1 = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text1 = welcome_text_elt1.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text1

            # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)

        # закрываем браузер после всех манипуляций
    def tearDown(self):
        self.browser.quit()





    if __name__ == "__main__":
     unittest.main()