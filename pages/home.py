import dash_bootstrap_components as dbc
import dash
from dash import html
from components.card_menu import card_layout

dash.register_page(__name__, path="/", title="Menu Principal", name="Menu Principal")

def layout():
    return card_layout()

