# метод execute_script
# скроллим нужный элемент
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
time.sleep(5)
browser.execute_script("return arguments[0].scrollIntoView(true);", button) # js-скрипт для скролла
time.sleep(5)
button.click()
