import dash_bootstrap_components as dbc
from dash import html

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

navbar = dbc.NavbarSimple(
    children=[
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Navbar", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plotly.com",
                style={"textDecoration": "none"},
            ),
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="primary",
    dark=True,
)