import pandas as pd
import numpy as np

import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# -------------------------------------------------------
# Import and parse data

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
df = pd.read_csv(url)
df = df.sort_values(by=['state', 'county', 'date'], ascending=True)


# sum data by county
df_county = df.groupby(['date', 'state', 'county']).sum()
df_county = df_county.drop('fips', axis=1)
df_county = df_county.sort_values(by=['state', 'county', 'date'], ascending=True)

df_county = df_county.reset_index()
df_county['st_cnty'] = df_county['state'] + ", " + df_county['county']
dropdown = np.array(df_county['st_cnty'].drop_duplicates())

print(df_county.head())

# -------------------------------------------------------
# App Layout
app.layout = html.Div([

    html.H1("Daily Covid deaths by State and County", style={'text_align': 'center'}),
    dcc.Dropdown(id="slct_state",
                 options=[{"label":x, "value":x} for x in dropdown],
                 multi=False,
                 value= 'Alabama, Autauga',
                 style={'width':'40%'}
                 ),
    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='deaths_chart', figure={})
])

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='deaths_chart', component_property='figure')],
    [Input(component_id='slct_state', component_property='value')]
)

def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "Selected state and county is: {}".format(option_slctd)

    dff = df_county.copy()
    dff = dff[dff['st_cnty'] == option_slctd]
    deaths = dff['deaths']
    dff['daily'] = [0] + [i - j for i, j in zip(deaths[:-1], deaths[1:])]
    dff['daily'] = dff['daily'].apply(lambda x: x * -1)
    # Plotly Express
    fig = px.bar(
        data_frame=dff,
        x='date',
        y='daily',
        template='plotly_dark')

    return container, fig

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)