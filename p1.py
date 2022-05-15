import pandas as pd
from IPython.display import display


url = r'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

tables = pd.read_html(url)

sp500_table = tables[0]

display(sp500_table)
