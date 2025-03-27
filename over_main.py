# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# from classXindeX import XindeX          # ■ XINDEX A PELO
from classXindeX import Over_Main       # ■ PADRE DE XINDEX CON ■ COLOR EN HEAD Y PIE  ■ BEGIN ** ■ LANZAR DEMONIO << >> ■ LANZA BACKGROUND => 
from Sdata import Sdata                 # ■ AYUDA PARA EL OVER-MAIN PARA PEDIR DATOS SEGUROS AL USUARIO

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import os               # SISTEMA OPERATIVO(PARA LIMPIAR LA TERMINAL)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import tkinter as tk    # SOLO EN CASO DE NECESITARLO

# ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
# DEF: CREA UN INDICE MULTINIVEL CON GENETICA QUE EJECUTA LAS FUNCIONES ASOCIADAS A CADA MENU
# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# ████████████████████████████████████████████ XINDEX ███████████████████████████████████████████████
# ████████████████████████████████████████████ XINDEX ███████████████████████████████████████████████

# The_X_Men = XindeX(head_datapush  = " XINDEX - OVER-MAIN ")

# 1- INSTANCIO EL OBJETO ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
#   ■ [tipo_index='a']  , TIPO DE INDICE a.1. , b.2.1 etc. OTROS TIPOS: ■ 1 or '1' ■ 'A' ■ 'A1' or '1A' or 'a1' or '1a'
#   ■ [b_mode_all=False], SOLO SE EJECUTAN LOS HIJOS Y LOS PADRES PUEDEN SER BEGGINER **
#   ■ [b_loop=True]     , SE SALE POR <<< 
The_X_Men = Over_Main(tipo_index='a', b_mode_all=False, b_loop=True )

def main():
    global The_X_Men

    # ■- CREO LOS MENUS Y SUS FUNCIONES ASOCIADAS ▄▄▄▄▄▄▄▄▄▄▄▄
    Menu1 = The_X_Men.addX(titulo='Menu1', padre=None , ipadre=None, lst_items = [ ("Info XindeX" , None), ("Estilos" , None),("Procesos" , None), ("From-To" , from_to) ])
    # ■- ADD UN MENU CON ITEMS Y FUNCIONES Y LE ASIGNA CONFIGURACION ..... (Uso Recomendado por claridad)
    The_X_Men.addX( titulo='sub-Xindex' , padre='Menu1' , ipadre="Info XindeX" , lst_items = [ ("Sobre XindeX" , sobre_xindex) , ("Parametros Mystyca", parametros ), ("Ejemplos Uso" , None ) ] )    
    The_X_Men.addX( titulo='sub-Estilos', padre='Menu1' , ipadre = 'Estilos' , lst_items = [ ("Ver Estilos", None) , ("Version Web" , version_web) ] )    
    The_X_Men.addX( titulo='sub-Procesos', padre='Menu1' , ipadre = 'Procesos' , lst_items = [ ("Listar Proceso", listar_procesos) , ("Lanzar Proceso" , None), ("Detener Proceso" , None) ] )    
    
    The_X_Men.addX( titulo='sub-Aux', padre='sub-Estilos' , ipadre = 'Ver Estilos' , lst_items = [ ("aux 1", None) , ("aux 2" , None), ("aux 3" , None) ] )    
    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ FORMA LARGA Y MAS ANTIGUA.
    # ■ AÑADE Y CONFIGURA - es el camino largo... o por partes.
    # The_X_Men.addX(titulo='subXindex', lst_items=[ ("Info Inicial" , None) ,  ("Configuracion XindeX", None ), ("Explicacion Parametros", parametros ), ("Ejemplos Uso" , None ) ])
    # The_X_Men.config(titulo='subXindex' , suPadre='Menu1' , indexInPadre='Info XindeX' )    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # ■ 4- LLAMO A MYSTYCA PARA VISUALIZAR EL MENU ■■■■■■■■■■■                               
    retorno = The_X_Men.mystyca( titulo='Menu1', head_datapush  = " XINDEX - OVER-MAIN " , pad_x=5 )
    # retorno = The_X_Men.mystyca( titulo='Menu1',  pad_x=30 )

    # 5- RETORNO DE MYSTYCA ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    print(f"::: T H E   E N D  en MAIN() ::: {retorno if retorno else 'no retorno'} ")


