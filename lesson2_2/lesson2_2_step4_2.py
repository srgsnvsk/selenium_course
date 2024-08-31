# выводим другой title
import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("document.title='Script executing';") # title
time.sleep(7)
