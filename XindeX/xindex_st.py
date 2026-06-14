import streamlit as st
import streamlit.components.v1 as components
import ast
import json
import os

st.set_page_config(page_title="Configurador XindeX", layout="centered")

ARCHIVO_CONFIG = "config_menu.json"
ARCHIVO_RETORNO = "temp_menu_resultado.json"
ARCHIVO_FUNCIONES = os.path.join(os.path.dirname(__file__), "..", "over_main.py")

FUNCION_SIN_ASIGNAR = "Ninguna"


def obtener_funciones_disponibles():
    """Devuelve las funciones configurables desde las claves de DICC_FUNCIONES."""
    with open(ARCHIVO_FUNCIONES, "r", encoding="utf-8") as archivo:
        arbol = ast.parse(archivo.read(), filename=ARCHIVO_FUNCIONES)

    for nodo in arbol.body:
        if not isinstance(nodo, ast.Assign):
            continue

        tiene_dicc_funciones = any(
            isinstance(objetivo, ast.Name) and objetivo.id == "DICC_FUNCIONES"
            for objetivo in nodo.targets
        )
        if not tiene_dicc_funciones or not isinstance(nodo.value, ast.Dict):
            continue

        funciones = [
            clave.value
            for clave in nodo.value.keys
            if isinstance(clave, ast.Constant)
        ]
        return [
            FUNCION_SIN_ASIGNAR,
            *(funcion for funcion in funciones if funcion != FUNCION_SIN_ASIGNAR),
        ]

    return [FUNCION_SIN_ASIGNAR]


def validar_nodos_config(nodos):
    """Devuelve una lista limpia de nodos o None si el JSON no sirve para el menú."""
    if not isinstance(nodos, list):
        return None

    nodos_limpios = []
    for nodo in nodos:
        if not isinstance(nodo, dict):
            return None

        texto = nodo.get("texto")
        indentacion = nodo.get("indentacion", 0)
        funcion = nodo.get("funcion")

        if not isinstance(texto, str) or not texto.strip():
            return None
        if not isinstance(indentacion, int) or indentacion < 0:
            return None
        if funcion is not None and funcion not in obtener_funciones_disponibles():
            return None

        nodos_limpios.append({
            "texto": texto.strip(),
            "indentacion": indentacion,
            "funcion": funcion,
        })

    return nodos_limpios


def cargar_config_guardada():
    if not os.path.exists(ARCHIVO_CONFIG):
        return []

    try:
        with open(ARCHIVO_CONFIG, "r", encoding="utf-8") as f:
            nodos = json.load(f)
    except (OSError, json.JSONDecodeError):
        st.warning("No se pudo leer config_menu.json. Se iniciará un menú nuevo.")
        return []

    nodos_validos = validar_nodos_config(nodos)
    if nodos_validos is None:
        st.warning("config_menu.json no tiene el formato esperado. Se iniciará un menú nuevo.")
        return []

    return nodos_validos

if "datos_actuales" not in st.session_state:
    # 🧠 Si config_menu.json existe y es válido, se carga para poder editarlo.
    st.session_state.datos_actuales = cargar_config_guardada()

# st.title("Configurador XindeX")
# st.caption("Organiza la jerarquía arrastrando. Asigna las funciones a la derecha.")

# 1. CARGAMOS EL COMPONENTE DESDE LA CARPETA
ruta_componente = os.path.join(os.path.dirname(__file__), "./")
arbol_componente = components.declare_component("arbol_interactivo", path=ruta_componente)

# 2. RENDERIZAMOS Y RECIBIMOS LA LISTA ITERABLE DE PYTHON
estructura_actualizada = arbol_componente(
    key="mi_arbol",
    datos_arbol=st.session_state.datos_actuales,
    funciones_disponibles=obtener_funciones_disponibles(),
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
            "funcion": nodo.get("funcion") if nodo.get("funcion") != FUNCION_SIN_ASIGNAR else None,
        }
        for nodo in estructura_actualizada
        if isinstance(nodo, dict)
    ]
    st.session_state.datos_actuales = datos_finales

st.markdown("---")
st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #198754;
        border-color: #198754;
        color: #ffffff;
    }
    div.stButton > button:hover {
        background-color: #157347;
        border-color: #146c43;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# 4. GUARDADO Y SALIDA LIMPIA
if st.button("💾 Guardar y Ejecutar Índice", use_container_width=True):
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
