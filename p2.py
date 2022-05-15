from IPython.display import display
import pandas as pd


url = r'https://spbexchange.ru/ru/stocks/ratings.aspx'

tables = pd.read_html(url)

rating_table = tables[0]

rating_table.to_csv('out.csv')
