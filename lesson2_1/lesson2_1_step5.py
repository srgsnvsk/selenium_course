from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


# рассчитываем значение функции
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # подхватываем значение х
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    # заполняем поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    # отмечаем чекбокс
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    # отмечаем радиобаттон
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    # нажимаем submit
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
