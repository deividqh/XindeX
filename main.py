import os           
from enum import Enum
import tkinter as tk
import threading
from classXindeX import XindeX 
from classXindeX import Over_Main 

# ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
# DEF: CREA UN INDICE MULTINIVEL CON GENETICA QUE EJECUTA LAS FUNCIONES ASOCIADAS A CADA MENU
# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# ████████████████████████████████████████████ XINDEX ███████████████████████████████████████████████
# ████████████████████████████████████████████ XINDEX ███████████████████████████████████████████████

# 1- INSTANCIO EL OBJETO ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# The_X_Men = XindeX(head_datapush  = " XINDEX - OVER-MAIN ")
The_X_Men = Over_Main(tipo_index='a', b_mode_all=False, b_loop=True )

def main():
    global The_X_Men

    # 2- CREO LOS MENUS Y SUS FUNCIONES ASOCIADAS ▄▄▄▄▄▄▄▄▄▄▄▄
    Menu1 = The_X_Men.addX(titulo='Menu1', lst_items = [ ("Info XindeX" , None), ("Estilos" , None),("Flask" , None), ("BBDD" , None) ],  fraseHead = " - M A I N M E N U - ")
    
    # 3- COFIGURO LA GENETICA DEL INDICE ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    The_X_Men.config(titulo='Menu1'  , suPadre=None , indexInPadre = None )
    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ FORMA LARGA Y MAS ANTIGUA.
    # ■ AÑADE Y CONFIGURA - es el camino largo... o por partes.
    # The_X_Men.addX(titulo='subXindex', lst_items=[ ("Info Inicial" , None) ,  ("Configuracion XindeX", None ), ("Explicacion Parametros", explicacion_parametros ), ("Ejemplos Uso" , None ) ])
    # The_X_Men.config(titulo='subXindex' , suPadre='Menu1' , indexInPadre='Info XindeX' )    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    
    # ■ 2-3 ADD UN MENU CON ITEMS Y FUNCIONES Y LE ASIGNA CONFIGURACION ..... (Uso Recomendado por claridad)
    The_X_Men.addX( titulo='subXindex' , padre='Menu1' , ipadre="Info XindeX" , lst_items = [ ("Info Inicial" , None) ,  ("Configuracion XindeX", None ), ("Explicacion Parametros", explicacion_parametros ), ("Ejemplos Uso" , None ) ] )    
    The_X_Men.addX( titulo='subEstilos', padre='Menu1' , ipadre = 'Estilos' , lst_items = [ ("Ver Estilos", None) , ("Version Web" , version_web) ] )    

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # ■ 4- LLAMO A MYSTYCA PARA VISUALIZAR EL MENU ■■■■■■■■■■■                               
    retorno = The_X_Men.mystyca( titulo='Menu1', head_datapush  = " XINDEX - OVER-MAIN " , pad_x=20 )
    # retorno = The_X_Men.mystyca( titulo='Menu1',  pad_x=50 )

    # 5- RETORNO DE MYSTYCA ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    print(f"::: T H E   E N D  en MAIN() ::: {retorno if retorno else 'no retorno'} ")


# ████████████████████████████████████████████ FUNCIONES DEFINIDAS EN XINDEX ███████████████████████████████████████████████
# ████████████████████████████████████████████ FUNCIONES DEFINIDAS EN XINDEX ███████████████████████████████████████████████

def explicacion_parametros():
    print('\n ■■■■■■■■■■■■■ EXPLICACION DE LOS PARAMETROS PASADOS A MYSTICA ■■■■■■■■■■■■■■')
    print(""" retorno = The_X_Men.mystyca(  
                            titulo      = Menu1, 
                            b_terminator    = True, 
                            tipo_index = a, 
                            b_mode_all     = False, 
                            b_loop        = True , 
                            pad_x        = 50) 
    """)

    print("""     
    ■ [titulo](str)         ◄► Id del Menu Añadido y Configurado 
        
    ■ [b_terminator](bool)      True  ◄► Cuando sale de aquí ya se ha ejecutado la funcion del menu.....lleve donde lleve, pero tiene que estar  
                            False ◄► Se retorna a main la respuesta y se gestiona por el usuario.
    
    ■ [b_mode_all](bool)       True ◄► Solo se ejecutan ( o solo es opcion valida) los subMenus Finales (no padres) 
                            False ◄► Se ejecuta (solo los que son opcion valida) todo lo que no sea None en func.

    ■ [tipo_index](str)  '1'  ◄► Numerico(byDef)   █ 'a' ::: Alfabetico Min █ 'A' ::: Alfabetico May  █ 'A1', '1A', a1, 1a ::: Mixto
    
    ■ [b_loop](bool)          True ◄►  Ejecuta Items del XindeX y solo sale por '<<<'  (byDef)
                            False ◄► Si sólo ejecutamos una vez y retorna respuesta 
    
    ■ [pad_x](int)           Espacio entre el final del caracter mas a la derecha y el marco derecho del XindeX
    """)

def version_web():
    global The_X_Men    
    print(f'Accion version Web WIP')
    The_X_Men.get_web_lsts_lens_linea(titulo='Menu1',  tipo_index='a', b_mode_all=False, b_loop=True, pad_x=30)

def lanza_flask():
    print('L a n z a   F l a s k ')
    # from proyecto_final_v1 import funciones_tablas
    # from proyecto_final_v1.main import app as servidor_flask
    # servidor_flask.run()


# ████████████████████████████████████████████ INICIO ███████████████████████████████████████████████
# ████████████████████████████████████████████ INICIO ███████████████████████████████████████████████

if __name__ == "__main__":
    # ---- Limpio la terminal 
    os.system('cls')    
    # ---- Empezamos!!
    main() 
