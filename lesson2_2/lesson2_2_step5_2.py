# метод execute_script
# скроллим нужный элемент на заданное количество пикселей
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
time.sleep(5)
browser.execute_script("window.scrollBy(0, 100);") # js-скрипт для скролла на 100 пикселей
time.sleep(5)
button.click()
