import time
from selenium import webdriver
import collection
import pandas as pd
from bs4 import BeautifulSoup
from itertools import count

wd = webdriver.Chrome('C:\cafe24\python\webdriver/chromedriver.exe')
wd.get('http://www.cafe24.com')

time.sleep(10)  # 초단위

html = wd.page_source
print(html)

wd.quit()

