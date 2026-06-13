import os
import sys
import multiprocessing
from colorama import init, Fore, Style

# Importamos XindeX y nuestras funciones
from XindeX.classXindeX import Over_Main
import funciones_over_main as cmd

# ■ EL MAPA DE FUNCIONES (El Enrutador)
# Aquí asocias los nombres(str) que aparecerán en la web con tus funciones reales
DICCIONARIO_FUNCIONES = {
    "version_web": cmd.version_web,
    "set_style": cmd.set_style,
    "from_to": cmd.from_to,
    "listar_procesos": cmd.listar_procesos,
    "subprocess_os": cmd.subprocess_os,
    "lanzar_proceso": cmd.lanzar_proceso,
    "cambiar_estilo_marco": cmd.cambiar_estilo_marco,
    "Ninguna": None
}

if __name__ == "__main__":
    multiprocessing.freeze_support()
    init() # Inicializa Colorama
    os.system('cls' if os.name == 'nt' else 'clear')

    # ■ LA MAGIA: La clase Over_Main se encarga de TODO
    # Detectará automáticamente si has puesto 'python over_main.py --config'
    The_X_Men = Over_Main(
        dicc_funciones=DICCIONARIO_FUNCIONES,
        tipo_index='a', 
        b_mode_all=True, 
        b_loop=True, 
        # b_config=True,
    )
    
    # ■ ARRANCAMOS XINDEX
    retorno = The_X_Men.mystyca(titulo='MAIN_MENU', head_datapush=" XINDEX CONFIGURADO ", pad_x=5)
    print(f"\n{Fore.GREEN}::: T H E   E N D ::: {retorno}{Style.RESET_ALL}")