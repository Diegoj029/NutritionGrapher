import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from data import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash()

df = GraphDataFrame()

categories = df.getCategories()
option_list = getCategoryOptions(categories)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(id = 'H1', children = 'Representación de cantidad de calorías por categoría alimenticia', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),
    # All elements from the top of the page
    html.Div([
        html.Div([
            html.H2(children='Cantidad de calorias por categoría alimenticia'),

            html.Div(children='''
                Seleccione categoría
            '''),
            dcc.Dropdown( id = 'dropdown1',
            options = option_list,
            value = option_list[0]['value']),
            dcc.Graph(
                id='bar_plot1',
            ),  
        ], className='six columns'),
        html.Div([
            html.H2(children='Cantidad de calorias por categoría alimenticia'),

            html.Div(children='''
                Seleccione su propósito
            '''),
            dcc.Dropdown( id = 'dropdown2',
            options = [
                    {'label':'Enflacar', 'value':'enflacar' },
                    {'label': 'Ganar Músculo', 'value':'ganar_musculo'},
                    ],
            value = 'enflacar'),
            dcc.Graph(
                id='bar_plot2',
            ),  
        ], className='six columns'),
    ], className='row'),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.Div([
            html.H2(children='Cantidad de calorias por categoría alimenticia'),

            html.Div(children='''
                Seleccione la propiedad alimenticia de su interés
            '''),
            dcc.Dropdown( id = 'dropdown3',
            options = [
                    {'label':'Sodio', 'value':'sodium' },
                    {'label': 'Calcio', 'value':'calcium'},
                    {'label': 'Vitamitas', 'value':'vitamin'},
                    ],
            value = 'sodium'),
            dcc.Graph(
                id='bar_plot3',
            ),  
        ], className='six columns'),
        html.Div([
            html.H2(children='Cantidad de calorias por categoría alimenticia'),

            html.Div(children='''
                Seleccione los ejes x y y
            '''),
            dcc.Dropdown( id = 'dropdown4',
            options = [
                    {'label':'100g', 'value':'serving_size' },
                    ],
            value = 'serving_size'),
            dcc.Dropdown( id = 'dropdown5',
            options = [
                    {'label':'Calorias', 'value':'calories' },
                    {'label': 'Sodio', 'value':'sodium'},
                    {'label': 'Calcio', 'value':'calcium'},
                    ],
            value = 'calories'),
            dcc.Graph(
                id='bar_plot4',
            ),  
        ], className='six columns'),
    ], className='row'),
])

@app.callback(Output(component_id='bar_plot1', component_property= 'figure'),
              [Input(component_id='dropdown1', component_property= 'value')])
def graph1_update(dropdown1_value):
    print(dropdown1_value)
    data = df.getDataCategory(dropdown1_value)
    print(data)
    fig1 = px.scatter(data, x="name", y="calories", color="category", symbol="category")
    
    fig1.update_layout(title = '',
                      xaxis_title = 'Nombre',
                      yaxis_title = 'Cantidad de calorías por categoría alimenticia'
                      )
    return fig1

@app.callback(Output(component_id='bar_plot2', component_property= 'figure'),
              [Input(component_id='dropdown2', component_property= 'value')])
def graph2_update(dropdown2_value):
    print(dropdown2_value)
    data = df.getDataPurpose(dropdown2_value)
    print(data)
    fig2 = px.scatter(data, x="category", y="calories", color="name", symbol="name")
    
    fig2.update_layout(title = '',
                      xaxis_title = 'Categorías',
                      yaxis_title = 'Cantidad de calorías por categoría alimenticia'
                      )
    return fig2

@app.callback(Output(component_id='bar_plot3', component_property= 'figure'),
              [Input(component_id='dropdown3', component_property= 'value')])
def graph3_update(dropdown3_value):
    print(dropdown3_value)
    data = df.getDataProperty(dropdown3_value)
    print(data)
    fig3 = px.scatter(data, x="category", y=dropdown3_value, color="category", symbol="category", marginal_x="histogram")
    
    fig3.update_layout(title = '',
                      xaxis_title = 'Categorías',
                      yaxis_title = 'Cantidad de calorías por categoría alimenticia'
                      )
    return fig3  

@app.callback(Output(component_id='bar_plot4', component_property= 'figure'),
              [Input(component_id='dropdown4', component_property= 'value'),
               Input(component_id='dropdown5', component_property= 'value')])
def graph4_update(dropdown4_value, dropdown5_value):
    print(dropdown5_value)
    data = df.getDataCharacteristics(dropdown5_value)
    print(data)
    fig4 = px.scatter(data, x="category", y=dropdown5_value, color="category", symbol="category")
    
    fig4.update_layout(title = '',
                      xaxis_title = 'Categorías',
                      yaxis_title = 'Cantidad de calorías por categoría alimenticia'
                      )
    return fig4  


if __name__ == '__main__':
    app.run_server(debug=False)