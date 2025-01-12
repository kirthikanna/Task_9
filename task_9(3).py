#3)Extract the entire contents of the webpage and save it in a text file whose name will be "Webpage_task_11.txt"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import service
import time
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(5)
page_content = driver.find_element(By.XPATH,'/html/body').text
file = open('Webpage_task_11.txt','w')
file.write(page_content)
print("webpage content saved to 'Webpage_task_11.txt'")
file.close()