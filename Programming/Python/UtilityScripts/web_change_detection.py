from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys

import time
import winsound



driver = webdriver.Chrome("C:\\Users\\Harshitha\\Downloads\\chromedriver_win32_Latest\\chromedriver.exe")
driver.get('https://entrar.in/login/login')

wait = WebDriverWait(driver, 600) 
login_username = driver.find_element_by_name("username")
login_username.send_keys("B/16609")
login_password = driver.find_element_by_name("password")
login_password.send_keys("varun@2009")
login_password.send_keys(Keys.ENTER)
driver.get('https://entrar.in/classroom_creation_crm_new/s_display')
while True :                        
    time.sleep(5)
    search=driver.find_element_by_name('select')
    search.click()

    try :
        element = driver.find_element_by_link_text("Join")
        frequency = 2500 
        duration = 500  
        for x in range(10):
            winsound.Beep(frequency, duration)
        break 
    except :
        continue 
    else :
        frequency = 2500 
        duration = 500  
        for x in range(10):
            winsound.Beep(frequency, duration)
        break 
        
    # print(element)