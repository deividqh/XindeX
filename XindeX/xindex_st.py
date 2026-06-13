import streamlit as st
import streamlit.components.v1 as components
import json
import os

st.set_page_config(page_title="Configurador XindeX", layout="centered", initial_sidebar_state="collapsed")

ARCHIVO_CONFIG = "config_menu.json"

# NOMBRES DE LAS FUNCIONES DISPONIBLES EN EL DESPLEGABLE
FUNCIONES_DISPONIBLES = [
    "Ninguna", "version_web", "set_style", "from_to", 
    "listar_procesos", "subprocess_os", "lanzar_proceso", "cambiar_estilo_marco"
]

# 1. ESTADO INICIAL (Modo Edición vs Primera vez)
if "datos_actuales" not in st.session_state:
    if os.path.exists(ARCHIVO_CONFIG):
        with open(ARCHIVO_CONFIG, "r", encoding='utf-8') as f:
            st.session_state.datos_actuales = json.load(f)
    else:
        st.session_state.datos_actuales = [
            {"texto": "Menú Principal", "indentacion": 0, "funcion": None},
            {"texto": "Opciones Avanzadas", "indentacion": 1, "funcion": None},
            {"texto": "Listar Procesos", "indentacion": 2, "funcion": "listar_procesos"}
        ]

st.title("⚙️ Configurador XindeX")
st.caption("Organiza la jerarquía visualmente y asigna funciones. Arrastra a la derecha para crear submenús.")

