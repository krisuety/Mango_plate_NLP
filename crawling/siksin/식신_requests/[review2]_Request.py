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

# 322 => [[1, 100], [101, 100], [201, 100], [301, 21]]
# 350 => [[1, 100], [101, 100], [201, 100], [301, 49]]

def Paging(num):
    result = []
    start = 1
    while num > 100:    
        limit = 100
        result.append([start,limit])
        num -= 100
        start = start + limit
    result.append([start, num-1])
    return result


with open('C:/Users/hky/Desktop/link.csv', 'r') as f:
    data = csv.reader(f)
    result = []
    # ['대구', ' 동성로/중앙로/종로', 'https://www.siksinhot.com/taste?upHpAreaId=6&hpAreaId=195&isBestOrd=N', '6', '195', '2112']
    for row in data:
        print(f'> [ 진행 ] => {row[0]}, {row[1]} (댓글수: {int(row[5])-1})')
        temp_lst = Paging(int(row[-1]))
        for (start, limit) in temp_lst:
            try:
                url = f'https://api.siksinhot.com/v1/story/hpArea?idx={start}&limit={limit}&sort=T&upHpAreaId={row[3]}&hpAreaId={row[4]}&lat=&lng=&isBestOrd=N'
                headers = {
                        "Accept": "application/json, text/plain, */*",
                        "Origin": "https://www.siksinhot.com",
                        "Referer": "https://www.siksinhot.com/taste?upHpAreaId=1&hpAreaId=511&isBestOrd=N",
                        "siksinOauth": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjAsImlhdCI6MTU2MDYwODMyMiwiZXhwIjoxNTYwNjk0NzIyLCJpc3MiOiJzaWtzaW4ifQ.pUhjGpyjsx0TrvULXmtCmGMeHlJUtuc6f4YBGKchH-c",
                        "User-Agent": "Chrome/74.0.3729.169",
                        'limit': '50'
                    }
                
        
                
                response = requests.get(url, headers=headers)
                
                data_lst = response.json()['data']['list']
                data_lst = list(map(lambda x: x['storyContents'], data_lst ))
                result += data_lst
            except:
                print(f'[오류] => start: {start}, limit: {limit}')
        print(f'> [ 완료 ] => 현재까지 댓글 수 : [{len(result)}개]\n====================================')
        
    
    df = pd.DataFrame(result, columns=["reviews"])
    df['reviews'] = df['reviews'].str.replace('[^\w\s#@/:%.,_-]', '', flags=re.UNICODE)
    df = df.dropna().reset_index(drop=True)
    df.to_excel("siksin_gangnam_reviews_2.xlsx", sheet_name='sheet1')


