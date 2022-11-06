from utils.data import Dataset
from dash import html, dcc

filtering_panel = html.Div([
    html.H2("Dataset filtering:"),
    html.Label('Buy type:'),
    dcc.Checklist(id='input-buy-type',
                  options=Dataset().get_unique_values('type_achat'),
                  value=Dataset().get_unique_values('type_achat'),
                  labelStyle={'display': 'block'}),
    html.Label('Property type:'),
    dcc.Checklist(id='input-property-type',
                  options=Dataset().get_unique_values('type_bien'),
                  value=Dataset().get_unique_values('type_bien'),
                  labelStyle={'display': 'block'}),
    html.Label('City:'),
    dcc.Dropdown(id='input-commune',
                  options=Dataset().get_unique_values('commune'),
                  value=Dataset().get_unique_values('commune'),
                  multi=True),
    html.Label('Number of rooms:'),
    dcc.RangeSlider(id='input-num-rooms',
                    min=0,
                    max=Dataset().get_aggregate('nombre_pieces', max),
                    value=[0, Dataset().get_aggregate('nombre_pieces', max)],
                    step=1)
])