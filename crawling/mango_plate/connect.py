
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome(chrome_options=options)

driver.implicitly_wait(3)

def initpage(gu, num):
    driver.get('http://www.mangoplate.com/search/{}?keyword={}&page={}'
               .format(gu, gu, num))
    time.sleep(3)

def connect(url):
    driver.get('https://www.mangoplate.com/' + url)

