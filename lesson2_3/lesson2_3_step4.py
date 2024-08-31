from selenium import webdriver # webdriver набор команд управления браузером
from selenium.webdriver.common.by import By # класс By способ поиска элемента
import time # паузы
import math

# рассчитываем значение функции
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# конструкция try/finnaly для закрытия браузера если тест упадет с ошибкой
try:
    link = "http://suninjuly.github.io/alert_accept.html" # ссылка
    browser = webdriver.Chrome()
    browser.get(link)

    # жмакаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    # алерт
    alert = browser.switch_to.alert # переключаемся на окно
    alert.accept() # соглашаемся
    
    # подхватываем значение х
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    # заполняем поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    
    # нажимаем submit
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    # копируем из алерта число для ответа
    print(browser.switch_to.alert.text.split()[-1])

finally:
    # ожидание
    time.sleep(5)
    # закрытие браузера
    browser.quit()

# пустая строка
