import dash
from dash import html, dcc, callback, Input, Output, State


from components.navbar import navbar
from components.filtering_panel import filtering_panel, get_filter_list
from utils import images as img
from utils.layout import get_side_bar_layout
from utils.data import Dataset

dash.register_page(__name__, path='/plots')

layout = html.Div(children=[
    navbar,
    html.Img(src=img.get_asset_img(img_file_name='only_lyon_logo.png')),
    html.H1(children='This is our Plots page'),

    get_side_bar_layout(
        filtering_panel,
        html.Div(children=[
            html.H2('Data table : '),
            dcc.Loading(
                id="loading-sign-plot",
                children=[
                    html.Div(children='''Our plots will appear here''')
                    ],
                type="circle",
                )
        ])
    )
    
])