# ████████████████████████████████████████████ FUNCIONES DEFINIDAS EN XINDEX ███████████████████████████████████████████████
# ████████████████████████████████████████████ FUNCIONES DEFINIDAS EN XINDEX ███████████████████████████████████████████████

def parametros():
    print('\n ■■■■■■■■■■■■■ EXPLICACION DE LOS PARAMETROS PASADOS A MYSTICA ■■■■■■■■■■■■■■')
    print(""" retorno = The_X_Men.mystyca(  
                            titulo          = Menu1, 
                            b_terminator    = True, 
                            tipo_index      = 'a', 
                            b_mode_all      = False, 
                            b_loop          = True , 
                            pad_x           = 50) 
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

def listar_procesos():
    global The_X_Men    
    print(f'{The_X_Men.listar_procesos()}')

def version_web():
    global The_X_Men    
    print(f'Accion version Web WIP')
    The_X_Men.get_web_lsts_lens_linea(titulo='Menu1',  tipo_index='a', b_mode_all=False, b_loop=True, pad_x=15)

def lanza_flask():
    print('LANZA FLASK')
    # from proyecto_final_v1 import funciones_tablas
    # from proyecto_final_v1.main import app as servidor_flask
    # servidor_flask.run()

def sobre_xindex():
    print(""" from classXindeX import XindeX          # ■ XINDEX A PELO
from classXindeX import Over_Main       # ■ PADRE DE XINDEX CON ■ COLOR EN HEAD Y PIE  ■ BEGIN ** ■ LANZAR DEMONIO << >> ■ LANZA BACKGROUND => 
from Sdata import Sdata                 # ■ AYUDA PARA EL OVER-MAIN PARA PEDIR DATOS SEGUROS AL USUARIO

def main():
    # ■■■■■■ INSTANCIO EL OBJETO ■■■■■■

    The_X_Men = Over_Main(tipo_index='a', b_mode_all=False, b_loop=True )
    
    
    # ■■■■■■ ADD UN MENU CON ITEMS Y FUNCIONES Y LE ASIGNA CONFIGURACION GENETICA(padre, ipadre) ■■■■■■
    
    Menu1 = The_X_Men.addX(titulo='Menu1', padre=None , ipadre=None, lst_items = [ ('Info XindeX' , None),('Procesos' , None))
    
    The_X_Men.addX( titulo='sub-Xindex' , padre='Menu1' , ipadre='Info XindeX' , lst_items = [ ('Sobre XindeX' , None) , ('Parametros Mystyca', parametros ) ] )    
    
    The_X_Men.addX( titulo='sub-Estilos', padre='sub-Xindex' , ipadre = 'Sobre XindeX' , lst_items = [ ("Ver Estilos", None) , ("Version Web" , version_web) ] )    
    
    The_X_Men.addX( titulo='sub-Procesos', padre='Menu1' , ipadre = 'Procesos' , lst_items = [ ("Listar Proceso", listar_procesos) , ("Lanzar Proceso" , None) ])    

    
    # ■■■■■■ LLAMO A MYSTYCA PARA VISUALIZAR EL MENU ■■■■■■■■■■■                               
    
    retorno = The_X_Men.mystyca( titulo='Menu1', head_datapush  = 'XINDEX - OVER-MAIN' , pad_x=5 )
""")

def from_to():
    global The_X_Men    
    sdata = Sdata.get_data(key_dict='FD', tipo=int, msg_entrada='INTRO FILA-DESDE: ', permite_nulo=False)
    sdata = Sdata.get_data(key_dict='FH', dicc=sdata, tipo=int, msg_entrada='INTRO FILA-HASTA: ', permite_nulo=False)
    print(f'FROM {sdata["FD"]} TO {sdata["FH"]}')
        
    The_X_Men.F_RANK_Y.imprimir(sp_between = 2, ancho_columna = None, fila_from=sdata['FD'], fila_to=sdata['FH'] )

# ████████████████████████████████████████████ INICIO ███████████████████████████████████████████████
# ████████████████████████████████████████████ INICIO ███████████████████████████████████████████████

if __name__ == "__main__":
    # ---- Limpio la terminal 
    os.system('cls')    
    # ---- Empezamos!!
    main() 