# 2. EL COMPONENTE (Copia exacta de la lógica visual de identa6.html)
html_ui = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{ background-color: #f1f3f5; padding: 15px; font-family: sans-serif; }}
        .contenedor-arbol {{ padding: 25px; background: #fff; border: 1px solid #dee2e6; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }}
        .item-arbol {{ background: #fff; border: 1px solid #ced4da; border-radius: 4px; padding: 10px 15px; margin: 6px 0; max-width: 550px; cursor: grab; display: flex; align-items: center; font-weight: 500; transition: background-color 0.2s; }}
        .item-arbol:hover {{ border-color: #0d6efd; background-color: #f8f9fa; }}
        .numero-indice {{ color: #0d6efd; font-weight: 700; margin-right: 10px; font-family: monospace; }}
        .item-arbol.arrastrando {{ opacity: 0.4; border: 2px dashed #0d6efd; }}
        .btn-delete {{ margin-left: auto; color: red; cursor: pointer; border: none; background: none; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="row g-3 mb-4">
        <div class="col-12 input-group">
            <input type="text" id="txtElemento" class="form-control" placeholder="Añadir nuevo menú...">
            <button id="btnAgregar" class="btn btn-primary">Agregar Nodo</button>
        </div>
    </div>
    <div id="arbol" class="contenedor-arbol"></div>

<script>
    const datosIniciales = {json.dumps(st.session_state.datos_actuales)};
    const contenedor = document.getElementById("arbol");
    const ANCHO_PASO = 40; 
    let dragElement = null; let xInicial = 0; let indInicial = 0;

    function crearNodo(texto, indentacion) {{
        const item = document.createElement("div");
        item.className = "item-arbol"; item.draggable = true; 
        item.dataset.indentacion = indentacion;
        item.style.marginLeft = `${{indentacion * ANCHO_PASO}}px`;

        const num = document.createElement("span"); num.className = "numero-indice";
        const txt = document.createElement("span"); txt.className = "texto-nodo"; txt.textContent = texto;
        
        const btnDel = document.createElement("button"); btnDel.className = "btn-delete"; btnDel.innerHTML = "X";
        btnDel.onclick = function() {{ item.remove(); actualizarArbol(); enviarDatos(); }};

        item.appendChild(num); item.appendChild(txt); item.appendChild(btnDel);

        item.addEventListener("dragstart", (e) => {{ dragElement = item; item.classList.add("arrastrando"); xInicial = e.clientX; indInicial = parseInt(item.dataset.indentacion, 10); }});
        item.addEventListener("dragend", () => {{ if(dragElement) dragElement.classList.remove("arrastrando"); dragElement = null; actualizarArbol(); enviarDatos(); }});
        return item;
    }}

    document.getElementById("btnAgregar").addEventListener("click", () => {{
        const input = document.getElementById("txtElemento"); if (!input.value.trim()) return;
        contenedor.appendChild(crearNodo(input.value.trim(), 0)); input.value = ""; actualizarArbol(); enviarDatos();
    }});

    datosIniciales.forEach(dato => contenedor.appendChild(crearNodo(dato.texto, dato.indentacion)));
    actualizarArbol();

    contenedor.addEventListener("dragover", (e) => {{
        e.preventDefault(); if (!dragElement) return;
        const deltaX = e.clientX - xInicial;
        let nuevaInd = Math.max(0, indInicial + Math.round(deltaX / ANCHO_PASO));
        dragElement.dataset.indentacion = nuevaInd;
        dragElement.style.marginLeft = `${{nuevaInd * ANCHO_PASO}}px`;

        const elementos = [...contenedor.querySelectorAll(".item-arbol:not(.arrastrando)")];
        const cercano = elementos.reduce((closest, child) => {{
            const box = child.getBoundingClientRect(); const offset = e.clientY - box.top - box.height / 2;
            return (offset < 0 && offset > closest.offset) ? {{ offset: offset, element: child }} : closest;
        }}, {{ offset: Number.NEGATIVE_INFINITY }}).element;

        if (cercano == null) contenedor.appendChild(dragElement); else contenedor.insertBefore(dragElement, cercano);
    }});

    function actualizarArbol() {{
        const items = contenedor.querySelectorAll(".item-arbol");
        let contadores = []; let lastInd = 0;
        items.forEach((item, index) => {{
            let currInd = parseInt(item.dataset.indentacion, 10);
            if (index === 0) currInd = 0; else if (currInd > lastInd + 1) currInd = lastInd + 1; 
            item.dataset.indentacion = currInd; item.style.marginLeft = `${{currInd * ANCHO_PASO}}px`;
            
            if (currInd < contadores.length) contadores = contadores.slice(0, currInd + 1);
            while (contadores.length <= currInd) contadores.push(0);
            contadores[currInd]++;
            item.querySelector(".numero-indice").textContent = contadores.join(".") + ".";
            lastInd = currInd;
        }});
    }}

    function enviarDatos() {{
        const items = contenedor.querySelectorAll(".item-arbol");
        const datos = Array.from(items).map(item => ({{ texto: item.querySelector(".texto-nodo").textContent, indentacion: parseInt(item.dataset.indentacion, 10) }}));
        window.parent.postMessage({{ isstreamlit: true, type: "streamlit:setComponentValue", value: datos }}, "*");
    }}
    setTimeout(enviarDatos, 600); // Enviar estado inicial tras carga
</script>
</body>
</html>
"""

# Recibimos el drag & drop del HTML
estructura_actualizada = components.html(html_ui, height=450, scrolling=True)

# 3. MAPEADO DE FUNCIONES EN PYTHON
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

# 4. GUARDADO ATÓMICO Y CIERRE LIMPIO
st.markdown("---")
if st.button("💾 Guardar y Ejecutar Índice", type="primary", use_container_width=True):
    if not datos_finales:
        st.warning("El índice no puede estar vacío.")
    else:
        # Guardado atómico (robusto frente a fallos)
        with open("temp_menu.json", "w", encoding='utf-8') as f:
            json.dump(datos_finales, f, indent=4)
        os.replace("temp_menu.json", ARCHIVO_CONFIG)
        
        st.success("✅ ¡Configuración guardada! Puedes cerrar esta pestaña. El programa principal continuará en tu consola.")
        
        # Muerte limpia del subproceso (Over_Main detectará el cierre y continuará)
        os._exit(0)