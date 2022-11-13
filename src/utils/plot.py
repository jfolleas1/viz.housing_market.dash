import plotly.express as px

def build_1d_plot(data, x="prix"):
    fig = px.histogram(data, x=x)
    return fig