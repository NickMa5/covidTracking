import requests
import json
import urllib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

state = input("Enter state initials: ").upper()

if str.isalpha(state) == False:
    print("No numbers allowed.")
elif len(state) != 2:
    print("Initials can only be 2 letters.")
elif len(state) == 2:
    print(state)
# api source for additional info, https://covidtracking.com/api
# https://covidtracking.com/api/v1/states/
url = "https://covidtracking.com/api/v1/states/" + state + "/daily.json"

data = requests.get(url).json()

#print("positive " + str(data['positive']))

def get_data(key):
    empty_list = []
    for item in data:
        total = item.get(key)
        empty_list.append(total)
    return empty_list

dates = get_data('date')
total_positive = get_data('positive')
diff = [i-j for i, j in zip(total_positive[:-1], total_positive[1:])]+[0]
df = pd.DataFrame(list(zip(dates, total_positive, diff)), columns=['date', 'positive', 'diff'])
df['date'] = df['date'].astype('str')
# df['date'] = pd.to_datetime(df['date'], yearfirst=True, format="%Y/%m/%d").dt.date
df = df.sort_values(by='date', ascending=True)
print(dates)
print(total_positive)
print(diff)
print(df)
print(df.info())

# fig, ax = plt.subplots()
# #fig.set_size_inches(8, 15)
# plt.xticks(rotation=70)
# sns.barplot(data=df, x="date", y="diff")
# plt.show()

fig, ax1 = plt.subplots(figsize=(20, 6))
color = 'tab:green'
ax1.set_title(f"{state}: Covid 19 Cases", fontsize=16)
ax1.set_xlabel('Dates', fontsize=16)
ax1.set_ylabel('Daily Increase', fontsize=16, color=color)
ax1 = sns.barplot(x='date', y='diff', data=df, palette='summer')
ax1.tick_params(axis='y')
ax1.set_xticklabels(labels=df.date, rotation=60)
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Cumlative', fontsize=16, color=color)
ax2.set_xticklabels(labels=df.date, rotation=60)
ax2 = sns.lineplot(x='date', y='positive', data=df, sort=False, color=color)
ax2.tick_params(axis='y', color=color)
plt.show()