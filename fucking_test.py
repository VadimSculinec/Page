import pytest

from pages.product_page import ProductPage


def test_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = ProductPage(browser, link, 5)
    page.open()
    page.should_be_button_add()
    page.add_product()
    page.solve_quiz_and_get_code()
    page.should_correct_book_name(page.extract_text_book(), page.extract_text_book_from_adress())
