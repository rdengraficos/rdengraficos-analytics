from dash import Dash, html, dcc
import dash
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from components.navbar import navbar


app = Dash(__name__,use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


app.layout = html.Div(children=[
    navbar, 
    dbc.Container([
         dash.page_container
    ],fluid=False)
])

if __name__ == '__main__':
    app.run(debug=True)