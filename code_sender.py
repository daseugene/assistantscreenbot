from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("Desktop/chromewebdriver")

driver.get("https://remotedesktop.google.com/support")

driver.find_element(By.CLASS_NAME, 'Xb9hP')

next1 = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
next1.click()



