import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# state = input("Enter state: ").upper()
# county = input("Enter county: ").upper()

#df = pd.read_csv('us-counties.csv')
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
df = pd.read_csv(url)
df = df.sort_values(by=['state', 'county', 'date'], ascending=True)
df = df.set_index(['state', 'county'])
df2 = df.loc[('Tennessee', 'Davidson')]

#df2 = df.loc[[df['county'] == 'Davidson', df['state'] == 'Tennessee']]
df2 = df2.reset_index()
print(df2)
cases = df2['cases']

df2['daily'] = [0] + [i-j for i, j in zip(cases[:-1], cases[1:])]
df2['daily'] = df2['daily'].apply(lambda x: x * -1)
# diff = [i-j for i, j in zip(cases[:-1], cases[1:])]+[0]
print(cases)
print(df2)

fig, ax = plt.subplots(figsize=(15,5))
ax.axhline(df2.daily.iloc[-14:].mean(), color='blue', linewidth=2)
ax.axhline(df2.daily.iloc[-21:].mean(), color='green', linewidth=2)
ax.axhline(df2.daily.mean(), color='red', linewidth=2)
plt.xticks(rotation=60)
ax.set_title('Davidson, TN Positive Cases', fontsize=15)
sns.barplot(data=df2, x="date", y="daily", palette='winter')
plt.show()

# fig, ax1 = plt.subplots(figsize=(20, 6))
# color = 'tab:green'
# ax1.set_title(f"{state}, {county} county: Covid 19 Cases", fontsize=16)
# ax1.set_xlabel('Dates', fontsize=16)
# ax1.set_ylabel('Daily Increase', fontsize=16, color=color)
# ax1 = sns.barplot(x='date', y='daily', data=df2, palette='summer')
# ax1.tick_params(axis='y')
# ax1.set_xticklabels(labels=df.date, rotation=60)
# ax2 = ax1.twinx()
# color = 'tab:red'
# ax2.set_ylabel('Cumlative', fontsize=16, color=color)
# ax2.set_xticklabels(labels=df.date, rotation=60)
# ax2 = sns.lineplot(x='date', y='cases', data=df2, sort=True, color=color)
# ax2.tick_params(axis='y', color=color)
# plt.show()


#df3 = pd.DataFrame(list(zip(df2, diff)), columns=['state', 'county', 'date', 'fips', 'cases', 'deaths', 'delta'])

# state = input("Enter state initials: ").upper()
#
# if str.isalpha(state) == False:
#     print("No numbers allowed.")
# elif len(state) != 2:
#     print("Initials can only be 2 letters.")
# elif len(state) == 2:
#     print(state)
#
# def new_df(state, county):
#     input(state, county)
#     df2 = df.loc[state,county]
#
# print(df.head(3))
# print(df2.head(3))