import pandas as pd
import re
from datetime import datetime, date, time
from matplotlib import pyplot

df = pd.read_csv ('baba.csv')
print(df)

p1 = df.iat[0, 2]

print(df.shape[0])


### Приводим данные в читаемый вид

for i in range(df.shape[0]):
    p1 = df.iat[i, 2]
    p1 = p1.replace(".", "")
    p1 = p1.replace(",", ".")
    df.iat[i, 2] = p1

    p1 = df.iat[i, 4]
    p1 = p1.replace(",", ".")
    df.iat[i, 4] = p1


### Заменяем рубли на доллары, чтобы сравнивать в одной валюте


for i in range(df.shape[0]):
    p1 = float(df.iat[i, 2])

    change = float(df.iat[i, 4])

    p1 /= change
    df.iat[i, 2] = p1


print(df)

df.to_csv('baba-ann.csv', mode='a', index=False, header=False)

### Будем насчитывать волатильность каждой биржы по каждому дню

msc = []
ldn = []
pit = []

dif1 = 0
dif2 = 0
dif3 = 0

mnmsc = mxmsc = df.iat[0, 2]
mnldn = mxldn = df.iat[0, 1]
mnpit = mxpit = df.iat[0, 0]
was = int(df.iat[0, 3][8:10])

for i in range(df.shape[0]):
    now = int(df.iat[i, 3][8:10])
    if (was == now):
        mnmsc = min(mnmsc, float(df.iat[i, 2]))
        mxmsc = max(mxmsc, float(df.iat[i, 2]))
        mnldn = min(mnldn, float(df.iat[i, 1]))
        mxldn = max(mxldn, float(df.iat[i, 1]))
        mnpit = min(mnpit, float(df.iat[i, 0]))
        mxpit = max(mxpit, float(df.iat[i, 0]))
    else :
        was = now
        msc.append((mxmsc - mnmsc))
        ldn.append((mxldn - mnldn))
        pit.append((mxpit - mnpit))

        mnmsc = mxmsc = df.iat[i, 2]
        mnldn = mxldn = df.iat[i, 1]
        mnpit = mxpit = df.iat[i, 0]


    dif1 = dif1 + (max(df.iat[i, 2], df.iat[i, 1]) / min(df.iat[i, 2], df.iat[i, 1]))
    dif2 = dif2 + (max(df.iat[i, 2], df.iat[i, 0]) / min(df.iat[i, 2], df.iat[i, 0]))
    dif3 = dif3 + (max(df.iat[i, 1], df.iat[i, 0]) / min(df.iat[i, 1], df.iat[i, 0]))


msc.append((mxmsc - mnmsc))
ldn.append((mxldn - mnldn))
pit.append((mxpit - mnpit))

dif1 /= df.shape[0]
dif2 /= df.shape[0]
dif3 /= df.shape[0]

print("Differences are")
print("msc-ldn ")
print(dif1)
print("msc-pit ")
print(dif2)
print("ldn-pit ")
print(dif3)

d = {'msc': msc, 'ldn': ldn, 'pit': pit}

df2 = pd.DataFrame(data=d)
df2.to_csv('baba-an.csv')

#pyplot.plot(msc, 'bo', label='msc volatil')
#pyplot.plot(ldn, 'ro', label='ldn volatil')
#pyplot.plot(pit, 'go', label='pit volatil')
#pyplot.ylim(ymax = 1.02, ymin = 0.98)
#pyplot.legend()
#pyplot.show()

avmsc = 0
avldn = 0
avpit = 0

for i in range(len(msc)):
    avmsc += msc[i]
    avldn += ldn[i]
    avpit += pit[i]

avmsc /= len(msc)
avldn /= len(ldn)
avpit /= len(pit)

print(avmsc)
print(avldn)
print(avpit)
