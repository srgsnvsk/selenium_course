# import pytest
# from selenium.webdriver.common.by import By

# link = "http://selenium1py.pythonanywhere.com/"

# def test_guest_should_see_login_link(browser):
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")



# pytest --browser_name=chrome --language=en-gb -s test_file.py

# import pytest
# from selenium.webdriver.common.by import By

# def test_guest_should_see_login_link(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     assert browser.find_element(By.CSS_SELECTOR, "#login_link"), "Login link is not present on the page"



# import pytest
# from selenium.webdriver.common.by import By

# def test_guest_can_go_to_login_page(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()



# import pytest
# from selenium.webdriver.common.by import By

# link = "http://selenium1py.pythonanywhere.com/"

# def go_to_login_page(browser):
#     link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     link.click()

# def test_guest_can_go_to_login_page(browser):
#    browser.get(link)
#    go_to_login_page(browser)

from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()