# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
title = driver.title

el = driver.find_element(By.TAG_NAME, 'div')
print(el.text)
