import streamlit as st
import streamlit.components.v1 as components
import json
import os

st.set_page_config(page_title="Configurador XindeX", layout="centered")

ARCHIVO_CONFIG = "config_menu.json"

# DEBE COINCIDIR EXACTAMENTE CON LAS CLAVES DEL DICCIONARIO EN over_main.py
FUNCIONES_DISPONIBLES = [
    "Ninguna", "version_web", "set_style", "from_to", 
    "listar_procesos", "subprocess_os", "lanzar_proceso", "cambiar_estilo_marco"
]

if "datos_actuales" not in st.session_state:
    if os.path.exists(ARCHIVO_CONFIG):
        with open(ARCHIVO_CONFIG, "r", encoding='utf-8') as f:
            st.session_state.datos_actuales = json.load(f)
    else:
        st.session_state.datos_actuales = [
            {"texto": "Menú Principal", "indentacion": 0, "funcion": None},
            {"texto": "Configuración", "indentacion": 1, "funcion": None},
            {"texto": "Ver Procesos", "indentacion": 2, "funcion": "listar_procesos"}
        ]

# st.title("Configurador XindeX")
# st.caption("Organiza la jerarquía arrastrando. Asigna las funciones a la derecha.")

# 1. CARGAMOS EL COMPONENTE DESDE LA CARPETA
ruta_componente = os.path.join(os.path.dirname(__file__), "./")
arbol_componente = components.declare_component("arbol_interactivo", path=ruta_componente)

# 2. RENDERIZAMOS Y RECIBIMOS LA LISTA ITERABLE DE PYTHON
estructura_actualizada = arbol_componente(key="mi_arbol", datos_arbol=st.session_state.datos_actuales)

# 3. PINTAMOS LOS SELECTBOX DE FUNCIONES
st.markdown("### 🔌 Mapeo de Funciones")
datos_finales = []

if estructura_actualizada:
    dic_previo = {d["texto"]: d.get("funcion") for d in st.session_state.datos_actuales}
    
    for i, nodo in enumerate(estructura_actualizada):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"<div style='margin-top:5px; margin-left:{nodo['indentacion']*25}px;'>👉 <b>{nodo['texto']}</b></div>", unsafe_allow_html=True)
        with col2:
            func_actual = dic_previo.get(nodo['texto'])
            idx_defecto = FUNCIONES_DISPONIBLES.index(func_actual) if func_actual in FUNCIONES_DISPONIBLES else 0
            func_sel = st.selectbox("Función", FUNCIONES_DISPONIBLES, index=idx_defecto, key=f"sel_{i}_{nodo['texto']}", label_visibility="collapsed")
            
        datos_finales.append({
            "texto": nodo["texto"],
            "indentacion": nodo["indentacion"],
            "funcion": func_sel if func_sel != "Ninguna" else None
        })

st.markdown("---")
# 4. GUARDADO Y SALIDA LIMPIA
if st.button("💾 Guardar y Ejecutar Índice", type="primary", use_container_width=True):
    if not datos_finales:
        st.warning("El índice no puede estar vacío.")
    else:
        with open("temp_menu.json", "w", encoding='utf-8') as f:
            json.dump(datos_finales, f, indent=4)
        os.replace("temp_menu.json", ARCHIVO_CONFIG)
        
        st.success("✅ ¡Guardado! La terminal va a continuar.")
        os._exit(0)