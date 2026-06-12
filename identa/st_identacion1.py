import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(page_title="Gestor de Índice", layout="centered")

st.title("Gestor de Índice Jerárquico Dinámico")
st.caption("Organiza todo visualmente mediante Drag and Drop y presiona 'Guardar' al finalizar.")

# 1. Datos iniciales que Python le pasa al componente interactivo
if "datos_actuales" not in st.session_state:
    st.session_state.datos_actuales = [
        {"texto": "Introducción", "indentacion": 0},
        {"texto": "Antecedentes", "indentacion": 1},
        {"texto": "Marco Teórico", "indentacion": 0},
        {"texto": "Conclusiones", "indentacion": 0}
    ]

# 2. El HTML Completo convertido en un "Widget" interactivo para Streamlit
# Añadimos un puente (window.parent.postMessage) para enviar los datos a Python sin recargar la página
html_interactivo = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{ background-color: #ffffff; padding: 10px; font-family: sans-serif; }}
        .contenedor-arbol {{ padding: 25px; background-color: #ffffff; border: 1px solid #dee2e6; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05); }}
        .item-arbol {{ background: #ffffff; border: 1px solid #ced4da; border-radius: 4px; padding: 10px 15px; margin: 6px 0; max-width: 550px; cursor: grab; user-select: none; display: flex; align-items: center; font-weight: 500; color: #212529; box-shadow: 0 1px 3px rgba(0,0,0,0.05); transition: transform 0.15s ease, margin-left 0.2s ease, background-color 0.2s; }}
        .item-arbol:hover {{ border-color: #0d6efd; background-color: #f8f9fa; }}
        .numero-indice {{ color: #0d6efd; font-weight: 700; margin-right: 10px; font-family: monospace; }}
        .item-arbol.arrastrando {{ opacity: 0.4; background-color: #e9ecef; border: 2px dashed #0d6efd; cursor: grabbing; transform: scale(0.98); }}
    </style>
</head>
<body>

    <div class="row g-3 mb-4">
        <div class="col-12">
            <div class="input-group shadow-sm">
                <input type="text" id="txtElemento" class="form-control" placeholder="Ingresa un nuevo título para el índice">
                <button id="btnAgregar" class="btn btn-primary" style="min-width: 160px;">Agregar al Índice</button>
            </div>
        </div>
        <div class="col-12">
            <div class="input-group shadow-sm">
                <select id="cmbEliminar" class="form-select">
                    <option value="" selected disabled>Selecciona un elemento para eliminar...</option>
                </select>
                <button id="btnEliminar" class="btn btn-danger" style="min-width: 160px;">Eliminar del Índice</button>
            </div>
        </div>
    </div>
    
    <div id="arbol" class="contenedor-arbol"></div>

<script>
    // Recibimos los datos iniciales desde el st.session_state de Python
    const datosIniciales = {json.dumps(st.session_state.datos_actuales)};

    const contenedor = document.getElementById("arbol");
    const inputElemento = document.getElementById("txtElemento");
    const btnAgregar = document.getElementById("btnAgregar");
    const comboEliminar = document.getElementById("cmbEliminar");
    const btnEliminar = document.getElementById("btnEliminar");

    let elementoArrastrado = null;
    let xInicial = 0;
    let indentacionInicial = 0;
    const ANCHO_PASO = 40; 

    btnAgregar.addEventListener("click", agregarNuevoNodo);
    inputElemento.addEventListener("keydown", (e) => {{ if (e.key === "Enter") agregarNuevoNodo(); }});

    btnEliminar.addEventListener("click", () => {{
        const idx = comboEliminar.value;
        if (idx === "") return;
        const items = contenedor.querySelectorAll(".item-arbol");
        if (items[idx]) {{
            items[idx].remove();
            actualizarEstructuraArbol();
            enviarDatosAPython(); // Notificar cambio
        }}
    }});

    function crearNodoDOM(texto, indentacion) {{
        const item = document.createElement("div");
        item.className = "item-arbol";
        item.draggable = true; 
        item.dataset.indentacion = indentacion;
        item.style.marginLeft = `${{indentacion * ANCHO_PASO}}px`;

        const spanNumero = document.createElement("span");
        spanNumero.className = "numero-indice";
        const spanTexto = document.createElement("span");
        spanTexto.className = "texto-nodo";
        spanTexto.textContent = texto;

        item.appendChild(spanNumero);
        item.appendChild(spanTexto);

        item.addEventListener("dragstart", (e) => {{
            elementoArrastrado = item;
            item.classList.add("arrastrando");
            xInicial = e.clientX;
            indentacionInicial = parseInt(item.dataset.indentacion, 10);
        }});

        item.addEventListener("dragend", () => {{
            if (elementoArrastrado) elementoArrastrado.classList.remove("arrastrando");
            elementoArrastrado = null;
            actualizarEstructuraArbol();
            enviarDatosAPython(); // Enviar orden final tras soltar
        }});

        return item;
    }}

    function agregarNuevoNodo() {{
        const valor = inputElemento.value.trim();
        if (valor === "") return;
        const nodosExistentes = Array.from(contenedor.querySelectorAll(".texto-nodo"));
        if (nodosExistentes.some(span => span.textContent.toLowerCase() === valor.toLowerCase())) {{
            alert("El elemento ya existe.");
            return;
        }}
        const nuevoNodo = crearNodoDOM(valor, 0);
        contenedor.appendChild(nuevoNodo);
        inputElemento.value = "";
        actualizarEstructuraArbol();
        enviarDatosAPython();
    }}

    // Renderizado inicial
    datosIniciales.forEach(dato => contenedor.appendChild(crearNodoDOM(dato.texto, dato.indentacion)));
    actualizarEstructuraArbol();

    contenedor.addEventListener("dragover", (e) => {{
        e.preventDefault(); 
        if (!elementoArrastrado) return;
        const deltaX = e.clientX - xInicial;
        const cambioNivel = Math.round(deltaX / ANCHO_PASO);
        let nuevaIndentacion = Math.max(0, indentacionInicial + cambioNivel);
        elementoArrastrado.dataset.indentacion = nuevaIndentacion;
        elementoArrastrado.style.marginLeft = `${{nuevaIndentacion * ANCHO_PASO}}px`;

        const elementoCercano = obtenerElementoPosterior(contenedor, e.clientY);
        if (elementoCercano == null) contenedor.appendChild(elementoArrastrado);
        else contenedor.insertBefore(elementoArrastrado, elementoCercano);
    }});

    function actualizarEstructuraArbol() {{
        const items = contenedor.querySelectorAll(".item-arbol");
        let contadoresNivel = []; 
        let indentacionAnterior = 0;

        comboEliminar.innerHTML = '<option value="" selected disabled>Selecciona un elemento para eliminar...</option>';

        items.forEach((item, index) => {{
            let indentacionActual = parseInt(item.dataset.indentacion, 10);
            if (index === 0) indentacionActual = 0; 
            else if (indentacionActual > indentacionAnterior + 1) indentacionActual = indentacionAnterior + 1; 

            item.dataset.indentacion = indentacionActual;
            item.style.marginLeft = `${{indentacionActual * ANCHO_PASO}}px`;

            if (indentacionActual < contadoresNivel.length) contadoresNivel = contadoresNivel.slice(0, indentacionActual + 1);
            while (contadoresNivel.length <= indentacionActual) contadoresNivel.push(0);
            contadoresNivel[indentacionActual]++;

            const cadenaIndice = contadoresNivel.join(".") + ".";
            item.querySelector(".numero-indice").textContent = cadenaIndice;
            indentacionAnterior = indentacionActual;

            // Actualizar el combo select
            const option = document.createElement("option");
            option.value = index;
            option.textContent = `${{cadenaIndice}} ${{item.querySelector(".texto-nodo").textContent}}`;
            comboEliminar.appendChild(option);
        }});
    }}

    function obtenerElementoPosterior(contenedor, y) {{
        const elementosArrastrables = [...contenedor.querySelectorAll(".item-arbol:not(.arrastrando)")];
        return elementosArrastrables.reduce((masCercano, hijo) => {{
            const caja = hijo.getBoundingClientRect();
            const offset = y - caja.top - caja.height / 2;
            if (offset < 0 && offset > masCercano.offset) return {{ offset: offset, element: hijo }};
            else return masCercano;
        }}, {{ offset: Number.NEGATIVE_INFINITY }}).element;
    }}

    // PUENTE DE COMUNICACIÓN CON STREAMLIT
    function enviarDatosAPython() {{
        const items = contenedor.querySelectorAll(".item-arbol");
        const datosEstructura = Array.from(items).map(item => ({{
            texto: item.querySelector(".texto-nodo").textContent,
            indentacion: parseInt(item.dataset.indentacion, 10)
        }}));
        
        // Enviamos la estructura limpia en formato JSON a la app de Streamlit
        window.parent.postMessage({{
            isstreamlit: true,
            type: "streamlit:setComponentValue",
            value: datosEstructura
        }}, "*");
    }}
    
    // Enviar estado inicial para sincronizar
    setTimeout(enviarDatosAPython, 500);
</script>
</body>
</html>
"""

# 3. Renderizamos el componente HTML y capturamos sus datos en "tiempo real" en Python
# Retorna la lista JSON actualizada solo cuando se muta el árbol (sin recargar la UI)
datos_recibidos = components.html(html_interactivo, height=550, scrolling=True)

st.markdown("---")

# 4. Botón de confirmación estático en Streamlit
if st.button("💾 Guardar Cambios en Base de Datos / Sistema", type="primary", use_container_width=True):
    if datos_recibidos:
        st.session_state.datos_actuales = datos_recibidos
        st.success("¡Estructura guardada con éxito en Python!")
        st.json(st.session_state.datos_actuales)
    else:
        st.warning("No se han detectado movimientos o interacciones aún.")