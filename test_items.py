link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_btn_add_to_basket_is_exist(browser):
    browser.get(link)
    assert len(browser.find_elements_by_css_selector(".btn-add-to-basket")) > 0, \
        "Кнопка добавить в корзину не найдена"
