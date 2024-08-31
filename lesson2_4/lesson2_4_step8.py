from selenium import webdriver # webdriver набор команд управления браузером
from selenium.webdriver.common.by import By # класс By способ поиска элемента
from selenium.webdriver.support.ui import WebDriverWait # классявных ожиданий. используется совместно с expected_conditions
from selenium.webdriver.support import expected_conditions as EC # инструмент явного ожидания
import time # паузы
import math


# рассчитываем значение функции
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# конструкция try/finnaly для закрытия браузера если тест упадет с ошибкой
try:
    link = "http://suninjuly.github.io/explicit_wait2.html" # ссылка
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока цена не станет $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    
    # находим кнопку book
    btn_book = browser.find_element(By.ID, "book")
    btn_book.click()

    # скролл
    browser.execute_script("window.scrollBy(0, 100);")
    
    # подхватываем значение х
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    
    # заполняем поле
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
    
    # нажимаем submit
    btn_solve = browser.find_element(By.CSS_SELECTOR, "#solve")
    btn_solve.click()
    
    # копируем из алерта число для ответа
    print(browser.switch_to.alert.text.split()[-1])

finally:
    # ожидание
    time.sleep(5)
    # закрытие браузера
    browser.quit()

# пустая строка
