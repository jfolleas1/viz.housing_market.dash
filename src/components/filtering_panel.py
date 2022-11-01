from utils.data import Dataset
from dash import html, dcc

filtering_panel = html.Div([
    html.H2("Dataset filtering:"),
    html.Label('Buy type:'),
    dcc.Checklist(id='input-buy-type',
                  options=Dataset().get_unique_values('type_achat'),
                  value=Dataset().get_unique_values('type_achat'))
])