import os
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from plotly import graph_objs as go
import pandas as pd
from django_plotly_dash import DjangoDash

path = 'C:\DEV\DashPloty\Data\gapminderDataFiveYear.csv'

# df = pd.read_csv(os.path.join(os.path.dirname(__file__)), "..\data\gapminderDataFiveYear.csv")
df = pd.read_csv(path)
# print(df)

opcao_ano = []

for ano in df['year'].unique():
    opcao_ano.append({'label': str(ano), 'value': ano})

app = DjangoDash('test1')

app.layout = html.Div([

    dcc.Graph(id='graph'),
    dcc.Dropdown(id='year-picker', options=opcao_ano, value=df['year'].min())
])

@app.callback(Output('graph', 'figure'),
              [Input('year-picker', 'value')])

def update_figura(ano_selec):

    df_filtro = df[df['year']==ano_selec]

    traces = []

    for conti_nome in df_filtro['continent'].unique():
        df_por_conti = df_filtro[df_filtro['continent']==conti_nome]
        traces.append(go.Scatter(
            x=df_por_conti['gdpPercap'],
            y=df_por_conti['lifeExp'],
            mode='markers',
            opacity=0.7,
            name=conti_nome
        ))
    return {'data': traces,
            'layout': go.Layout(title='Pesquisa',
                                xaxis={'title': 'Renda per Cap', 'type': 'log'},
                                yaxis={'title': 'Expectativa de vida', 'type': 'log'})}


# if __name__ == '__main__':
#     app.run_server()