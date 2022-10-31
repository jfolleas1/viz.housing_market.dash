import dash
from dash import html, dcc

from components.navbar import navbar
from utils import images as img

dash.register_page(__name__, path='/map')

layout = html.Div(children=[
    navbar,
    html.Img(src=img.get_asset_img(img_file_name='only_lyon_logo.png')),
    html.H1(children='This is our Map page'),
    html.Div(children='''
        Dash: A web application framework for your data.
    ''')
])