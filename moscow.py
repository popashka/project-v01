from IPython.display import display
import pandas as pd
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

url = 'https://tools.morningstar.co.uk/uk/stockreport/default.aspx?SecurityToken=0P0000DGH3]3]0]E0WWE$$ALL'

response = requests.get(url)
print(response.status_code)


soup = BeautifulSoup(response.text, "html.parser")
#print(soup)

all = soup.findAll('span', class_='price')

lukoil_ldn = all[0].text
print(lukoil_ldn)

url2 = 'https://tools.morningstar.co.uk/uk/stockreport/default.aspx?SecurityToken=0P0000TM4T]3]0]E0WWE$$ALL'
response = requests.get(url2)
print(response.status_code)


soup = BeautifulSoup(response.text, "html.parser")
#print(soup)

all = soup.findAll('span', class_='price')

sber_ldn = all[0].text
print(sber_ldn)


url3 = 'https://www.finam.ru/quote/moex-akcii/lukoil/'
response = requests.get(url3)
print(response.status_code)


soup = BeautifulSoup(response.text, "html.parser")
#print(soup)

all = soup.findAll('span', class_='PriceInformation__price--26G')
print(all[0].text)
