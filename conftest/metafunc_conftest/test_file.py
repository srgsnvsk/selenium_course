import pytest
from selenium.webdriver.common.by import By

def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, "#login_link"), "Login link is not present on the page"
