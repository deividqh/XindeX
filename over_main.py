# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
from XindeX.classXindeX import Over_Main       # ■ PADRE DE XINDEX CON ■ COLOR EN HEAD Y PIE  ■ BEGIN ** ■ LANZAR DEMONIO << >> ■ LANZA BACKGROUND => 
# from XindeX.Sdata import Sdata                 # ■ AYUDA PARA EL OVER-MAIN PARA PEDIR DATOS SEGUROS AL USUARIO
from colorama import Fore, Style, init  # ■ COLORAMA PARA COLORES EN TERMINAL....por si se quiere usar colores para 'ayudas'
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import os               # SISTEMA OPERATIVO(PARA LIMPIAR LA TERMINAL)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import multiprocessing  # PARA PROCESOS EN BACKGROUND Y DEMONIOS
# ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
import funciones_over_main as cmd
# DEF: CREA UN INDICE MULTINIVEL CON GENETICA QUE EJECUTA LAS FUNCIONES ASOCIADAS A CADA MENU
# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# ████████████████████████████████████████████ XINDEX ███████████████████████████████████████████████
# ████████████████████████████████████████████ XINDEX ███████████████████████████████████████████████

# 1- INSTANCIO EL OBJETO ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
The_X_Men = Over_Main(tipo_index='a', b_mode_all=True, b_loop=True )

def main():
    global The_X_Men

    # ■- CREO LOS MENUS Y SUS FUNCIONES ASOCIADAS ▄▄▄▄▄▄▄▄▄▄▄▄
    Menu1 = The_X_Men.addX(titulo='Menu1', padre=None , ipadre=None, 
                    lst_items = [   ("Info XindeX" , None), 
                                    ("Estilos" , None),
                                    ("Procesos" , None), 
                                    ("From-To" , cmd.from_to(The_X_Men)) ] )
    
    The_X_Men.addX( titulo='sub-Xindex' , padre='Menu1'   , ipadre="Info XindeX", 
                    lst_items = [ ("Sobre XindeX" , None) , ("Parametros Mystyca", None ), ("Ejemplos Uso" , None ) ] )    
    
    The_X_Men.addX( titulo='sub-Estilos', padre='Menu1'   , ipadre='Estilos'    , 
                    lst_items = [ ("Ver Estilos", None) , ("Version Web" , cmd.version_web(The_X_Men)) ] )    
    
    The_X_Men.addX( titulo='sub-Procesos', padre='Menu1'  , ipadre='Procesos'   , 
                    lst_items = [ ("Listar Proceso", cmd.listar_procesos(The_X_Men)) , ("Lanzar Proceso" , lambda: cmd.lanzar_proceso(The_X_Men)), ("Detener Proceso" , None) , ('OS procesos', lambda: cmd.subprocess_os(The_X_Men))] )    
    
    The_X_Men.addX( titulo='sub-Aux', padre='sub-Estilos' , ipadre='Ver Estilos', 
                    lst_items = [ ("Switch b_mode_all", lambda: cmd.set_style(The_X_Men)), ("Cambiar Estilo Marco" , cmd.cambiar_estilo_marco(The_X_Men)), ("aux 3" , None) ] )    
    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ FORMA LARGA Y MAS ANTIGUA.
    # ■ AÑADE Y CONFIGURA - es el camino largo... o por partes.
    # The_X_Men.addX(titulo='subXindex', lst_items=[ ("Info Inicial" , None) ,  ("Configuracion XindeX", None ), ("Explicacion Parametros", parametros ), ("Ejemplos Uso" , None ) ])
    # The_X_Men.config(titulo='subXindex' , suPadre='Menu1' , indexInPadre='Info XindeX' )    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # ■ 4- LLAMO A MYSTYCA PARA VISUALIZAR EL MENU ■■■■■■■■■■■                               
    retorno = The_X_Men.mystyca( titulo='Menu1', head_datapush  = " XINDEX - OVER-MAIN " , pad_x=5 )

    # 5- RETORNO DE MYSTYCA ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    print(f"::: T H E   E N D  en MAIN() ::: {retorno if retorno else 'no retorno'} ")


# ████████████████████████████████████████████ FUNCIONES DEFINIDAS EN XINDEX ███████████████████████████████████████████████
# ████████████████████████████████████████████ FUNCIONES DEFINIDAS EN XINDEX ███████████████████████████████████████████████



# ████████████████████████████████████████████ INICIO ███████████████████████████████████████████████
# ████████████████████████████████████████████ INICIO ███████████████████████████████████████████████

if __name__ == "__main__":
    
    multiprocessing.freeze_support()
    # ---- Limpio la terminal 
    os.system('cls')    
    # ---- Empezamos!!
    main() 
