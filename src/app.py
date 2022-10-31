# Run this app with `python src/app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

import dash_bootstrap_components as dbc

from flask import Flask


server = Flask(__name__)
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)
app.title = "Lyon housing market"

server = app.server         # the server is needed to deploy the application

if __name__ == "__main__":
    app.run_server(
        debug=True,
    )