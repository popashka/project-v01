import time
from IPython.display import display
import pandas as pd
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

while(True):
    url = 'https://ru.investing.com/currencies/usd-rub'
    response = requests.get(url)
    print(response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")

    all = soup.findAll('span', class_='text-2xl')
    print(all[0].text)
    #d = {'col1': [1], 'col2': [all[0].text]}
    #df = pd.DataFrame(data=d)
    #df.to_csv('out.csv', mode='a', index=False, header=False)

    time.sleep(3)