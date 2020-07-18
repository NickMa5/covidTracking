import pandas as pd
import numpy as np

import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# -------------------------------------------------------
# Import and sort data by state then county
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
df = pd.read_csv(url)
df = df.drop(columns='fips', axis=1)
df = df.sort_values(by=['state', 'county', 'date'], ascending=True)

# sum data by state
df_state = df.groupby(['date', 'state']).sum()
df_state = df_state.sort_values(by=['state', 'date'], ascending=True)
df_state = df_state.reset_index()
print(df_state.head())

# sum data by county
df_county = df.groupby(['date', 'state', 'county']).sum()
df_county = df_county.sort_values(by=['state', 'county', 'date'], ascending=True)
df_county = df_county.reset_index()
df_county['st_cnty'] = df_county['state'] + ", " + df_county['county']


print(df_county.head())

# create drop down list for app
st_drpdwn = np.array(df_state['state'].drop_duplicates())
cnty_drpdwn = np.array(df_county['st_cnty'].drop_duplicates())

# -------------------------------------------------------
# App Layout
app.layout = html.Div([
    html.H1("Daily positive covid cases by state and county.", style={"text-align":"center"}),

    html.H3("Select state.", style={"text-align":"left"}),
    dcc.Dropdown(id="slct_state",
                 options=[{"label":x, "value":x} for x in st_drpdwn],
                 value="Alabama",
                 multi=False,
                 style={"width":"40%"}),
    html.Div(id='st_container', children=[]),
    html.Br(),

    dcc.Graph('st_bar_chart',figure={}),
    html.Br(),

    html.H3("Select county.", style={"text-align":"left"}),
    dcc.Dropdown(id="slct_cnty",
                 options=[{"label": x, "value": x} for x in cnty_drpdwn],
                 value='Alabama, Autauga',
                 multi=False,
                 style={"width": "40%"}),
    html.Div(id='cnty_container', children=[]),
    html.Br(),

    dcc.Graph('cnty_bar_chart', figure={})
])

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='st_container', component_property='children'),
     Output(component_id='cnty_container', component_property='children'),
     Output(component_id='st_bar_chart', component_property='figure'),
     Output(component_id='cnty_bar_chart', component_property='figure')],

    [Input(component_id='slct_state', component_property='value'),
     Input(component_id='slct_cnty', component_property='value')]
)

# State dataframe for graph
def update_state_graph(state_slctd):
    print(state_slctd)
    print(type(state_slctd))

    container = "Selected state is: {}".format(state_slctd)

    dff = df_state.copy()
    dff = dff[dff['state'] == state_slctd]
    st_cases = dff['cases']
    dff['daily'] = [0] + [i - j for i, j in zip(st_cases[:-1], st_cases[1:])]
    dff['daily'] = dff['daily'].apply(lambda x: x * -1)
    # Plotly Express
    fig = px.bar(
        data_frame=dff,
        x='date',
        y='daily',
        template='plotly_dark')

    return container, fig

# County dataframe for graph
def update_county_graph(county_slctd):
    print(county_slctd)
    print(type(county_slctd))

    container = "Selected state and county is: {}".format(county_slctd)

    dff_ct = df_county.copy()
    dff_ct = dff_ct[dff_ct['st_cnty'] == county_slctd]
    cases = dff_ct['cases']
    dff_ct['daily'] = [0] + [i - j for i, j in zip(cases[:-1], cases[1:])]
    dff_ct['daily'] = dff_ct['daily'].apply(lambda x: x * -1)
    # Plotly Express
    fig = px.bar(
        data_frame=dff_ct,
        x='date',
        y='daily',
        template='plotly_dark')

    return container, fig

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)