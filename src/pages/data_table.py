import dash
from dash import html, dcc, callback, Input, Output, State

from components.navbar import navbar
from components.filtering_panel import filtering_panel, get_filter_list
from utils import images as img
from utils.layout import get_side_bar_layout
from utils.data import Dataset

dash.register_page(__name__, path='/data-table')

layout = html.Div(children=[
    navbar,
    html.Img(src=img.get_asset_img(img_file_name='only_lyon_logo.png')),
    html.H1(children='This is our Data table page'),
    get_side_bar_layout(
        filtering_panel,
        html.Div(children=[
            html.H2('Data table : '),
            dcc.Loading(
                id="loading-sign",
                children=[
                    dash.dash_table.DataTable(
                    data=Dataset().get_selection([]).to_dict('records'),
                    id='data-table',
                    page_size=10,
                    columns=[{"name": i, "id": i} for i in Dataset().get_selection([]).columns],
                    style_table={'overflowY': 'scroll'},
                    style_as_list_view=True,
                    style_cell={'padding': '20px'},
                    style_header={
                        'fontWeight': 'bold'
                    }
                    )],
                type="circle",
                ),
            html.Button("Download CSV", id="btn_csv"),
            dcc.Download(id="download-dataframe-csv"),
        ])
    )
])

@callback(
    Output("loading-sign", "children"),
    Output("data-table", "data"),
    Input("apply-filter-button", "n_clicks"),
    State("data-filtering-pannel", "children"),
    State("loading-sign", "children"),
    prevent_initial_call=True
)
def apply_filter_on_data(n_clicks, filters_panel_content, loading_sign_children):
    filters = get_filter_list(filters_panel_content)
    new_data = Dataset().get_selection(filters).to_dict('records')
    return loading_sign_children, new_data

@callback(
    Output("download-dataframe-csv", "data"),
    Input("btn_csv", "n_clicks"),
    State("data-filtering-pannel", "children"),
    prevent_initial_call=True,
)
def func(n_clicks, filters_panel_content):
    filters = get_filter_list(filters_panel_content)
    selected_data = Dataset().get_selection(filters)
    return dcc.send_data_frame(selected_data.to_csv, "lyon_housing_market.csv")