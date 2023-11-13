import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("F:/ML Study/web_scraping_smartprix/msedgedriver.exe")       # local file path webdriver application

driver = webdriver.Edge(service = s)

driver.get('https://www.smartprix.com/laptops')     # smartprix site url
time.sleep(1)

for i in range(0,10):      # Fetching data for only 10 pages  i.e. 200 items info
    time.sleep(1)
    driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/div[1]/div[3]/div[3]').click()
html = driver.page_source
with open('smartprix.html','w',encoding='utf-8') as f:     # Writing content in html file
    f.write(html)

# give input in order to present closing of browser
input()








