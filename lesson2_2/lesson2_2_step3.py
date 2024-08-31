from selenium import webdriver # webdriver набор команд управления браузером
from selenium.webdriver.common.by import By # класс By способ поиска элемента
from selenium.webdriver.support.ui import Select # класс Select для работы с выпадашками
import time # паузы

# конструкция try/finnaly для закрытия браузера если тест упадет с ошибкой
try:
    link = "http://suninjuly.github.io/selects1.html" # ссылка
    browser = webdriver.Chrome()
    browser.get(link)

    # находим элементы num1 и num2 и забираем текстовые значения
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    get_num1 = num1.text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    get_num2 = num2.text
    # преобразуем str в int 
    int_num1, int_num2  = int(get_num1), int(get_num2)
    # считаем сумму
    sum = int_num1 + int_num2
    # преобразуем int в str
    sum = str(sum)
    # наглядно посмотреть для отладки
    print(get_num1)
    print(get_num2)
    print(sum)

    # находим выпадающий список и выбираем значение равное сумме sum
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)

    # нажимаем отправить 
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    # ожидание
    time.sleep(5)
    # закрытие браузера
    browser.quit()

# пустая строка
