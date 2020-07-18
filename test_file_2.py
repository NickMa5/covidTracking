
option_slctd = "Tennessee"

def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "Selected state is: {}".format(option_slctd)
    print(option_slctd)

    dff = df.copy()
    dff = dff[dff['state'] == option_slctd]
    st_cases = dff['cases']
    dff['daily'] = [0] + [i - j for i, j in zip(st_cases[:-1], st_cases[1:])]
    dff['daily'] = dff['daily'].apply(lambda x: x * -1)
    # Plotly Express
    fig = px.bar(
        data_frame=dff,
        x='date',
        y='daily',
        template='plotly_dark')

    return container, fig, option_slctd

def update_state_graph(st_slctd):
    print(st_slctd)
    print(type(st_slctd))

    container = f"Selected state is: {st_slctd}."

    dff = df.copy()
    dff_state = dff[dff['state'] == st_slctd]
    dff_state = df.groupby(['date', 'state']).sum()
    dff_state = dff_state.sort_values(by=['state', 'date'], ascending=True)
    dff_state = dff_state.reset_index()
    st_cases = dff_state['cases']
    dff_state['daily'] = [0] + [i - j for i, j in zip(st_cases[:-1], st_cases[1:])]
    dff_state['daily'] = dff_state['daily'].apply(lambda x: x * -1)

    # Plotly Express
    fig = px.bar(
        data_frame=dff,
        x='date',
        y='daily',
        template='plotly_dark')

    return container, fig

# def update_cnty_graph(cnty_slctd):
#     print(cnty_slctd)
#     print(type(cnty_slctd))
#
#     container = "Selected county is: {}".format(cnty_slctd)
#
#     dff_cnty = dff[(dff['county'] == cnty_slctd) & (dff['county'] == cnty_slctd)]
#     st_cases = dff['cases']
#     dff['daily'] = [0] + [i - j for i, j in zip(st_cases[:-1], st_cases[1:])]
#     dff['daily'] = dff['daily'].apply(lambda x: x * -1)
#
#     # Plotly Express
#     fig = px.bar(
#         data_frame=dff,
#         x='date',
#         y='daily',
#         template='plotly_dark')
#
#     return container, fig

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)



# def update_graph(st_slct, cnty_slct):
#     print(st_slct)
#     print(type(st_slct))
#     print(cnty_slct)
#     print(type(cnty_slct))
#
#     container = f"Covid cases in {cnty_slct}, {st_slct}."
#
#     dff = df.copy()
#     dff = dff[dff['state'] == st_slct]
#     dff = dff[dff['county'] == cnty_slct]
#
#     cases = dff['cases']
#     dff['daily'] = [0] + [i - j for i, j in zip(cases[:-1], cases[1:])]
#     dff['daily'] = dff['daily'].apply(lambda x: x * -1)
#
#     # Plotly Express
#     fig = px.bar(
#         data_frame=dff,
#         x='date',
#         y='daily',
#         template='plotly_dark')
#
#     return container, fig