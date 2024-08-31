import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://stepik.org/catalog?auth=login"

# Нужна тут фикстура?
@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestAuthLogin():

    def test_user_autorization(self, browser):
        browser.get(link)
        # явное ожидание
        # как только элемент загрузится, он сохранится в переменной email
        email = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#id_login_email"))
        )
        email.send_keys("srgsnvsk@gmail.com")

        password = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#id_login_password"))
        )
        password.send_keys("100Bullets")

        login = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="sign-form__btn button_with-loader "]'))
        )         
        login.click()
      
        # Дополнительное ожидание для проверки успешного логина
        # Ожидаем элемент, который появляется после успешного логина
        success_element = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar__profile-img"))
        )

        # Проверка, что логин был успешным (элемент присутствует на странице)
        assert success_element is not None

        # Можно добавить дополнительное ожидание на несколько секунд
        time.sleep(5)

