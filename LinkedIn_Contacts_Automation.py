#⭐ STARTER CODE ⭐
#************************************

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/ASUS/Desktop/chromedriver.exe')
driver.get('https://www.linkedin.com')
time.sleep(5)

#********** LOG IN *************

username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys('fehmiess007@gmail.com')
password.send_keys('infernoTN007')
time.sleep(2)

submit = driver.find_element_by_xpath("//button[@type='submit']").click()


#***************** ADD CONTACTS ***********************
search_bar=driver.find_element_by_xpath("//input[@aria-label='Search']")
search_bar.send_keys("human resource")
time.sleep(2)
search_bar.send_keys(Keys.ENTER)
time.sleep(5)
people = driver.find_element_by_xpath("//button[@aria-label='People']").click()
time.sleep(5)
for  i in range(5):
  
    
    all_buttons=driver.find_elements_by_tag_name("button")
    connect_buttons=[btn for btn in all_buttons if (btn.text=="Connect" or btn.text=="Connect")]
    for btn in connect_buttons:
        driver.execute_script("arguments[0].click();",btn)
        time.sleep(2)
        
        send = driver.find_element_by_xpath("//button[@aria-label='Send now']").click()
    next = driver.find_element_by_xpath("//button[@aria-label='Next']").click()
    