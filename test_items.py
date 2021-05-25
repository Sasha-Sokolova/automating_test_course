import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_put_item_into_basket(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_elements_by_xpath("//button[@type='submit']")
    print(len(button))
    # проверяем наличие кнопки
    assert len(button)>0

    for i in button:
        if i.get_attribute("value") == "Ajouter au panier":
            print("it's French!")
        else:
            print("It's another language")