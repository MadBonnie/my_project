import pandas as pd
import streamlit as st
import plotly_express as px
import time


st.header('Proyecto - César Barrios')

welcome_msg = """
Este es mi primer proyecto en TripleTen.
Soy César Barrios, futuro analista de datos. 
No es mucho, pero es trabajo honesto. 
:)
"""


def stream_data():
    for word in welcome_msg.split(" "):
        yield word + " "
        time.sleep(0.02)

if st.button("Introducción:"):
    st.write_stream(stream_data)

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')    
    fig = px.histogram(car_data, x="odometer") 
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
