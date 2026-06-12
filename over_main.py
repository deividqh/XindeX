# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
from XindeX.classXindeX import Over_Main       # ■ PADRE DE XINDEX CON ■ COLOR EN HEAD Y PIE  ■ BEGIN ** ■ LANZAR DEMONIO << >> ■ LANZA BACKGROUND => 
# from XindeX.Sdata import Sdata                 # ■ AYUDA PARA EL OVER-MAIN PARA PEDIR DATOS SEGUROS AL USUARIO
from colorama import Fore, Style, init  # ■ COLORAMA PARA COLORES EN TERMINAL....por si se quiere usar colores para 'ayudas'
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import os               # SISTEMA OPERATIVO(PARA LIMPIAR LA TERMINAL)
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import multiprocessing  # PARA PROCESOS EN BACKGROUND Y DEMONIOS
# ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
import funciones_over_main as cmd   # ■ (Opt)FUNCIONES ASOCIADAS A LOS ITEMS DE LOS MENUS, SE DEFINEN EN ESTE ARCHIVO PARA SIMPLIFICAR LA LECTURA DE ESTE ARCHIVO PRINCIPAL Y PARA QUE LAS FUNCIONES PUEDAN ACCEDER AL OBJETO MENU PRINC

# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# ████████████████████████████████████████████ XINDEX ███████████████████████████████████████████████
# DEF: CREA UN INDICE MULTINIVEL CON GENETICA QUE EJECUTA LAS FUNCIONES ASOCIADAS A CADA MENU
# ████████████████████████████████████████████ XINDEX ███████████████████████████████████████████████

# INSTANCIO EL OBJETO ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
The_X_Men = Over_Main(tipo_index='a', b_mode_all=True, b_loop=True )


# ( Opt ) Tiene que haber un The_X_Men declarado global en funciones_over_ma
cmd.The_X_Men = The_X_Men

def main():
    # ■- CREO LOS MENUS Y SUS FUNCIONES ASOCIADAS ▄▄▄▄▄▄▄▄▄▄▄▄
    Menu1 = The_X_Men.addX(titulo='Menu1', padre=None , ipadre=None, 
                    lst_items = [   ("Info XindeX" , None), 
                                    ("Estilos" , None),
                                    ("Procesos" , None), 
                                    ("From-To" ,  cmd.from_to) ] )
    
    The_X_Men.addX( titulo='sub-Xindex' , padre='Menu1'   , ipadre="Info XindeX", 
                    lst_items = [   ("Sobre XindeX" , None) , 
                                    ("Parametros Mystyca", None ), 
                                    ("Ejemplos Uso" , None ) ] )    
    
    The_X_Men.addX( titulo='sub-Estilos', padre='Menu1'   , ipadre='Estilos'    , 
                    lst_items = [   ("Ver Estilos", None) , 
                                    ("Version Web" ,  cmd.version_web) ] )    
    
    The_X_Men.addX( titulo='sub-Procesos', padre='Menu1'  , ipadre=2   , 
                    lst_items = [   ("Listar Proceso",  cmd.listar_procesos) , 
                                    ("Lanzar Proceso" ,  cmd.lanzar_proceso), 
                                    ("Detener Proceso" , None) , 
                                    ('OS procesos',  cmd.subprocess_os)] )    
    
    The_X_Men.addX( titulo='sub-Aux', padre='sub-Estilos' , ipadre='Ver Estilos', 
                    lst_items = [   ("Switch b_mode_all",  cmd.set_style), 
                                    ("Cambiar Estilo Marco" ,  cmd.cambiar_estilo_marco), 
                                    ("aux 3" , None) ] )    
    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ FORMA LARGA Y MAS ANTIGUA.
    # ■ AÑADE Y CONFIGURA - es el camino largo... o por partes.
    # The_X_Men.addX(titulo='subXindex', lst_items=[ ("Info Inicial" , None) ,  ("Configuracion XindeX", None ), ("Explicacion Parametros", parametros ), ("Ejemplos Uso" , None ) ])
    # The_X_Men.config(titulo='subXindex' , suPadre='Menu1' , indexInPadre='Info XindeX' )    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # ■ LLAMO A MYSTYCA PARA VISUALIZAR EL MENU ■■■■■■■■■■■                               
    retorno = The_X_Men.mystyca( titulo='Menu1', head_datapush  = " XINDEX - OVER-MAIN " , pad_x=5 )

    # 5- RETORNO DE MYSTYCA ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    print(f"::: T H E   E N D  en MAIN() ::: {retorno if retorno else 'no retorno'} ")


# ████████████████████████████████████████████ FUNCIONES DEFINIDAS EN XINDEX ███████████████████████████████████████████████
# ████████████████████████████████████████████ FUNCIONES DEFINIDAS EN XINDEX ███████████████████████████████████████████████



# ████████████████████████████████████████████ INICIO ███████████████████████████████████████████████
# ████████████████████████████████████████████ INICIO ███████████████████████████████████████████████

if __name__ == "__main__":
    multiprocessing.freeze_support()    # PARA QUE FUNCIONE CORRECTAMENTE EN WINDOWS LA CREACION DE PROCESOS HIJOS (BACKGROUNDS O DEMONIOS)    
    os.system('cls')                    # ---- Limpio la terminal 
    # ---- Empezamos!!
    main() 
