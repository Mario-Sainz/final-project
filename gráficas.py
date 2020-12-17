import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

#fuente de las gráficas = https://towardsdatascience.com/cheat-codes-to-better-visualisations-with-plotly-express-21caece3db01
def gráfica_precios():
    data = pd.read_csv("data/houses-monthly-london.csv")
    fig = px.line(data, x="date", y="average_price", color='area')
    st.plotly_chart(fig)
#https://www.codegrepper.com/code-examples/python/plotly+express+in+streamlit

def gráfica_seguridad():
    data = pd.read_csv("data/houses-monthly-london.csv")
    fig = px.line(data, x="date", y="no_of_crimes", color='area')
    st.plotly_chart(fig)


def gráfica_venta_casas():
    data = pd.read_csv("data/houses-monthly-london.csv")
    fig =  px.line(data, x="date", y="houses_sold", color='area')
    st.plotly_chart(fig)

def gráfica_regiones():
    data = pd.read_csv("data/houses-monthly-london.csv")
    prices_london =data [data['borough_flag'] == 1]
    prices_south_east = data[data['area'] == 'south east']
    prices_south_west = data[data['area'] == 'south west']
    prices_north_west = data[data['area'] == 'north west']
    prices_yorks_and_the_humber = data[data['area'] == 'yorks and the humber']
    prices_east_of_england = data[data['area'] == 'east of england']
    prices_west_midlands = data[data['area'] == 'west midlands']
    prices_east_midlands = data[data['area'] == 'east midlands']
    prices_north_east = data[data['area'] == 'north east']

    london_mean_price = prices_london.groupby('date')['average_price'].mean()
    south_east_mean_price = prices_south_east.groupby('date')['average_price'].mean()
    south_west_mean_price = prices_south_west.groupby('date')['average_price'].mean()
    north_west_mean_price = prices_north_west.groupby('date')['average_price'].mean()
    yorks_and_the_humber_mean_price = prices_yorks_and_the_humber.groupby('date')['average_price'].mean()
    east_of_england_mean_price = prices_east_of_england.groupby('date')['average_price'].mean()
    west_midlands_mean_price = prices_west_midlands.groupby('date')['average_price'].mean()
    east_midlands_mean_price = prices_east_midlands.groupby('date')['average_price'].mean()
    north_east_mean_price = prices_north_east.groupby('date')['average_price'].mean()

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=london_mean_price.index, y=london_mean_price.values,mode='lines',name='London',))

    fig.add_trace(go.Scatter(x=south_east_mean_price.index, 
                                y=south_east_mean_price.values,
                                mode='lines',
                                name='South east',
                                ))

    fig.add_trace(go.Scatter(x=south_west_mean_price.index, 
                            y=south_west_mean_price.values,
                            mode='lines',
                            name='South west',
                            ))
    fig.add_trace(go.Scatter(x=north_west_mean_price.index, 
                            y=north_west_mean_price.values,
                            mode='lines',
                            name='North west',
                            ))
    fig.add_trace(go.Scatter(x=yorks_and_the_humber_mean_price.index, 
                            y=yorks_and_the_humber_mean_price.values,
                            mode='lines',
                            name='Yorks and the humber',
                            ))
    fig.add_trace(go.Scatter(x=east_of_england_mean_price.index, 
                            y=east_of_england_mean_price.values,
                            mode='lines',
                            name='East of england',
                            ))
    fig.add_trace(go.Scatter(x=west_midlands_mean_price.index, 
                            y=west_midlands_mean_price.values,
                            mode='lines',
                            name='West midlands',
                            ))
    fig.add_trace(go.Scatter(x=east_midlands_mean_price.index, 
                            y=east_midlands_mean_price.values,
                            mode='lines',
                            name='East midlands',
                            ))
    fig.add_trace(go.Scatter(x=north_east_mean_price.index, 
                            y=north_east_mean_price.values,
                            mode='lines',
                            name='North east',
                            ))



    fig.update_layout(
        template='gridon',
        title='Precio medio de las viviendas por regiones',
        xaxis_title='Año',
        yaxis_title='Precio',
        xaxis_showgrid=False,
        yaxis_showgrid=False,
        legend=dict(y=-.2, orientation='h'),
        shapes=[
            dict(
                type="line",
                x0='2016-06-23',
                x1='2016-06-23',
                y0=0,
                y1=london_mean_price.values.max()*1.2,
                line=dict(
                color="LightSalmon",
                dash="dashdot"
                )
            )
        ],
        annotations=[
                dict(text="Votación del Brexit", x='2016-06-23', y=london_mean_price.values.max()*1.2),
        ]
    )

    st.plotly_chart(fig)


def casas_vendidas(zona:str):
    data = pd.read_csv("data/regiones-london.csv")
    north = data[data['area'] == zona]
    fig =  px.line(north, x="date", y="houses_sold", color='area')
    st.plotly_chart(fig)



def media_salarios(municipio:str):
    data1 = pd.read_csv("data/houses-yearly-london.csv")
    london = data1[data1['borough_flag'] == 1]
    data2=london[london.area==municipio]
    fig = px.line(data2,x="date", y=["mean_salary"], color="area")
    st.plotly_chart(fig)

def numero_trabajos(municipio:str):
    data1 = pd.read_csv("data/houses-yearly-london.csv")
    london = data1[data1['borough_flag'] == 1]
    data2=london[london.area== municipio]
    fig = px.line(data2,x="date", y=["number_of_jobs", "population_size"], color="area")
    st.plotly_chart(fig)

def hogares_reciclan(municipio:str):
    data1 = pd.read_csv("data/houses-yearly-london.csv")
    london = data1[data1['borough_flag'] == 1]
    data2=london[london.area== municipio]
    fig = px.line(data2,x="date", y=["recycling_pct"], color="area")
    st.plotly_chart(fig)

def precios_medios(municipio:str):
    data2 = pd.read_csv("data/houses-monthly-london.csv")
    london = data2[data2['borough_flag'] == 1]
    data3=london[london.area== municipio]
    fig = px.line(data3,x="date", y=["average_price"], color="area")
    st.plotly_chart(fig)

def crimenes_zona(municipio:str):
    data2 = pd.read_csv("data/houses-monthly-london.csv")
    london = data2[data2['borough_flag'] == 1]
    data3=london[london.area== municipio]
    fig = px.line(data3,x="date", y=["no_of_crimes"], color="area")
    st.plotly_chart(fig)

def codigo_postal_zona(municipio:str):
    data3 = pd.read_csv("data/c.postal-london.csv")
    zipcode = data3[data3.area == municipio]["code"].unique()[0]
    return zipcode
