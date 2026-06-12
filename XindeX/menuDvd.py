# Llamada a una funcion desde otro archivo:
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# from ..dvd import RAM
# result= RAM.MenuLista(menu)    

# import os           #Para Limpiar la terminal con  os.system('cls') 
# import  menuDvd     #Funcion que crea un menu y devuelve un int(opcion)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Para añadir ejercicios al menu, En el archivo que usO el Menú.
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

# • • • • • • • • • DEFINICION FUNCIONES • • • • • • • • •
# def ejer01():
#     print('Ejercicio 1')
# def ejer02():
#     print('Ejercicio 2')

# • • • • • • • • • CREACION DEL MENU • • • • • • • • •
# menu={"Ejercicio_1": ejer01, "Ejercicio_2":ejer02 }
# while (True):
#     i=menuDvd.MenuDiccionario(menu, tituloMenu='Menu de Ejercicios')
#     if i==0: 
#       break  # PRIMERO LA DE SALIDA
#     for idx , ejer in enumerate(menu):
#         if i==idx+1:
#             os.system('cls')
#             menu[ejer]()
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


# ----------MENU BASIC--------------
# menu=["SALIR", "XXX", "YYY"]
def MenuLista(menu, tituloMenu, num_char=40,char_1='■', char_2='•', char_3='■'):
    salir=["SALIR"]
    menu=salir+menu    
    # Imprime Menu:
    # print('\n'+char_1*40+'\n'+tituloMenu+'\n'+char_2*40)
    print(f'\n{char_1*num_char}\n{tituloMenu}\n{char_2*num_char}')
    for index,opc in enumerate(menu):
        print (f'{index}....{opc}')
    print (f'{char_3*num_char}')    
    
    while(True):
        # Selecciona Opcion:
        i=input("Intro opcion • • •  ")    
        # Si todo lo introducido en la cadena son digitos = True
        if i.isdigit():
            i=abs(int(i))
            if i==0: 
                return None
            if i > len(menu): 
                continue
            else:                
                return i
        else:
            continue
    

def MenuDiccionario(menu, tituloMenu, num_char=40,char_1='■', char_2='•', char_3='_', texto_exit=None):
    from colorama import Fore, Back, Style, init

    if not isinstance( menu , dict ): 
        return -1

    if texto_exit:
        salir={texto_exit: 0}
    else:
        salir={"❌ SALIR | '-' clear": 0}
    
    # Asi puedes adjuntar por el principio (y recibir en una funcion) un diccionario(**), una lista se envia así(*)
    menuSalir = {**salir, **menu}
    menu = menuSalir    # menu entra por Referencia, cambia en la funcion que lo llama tb. 
    
    # Imprime Menu:    
    print(f'\n{Fore.CYAN}{char_1*num_char}{Style.RESET_ALL}')
    print(f'{tituloMenu}')
    print(f'{char_2*num_char}')
    for index,tit in enumerate(menuSalir):
        print (f'{index}....{tit}')
    print (f'{char_3 * num_char}')
    
    # Selecciona Opcion:
    i = input("Intro opcion __ ")
    if i.isdigit():
        i=abs(int(i))
    else:
        if i=='-':
            import os
            os.system('cls')
        else:
            return -1

    return i

def MenuDvd(menu, tituloMenu="M E N U", num_char=40, char_1='_', char_2='*', char_3='-'):
    if isinstance(menu, list):        
        return MenuLista(menu, tituloMenu, num_char=num_char, char_1=char_1, char_2=char_2, char_3=char_3)
    elif isinstance(menu,dict):
        return MenuDiccionario(menu, tituloMenu)