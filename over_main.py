import os
import sys
import multiprocessing

# Importamos XindeX y las funciones (Asegúrate de que las rutas a tus carpetas son correctas)
from XindeX.classXindeX import Over_Main
import funciones_over_main as cmd

# ■ EL MAPA DE EJECUCIÓN(Cambiar segun necesidad) 
DICC_FUNCIONES = {
    "version_webbb": cmd.version_web,
    "set_style": cmd.set_style,
    "from_to": cmd.from_to,
    "listar_procesos": cmd.listar_procesos,
    "subprocess_os": cmd.subprocess_os,
    "lanzar_proceso": cmd.lanzar_proceso,
    "cambiar_estilo_marco": cmd.cambiar_estilo_marco
}

if __name__ == "__main__":
    multiprocessing.freeze_support()
    os.system('cls' if os.name == 'nt' else 'clear')

    # La clase Over_Main se encarga automáticamente de detectar --config y lanzar el configurador si hace falta.
    menu_xindex = Over_Main( dicc_funciones=DICC_FUNCIONES, tipo_index='a', b_mode_all=True, b_loop=True )
    
    # ⚠️ Puente Opcional solo para este archivo. Borrar al replicar.
    cmd.The_X_Men = menu_xindex  

    # ■ EJECUCIÓN
    menu_xindex.mystyca(titulo='MAIN_MENU', head_datapush=" Configuración del Menú XindeX ", pad_x=5)
    # ■ SALIDA
    print(f"\n::: T H E   E N D :::")