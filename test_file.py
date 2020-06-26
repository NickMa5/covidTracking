# L = [10, 8, 5, 4, 2, 1]
# print(L)
# print(type(L))
#
# diff = [i-j for i, j in zip(L[:-1], L[1:])]+[0]
# print(diff)

import pandas as pd
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
df = pd.read_csv(url)

print(df)