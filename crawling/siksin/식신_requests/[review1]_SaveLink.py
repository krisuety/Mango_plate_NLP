from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import requests
import itertools
import numpy as np
import pandas as pd
import re
import csv

#options
options = Options()
options.add_argument('headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(3)
# driver = webdriver.Chrome()

link_list = []
# 1 ~ 17까지 있음
for i in range(1,18):
    print('======================================')
    print(f'> [ {i} / 17 ] => 총 지역수')
    print('======================================')
    driver.get(f'https://www.siksinhot.com/taste?upHpAreaId={i}&hpAreaId=&isBestOrd=Y')
    driver.find_element_by_css_selector('div.select > a').click()
    num_loc = len(driver.find_elements_by_css_selector('div.area_detail_list li'))  # 장소 개수
    for j in range(2, num_loc+1):
        try:
            link = driver.find_element_by_css_selector(f'div.area_detail_list li:nth-child({j}) > a').get_attribute("href")
            link_areaid_up = int(re.search('upHpAreaId=(.*)&hpAreaId', link).group(1)) # 지역번호
            link_areaid_dw = int(re.search('hpAreaId=(.*)&isBestOrd' , link).group(1)) # 장소번호
            
            driver.get(link)
            num_review = int(driver.find_element_by_css_selector('div.category_menu > ul > li:last-child > a > span').text[1:-1])
            area_up = driver.find_element_by_css_selector( 'div.select > a' ).text.split(',')[0]
            area_dw = driver.find_element_by_css_selector( 'div.select > a' ).text.split(',')[1]
            link_list.append([ area_up, area_dw, link, link_areaid_up, link_areaid_dw, num_review ])
            print(f'> ( {j} / {num_loc} ) => {area_up}, {area_dw}')
        except:
            print(f'> [ 오류 ] ★★★★★★')


# 파일로 저장
with open('C:/Users/hky/Desktop/link.csv', 'w', newline='') as f: 
    file = csv.writer(f)
    for row in link_list:
        file.writerow(row)
