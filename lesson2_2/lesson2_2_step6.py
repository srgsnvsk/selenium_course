from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


# рассчитываем значение функции
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # подхватываем значение х
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    # заполняем поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    # скроллим
    browser.execute_script("window.scrollBy(0, 150);")
    # отмечаем чекбокс
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    # отмечаем радиобаттон
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    # нажимаем submit
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    # копируем из алерта число для ответа
    print(browser.switch_to.alert.text.split()[-1])

finally:
    # ожидание
    time.sleep(5)
    # закрываем браузер
    browser.quit()

# пустая строка
