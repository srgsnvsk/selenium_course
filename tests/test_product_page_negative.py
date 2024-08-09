import pytest
from pages.product_page import ProductPage
# import time

@pytest.mark.xfail(reason="Такое вот падающее задание")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.add_to_basket() # добавляем в корзину
    page.should_not_be_success_message() # проверяем, что нет сообщения об успехе

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.should_not_be_success_message() # проверяем, что нет сообщения об успехе

@pytest.mark.xfail(reason="Такое вот падающее задание")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.add_to_basket() # добавляем в корзину
    page.should_disappear_success_message() # проверяем, что элемент исчезает
    
