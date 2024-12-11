from selenium import webdriver
import os
import time
import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

url = 'https://www.linkedin.com/jobs/search/?currentJobId=3492578215&geoId=105365761&keywords=data%20analyst&location=Nigeria&refresh=true'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(r"C:\\Users\\ADMIN\\Desktop\\dsalab\\chromedriver-win64\\chromedriver.exe")
driver.get(url)
jobs = driver.find_elements(By.TAG_NAME,'li')
company_name = []
for job in jobs:
      company = job.find_element(By.XPATH,"//h4").text
      company_name.append(company)
      print(company)