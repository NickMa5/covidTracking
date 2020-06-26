import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
#if you want graphs to automatically without plt.show
plt.style.use('fivethirtyeight') #a style that can be used for plots - see style reference above


# api source for additional info, https://covidtracking.com/api
url = "https://covidtracking.com/api/v1/states/current.json"

data = {}
data = requests.get(url).json()
# data1 = json.loads(data)
print(data)
print(type(data))
# states = []
# for item in data:
#     name = item.get('state')
#     states.append(name)
#
# total_positive = []
# for item in data:
#     total = item.get('positive')
#     total_positive.append(total)

def get_data(key):
    empty_list = []
    for item in data:
        total = item.get(key)
        empty_list.append(total)
    return empty_list

states = get_data('state')
total_positive = get_data('positive')

df = pd.DataFrame(list(zip(states, total_positive)), columns=['state', 'positive'])

print(states)
print(total_positive)
print(df)

fig, ax = plt.subplots()
fig.set_size_inches(15, 10)
plt.xticks(rotation=90)
sns.barplot(data=df, x="state", y="positive")
plt.show()
# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile)