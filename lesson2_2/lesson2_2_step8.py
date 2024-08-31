from selenium import webdriver # webdriver набор команд управления браузером
from selenium.webdriver.common.by import By # класс By способ поиска элемента
import time # паузы
import os # модуль для работы с ОС

# конструкция try/finnaly для закрытия браузера если тест упадет с ошибкой
try:
    link = "http://suninjuly.github.io/file_input.html" # ссылка
    browser = webdriver.Chrome()
    browser.get(link)

    # фамилия
    f_name = browser.find_element(By.CSS_SELECTOR, f'input[placeholder="{'Enter first name'}"]')
    f_name.send_keys("Торвальдс")
    # имя
    l_name = browser.find_element(By.CSS_SELECTOR, f'input[placeholder="{'Enter last name'}"]')
    l_name.send_keys("Линус")
    # почта
    mail = browser.find_element(By.CSS_SELECTOR, f'input[placeholder="{'Enter email'}"]')
    mail.send_keys("example@mail.com")
    
    obzor = browser.find_element(By.CSS_SELECTOR, "#file")
    # загружаем файл с пекарни
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')
    obzor.send_keys(file_path)
    
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
