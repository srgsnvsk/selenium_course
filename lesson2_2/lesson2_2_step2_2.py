# ищем элемент по видимому тексту 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text("1") # ищем элемент с текстом "1"

# пустая строка
