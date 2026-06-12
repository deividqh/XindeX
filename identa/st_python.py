import streamlit as st
import io
import contextlib
import traceback

st.title("Ejecución de código Python en Streamlit")
code = st.text_area("Introduce tu código Python aquí:", height=200, value="print('¡Hola Mundo!')\na = 5\nb = 10\nprint(f'La suma es: {a + b}')")
if st.button("Ejecutar Código"):
    buffer = io.StringIO()
    # Mantenemos la redirección activa para capturar prints y errores en el mismo sitio
    with contextlib.redirect_stdout(buffer):
        try:
            exec(code, {})  # El diccionario vacío ayuda a aislar un poco el entorno global
        except Exception as e:
            # Imprime el error directamente en el buffer para que el usuario vea dónde falló
            print(f"❌ Error en la ejecución:\n{traceback.format_exc()}")
    # Mostramos el resultado finalizado
    output = buffer.getvalue()
    st.text_area("Salida del Código:", value=output, height=200)
