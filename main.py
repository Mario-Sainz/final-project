import streamlit as st
from PIL import Image 
import pandas as pd
import gráficas as gr
import plotly.express as px
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
from streamlit_folium import folium_static


#Poner título
#st.title("El mundo inmobiliario en Londres")
st.markdown("<h1 style='text-align: center; color: black;'>¿Quieres conocer el mundo inmobiliario de Londres?</h1>", unsafe_allow_html=True)

#Poner imagen
image = Image.open('data/londres.jpg')
st.image(image,use_column_width=True)

#Breve resumen de la funcionalidad de la API
st.write(
"""
¿Quieres venir a vivir a Londres? ¿No sabes que zona escoger para vivir? ¿Quieres invertir en la inmobiliaria de Londres?

Bien, estas en el lugar adecuado! Aqui, podrás tener la información que necesitas de las distintas zonas de Londres.

"""
)
#Resumen del apartado general de Londres
st.header("1- Información general")
st.write(
"""
A continuación, se puede apreciar un estudio general del mundo inmobiliario en Inglaterra.

1.1 Evolución de los precios medios de las viviendas de todas las regiones de Inglaterra.

 - Cuales son las regiones con mayores y menores precios
 - Comparativa del resto de regiones con Londres
 - Visualizar la tendencia de los precios 

"""
)

#Gráfica de la evolución de los precios
gr.gráfica_regiones()


st.write(
"""
1.2 Evolución del número de casas vendidas en cada región de Inglaterra, mensualmente desde 1995 hasta 2020. 
 
 - Tendencias de las ventas de casas
 - Crisis del 2008 
"""
)

#Gráfica de las ventas de inmuebles por zonas
data = pd.read_csv("data/regiones-london.csv")
zona = st.selectbox("Elige una región", list(data.area.unique()))
gr.casas_vendidas(zona)

map_1 = folium.Map(location = [51.51753,-0.11214], zoom_start = 6)
folium_static(map_1)



#Apartado mas concreto por zona elegida.
st.header("2- Información específica de los municipios de Londres")

st.write(
"""
Elige una zona y obtendrás información de ella:
"""
)


#Selector por zonas
data1 = pd.read_csv("data/houses-yearly-london.csv")
data2 = pd.read_csv("data/houses-monthly-london.csv")
data3 = pd.read_csv("data/c.postal-london.csv")
london = data1[data1['borough_flag'] == 1]
london = data2[data2['borough_flag'] == 1]
zona = st.selectbox("Elige un municipio", list(london.area.unique()))
st.write(
"""
Código Postal:
"""
)
data3 = pd.read_csv("data/c.postal-london.csv")
data2=data3[data3.area == zona]["code"].unique()[0]
data2
tipo_gráfica = st.selectbox("Elige que gráfica quieres ver", ["Precio medio viviendas", "Salario medio", "Porcentage de hogares que reciclan", "Número de trabajos/Número de habitantes", "Número de crímenes"])


if  tipo_gráfica == "Salario medio":
    gr.media_salarios(zona)
if tipo_gráfica == "Número de trabajos/Número de habitantes":
    gr.numero_trabajos(zona)
if tipo_gráfica == "Porcentage de hogares que reciclan":
    gr.hogares_reciclan(zona)
if tipo_gráfica == "Precio medio viviendas":
    gr.precios_medios(zona)
if tipo_gráfica == "Número de crímenes":
    gr.crimenes_zona(zona)



