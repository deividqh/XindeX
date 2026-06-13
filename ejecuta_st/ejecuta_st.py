import multiprocessing
import subprocess
import os
import json

def ejecutar_streamlit(datos_compartidos):
    # Ejecutamos tu archivo de streamlit
    # Al ser un subproceso, se detiene aquí hasta que cierres Streamlit con os._exit(0)
    subprocess.run(["streamlit", "run", "./ejecuta_st/ejecutado_st.py"])
    
    # Al cerrarse la app, buscamos el archivo temporal que generó Streamlit
    if os.path.exists("temp_data.json"):
        with open("temp_data.json", "r") as f:
            datos_recuperados = json.load(f)
            
        # Pasamos los datos del diccionario temporal al diccionario compartido de multiprocessing
        for clave, valor in datos_recuperados.items():
            datos_compartidos[clave] = valor
            
        # Borramos el archivo temporal para mantener todo limpio (como si solo usáramos RAM)
        os.remove("temp_data.json")

if __name__ == '__main__':
    # Creamos un administrador de memoria para compartir datos entre procesos
    with multiprocessing.Manager() as manager:
        datos_compartidos = manager.dict()
        
        # Lanzamos la función que ejecuta Streamlit
        proceso = multiprocessing.Process(target=ejecutar_streamlit, args=(datos_compartidos,))
        proceso.start()
        
        # El programa principal se queda a la espera
        proceso.join()
        
        print("\n--- Continuación del script principal ---")
        
        # Verificamos que los datos hayan pasado correctamente al diccionario principal
        if 'texto_usuario' in datos_compartidos:
            print("Diccionario completo recuperado:")
            print(dict(datos_compartidos)) # Convertimos a dict normal para imprimir
            print(f"\nEl valor introducido fue: {datos_compartidos['texto_usuario']}")
        else:
            print("El usuario cerró la ventana sin guardar datos o hubo un error.")