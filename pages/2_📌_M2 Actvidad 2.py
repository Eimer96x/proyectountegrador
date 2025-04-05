import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

df= pd.read_csv("static/datasets/estudiantes_colombia.csv")

# ... existing code

st.subheader("Primeras 5 filas del dataset")
st.write(df.head())

st.subheader("Últimas 5 filas del dataset")
st.write(df.tail())

st.subheader("Resumen del dataset")
st.write("Información del dataset:")
st.write(df.info())
st.write("Descripción estadística del dataset:")
st.write(df.describe())

st.subheader("Selección de columnas específicas")
columnas = st.multiselect("Selecciona las columnas que quieres ver:", df.columns)
if columnas:
    st.write(df[columnas])

st.subheader("Filtrar estudiantes por promedio")
promedio_min = st.slider("Selecciona el promedio mínimo:", min_value=0.0, max_value=5.0, value=3.0, step=0.1)
estudiantes_filtrados = df[df['promedio'] > promedio_min]
st.write(f"Estudiantes con promedio mayor a {promedio_min}:")
st.write(estudiantes_filtrados)