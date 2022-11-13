import plotly.express as px

def build_1d_plot(data, x="prix"):
    fig = px.histogram(data, x=x)
    return fig


def build_2d_plot(data, x="surface_logement", y="prix", c=None):
    fig = px.scatter(data, x=x, y=y, color=c, opacity=0.5)
    return fig

def build_3d_plot(data, x="surface_logement", y="prix", z="nombre_pieces", c=None):
    fig = px.scatter_3d(data, x=x, y=y, z=z, color=c, opacity=0.5)
    return fig