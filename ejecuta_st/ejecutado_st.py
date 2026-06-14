import streamlit as st
import streamlit.components.v1 as components
import os
import json

st.set_page_config(layout="wide") # Para darle más espacio al árbol
st.title("Configuración de Índice")

# 1. Declarar el componente apuntando a la carpeta donde está el HTML
arbol_component = components.declare_component(
    "arbol_dinamico",
    path="./componente_arbol"
)

# 2. Renderizar el componente y esperar datos
# Esto mostrará tu HTML. Cuando JS envíe los datos, 'datos_desde_js' dejará de ser None
datos_desde_js = arbol_component(key="mi_arbol")

if datos_desde_js is not None:
    # 3. Guardamos el diccionario en el archivo temporal esperado por ejecuta_st.py
    with open("temp_data.json", "w", encoding="utf-8") as f:
        json.dump(datos_desde_js, f, ensure_ascii=False, indent=4)
        
    st.success("¡Datos guardados con éxito! Cerrando la ventana...")
    
    # 4. Forzamos la parada del servidor Streamlit para que ejecuta_st.py continúe
    os._exit(0)