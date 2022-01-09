import dash
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

path = "C:/Users/irfan/OneDrive/Desktop/MO TECH/covid-variants.csv"
dat = pd.read_csv(path)

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Covid Variants Dashboard',
            style={
                'textAlign' : 'center',
                'color' : '#15005B'
            }),
    html.H3(children='This dashboard shows the latest data of different variants of the corona virus and its effect worldwide', style={ 'textAlign': 'center' }),
    html.H4(children='Select the country whose data you need from the dropdown below'),

    dcc.Dropdown(id='geo-drop', options=[{'label':i, 'value': i}
                                         for i in dat['location'].unique()],
                 placeholder="Select a Country",),
    dcc.Graph(id='Graph')
], className="banner")

#app.css.append_css({
#    "external_url":'http://""'
#})

@app.callback(
    Output(component_id='Graph', component_property='figure'),
    Input(component_id='geo-drop', component_property='value')
)
def update_graph(selected_geography):
    filtered_dat = dat[dat['location'] == selected_geography]
    fig= px.scatter(filtered_dat, y='perc_sequences', x='num_sequences',size = 'num_sequences_total', color='variant' ,labels={
                     "variant": "VARIANTS",
                     "num_sequences": "Number Of Sequences Recorded","perc_sequences": "Percentage of Sequences",
                    }, title=f'Covid Variants and effect in {selected_geography}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
