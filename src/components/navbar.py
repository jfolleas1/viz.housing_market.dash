# from dash import html
# import dash_bootstrap_components as dbc

# navbar = dbc.Navbar(dbc.Container(
#     [html.H1(children='Navbar')]
# ),color='dark', dark=True)


# package imports
from dash import html, callback, Output, Input, State
import dash_bootstrap_components as dbc

# local imports
from utils import images as img

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"


# component
navbar = dbc.NavbarSimple(
    children=[
        
        dbc.NavItem(dbc.NavLink("Data table", href="/data-table")),
        dbc.NavItem(dbc.NavLink("Map", href="#")),
        dbc.NavItem(dbc.NavLink("Plots", href="#")),
        dbc.NavItem(dbc.NavLink("Linear model", href="#")),
        html.A(html.Img(src=img.get_asset_img(img_file_name='plotly_logo_small.png'), height='30px'),
               href='https://plotly.com')
    ],
    brand="Lyon housing market dashboard",
    brand_href="/",
    color="red",
    dark=True,
)
    #             html.H1(children='Navbar', color='white'),
    #             html.A(
    #                 dbc.Row(
    #                     [
    #                         dbc.Col(html.Img(src=img.get_asset_img(img_file_name='plotly_logo_small.png'), height='30px')),
    #                     ],
    #                     align='center',
    #                     className='g-0',
    #                 ),
    #                 href='https://plotly.com',
    #                 style={'textDecoration': 'none'},
    #             ),
    #             dbc.NavbarToggler(id='navbar-toggler', n_clicks=0),
    #             dbc.Collapse(
    #                 dbc.Nav(
    #                     [
    #                         dbc.NavItem(
    #                             dbc.NavLink(
    #                                 'Home',
    #                                 href='/'
    #                             )
    #                         )
    #                     ]
    #                 ),
    #                 id='navbar-collapse',
    #                 navbar=True
    #             ),
    #         ]),
    #     ]
    # ),
    # color='dark',
    # dark=True,
# )

