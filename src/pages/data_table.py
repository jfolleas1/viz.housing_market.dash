import dash
from dash import html, dcc

from components.navbar import navbar
from components.filtering_panel import filtering_panel
from utils import images as img
from utils.layout import get_side_bar_layout

dash.register_page(__name__, path='/data-table')

layout = html.Div(children=[
    navbar,
    html.Img(src=img.get_asset_img(img_file_name='only_lyon_logo.png')),
    html.H1(children='This is our Data table page'),
    get_side_bar_layout(
        filtering_panel,
        html.Div("My main pannel")
    )
])