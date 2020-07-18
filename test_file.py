# L = [10, 8, 5, 4, 2, 1]
# print(L)
# print(type(L))
#
# diff = [i-j for i, j in zip(L[:-1], L[1:])]+[0]
# print(diff)

import pandas as pd
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
df = pd.read_csv(url)

print(df.head())

# sum data by state
df_county = df.copy()
df_county = df_county.groupby(['date', 'state', 'county']).sum()
df_county = df_county.drop('fips', axis=1)
df_county = df_county.sort_values(by=['state', 'county', 'date'], ascending=True).reset_index()
df_county['st_cnty'] = df_county['state'] + ", " + df_county['county']
print(df_county.head())

dff = df_county.copy()
deaths = dff['deaths']
dff['daily'] = [0] + [i - j for i, j in zip(deaths[:-1], deaths[1:])]
dff['daily'] = dff['daily'].apply(lambda x: x * -1)
print(dff[dff['st_cnty']=='Tennessee, Davidson'])

# # state dataframe
# dff = df.copy()
# dff = dff[dff['state'] == st_slctd]
# dff_state = df.groupby(['date', 'state']).sum()
# dff_state = dff_state.sort_values(by=['state', 'date'], ascending=True)
# dff_state = dff_state.reset_index()
# st_cases = dff_state['cases']
# dff_state['daily'] = [0] + [i - j for i, j in zip(st_cases[:-1], st_cases[1:])]
# dff_state['daily'] = dff_state['daily'].apply(lambda x: x * -1)
#
# # county dataframe
#
# def update_state_graph(st_slctd):
#     print(st_slctd)
#     print(type(st_slctd))
#
#     container = f"Selected state is: {st_slctd}."
#
#     dff = df.copy()
#     dff = dff[dff['state'] == st_slctd]
#     dff_state = df.groupby(['date', 'state']).sum()
#     dff_state = dff_state.sort_values(by=['state', 'date'], ascending=True)
#     dff_state = dff_state.reset_index()
#     st_cases = dff_state['cases']
#     dff_state['daily'] = [0] + [i - j for i, j in zip(st_cases[:-1], st_cases[1:])]
#     dff_state['daily'] = dff_state['daily'].apply(lambda x: x * -1)
#
#     return dff_state.head()
#
# def update_cnty_graph(st_slctd,cnty_slctd):
#     print(st_slctd, cnty_slctd)
#     print(type(st_slctd), type(cnty_slctd))
#
#     container = f"Selected state and county is: {cnty_slctd}, {st_slctd}."
#
#     dff = df.copy()
#     dff_cnty = dff[(dff['state'] == st_slctd) & (dff['county'] == cnty_slctd)]
#     cnty_cases = dff_cnty['cases']
#     dff_cnty['daily'] = [0] + [i - j for i, j in zip(cnty_cases[:-1], cnty_cases[1:])]
#     dff_cnty['daily'] = dff_cnty['daily'].apply(lambda x: x * -1)
#
#     return dff_cnty
#
#
# print(dff_st.head())
# print(dff_cnty.head())