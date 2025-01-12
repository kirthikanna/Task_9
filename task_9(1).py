#Title of the webpage

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import service
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
print(driver.title)
