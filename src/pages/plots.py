from re import I
import dash
from dash import html, dcc, callback, Input, Output, State




from components.navbar import navbar
from components.filtering_panel import filtering_panel, get_filter_list
from utils import images as img
from utils.layout import get_side_bar_layout
from utils.data import Dataset
from utils import plot as plt

dash.register_page(__name__, path='/plots')

layout = html.Div(children=[
    navbar,
    html.Div(children=[

        html.Img(src=img.get_asset_img(img_file_name='only_lyon_logo.png')),
        html.H1(children='Data plots'),
        html.P("This page allow the visualisation of the data using 1, 2 and 3 dimensionnal plots."),
        get_side_bar_layout(
            filtering_panel,
            html.Div(children=[
                html.H2('Plots : '),
                html.Div([
                    dcc.Tabs([
                        dcc.Tab(label='1-D plot', children=[
                            dcc.Loading(id="loading-sign-plot-1d", children=[
                                dcc.Graph(id="1d-plot-graph", figure=plt.build_1d_plot(Dataset().get(), x="prix")),
                                html.Div(children=[
                                    html.Div(children=[
                                        html.H4("X axis : "),
                                        dcc.Dropdown(options=Dataset().get().columns,
                                                    value='prix', id='1d-plot-x-dropdown'),
                                    ], style={'width': '30%', 'display': 'inline-block'})
                                ]),
                            ], type="circle")
                        ]),
                        dcc.Tab(label='2-D plot', children=[
                            dcc.Loading(id="loading-sign-plot-2d", children=[
                                dcc.Graph(id="2d-plot-graph", figure=plt.build_2d_plot(Dataset().get(),
                                x="surface_logement", y="prix")),
                                html.Div(children=[
                                    html.Div(children=[
                                        html.H4("X axis : "),
                                        dcc.Dropdown(options=Dataset().get().columns,
                                                    value='surface_logement', id='2d-plot-x-dropdown'),
                                    ], style={'width': '33%', 'display': 'inline-block'}),
                                    html.Div(children=[
                                        html.H4("Y axis : "),
                                        dcc.Dropdown(options=Dataset().get().columns,
                                                    value='prix', id='2d-plot-y-dropdown'),
                                    ], style={'width': '33%', 'display': 'inline-block'}),
                                    html.Div(children=[
                                        html.H4("Color : "),
                                        dcc.Dropdown(options=Dataset().get().columns,
                                                    value=None, id='2d-plot-c-dropdown'),
                                    ], style={'width': '33%', 'display': 'inline-block'})
                                ]),
                            ], type="circle")
                        ]),
                        dcc.Tab(label='3-D plot', children=[
                            dcc.Loading(id="loading-sign-plot-3d", children=[
                                dcc.Graph(id="3d-plot-graph", figure=plt.build_3d_plot(Dataset().get(),
                                x="surface_logement", y="prix", z="nombre_pieces")),
                                html.Div(children=[
                                    html.Div(children=[
                                        html.H4("X axis : "),
                                        dcc.Dropdown(options=Dataset().get().columns,
                                                    value='surface_logement', id='3d-plot-x-dropdown'),
                                    ], style={'width': '25%', 'display': 'inline-block'}),
                                    html.Div(children=[
                                        html.H4("Y axis : "),
                                        dcc.Dropdown(options=Dataset().get().columns,
                                                    value='prix', id='3d-plot-y-dropdown'),
                                    ], style={'width': '25%', 'display': 'inline-block'}),
                                    html.Div(children=[
                                        html.H4("Z axis : "),
                                        dcc.Dropdown(options=Dataset().get().columns,
                                                    value='nombre_pieces', id='3d-plot-z-dropdown'),
                                    ], style={'width': '25%', 'display': 'inline-block'}),
                                    html.Div(children=[
                                        html.H4("Color : "),
                                        dcc.Dropdown(options=Dataset().get().columns,
                                                    value=None, id='3d-plot-c-dropdown'),
                                    ], style={'width': '25%', 'display': 'inline-block'})
                                ]),
                            ], type="circle")
                        ]),
                    ])
                ])      
            ])
        )
    ], style={"padding-left": "3%", "padding-right": "3%"})
])

@callback(
    Output("loading-sign-plot-1d", "children"),
    Output("1d-plot-graph", "figure"),
    Input("apply-filter-button", "n_clicks"),
    Input("1d-plot-x-dropdown", "value"),
    State("data-filtering-pannel", "children"),
    State("loading-sign-plot-1d", "children"),
    prevent_initial_call=True
)
def apply_filter_on_plot(n_clicks, x, filters_panel_content, loading_sign_children):
    filters = get_filter_list(filters_panel_content)
    new_data = Dataset().get_selection(filters).to_dict('records')
    plot_1d = plt.build_1d_plot(data=new_data, x=x)
    return loading_sign_children, plot_1d


@callback(
    Output("loading-sign-plot-2d", "children"),
    Output("2d-plot-graph", "figure"),
    Input("apply-filter-button", "n_clicks"),
    Input("2d-plot-x-dropdown", "value"),
    Input("2d-plot-y-dropdown", "value"),
    Input("2d-plot-c-dropdown", "value"),
    State("data-filtering-pannel", "children"),
    State("loading-sign-plot-2d", "children"),
    prevent_initial_call=True
)
def apply_filter_on_plot(n_clicks, x, y, c, filters_panel_content, loading_sign_children):
    filters = get_filter_list(filters_panel_content)
    new_data = Dataset().get_selection(filters).to_dict('records')
    plot_2d = plt.build_2d_plot(data=new_data, x=x, y=y, c=c)
    return loading_sign_children, plot_2d

@callback(
    Output("loading-sign-plot-3d", "children"),
    Output("3d-plot-graph", "figure"),
    Input("apply-filter-button", "n_clicks"),
    Input("3d-plot-x-dropdown", "value"),
    Input("3d-plot-y-dropdown", "value"),
    Input("3d-plot-z-dropdown", "value"),
    Input("3d-plot-c-dropdown", "value"),
    State("data-filtering-pannel", "children"),
    State("loading-sign-plot-3d", "children"),
    prevent_initial_call=True
)
def apply_filter_on_plot(n_clicks, x, y, z, c, filters_panel_content, loading_sign_children):
    filters = get_filter_list(filters_panel_content)
    new_data = Dataset().get_selection(filters).to_dict('records')
    plot_3d = plt.build_3d_plot(data=new_data, x=x, y=y, z=z, c=c)
    return loading_sign_children, plot_3d
