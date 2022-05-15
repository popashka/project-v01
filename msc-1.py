from IPython.display import display
import pandas as pd
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

url = 'https%3A%2F%2Fwww.moex.com%2Fru%2Fmarketdata%2F%23%2Fmode%3Dgroups%26group%3D4%26collection%3D3%26boardgroup%3D57%26data_type%3Dhistory%26date%3D2021-12-30&rn=544124220&wv-type=3&browser-info=bt%3A1%3Agdpr%3A14%3Aet%3A1641133032%3Aw%3A375x800%3Av%3A722%3Az%3A180%3Ai%3A20220102171711%3Au%3A164112684738862952%3Avf%3Aykcyjkqfpgygy7cm9r%3Awe%3A1%3Ast%3A1641133032&t=gdpr(14)ti(2)'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_='GeneralValue_cell_3uWJX')

print(quotes)
