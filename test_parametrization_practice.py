import pytest
from selenium import webdriver
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()

    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_get_answer(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)


    field = WebDriverWait(browser,0).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']"))
    )
    answer = math.log(int(time.time()))
    field.send_keys(str(answer))

    button = WebDriverWait(browser,0).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='submit-submission']"))
    )
    button.click()

    check = WebDriverWait(browser,1).until(
        EC.presence_of_element_located((By.XPATH,"//pre[@class='smart-hints__hint']"))).text

    print(check)

    assert "Correct!" in check