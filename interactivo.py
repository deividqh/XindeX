from classXindeX import Over_Main
import os
import multiprocessing

def ejer_m1_1():
    print(f"\nEjercicio 1 ")
def ejer_m1_2():
    print(f"\nEjercicio 2 ")
def ejer_m1_3():
    print(f"\nEjercicio 3 ")

# ■ ■ ■ ■ ■ Para hacer un menu interactivo 
# desde el menú principal se crean los items que llaman a una funcion dedicada (m1, m2, m3).
# en cada funcion(m1, m2, m3) se crea un nuevo Over_Main que tiene los diferentes items.

# ■ ■ ■ ■ ■ Si se quiere un menu con 3 módulos, cada módulo con 10 ejercicios, se deben 
# crear 1 menu principal over_main + 3 submenus over_main tambien  + 30 items, 

# ■ ■ ■ ■ ■ Pongo los mismos ejercicios para simular los 3 módulos, pero deben ser distintos
# ■ ■ ■ ■ ■ y en otro archivo. .. pero para simularlo, los pongo iguales.


def m1():
    xm1 = Over_Main(tipo_index='a', b_mode_all=False, b_loop=True)
    xm1.addX( titulo='M1', padre=None, ipadre=None, 
                    lst_items=[ ('ejer_m1_1', ejer_m1_1), 
                                ('ejer_m1_2', ejer_m1_2), 
                                ('ejer_m1_3', ejer_m1_3), 
                            ])
    xm1.mystyca( titulo='M1', head_datapush="Ejercicios del Módulo 1", pad_x=15 )

def m2():
    xm1 = Over_Main(tipo_index='A', b_mode_all=False, b_loop=True)
    xm1.addX( titulo='M2', padre=None, ipadre=None, 
                    lst_items=[ ('ejer_m2_1', ejer_m1_1), 
                                ('ejer_m2_2', ejer_m1_2), 
                                ('ejer_m2_3', ejer_m1_3), 
                            ])
    xm1.mystyca( titulo='M2', head_datapush="Ejercicios del Módulo 2", pad_x=15 )

def m3():
    xm1 = Over_Main(tipo_index='1', b_mode_all=False, b_loop=True)
    xm1.addX( titulo='M3', padre=None, ipadre=None, 
                    lst_items=[ ('ejer_m3_1', ejer_m1_1), 
                                ('ejer_m3_2', ejer_m1_2), 
                                ('ejer_m3_3', ejer_m1_3), 
                            ])
    xm1.mystyca( titulo='M3', head_datapush="Ejercicios del Módulo 3", pad_x=15 )


def main():
    NUM_MODULOS = 16 
    EJERCICIOS_POR_MODULO = 10
    
    The_X_Men = Over_Main(tipo_index='a', b_mode_all=False, b_loop=True)
    
    The_X_Men.addX( titulo='Menu_Principal', padre=None, ipadre=None, 
                    lst_items=[ ('Mod1', m1), 
                                ('Mod2', m2), 
                                ('Mod3', m3), 
                            ])

    # ■ 2. SUBMENÚS CON LA GENÉTICA CONECTADA
    # for i in range(1, NUM_MODULOS + 1):
    #     nombre_modulo = f"Modulo {i}"        
    #     items_sub = [(f"Ejercicio {j}", ejecutar_ejercicio) for j in range(1, EJERCICIOS_POR_MODULO + 1)]
    #     The_X_Men.addX( titulo=f'Submenu_Mod_{i}', padre='Menu_Principal',  ipadre=nombre_modulo,    
    #                     lst_items=items_sub)

    # ■ 3. LANZAR EL ENTORNO
    The_X_Men.mystyca( titulo='Menu_Principal', head_datapush="SELECCIONA UN MÓDULO", pad_x=5 )


if __name__ == "__main__":
    multiprocessing.freeze_support()
    os.system('cls' if os.name == 'nt' else 'clear')    
    main()