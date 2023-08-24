import dash_bootstrap_components as dbc
import dash
from dash import html, dcc
from controller.lidom_controller import *

dash.register_page(__name__,
                   path='/lidom_analytics',
                   title='Analiticas Lidom',
                   name='Analiticas Lidom'
)

layout = html.Div([
      dcc.Dropdown(['2020','2021', '2022'], '2022', id='temporada'),
      html.Div(id='ganados_grafico')
])