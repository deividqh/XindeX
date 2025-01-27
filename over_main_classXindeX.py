import os           
from enum import Enum

import tkinter as tk
import threading

from classXindeX import XindeX 
# from classXindeX import Over_Main
# from fromdvd.classMenuDvd.classMotorMain import Over_Main

# ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
# DEF: CREA UN INDICE MULTINIVEL CON GENETICA QUE EJECUTA LAS FUNCIONES ASOCIADAS A CADA MENU
# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# XindeX es el menu que ejecuta las siguentes acciones sobre las funciones: Repetir('<') , Salir ('<<<') , Info('?') 
# Over_Main amplia la funcionalidad de XindeX para ejecutar funciones en background e interactivas.


# ═════════════════════════════════
# ═════════════════════════════════
# ═════════════════════════════════
def main():
    # ▄▄▄▄▄▄▄ 1- INSTANCIO EL OBJETO ::: 
    # The_X_Men = Over_Main()
    The_X_Men = XindeX()


    # ▄▄▄▄▄▄▄ 2- CREO LOS MENUS Y SUS FUNCIONES ASOCIADAS :::
    list_Main = [ ("XindeX" , None), ("Hilos" , None),("Flask" , None), ("BBDD" , f_cajas)              ]
    Menu1=The_X_Men.addX(titulo='Menu1', lst_items=list_Main, fraseHead="| - M A I N M E N U - ")
    # ______________________
    lst_menu=[  ("Ejecutar Servidor",ejecutar_servidor), ("Ver Servidor",ver_servidor), ("Parar Servidor", None) ]
    The_X_Men.addX(titulo='subFlask', lst_items=lst_menu)
    # ______________________
    lst_menu=[  ("Estilos e Info", func1 ), 
                ("Mode Exec Finals", None ), 
                ("Alfabeto A" ,None ),("Alfabeto 1",None),("Alfabeto A1", None ),
                ("Guardar Menu BBDD" , guardar_menu )
                ]
    The_X_Men.addX(titulo='subXindex', lst_items=lst_menu)
    # ______________________
    lst_menu=[  ("Ver Hilos", None) , ("Detener Hilos", None), ("Ejecutar Funcion" , None) ]                  
    The_X_Men.addX(titulo='subHilos', lst_items=lst_menu)    
    
    # ______________________
    lst_menu=[  ("Guardar Menu BBDD", None) , ("Lanzar Flask", lanza_flask) ]                  
    The_X_Men.addX(titulo='subNivel', lst_items=lst_menu)    

    # ▄▄▄▄▄▄▄ 3- COFIGURO LA GENETICA DEL INDICE ::: 
    The_X_Men.config(titulo='Menu1'     , suPadre=None     , indexInPadre = None )
    The_X_Men.config(titulo='subFlask', suPadre='Menu1'  , indexInPadre='Flask' )
    The_X_Men.config(titulo='subXindex', suPadre='Menu1'  , indexInPadre='XindeX' )    
    The_X_Men.config(titulo='subHilos', suPadre='Menu1', indexInPadre='Hilos' )
    The_X_Men.config(titulo='subNivel', suPadre='Menu1', indexInPadre='BBDD' )





    # ▄▄▄▄▄▄▄ 4- LLAMO A MYSTYCA PARA VISUALIZAR EL MENU :::
    retorno = The_X_Men.Mystyca(titulo='Menu1', configurado=True, execFunc=True, tipo_marcador='a', execAll=False, Loop=True , padX=50)
    # [titulo]      = Id del Menu Añadido/Configurado/Mostrados sus Items.
    # [execFunc]    = True  ::: Cuando sale de aquí ya se ha ejecutado la funcion del menu.....lleve donde lleve, pero tiene que estar  
    #                 False ::: Se retorna a main la respuesta.
    # [configurado]  = True  ::: Con La configuracion previa | False ::: Muestra Menu Simple Numerico.
    # [tipo_marcador] = '1'   ::: Numerico(byDef) | 'a' ::: Alfabetico Min | 'A' ::: Alfabetico May  | 'A1', '1A', a1, 1a ::: Mixto
    # [execAll]    = True  ::: Solo se ejecutan ( o solo es opcion valida) los subMenus Finales (no padres) 
    #                 False ::: Se ejecuta ( o  solo es opcion valida) todo lo que no sea None en func.
    #                 si execFunc == False ::: No iterfiere pq refleja las opciones validas indmnt de si se ejecuta o se retorna. 
    # [Loop]        = True  ::: Se auto-e<<jecuta hasta que <<<. | False ::: Se ejecuta 1 vez y sale a main.   
    """ Ejemplos:
    >>>  retorno = The_X_Men.Mystyca(titulo='Menu1', execAll=False, Loop=True)
    >>>  retorno = The_X_Men.Mystyca(titulo='Menu1', configurado=True, execFunc=True )
    >>>  retorno = The_X_Men.Mystyca(titulo='Menu1', configurado=True, execFunc=True, tipo_marcador='1', execAll=False, Loop=True) """
    
    # ▄▄▄▄▄▄▄ 5- RETORNO DE MYSTYCA
    print(f"::: T H E   E N D  en MAIN() ::: {retorno if retorno else 'no retorno'} ")

# ==========================================================        
# ==========================================================        
# ==========================================================      
def func1():    print('soy func1')
def func2():    print('soy func2')
def func3():    print('soy func3')
def func4():    print('soy func4')
def func5():    print('soy func5')
def func6():    print('soy func6')
def func7():    print('soy func7')

# _____________________
def f_cajas():
    print('\nC a j a s ')
def ejecutar_servidor():
    print("\nE j e c u t a r   S e r v i d o r   F l a s k ")
# _____________________
def ver_servidor():
    print("\nV e r   S e r v i d o r   F l a s k ")

def guardar_menu():
    print('G u a r d a r   M e n u ')

def lanza_flask():
    print('L a n z a   F l a s k ')
    
    # from proyecto_final_v1 import funciones_tablas
    # from proyecto_final_v1.main import app as servidor_flask
    # servidor_flask.run()



""" 
>>> Las funciones tienen que estar definidas para poder ser pasadas al menu 
    Desde las funciones puedes importar y ejecutar cualquier programa o codigo.
    Ademas se tienen que ejecutar en hilos separados unos de otros y controlados desde Over_Main o hilo principal.
"""


# ==========================================================        
# ==========================================================        
# ==========================================================      
if __name__ == "__main__":
    # ---- Limpio la terminal 
    os.system('cls')    
    # ---- Empezamos!!
    main() 
