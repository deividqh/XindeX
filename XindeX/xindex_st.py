import streamlit as st
import streamlit.components.v1 as components
import json
import os

st.set_page_config(page_title="Configurador XindeX", layout="centered")

ARCHIVO_CONFIG = "config_menu.json"
ARCHIVO_RETORNO = "temp_menu_resultado.json"

# DEBE COINCIDIR EXACTAMENTE CON LAS CLAVES DEL DICCIONARIO EN over_main.py
FUNCIONES_DISPONIBLES = [
    "Ninguna", "version_web", "set_style", "from_to", 
    "listar_procesos", "subprocess_os", "lanzar_proceso", "cambiar_estilo_marco"
]

if "datos_actuales" not in st.session_state:
    # 🧠 KISS: --config fuerza empezar de cero; sin --config solo cargamos si existe JSON.
    empezar_desde_cero = os.environ.get("XINDEX_CONFIG_DESDE_CERO") == "1"

    if os.path.exists(ARCHIVO_CONFIG) and not empezar_desde_cero:
        with open(ARCHIVO_CONFIG, "r", encoding='utf-8') as f:
            st.session_state.datos_actuales = json.load(f)
    else:
        st.session_state.datos_actuales = []

# st.title("Configurador XindeX")
# st.caption("Organiza la jerarquía arrastrando. Asigna las funciones a la derecha.")

# 1. CARGAMOS EL COMPONENTE DESDE LA CARPETA
ruta_componente = os.path.join(os.path.dirname(__file__), "./")
arbol_componente = components.declare_component("arbol_interactivo", path=ruta_componente)

# 2. RENDERIZAMOS Y RECIBIMOS LA LISTA ITERABLE DE PYTHON
estructura_actualizada = arbol_componente(
    key="mi_arbol",
    datos_arbol=st.session_state.datos_actuales,
    funciones_disponibles=FUNCIONES_DISPONIBLES,
)

# 3. El componente ya integra el mapeo de funciones en cada fila del índice.
datos_finales = st.session_state.datos_actuales

if estructura_actualizada is not None:
    # 🧠 Compatibilidad: si llega un dict viejo, usamos su lista interna.
    if isinstance(estructura_actualizada, dict):
        estructura_actualizada = estructura_actualizada.get("arbol_jerarquico", [])

    datos_finales = [
        {
            "texto": nodo["texto"],
            "indentacion": nodo["indentacion"],
            "funcion": nodo.get("funcion") if nodo.get("funcion") != "Ninguna" else None,
        }
        for nodo in estructura_actualizada
        if isinstance(nodo, dict)
    ]
    st.session_state.datos_actuales = datos_finales

st.markdown("---")
# 4. GUARDADO Y SALIDA LIMPIA
if st.button("💾 Guardar y Ejecutar Índice", type="primary", use_container_width=True):
    if not datos_finales:
        st.warning("El índice no puede estar vacío.")
    else:
        # 🧠 Guardamos dos copias: una persistente y otra de retorno para el Python que lanzó Streamlit.
        with open("temp_menu.json", "w", encoding='utf-8') as f:
            json.dump(datos_finales, f, ensure_ascii=False, indent=4)
        os.replace("temp_menu.json", ARCHIVO_CONFIG)

        with open(ARCHIVO_RETORNO, "w", encoding='utf-8') as f:
            json.dump(datos_finales, f, ensure_ascii=False, indent=4)
        
        st.success("✅ ¡Guardado! La terminal va a continuar.")
        os._exit(0)
