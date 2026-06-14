import streamlit as st
import os
import json

st.title("Formulario de Entrada")

# Entrada de datos del usuario
usuario_input = st.text_input("Introduce el dato para tu script principal:")

# Botón para terminar y enviar los datos
if st.button("Finalizar y Guardar Datos"):
    if usuario_input:
        # 1. Creamos el diccionario con los datos
        datos_diccionario = {
            "texto_usuario": usuario_input,
            "estado": "completado"
        }
        
        # 2. Guardamos el diccionario en un archivo temporal
        with open("temp_data.json", "w") as f:
            json.dump(datos_diccionario, f)
            
        st.success("¡Datos enviados! Ya puedes cerrar esta pestaña.")
        
        # 3. Forzamos la parada del servidor Streamlit inmediatamente
        os._exit(0) 
    else:
        st.warning("Por favor, introduce algún dato antes de finalizar.")