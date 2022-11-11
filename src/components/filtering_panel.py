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
    dcc.RangeSlider(id='input-num-rooms-range',
                    min=0,
                    max=Dataset().get_aggregate('nombre_pieces', max),
                    value=[0, Dataset().get_aggregate('nombre_pieces', max)],
                    step=1),
    html.Label('Dwelling size:'),
    dcc.RangeSlider(id='input-dwelling-size-range',
                    min=0,
                    max=Dataset().get_aggregate('surface_logement', max),
                    value=[0, Dataset().get_aggregate('surface_logement', max)]),
    html.Label('Garden size:'),
    dcc.RangeSlider(id='input-garden-size-range',
                    min=0,
                    max=Dataset().get_aggregate('surface_terrain', max),
                    value=[0, Dataset().get_aggregate('surface_terrain', max)]),
    html.Label('Number of car sapce:'),
    dcc.RangeSlider(id='input-car-space-range',
                    min=0,
                    max=Dataset().get_aggregate('nombre_parkings', max),
                    value=[0, Dataset().get_aggregate('nombre_parkings', max)],
                    step=1),
    html.Label('Building age:'),
    dcc.RangeSlider(id='input-building-age-range',
                    min=0,
                    max=int(Dataset().get_aggregate('anciennete', max))+1,
                    value=[0, int(Dataset().get_aggregate('anciennete', max))+1],
                    step=5),
    html.Div([
        html.Div(
            [
                html.Label('Min Price:'),
                dcc.Input(id='input-price-min',
                      type='number',
                      min=0,
                      value=0)
            ]
            ,style={'width': '49%', 'display': 'inline-block'}
        ),
        html.Div(
            [
                html.Label('Max Price:'),
                dcc.Input(id='input-price-max',
                      type='number',
                      min=0,
                      value=Dataset().get_aggregate('prix', max))
            ]
            ,style={'width': '49%', 'display': 'inline-block'}
        )
    ])
])