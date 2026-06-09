import streamlit as st
import streamlit.components.v1 as components

# Configuración básica de la app
st.set_page_config(page_title="Gestor de Índice Profesional", layout="centered")

st.title("Gestor de Índice Jerárquico Dinámico")
st.caption("Organiza los elementos arrastrándolos verticalmente (orden) o lateralmente (jerarquía).")

# 1. Base de datos simulada en st.session_state (Estado de la Sesión)
if "datos_actuales" not in st.session_state:
    st.session_state.datos_actuales = [
        {"texto": "Introducción", "indentacion": 0},
        {"texto": "Antecedentes", "indentacion": 1},
        {"texto": "Marco Teórico", "indentacion": 0},
        {"texto": "Conclusiones", "indentacion": 0}
    ]

st.markdown("---")

# 2. CARGA DEL ARCHIVO HTML EXTERNO
# Leemos el archivo index.html que está guardado en el mismo directorio
with open("index.html", "r", encoding="utf-8") as file:
    codigo_html = file.read()

# 3. INTERFAZ INTERACTIVA (IFRAME)
# Pasamos la lista original a través de los argumentos nativos de Streamlit ('datos')
datos_recibidos = components.html(
    codigo_html,
    height=520,
    scrolling=True,
    # Esta variable se envía directamente al evento "message" del JavaScript
    datos=st.session_state.datos_actuales 
)

st.markdown("---")

# 4. BOTÓN DE ENVÍO ESTÁTICO (PROCESAMIENTO)
if st.button("💾 Guardar Cambios en el Sistema", type="primary", use_container_width=True):
    if datos_recibidos is not None:
        # Sincronizamos los movimientos del frontend con el backend en Python
        st.session_state.datos_actuales = datos_recibidos
        st.success("¡Estructura de datos procesada e indexada correctamente en Python!")
        
        # Mostramos los datos guardados finales como prueba
        st.json(st.session_state.datos_actuales)
    else:
        # Si el usuario no ha tocado nada todavía, guardamos el estado inicial por defecto
        st.info("Estructura guardada sin modificaciones adicionales.")
        st.json(st.session_state.datos_actuales)