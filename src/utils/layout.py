import dash_bootstrap_components as dbc
from dash import html


def get_side_bar_layout(side_bar_content, main_panel_content):
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                side_bar_content
                            )
                        ),
                        width={"size": 3}),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                main_panel_content
                            )
                        ),
                    )
                ],
            ),
        ],
    )

