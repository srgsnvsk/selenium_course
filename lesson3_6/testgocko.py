from selenium import webdriver   
Base_url = "https://www.mozilla.org/en-US/"
driver = webdriver.Firefox()    
#executable_path=r'/usr/local/bin/geckodriver'
driver.get(Base_url) 