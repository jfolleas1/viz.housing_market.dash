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
                            """dcc.Graph(id="2d-plot-graph")"""
                        ], type="circle")
                    ]),
                    dcc.Tab(label='3-D plot', children=[
                        dcc.Loading(id="loading-sign-plot-3d", children=[
                            """dcc.Graph(id="3d-plot-graph")"""
                        ], type="circle")
                    ]),
                ])
            ])      
        ])
    )
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
