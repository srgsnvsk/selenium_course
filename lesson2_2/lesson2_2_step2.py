from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)


browser.find_element(By.TAG_NAME, "select").click()
browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
# или строка может выглядеть так 
# browser.find_element(By.CSS_SELECTOR, "[value='1']").click()

# пустая строка
