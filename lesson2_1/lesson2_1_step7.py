from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим элемент и берем значение valuex
    find_img = browser.find_element(By.ID, "treasure")
    get_valuex = find_img.get_attribute("valuex")
    print("value of people valuex: ", get_valuex)
    assert get_valuex is not None, "Нету valuex"

    # вычисляем по формуле
    calculate = calc(get_valuex)
    
    # вставляем наше вычисление
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(calculate)
    
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
