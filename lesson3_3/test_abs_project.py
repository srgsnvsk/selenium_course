import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(
            By.CSS_SELECTOR, "input.form-control.first[placeholder='Input your first name']"
            )
        input1.send_keys("Ivan")
        input2 = browser.find_element(
            By.CSS_SELECTOR, "input.form-control.second[placeholder='Input your last name']"
            )
        input2.send_keys("Petrov")
        input3 = browser.find_element(
            By.CSS_SELECTOR, "input.form-control.third[placeholder='Input your email']"
            )
        input3.send_keys("example@email.com")
        input4 = browser.find_element(
            By.CSS_SELECTOR, "input.form-control.first[placeholder='Input your phone:']"
            )
        input4.send_keys("89009009090")
        input5 = browser.find_element(
            By.CSS_SELECTOR, "input.form-control.second[placeholder='Input your address:']"
        )
        input5.send_keys("Kursk")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # self.assertEqual
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
        input1.send_keys("Anastasiya")
        input2 = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
        input2.send_keys("Begunova")
        input3 = browser.find_element(By.XPATH, "//input[@class='form-control third']")
        input3.send_keys("ABmail@mail.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()

# пустая строка
