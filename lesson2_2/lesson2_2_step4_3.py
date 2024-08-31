# выводим title и вызываем alert
import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("document.title='Script executing';alert('Robots at work');") # title и alert
time.sleep(7)
