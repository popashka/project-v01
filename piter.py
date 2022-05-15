import pandas as pd
from IPython.display import display


url = r'https://spbexchange.ru/ru/market-data/default.aspx'

tables = pd.read_html(url)

international_companies = tables[0]
russian_companies = tables[1]

df = pd.DataFrame(data=russian_companies)
df2 = pd.DataFrame(data=international_companies)

lukoil = df.loc[df['Идентиф. Код ЦБ', 'Идентиф. Код ЦБ'] == 'LKOH']

print(lukoil)

price = lukoil.iat[0,3]

print(price)

sber = df.loc[df['Идентиф. Код ЦБ', 'Идентиф. Код ЦБ'] == 'SBER']

print(sber.iat[0, 3])

nvidia = df2.loc[df2['Идентиф. Код ЦБ', 'Идентиф. Код ЦБ'] == 'NVDA']

print(nvidia.iat[0, 3])

moderna = df2.loc[df2['Идентиф. Код ЦБ', 'Идентиф. Код ЦБ'] == 'MRNA']

print(moderna.iat[0, 3])