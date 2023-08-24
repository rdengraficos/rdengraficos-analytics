import dash_bootstrap_components as dbc
from dash import html
import dash

def card_layout():
    return dbc.Row(
        [
            dbc.Col(
                html.A(
                    [
                        dbc.Card(
                            [
                                dbc.CardImg(src="/static/images/lidom.jpg", top=True),
                                dbc.CardBody(
                                    [
                                        html.H6(
                                            "Estadística LIDOM", className="card-title"
                                        ),
                                        html.P(
                                            "Información general de las estaditicas de la liga dominicana de baseball ⚾.",
                                            className="card-text",
                                        ),
                                        dbc.Badge(
                                            "Deportes",
                                            pill=True,
                                            color="success",
                                            className="me-1",
                                        ),
                                    ]
                                ),
                            ],
                            style={"width": "14rem"},
                        )
                    ],
                    href=dash.page_registry["pages.lidom_analytics"]["path"],
                    style={"textDecoration": "none"},
                ),
            ),
            dbc.Col(
                html.A(
                    [
                        dbc.Card(
                            [
                                dbc.CardImg(src="/static/images/lidom.jpg", top=True),
                                dbc.CardBody(
                                    [
                                        html.H6(
                                            "Estadística LIDOM", className="card-title"
                                        ),
                                        html.P(
                                            "Información general de las estaditicas de la liga dominicana de baseball ⚾.",
                                            className="card-text",
                                        ),
                                        dbc.Badge(
                                            "Deportes",
                                            pill=True,
                                            color="success",
                                            className="me-1",
                                        ),
                                    ]
                                ),
                            ],
                            style={"width": "14rem"},
                        )
                    ],
                    href="https://plotly.com",
                    style={"textDecoration": "none"},
                ),
            ),
            dbc.Col(
                html.A(
                    [
                        dbc.Card(
                            [
                                dbc.CardImg(src="/static/images/lidom.jpg", top=True),
                                dbc.CardBody(
                                    [
                                        html.H6(
                                            "Estadística LIDOM", className="card-title"
                                        ),
                                        html.P(
                                            "Información general de las estaditicas de la liga dominicana de baseball ⚾.",
                                            className="card-text",
                                        ),
                                        dbc.Badge(
                                            "Deportes",
                                            pill=True,
                                            color="success",
                                            className="me-1",
                                        ),
                                    ]
                                ),
                            ],
                            style={"width": "14rem"},
                        )
                    ],
                    href="https://plotly.com",
                    style={"textDecoration": "none"},
                ),
            ),
        ]
    )
