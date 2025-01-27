import os
import re

""" 
    VARIABLES GLOBALES Y CONSTANTES 
"""
        #Cte para cuando se pide la opcion al usuario.
SALIR='<<<'
REPETIR='<'
from enum import Enum as Column
class COL(Column):    
    SP_I    = 0 ; A = 0      # Espacio Inicial
    X__NUM  = 1 ; B = 1      # Pre-num
    NUM     = 2 ; C = 2      # Num
    NUM__X  = 3 ; D = 3      # Pos-num
    __TAB   = 4 ; E = 4      # TAB
    X__ITEM = 5 ; F = 5      # Pre-Item
    ITEM    = 6 ; G = 6      # Item
    ITEM__X = 7 ; H = 7      # Pos-Item
    SP_F    = 8 ; I = 8      # Espacio Final

# ============================================================================================
# ============================================================================================
class MenuDvd():
    """ 
    Def: Define las partes esenciales de un menu Simple:  Head | Titulo | Cuello | Filas Body | Pie    
    Fila Body:  X_n__ | __n__ | __n_X | X_item__ | item | __item_X 
    """
    __TAB='    '
    __OPT=''
    CHAR_HEAD='-' 
    CHAR_CUELLO='-' 
    CHAR_PIE='-'
    NUM_CHAR=40                     
    X__NUM=''
    NUM__X='' 
    X__ITEM='' 
    ITEM__X=''

    def __init__(self, titulo, lst_item, lst_func=None, fraseHead=''):               
        """ RECOGE LOS VALORES """
        self.titulo     = titulo      # El titulo e indice del menu. aparece por defecto en el HEAD es el id del menu.
        self.lst_item = lst_item      # cada item(str) es el contenido del Menu. CUERPO 

        """ 
        Si no pasas lst_func (las funciones de cada item), las inicializo a None....don't worry :) """
        if lst_func==None:
            self.lst_func=[None for i in range(len(self.lst_item))]
        else:
            self.lst_func   = lst_func              # La funcion que se pasa asociada por posicion al Item de lst_item
        
        """ 
        La Frase Que se pone en la Impresion del Menu(Por defecto, el Titulo): """
        self.fraseHead = fraseHead if fraseHead != '' else self.titulo
        
        """ 
        Caracteres iniciales de una Fila(Linea) """
        self.X__num  = ''       # (char), Lo que va ANTES del Index
        self.num__X  = ''       # (char), Lo que va DESPUES del Index
        self.X__item = ''       # (char), Lo que va ANTES del Item
        self.item__X = ''       # (char), Lo que va DESPUES del Item
        
        """ 
        Variables para el entorno(cabecera y pie) by Def. Se Cambian en self.style """        
        self.char_head  = '-'   # 1º (char) que se repite num_char veces. es el SOMBRERO
        self.char_cuello= '-'   # 2º (char) que se repite num_char veces. es la PAJARITA 
        self.char_pie   = '-'   # 2º (char) que se repite num_char veces. es el ZAPATOS
        self.num_char   = 40      # Numero de (char) que hay en una linea.

        """ 
        Longitud de una fila del menu. """
        self.total_length = 0             
        
        """ 
        Mensaje Unico de pedida de dato al usuario """
        self.introData = '\nIntro Opt (XindeX)..... '     
        
        """ 
        GENERA EL ENTORNO: La linea de CABECERA - CUELLO - PIE """        
        self.sombrero = f'\n{ self.char_head * self.num_char }'
        self.cabeza = f'{self.fraseHead }'
        self.cuello = f'{self.char_cuello * self.num_char }'
        self.pie = f'{self.char_pie*self.num_char}'
        
        """ 
        GENERA LA LISTA DE NUMERACION """
        self.lst_numeracion_rltv=[i for i in range(len(self.lst_item))]
        
        """ 
        CARGA LAS LISTAS DE BEFORE-AFTER """
        self.lst__X_num=[]           #Lista de los caracteres que van antes del Numero del item.
        self.lst__num_X=[]           #Lista de los caracteres que van depues del Numero del item.
        self.lst__X_item=[]     #Lista de los caracteres que van antes del Item
        self.lst__item_X=[]     #Lista de los caracteres que van Despues del Item        
        for i in range(len(lst_item)):
            self.lst__X_num.append(self.X__num)
            self.lst__num_X.append(self.num__X)
            self.lst__X_item.append(self.X__item)
            self.lst__item_X.append(self.item__X)
        # ___________________________________________________
        """ VALIDACION DE TAMAÑO DE LISTAS. IGUALAR TODAS A:  self.lst_item       """
        self.igualarListas(listaKeys=self.lst_item, listaToReLong=self.lst_func)
        self.igualarListas(listaKeys=self.lst_item, listaToReLong=self.lst_numeracion_rltv)
        # Entorno____________
        self.igualarListas(listaKeys=self.lst_item, listaToReLong=self.lst__X_num)
        self.igualarListas(listaKeys=self.lst_item, listaToReLong=self.lst__num_X)
        self.igualarListas(listaKeys=self.lst_item, listaToReLong=self.lst__X_item)
        self.igualarListas(listaKeys=self.lst_item, listaToReLong=self.lst__item_X)        
        # __________________________________
        """ GENERACION DEL DICCIONARIO  """        
        # Itrtr_valor_dicc = tuple(zip(self.lst_item, self.lst_func))            
        """ >>> 1º ==> Creo una tupla con el par lst_item, lst_func xa formar el self.dicc_menu
        """
        # val_dicc_menu={self.lst_numeracion_rltv[i]:valor_dicc  for i, valor_dicc in enumerate(Itrtr_valor_dicc)}                                          
        """ >>> 2º ==> { 2 : ( 'Sales' , compraProd ) } ==> (2) numeracion ('Sales') titulo-menu (compraProd) funcion sin parentesis
        """        
        # self.dicc_menu={self.titulo:val_dicc_menu}

        self.dicc_menu=dict(zip(self.lst_item, self.lst_func))
        """ 3º ==> D I C C I O N A R I O R E S U L T A D O 
        >>> {'Titulo Menu':  { : ( 'item_1_menu' , func_item_1 ) } }   ==> Se genera 1 por Menu. 
        Es de donde tiene que coger self.Terminator la informacion para ejecutar al funcion."""
        
        # print(self.dicc_menu)
        # __________________________________
        """ GENERACION DE LA LINEA DE SALIR  """        
        self.salir=self.get_row_Salir()
    
    def __str__(self):                
        return self.F_r_a_n_k_Y(bSalir=True, bCabeza=True, bCuerpo=True, bPie=True, esNumerado=True)
    # ____________________________________
    # VALIDA LA ESTRUCTURA DE ENTRADA (...llamada desde AddX)
    def valid_unpack(self, lst_items):
        """  
        >>> Opcion 1:
        lst_titulos = ["Tit-1", "Tit-2" , "Tit-3" ]
        lst_FNC    = ["func-1", "func-2" , "func-3" ]

        >>> Opcion 2:
        lst_titulos    = [ ('Tit-1',func-1), ('Tit-2', func-2) , ('Tit-3', func-3) ]
        """
        lst_ITM = []
        lst_FNC = []
        try:
            if isinstance(lst_items, list) or isinstance(lst_items, tuple):                
                for titulo, funcion in lst_items:
                    """ TITULO """
                    if not isinstance(titulo, str): 
                        print(f'Error en la Estructura de {lst_items} \nLos titulos deben ser String....revisa por favor ')
                        return None, None
                    else:
                        lst_ITM.append(titulo)
                    """ FUNCION """
                    if not callable(funcion):       # VALIDA FUNCION
                        if funcion != None:         # PERMITE NONE
                            return None, None
                        else:
                            lst_FNC.append(None)    
                    else:
                        lst_FNC.append(funcion)
            else:
                return None, None
            
            return lst_ITM, lst_FNC
        except:
            return None, None
        pass
    # ____________________________________________________________________
    # CAMBIA EL ESTILO(CARACTERES DE CABECERA, PIE, PRE-NUM , POST-NUM)
    def style(self, char_head= CHAR_HEAD, 
                    char_cuello=CHAR_CUELLO , 
                    char_pie=CHAR_PIE       , 
                    num_char= NUM_CHAR      , 
                    X__num   = X__NUM         ,
                    num__X   = NUM__X         , 
                    X__item= X__ITEM      ,
                    item__X= ITEM__X      ,
                    introData='\nIntro Opt (XindeX)..... '):

        # Asigna los nuevos valores_________________
        if char_head:   self.char_head  = char_head
        if char_cuello: self.char_cuello= char_cuello
        if char_pie:    self.char_pie   = char_pie        
        if num_char:    self.num_char   = num_char
        if X__num:       self.X__num      = X__num
        if num__X:       self.num__X      = num__X
        if X__item:    self.X__item   = X__item
        if item__X:    self.item__X   = item__X
        if introData:   self.introData  = introData
        # Inicia____________________________
        self.lst__X_num      = []
        self.lst__num_X       = []
        self.lst__X_item   = []
        self.lst__item_X    = []
        # Reset de los lst_______________________
        for i in range(len(self.lst_item)):
            self.lst__X_num.append(self.X__num)
            self.lst__num_X.append(self.num__X)
            self.lst__X_item.append(self.X__item)
            self.lst__item_X.append(self.item__X)
        # Reset de la cabecera y pie __________________
        # self.cabecera, self.pie = self.formar_entorno()
        self.sombrero, self.cabeza, self.cuello, self.pie = self.formar_entorno()
    # ___________________
    # Retorna 4 espacios
    def get_TAB(self):
        return self.__TAB
    # ___________________________
    # STRING DEL CUERPO EN LINEA
    def get_str_Body(self, esNumerado=True):
        """ >>> Def: Devuelve una cadena de impresion con el menu. un menu con cabecera, cuerpo y pie.
        [esNumerado]: Si quieres un menú numerado o no.
        """
        # if bVertical==True:
        #     saltoLinea='\n'
        # else:
        #     saltoLinea=''
        cuerpo=f''
        for i,item_menu in enumerate(self.lst_item):      
            cuerpo += (f'{ self.lst__X_num[i] if esNumerado==True else '' }')                # 'Opt-'
            cuerpo += (f'{ self.lst_numeracion_rltv[i] if esNumerado==True else '' }')            # 1            
            cuerpo += (f'{ str(self.lst__num_X[i]) if esNumerado==True else '' }')            # '-'
            cuerpo += (f'{ str(self.lst__X_item[i]) if self.lst__X_item[i] else '' }')    # TAB('    ')
            cuerpo += (f'{item_menu}')                                                      # 'Casa'
            cuerpo += (f'{ str(self.lst__item_X[i]) if self.lst__item_X[i] else '' }')      # __TAB + "Loren ipsum"
            """
             la última iteracion no imprime el \n """
            cuerpo += (f'{'\n'}')                        if i<(len(self.lst_item)-1) else ''
        pass        
        return cuerpo
    # ___________________________
    # DEVUELVE UNA FILA DEL MENU
    def get_strRow_Body(self, row, esNumerado=True):
        """ >>> Def: Devuelve una fila del menu. la que le pases. En formato f'' para poder ser impreso o .format()
        No incluye salir, Opt-0. La numeracion empieza en 1, pero la lista en 0 
        Opt-1-  Casa    Def:Loren ipsum
        """
        fila_menu=f''
        if 0 <= row < len(self.lst_item):
            for i , item_menu in enumerate(self.lst_item):            
                if i == row :
                    fila_menu += f'{ self.lst__X_num[i]          if esNumerado==True else f'' }'         # 'Opt-'                   
                    fila_menu += f'{ self.lst_numeracion_rltv[i]     if esNumerado==True else f'' }'         # 1         
                    fila_menu += f'{ str(self.lst__num_X[i])      if esNumerado==True else f'' }'         # '-'
                    fila_menu += f'{ str(self.lst__X_item[i])  if self.lst__X_item[i] else f'' }'     # TAB('    ')
                    fila_menu += f'{ item_menu }'                                                       # 'Casa'
                    fila_menu += f'{ str(self.lst__item_X[i])   if self.lst__item_X[i] else f'' }'      # TAB + 'Def: Loren ipsum'
                    
                    return fila_menu
            pass
        pass
    # ____________________
    # El item de una fila
    def get_item_row_body(self, row):
        """ >>> Def: Devuelve el ITEM de una fila  """
        fila_menu=f''
        if 0 <= row < len(self.lst_item):
            for i , item_menu in enumerate(self.lst_item):            
                if i == row :
                    return f'{ item_menu }'      
        # ____________________
    # El item de una fila
    def get_numRltv_row_body(self, row):
        """ >>> Def: Devuelve el ITEM de una fila  """
        fila_menu=f''
        if 0 <= row < len(self.lst_item):
            for i , numRltv in enumerate(self.lst_numeracion_rltv):            
                if i == row :
                    return f'{ numRltv }'                    
    # ____________________________________________
    # DEVUELVE UNA FILA DEL MENU En formato lista
    def get_lst_row_body(self, row, esNumerado=True):
        """ >>> Def: Devuelve una fila del menu. la que le pases. En formato f'' para poder ser impreso o .format()
        No incluye salir, Opt-0. La numeracion empieza en 1, pero la lista en 0 
        Opt-1-  Casa    Def:Loren ImprSkinpsum
        """
        fila_menu=[]
        if 0 <= row < len(self.lst_item):
            for i , item_menu in enumerate(self.lst_item):            
                if i == row :
                    fila_menu.append ( f'{ self.lst__X_num[i]           if esNumerado==True else f'' }')
                    fila_menu.append ( f'{ str(self.lst__num_X[i])      if esNumerado==True else f'' }')
                    fila_menu.append ( f'{ self.lst_numeracion_rltv[i]  if esNumerado==True else f'' }')
                    fila_menu.append ( f'{ str(self.lst__X_item[i])     if self.lst__X_item[i] else f'' }')
                    fila_menu.append ( f'{ item_menu }')                                                  
                    fila_menu.append ( f'{ str(self.lst__item_X[i])     if self.lst__item_X[i] else f'' }') 
                    fila_menu.append ( f'') 
                    
                    return fila_menu
            pass
        pass
    # ______________
    # FILA DE SALIR
    def get_row_Salir(self):
        salir =  f'{ self.lst__X_num[0] }'      # 'Opt-' SALIR Siempre es numerado y se pone la de todos
        salir += f'{'| (Salir).... <<<   |   (Help).... ?   |  (Repeat).... < ' }'  # 'SALIR'
        salir += f'{ self.lst__num_X[0] }'      # '-' SALIR Siempre es numerado y se pone la de todos
        salir += f'{ MenuDvd.__TAB }'           # TAB('    ')
        salir += f'{''}'                        # ZERO ( 0 )
        salir += f'{MenuDvd.__TAB}'             # Explicativo. se puede omitir.
        salir += f'{''}'                        # Lugar de la funcion para devolver el formato de 7

        return salir
    # _____________
    # CABEZA Y PIE
    def formar_entorno(self):
        """ Crea los str de lo que no es body """
        sombrero=f'\n{ self.char_head * self.num_char }'
        cabeza=f'{self.fraseHead }'
        cuello=f'{self.char_cuello * self.num_char }'
        pie = f'{self.char_pie*self.num_char}'
        return sombrero, cabeza, cuello , pie
    # ______________________________________
    # DEVUELVE UNA MATRIZ DEL BODY DEL MENU con Tantas piezas como partes tenga la filaa.
    def get_matriz(self):
        lst_matriz=[]
        for i  in range(self.lst_item):            
            lst_matriz.append(self.get_lst_row_body(row=i, esNumerado=True))
        return lst_matriz
    # __________________
    # IGUALA LAS LISTAS
    def igualarListas(self, listaKeys, listaToReLong, valorRelleno='Loren'):
        """             
        Trata las longitudes de las listas y las igualo según listaKeys como referencia.
        La que se Re-dimensiona creciendo o decreciendo para igualarse con listaKeys.
        [valorRelleno]: en caso de que listaKeys>listaToRelong, hay que rellenar con un nuevo valor. en caso de funciones, None(by Def)
        [Ejemplo de uso]:
        >>> listTOdict_byTcld_ToString.igualarListas(listaKeys=listaKeys, listaToReLong=listaTipos)        
        listaKeys y listaTipos son inmutables, se pasan por referencia y no hay que retornar valor. Aun así se retorna
        """
        if len(listaKeys)==len(listaToReLong):
            return listaToReLong
        elif len(listaKeys)>len(listaToReLong):
            # print("long dicc > longTipo.....tipos hasta longTipo y luego Tipo=str y PERMITENULL=False")
            listaNewTipos=[valorRelleno for i, (k) in enumerate(listaKeys) if i >= len(listaToReLong)]
            listaToReLong = listaToReLong + listaNewTipos
            # print(listaToReLong)
        else:
            # print("long dicc < longTipo.....vale hasta la long del dicc- hay que reducir la dimension del la listaToReLong")
            longListaTipos = len(listaToReLong)
            longListaKeys  = len(listaKeys)
            for i in range(longListaKeys , longListaTipos ):
                listaToReLong.pop()

        return listaToReLong
        pass
    # _____________
    # INPUT SEGURO. ENTRA POR CONFIG
    def pide_data_usuario(self, menu_dvd):
        respuesta=None
        while(True):
            i=input(f"{self.introData}")    
            try:
                if i == SALIR:          # A PULSADO  '<<<' ....SALIR
                    return None
                if i.isdigit():
                    i=abs(int(i))
                    if i > len(menu_dvd.lst_item): 
                        continue
                    else:                                            
                        respuesta =  i
                        break
                else:
                    continue
            except Exception as e:
                print(e)
                continue
        pass
        return respuesta
    # _________________________________________
    # DEVUELVE LAS PARTES DEL MENU QUE QUIERAS
    def F_r_a_n_k_Y(self, bSombrero=False, bCabeza=False, bCuello=False, bSalir=False ,  bCuerpo=False, bPie=False, esNumerado=False):
        lst_franky=[]
        retorno = ''
        if bSombrero:   lst_franky.append( f'{self.sombrero}' )
        if bCabeza:     lst_franky.append( f'{self.cabeza}' )
        if bCuello:     lst_franky.append( f'{self.cuello}' )
        if bSalir:      lst_franky.append( self.get_row_Salir() )       
        if bCuerpo:   
            for i in range(len(self.lst_item)):
                lst_franky.append(self.get_strRow_Body(row=i, esNumerado=True))
        if bPie:    lst_franky.append( self.pie )

        """ Juntamos todas las piezas reunidas """
        for i, parte_Franky in enumerate(lst_franky):
            retorno += str(parte_Franky)
            retorno += '\n' if i<(len(lst_franky)-1) else ''
        return retorno
    # __________________________________________________________________________________________________________
    # ESTATICA PARA CREAR MENUS RAPIDOS DE UNA LINEA PADRE Y DEVUELVE UN RESULTADO PARA SER RECOGIDO EN EL MAIN
    def MList(lst_item_menu, tituloMenu="M E N U", 
                msgItem='Intro Opcion...', 
                num_char=40,
                char_head='-', char_cuello='-', char_pie='-'):
        """ 
        Devuelve un lst_item_menu. Añade la opcion de salir.
        [lst_item_menu]: lista de str con los textos del lst_item_menu.

        """
        salir=["SALIR"]
        lst_item_menu=salir+lst_item_menu    
        # Imprime lst_item_menu:
        # print('\n'+char_head*40+'\n'+tituloMenu+'\n'+char_cuello*40)
        print(f'\n{char_head*num_char}\n{tituloMenu}\n{char_cuello*num_char}')
        for index,opc in enumerate(lst_item_menu):
            print (f'{index}....{opc}')
        print (f'{char_pie*num_char}')    
        
        while(True):
            # Selecciona Opcion:        
            i=input(f"{msgItem}")    
            # Si todo lo introducido en la cadena son digitos = True
            try:
                if i.isdigit():
                    i=abs(int(i))
                    if i==0: return None
                    if i>len(lst_item_menu): 
                        continue
                    else:                
                        return i
                else:
                    continue
            except Exception:
                continue
    # ________________________________
    # VALIDA LA ESTRUCTURA DE ENTRADA 
    def valida_estructura(listaTitulos, listaFunc):
        """  
        >>> Opcion 1:
        lst_titulos = ["Tit-1", "Tit-2" , "Tit-3" ]
        lst_func    = ["func-1", "func-2" , "func-3" ]

        >>> Opcion 2:
        lst_titulos    = [ ('Tit-1',func-1), ('Tit-2', func-2) , ('Tit-3', func-3) ]
        """
        try:
            if isinstance(listaTitulos, list) or isinstance(listaTitulos, tuple):
                for titulo in listaTitulos:
                    if not isinstance(titulo, str):
                        if isinstance(titulo, list)  or isinstance(titulo, tuple):
                            for titulo, funcion in listaDef:
                                if not isinstance(titulo, str):     # Obliga a Titulo String
                                    return False
                                if not callable(funcion):           # Obliga a Meter una funcion()
                                    if funcion != None:             # ... o None(en revision)
                                        return False
                                    pass
                                pass
                            pass
                        else:
                            return False
                    else:
                        return False
                    pass
                pass
            else:
                return False
        except:
            return False
        pass
        # Ahora validamos listaFunc(lista + funcion o None )
        try:
            if isinstance(listaFunc, list) :
                for funcion in listaFunc:
                    if not callable(funcion):
                        if funcion != None:             # ... o None(en revision)
                            return False
            else:
                return False
        except:
            return False
        pass

# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================

""" 
(*)Tipos de Menus que se intentan conseguir:
    -------------------------   head
    Menu1                       titulo
    -------------------------   cuello
    opt 1.....loren ipsum1  
        opt 1.1 loren ipsum_N
        opt 1.2 loren ipsum_M
    opt 2.....loren ipsum2
        opt 2.1 loren ipsum_U
        opt 2.2 loren ipsum_N
    opt 3.....loren ipsum3
    opt 4.....loren ipsum4
    _________________________   pie
    intro opcion:.....          
    -------------------------

    View(titulo, configurado=False, ExecFunc=False, bControl=False)

    -Muestra un Menu sencillo(configurado) y devuelve el control(ExecFunc) para que el usuario actue en el main(). se ejecuta sin hilos(bControl)
xxxxxxxxxxxxxxxxxxxxxxxxxxx otra opcion xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    Menu2
    -------------------------
    opt 1.....loren ipsum1
        opt 1.1 loren ipsum_N
            opt 1.1.1 loren ipsum_M
            opt 1.1.2 loren ipsum_U
    opt 2.....loren ipsum2
        opt 2.1 loren ipsum_U
        opt 2.2 loren ipsum_N
    opt 3.....loren ipsum3
    opt 4.....loren ipsum4
    _________________________
    intro opcion:..... 
    
    View(titulo, configurado=False, ExecFunc=True, bControl=False)
xxxxxxxxxxxxxxxxxxxxxxxxxx otra opcion xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    -------------------------
    Menu1
    -------------------------
    opt 1.....loren ipsum1
    opt 2.....loren ipsum2
    opt 3.....loren ipsum3
    opt 4.....loren ipsum4
    xxxxxxxxxxxxxxxxxxxxxxxxx
    intro opcion:.....  """        
from enum import Enum as TIT_FUNC
class Tit_Func(TIT_FUNC):
    TIT=0
    FUNC=1

from enum import Enum as MASTER_INDEX
class PADRE_IND(MASTER_INDEX):
    PADRE=0
    INDEX=1
""" 
>>> for tit_dicc, master_index in self.dicc_xgenx.items():
        if master_index[PADRE_IND.PADRE]==master_busca: pass
"""
from enum import Enum as TYPE_XINDEX
class TYPEX(TYPE_XINDEX):
    NUMERIC = 0
    ALF_MAX = 10
    ALF_MIN = 20
    MIXTO   = 30


class XindeX(MenuDvd):
    """ 
    >>> Def: Gestiona una lista de menus y sub menus y los muestra por Terminal.
    instancia: ElMenuXX=XindiceX()
    add:    Añade un menu con dos listas, una de Titulos y otra Opcional de funciones a Exec con cada titulo en 1:1
    cofig:  Configura la Escalera del Indice: Menu|Padre|indice_en_el_padre
    View:   Muestra un Menu: 1-Con Genetica/Sin Genetica, 2-Vuelve/Se Ejecuta 3-Control Sobre Estilos 4-
    """ 

    def __init__(self, esLoop=True):
        """ >>> Crea un menu Principal y gestiona una lista de menus secundarios que dependen del principal.
        [esLoop]: True=circular hasta Salida. | False=Sólo una ejecucion FALTA IMPLEMENTAR
        """        
        self.esLoop = esLoop    
        """ >>> Define si se sale por <<< o nos vale sólo para una ejecución...tb para definir mas adelante una última vuelta. 
        """
        self.pasos=0
        """ >>> Para las funciones recursivas Mystyca. Define las veces que se llama a la recursividad."""

        self.lst_menuXX=[]
        """ >>> Lista de objetos MenuDvd que mantiene un lst_item,  dicc_menu(num_n:[strMenu_n, func_n])  """

        self.lst_titulosXX=[]
        """ >>> Lista de titulos de menu introducidos. Me permite validar rapido  """

        self.lst_keys=[]
        """ >>> Lista de items de menu introducidos. Me permite validar rapido  """

        self.dicc_xgenx={}
        """ >>> diccionario que mantiene la genealogía de los menus. titulo:[master, index_en_master] ,  """

        self.lst_item_func=[]
        """ >>> diccionario que mantiene la genealogía de los menus. titulo:[master, index_en_master] ,  """

        self.lst_Lst_Valid_Opt=[]
        """ >>> Listado de la pareja (item_en_mystica, respuesta valida). Se tiene que pasar a Xavier_get_USUARIO()
        Modificada por tipo_xindex(Char o Num)"""

        self.lst_skin=[]
        """ La piel de Mystyca. Es la matriz a imprimir. lista de lista de str. Invocada desde Mystica en self.Mystica_Skin(). Funcion Recursiva """

        self.lst__men_itm_lev_ape_name_padr_ipadr=[]
        """ Los ojos de Mystyca. lista de lista de str. Invocada desde Mystica en self.Mystica_Eyes(). Funcion Recursiva """

        self.lst_Impresion = []
        """ Lista de String con la impresion final de Mystyca. """

        self.lst_opt_tipo_NUMERIC=[]
        self.lst_opt_tipo_ALF_MAX=[]
        self.lst_opt_tipo_ALF_MIN=[]
        self.lst_opt_tipo_MIXTO=[]
        """ TIPOS DE FORMATOS DE MENU.....  se forman en self.create_INDICEX()  """
        lst_INICIO = []
        lst_2SP = []
        lst_LEVEL = []
        lst_FIN = []
        lst_VACIO = []            

    # xxxxxxxxxxxxxxxxxxxxxxxxx
    # 1-AÑADE UN MENU AL GESTOR... en forma lst_items=[it1, it2, ...]  lst_func=[f1, f2, ....] (no usar) (Crea un MenuDvd)
    def add(self, titulo, lst_item, lst_func=None):     
        """  Crea un Objeto MenuDvd"""
        if titulo in self.lst_titulosXX: 
            return False
        try:
            new_menu=MenuDvd(titulo=titulo, lst_item=lst_item, lst_func=lst_func)
        except Exception as e:
            print(e)
            return None
        self.lst_titulosXX.append(titulo)
        self.lst_menuXX.append(new_menu)
        # print(f'Load Menu {titulo} Ok ;)')
        return new_menu
    
    # xxxxxxxxxxxxxxxxxxxxxxxxx
    # 1-AÑADE UN MENU AL GESTOR .... en forma (item_menu, funcion) (Crea un MenuDvd) (y si metes padre e ipadre se configura la genetica)
    def addX(self, titulo, lst_items=None, fraseHead='', padre=False, ipadre=None):             
        """ 
        [titulo]: Es el identificador del menu y sirve para la genetica.
        [lst_items]: (str, func) -> str es una cadena que será el texto en el menu. func puede ser None o el nombre de una funcion sin los parentesis.
        """
        # Desempaquetado:
        lst_itemX, lst_funcX = self.valid_unpack(lst_items=lst_items)
        if not lst_itemX and not lst_funcX:
            print(f'Error:: Estructura NO Valida: {lst_items} ')
            print(f'.... Recuerda: (item) Tiene que ser un String y de momento sin repetidos y (funcion) se escribe sin los parentesis y None es un valor Válido ')                
            return None
        """  """
        if titulo in self.lst_titulosXX: 
            return False
        try:
            new_menu=MenuDvd(titulo=titulo, lst_item=lst_itemX, lst_func=lst_funcX, fraseHead=fraseHead)
            """ >>> Se crea un objeto MenuDvd """
            # print(new_menu)
        except Exception as e:
            print(e)
            return None
        # ____________________________________________________________
        # Añade a la lista de titulos y a la lista de menus de XindeX
        self.lst_titulosXX.append(titulo)
        self.lst_menuXX.append(new_menu)
        print(f'Load Menu {titulo} Ok ;)', end=' | ')

        # ________________________________________________________________
        # >>> Code de: [padre] e [i_padre] como OPCIONALES
        # .... Sirve para llamar a config desde la addX !!!!!! Todo en 1.
        if padre==False:
            """ No introduce padre, no hago nada, salgo por donde vine """
            pass
        elif padre==None:
            if ipadre==None:
                """ es el Master"""
                self.config(titulo=titulo, suPadre=None, indexInPadre=None)
        elif isinstance(padre, str): 
            if padre not in self.lst_titulosXX: 
                """ No encontrado """
                pass
            else:
                """ Encontrado """
                if ipadre == None:
                    """ No Entra indice """
                    pass
                else:
                    """ Entra indice(num / str) """
                    self.config(titulo=titulo, suPadre=padre, indexInPadre=ipadre)
        # ______________
        # Retorno:
        return new_menu


    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    # 2-CONFIGURA LA RELACION PADRE HIJO(INDICE) DEL MENU         (dicc_xgenx)
    def config(self, titulo, suPadre=None, indexInPadre=None): 
        """ >>> Configura la relacion de los menus. 
        Maneja el dicc_xgenx que es el que gestiona la genealogía.
        """
        if not titulo in self.lst_titulosXX:   return None
        # ___________________________________________________
        # EN CASO DE QUE META UN INDICE DE CADENA DE TEXTO
        if isinstance(indexInPadre, str):
            b_match = False
            """ Puede ser que meta un item del menu al que quiere ir(item del padre) """
            menu_padre=self.get_menudvd(suPadre)
            if not menu_padre: return None
            for i, item_en_padre in enumerate(menu_padre.lst_item):
                if str(item_en_padre).strip().upper()==str(indexInPadre).strip().upper():
                    indexInPadre = i
                    b_match = True
                    break
            pass
            if b_match == False: return None
        """ 
        A N A L I S I S   D E   L A   G E N E T I C A  """
        # if isinstance(indexInPadre, int):
        if suPadre ==None and indexInPadre==None:
            self.dicc_xgenx[titulo]=['-', '-']
            """ Es un puro Master!!!  """

        elif suPadre == None and indexInPadre!=None:
            self.dicc_xgenx[titulo]=['-', '-']            
            """ Es un Master Fuerte pero confundido, le sobra el index """

        elif suPadre != None and indexInPadre==None:
            newIndex=self.busca_index_free(titulo_key=titulo, master_buscado=suPadre)            
            """ es un Sub Puro ????? esta machacando al anterior pq no da con el index libre"""
            if newIndex:
                self.dicc_xgenx[titulo]=[suPadre, newIndex]
            else:
                return False
        elif suPadre != None and indexInPadre!=None and str(indexInPadre).isdigit():
            """ es un Sub Selector Puro y machaca todo lo que pilla."""
            self.dicc_xgenx[titulo]=[suPadre, indexInPadre]
        else:
            """ Error No posible, pero lo dejo por legible.....o no ;) """        
        # else:
        #     return None
    # _______________________________________________       
    # RETORNA UN OBJ MENUDVD POR MEDIO DE SU TITULO             (obtiene el MenuDvd )
    def get_menudvd(self, titulo):
        """ >>> Retorna un objeto MenuDvd x su str titulo. """
        if titulo in self.lst_titulosXX:
            for menu in self.lst_menuXX:
                if str(menu.titulo) == str(titulo):
                    return menu
    # _________________
    # BUSCA INDEX FREE.                                         (Busca un indice libre)
    def busca_index_free(self, titulo_key,  master_buscado ):
        """ >>> Busca en el diccionario de configuracion << self.dicc_xgenx >> , un index libre(el siguiente). 
        Retorna: None si Error | indice para insertar si todo OK """
        lst_indexes=[]

        for tit_dicc, par_master_idx in self.dicc_xgenx.items():
            if master_buscado == par_master_idx[PADRE_IND.PADRE.value]:
                lst_indexes.append(par_master_idx[PADRE_IND.INDEX.value])
        
        # Cuando sale del bucle espero tener una lista de los index del master.
        if lst_indexes:
            try:
                max_index=max(lst_indexes)
                new_index=max_index+1
                if new_index>len(self.dicc_xgenx.keys()): 
                    return None
                return new_index
            except Exception as e:
                print(f'Error: {e} ')
                return None    
        else:
            return 1    #Todos los menus empiezan las opciones en 1 y el 0 es Salir.
    
    # 3-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    # MUESTRA UN MENU.....................  LLAMADA EXTERNA   (Imprime el menu con subMenus - Toma Control - Ejecuta Funciones)
    def Mystyca(self, titulo, configurado=False, execFunc=True, tipo_marcador=0, execAll=True, Loop=True, padX=30):
        """ 
        >>> [titulo]      = Id del Menu Añadido/Configurado/Mostrados sus Items.
        [execFunc]    = True  ::: Cuando sale de aquí ya se ha ejecutado la funcion del menu.....lleve donde lleve, pero tiene que estar  
                        False ::: Se retorna a main la respuesta.
        [configurado]  = True  ::: Con La configuracion previa | False ::: Muestra Menu Simple Numerico.
        [tipo_marcador] = '1'   ::: Numerico(byDef) | 'a' ::: Alfabetico Min | 'A' ::: Alfabetico May  | 'A1', '1A', a1, 1a ::: Mixto
            o bien: TIPEX.NUMERIC = 0 | TIPEX.ALF_MAX = 10 | TIPEX.ALF_MIN = 20 | TIPEX.MIXTO = 30
        ?????????????????????????????????????????????????????????
        [execAll] (bool) = True  ::: Solo se ejecutan ( o solo es OPCION-VALIDA) los subMenus Finales (no padres) 
            False ::: Se ejecuta ( o solo es opcion valida) todo lo que no sea None en func.
            si execFunc == False ::: No iterfiere pq execFunc se trata en Terminator y execAll se trata en Opcion_Valida. 
        [Loop] (bool) = True  ::: Se auto-ejecuta hasta que <<<. | False ::: Se ejecuta 1 vez y sale a main.
        [padX] (int)  = distancia entre el punto final del str del menu y el marco final.
        """    
        print('\nM Y S T Y C A')

        # Valida Titulo Repetido y Existencia en la genetica(Config)
        if self.validacion_show(titulo=titulo, configurado=configurado) == False : 
            print('Error en Títulos y/o Configuracion Genética')
            return None
        # mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
        menu_dvd=self.get_menudvd(titulo=titulo)
        """ C A C H A  EL  M E N U  mmmmmmmmmmmmmmm
        """
        # if configurado == True and self.get_lst_dict_hijosX(titulo=menu_dvd.titulo):        #  PRINT SUB-MENUS 
        if configurado == True:        #  PRINT SUB-MENUS 
            self.lst_keys    = self.Mystyca_Keys(menu_dvd = menu_dvd)
            """ >>> listado de los items que aparecen en el menu. en orden.  """          

            pass            
            lst_skin = self.Mystyca_Skin(menu_dvd=menu_dvd)
            """ >>> GENERA LA  M A T R I Z   D E   I M P R E S I O N   
            """
            if not lst_skin: return None               
            if lst_skin != self.lst_skin: self.lst_skin = lst_skin
            """ Si cambia de matriz, la asigna, si no, no hace nada. """

            # """ IIIIIIIIIIIIIIIIIIIIIIII - RCRSV - datos - IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
            self.lst__men_itm_lev_ape_name_padr_ipadr = self.mystyca_ScannerXgenX(menu_dvd=menu_dvd)            
            """ >>> IIIIIIIIIIIIIIIIIIIIIIIIII - CONFIGURACION DE MySTyCA - IIIIIIIIIIIIIIIIIIIIIIII
            """  
            # _______________________________________________
            self.lst_item_func = self.get_lst_item_funcion()
            """ >>> lista de diccionarios str_item:func_funcion (la funcion se asigna en el main.)"""

            """ ............. Imprime la lista...... solo en pruebas...... Borrar """
            # self.print_lst_List(lst_skin=self.lst__men_itm_lev_ape_name_padr_ipadr, numSP=12 , titulo = '\nMystyca  T r e e - X G e n X', lst_titulos=['TIT-MENU','ITEM','LEVEL','APELL','NOMB-REL', 'Padre', 'ind-Padre'] )

            # ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc            
            self.create_INDICEX(lst__men_itm_lev_ape_name_padr_ipadr=self.lst__men_itm_lev_ape_name_padr_ipadr  )
            """ >>> Crea los diferentes TIPOS DE INDICE: Alfabético, Numérico(by Def), Mixto.... Se pueden crear mas tipos. 
            Son las listas generales de todos los tipos de indices. Se almacenan en: self.lst_opt_tipo_NUMERIC | 
                                                                                     self.lst_opt_tipo_ALF_MAX | 
                                                                                     self.lst_opt_tipo_ALF_MIN | 
                                                                                     self.lst_opt_tipo_MIXTO   """

            self.lst_Lst_Valid_Opt = self.set_tipos_indice_validos(tipo_marcador)
            """ >>> LISTA DE List de Str(Matriz) de las OPCIONES VALIDAS 
                ...Esta lista hay que pasarla a  self.Xavier_get_USUARIO() para las respuestas OK
                Es Lo que el usuario puede aceptar como entrada: pej ( a.1 , 1.1 , A.1 )
                -Tb la lista de las opciones validas se la asigno a lst_skin con self.set_lst_columna_skin()  para la IMPR
                [tipo_marcador]: '1' , 'A', 'a' , '1a' 'a1' + Enum TYPEX
            """            
            if not self.lst_Lst_Valid_Opt: return None
            lst_Str_Valid_Opt = [('.').join(lst_V) for lst_V in self.lst_Lst_Valid_Opt]
            """ >>> L I S T A   DE  las  O P C I O N E S   V A L I D A S  en formato Texto para lst_skin """

            lst_Str_Valid_Opt_REMAT = [cadena+'.' for cadena in lst_Str_Valid_Opt]
            """ >>> El remate del punto final.... es sólo estética, superficialidad....pero tan necesaria. """

            """ ???????????????????????????????????????????????????????????????????????????????????????????
            # PRUEBA..... CAMBIO UN SOLO VALOR EN LA MATRIZ.............. BORRAR.......DE AQUI A TABLERO
            self.setV_skin(lst_skin=lst_skin, fila=1, columna=4, valor='dvd')
            ??????????????????????????????????????????????????????????????????????????????????????????????? """            
            
            # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            # ASIGNA VALORES A LAS COLUMNAS:....
            """ >>> La impresion trabaja linea a linea, al trabajar con lista de lista de str, puedo trabajar como matriz y alterar las columnas antes de ser impreso todo como lineas. """
            self.lst_INICIO = [f'{'|'}{' '*1}' for i in range(len(lst_Str_Valid_Opt_REMAT))]
            self.lst_2SP = [f'{' '*1}' for i in range(len(lst_Str_Valid_Opt_REMAT))]
            self.lst_LEVEL = [f'{int(row[2])*'    '}' for row in self.lst__men_itm_lev_ape_name_padr_ipadr]
            self.lst_FIN = [f'{'|'}' for i in range(len(lst_Str_Valid_Opt_REMAT))]
            self.lst_VACIO = [f'{''}' for i in range(len(lst_Str_Valid_Opt_REMAT))]            

            
            # ??????????????????? lista de str de valores validos: numeracion - item_menu
            self.set_lst_columna_skin(menu_dvd=menu_dvd, lst_skin=self.lst_skin, columna=0, lst_newValues=self.lst_VACIO)
            self.set_lst_columna_skin(menu_dvd=menu_dvd, lst_skin=self.lst_skin, columna=1, lst_newValues=self.lst_LEVEL)
            self.set_lst_columna_skin(menu_dvd=menu_dvd, lst_skin=self.lst_skin, columna=2, lst_newValues=lst_Str_Valid_Opt_REMAT)            
            self.set_lst_columna_skin(menu_dvd=menu_dvd, lst_skin=self.lst_skin, columna=3, lst_newValues=self.lst_2SP)
            self.set_lst_columna_skin(menu_dvd=menu_dvd, lst_skin=self.lst_skin, columna=5, lst_newValues=self.lst_2SP)
            
            lst_mystyca_skin_result = [''.join(mystyca_fila) for mystyca_fila in self.lst_skin]
            """ lista de str  """
            # ___________________________________________________________________________          
            self.set_lst_columna_skin(menu_dvd=menu_dvd, lst_skin=self.lst_skin, columna=0, lst_newValues=self.lst_INICIO)
            self.set_lst_columna_skin(menu_dvd=menu_dvd, lst_skin=self.lst_skin, columna=1, lst_newValues=self.lst_LEVEL)
            self.set_lst_columna_skin(menu_dvd=menu_dvd, lst_skin=self.lst_skin, columna=2, lst_newValues=lst_Str_Valid_Opt_REMAT)            
            self.set_lst_columna_skin(menu_dvd=menu_dvd, lst_skin=self.lst_skin, columna=3, lst_newValues=self.lst_2SP)
            # la Columna 4 ya tiene los datos buenos, por eso no la formateo
            self.set_lst_columna_skin(menu_dvd=menu_dvd, lst_skin=self.lst_skin, columna=5, lst_newValues=self.lst_2SP)
            # la Columna 6 la dejo en blanco de momento.
            # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            
            
            """ CREA una Lista de Strings con cada linea completa A IMPRIMIR....es la Transformacion"""
            lst_Mystyca_Transformacion = [''.join(mystyca_fila) for mystyca_fila in self.lst_skin]  

            """ DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
            D E C O R A C I O N   DEL  M A R C O , CIERRE DEL MENU: Determinar la longitud máxima de las líneas """
            max_length = max(len(line) for line in lst_Mystyca_Transformacion)
            self.total_length = max_length + padX
            
            """ Establezco el  F O R M A T O de esta manera para no colisionar la barra del final con el contenido de Mystica.  """
            formato_fila = "{:<" + str(self.total_length) + "}" + "{:<" + str(2) + "}"
            
            # Crear una nueva lista formateada para impresión
            self.lst_Impresion = [formato_fila.format(line, '|') for line in lst_Mystyca_Transformacion]
            """ >>> Aquí es donde se formatea cada LINEA de Mystyca  con un caracter que será el muro final de cada linea 
            Esto lo hago así por estética, para crear un marco al menú. la LOGICA de Mystica realmente termina enn lst_Mystica_Swap"""
            if not self.lst_Impresion: 
                print("Error en Mystyca")
                return None
            # DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
            
            """ VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV """
            self.ver_mystyca_transformacion(menu_dvd=menu_dvd)
            # VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
            
            """ 
            1 SOLA RESPUESTA Y VUELVES: lo gestiona el main( .... cualquier llamada ) 
            [respuesta] es el indice lineal en lst_keys o self.lst__men_itm_lev_ape_name_padr_ipadr"""
            if Loop == False:   
                """ UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU """
                respuesta, pre_respuesta = self.Xavier_get_USUARIO(menu_dvd=menu_dvd ,lst_Valid=self.lst_Lst_Valid_Opt, max_length=max_length , execAll=execAll, mystica_skin_str=lst_mystyca_skin_result )    
                # UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
                if respuesta == None:       
                    """ SALIR """
                    return
                else:
                    print(f'\nRespuesta encontrada en {respuesta}: {self.lst__men_itm_lev_ape_name_padr_ipadr[int(respuesta)][1]} ')
                    """ 
                    TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT """
                    titulo_menu = self.lst__men_itm_lev_ape_name_padr_ipadr[int(respuesta)][0]
                    item_menu   = self.lst__men_itm_lev_ape_name_padr_ipadr[int(respuesta)][1]
                    return self.Terminator(titulo_menu=titulo_menu, item=item_menu, pre_respuesta=pre_respuesta, respuesta=respuesta, execFunc=execFunc )    
                    # RETORNAMOS.....TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
            else:
                """ SALES POR <<< """
                while(True):
                    """ UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU """
                    respuesta, pre_respuesta = self.Xavier_get_USUARIO( menu_dvd=menu_dvd, lst_Valid=self.lst_Lst_Valid_Opt, max_length=max_length, execAll=execAll , mystica_skin_str=lst_mystyca_skin_result)   
                    # UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
                    if respuesta == None and pre_respuesta==None:       
                        """ SALIR """
                        return                  # Sale por Main(....por donde es llamada)
                    else:                       
                        print(f'   [{respuesta}] :) {self.lst__men_itm_lev_ape_name_padr_ipadr[int(respuesta)][1]} ', end='| -> ')
                        titulo_menu = self.lst__men_itm_lev_ape_name_padr_ipadr[int(respuesta)][0]
                        item_menu   = self.lst__men_itm_lev_ape_name_padr_ipadr[int(respuesta)][1]
                        """ TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT """
                        self.Terminator( titulo_menu=titulo_menu, item=item_menu, pre_respuesta=pre_respuesta, respuesta=respuesta, execFunc=execFunc)    
                        # TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

        # elif configurado == True and not self.get_lst_dict_hijosX(titulo=menu_dvd.titulo):
        #     """ >>> Configurado pero sin hijos.... tambien se muestra """
        #     self.Mystyca_withOut(menu_dvd=menu_dvd, execFunc=execFunc)
        elif configurado == False:            
            """ >>> Sin Configurar: ......Muestra el menu del tiron """            
            self.Mystyca_withOut(menu_dvd=menu_dvd, execFunc=execFunc)
        pass
    
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # R C R S V : Devuelve Todos los items en orden de impresion.
    # -----------------------------------------------------------------------------------------------
    def Mystyca_Keys(self, menu_dvd, level=None, retorno=None):
        """  """
        if level==None and retorno==None:     # 1ª ENTRADA
            level=-1 ; retorno=[] ; self.pasos=0 
        level += 1 ; self.pasos += 1
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        lst_hijos = self.get_lst_dict_hijosX(titulo=menu_dvd.titulo)        
        if  lst_hijos:         
            for i in range(len(menu_dvd.lst_item)):                
                retorno.append(menu_dvd.get_item_row_body(i))                
                for hijo in lst_hijos:
                    if hijo['ind_en_padre'] == i:                        
                        self.Mystyca_Keys(menu_dvd=hijo['menuDvd'] , level=level, retorno=retorno)
                        break    
        elif not lst_hijos:    
           for i, item in enumerate(menu_dvd.lst_item):                    
                retorno.append(item)
                
        # ___________________________________
        return retorno
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # R C R S V 
    # -----------------------------------------------------------------------------------------------
    def Mystyca_lst_padres(self, menu_dvd, level=None, retorno=None ):
        if level==None and retorno==None:     # 1ª ENTRADA
            level=-1   ; retorno=[] ; self.pasos=0 
        level += 1
        self.pasos+=1
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        lst_hijos = self.get_lst_dict_hijosX(titulo=menu_dvd.titulo)        
        if  lst_hijos:         
            for i in range(len(menu_dvd.lst_item)):
                for hijo in lst_hijos:
                    if hijo['ind_en_padre'] == i:                        
                        retorno.append(menu_dvd.get_item_row_body(row=i))                
                        self.Mystyca_lst_padres(menu_dvd=hijo['menuDvd'] , level=level, retorno=retorno)
                    pass
        elif not lst_hijos:
           for i, item in enumerate(menu_dvd.lst_item):
                pass 
                # retorno.append()
                # retorno.append(menu_dvd.get_lst_row_body(row=i))
        return retorno

   
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # R C R S V 
    # -----------------------------------------------------------------------------------------------
    def Mystyca_Skin(self, menu_dvd, level=None, retorno=None):
        if level==None and retorno==None:     # 1ª ENTRADA
            level=-1 ;  retorno=[] ; self.pasos=0 
        level += 1
        self.pasos+=1
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        lst_hijos = self.get_lst_dict_hijosX(titulo=menu_dvd.titulo)        
        if  lst_hijos:         
            bmatch=False
            for i, item in enumerate(menu_dvd.lst_item):
                retorno.append(menu_dvd.get_lst_row_body(row=i))
                # retorno.append(menu_dvd)
                for hijo in lst_hijos:
                    if hijo['ind_en_padre'] == i:                        
                        self.Mystyca_Skin(menu_dvd=hijo['menuDvd'] , level=level, retorno=retorno)
        elif not lst_hijos:
            for i, item in enumerate(menu_dvd.lst_item):
                retorno.append(menu_dvd.get_lst_row_body(row=i))
                # retorno.append(menu_dvd)
        return retorno
    
    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # R C R S V   
    # -----------------------------------------------------------------------------------------------
    def Mystyca_XgenX(self, menu_dvd, level=None, retorno=None, tituloMaster=None):
        """ Recorre el arbol de Menus y devuelve un lst [nombreMenu, lista impresion, level, nombrePadre, indice_en_Padre]
        Usa principalmente lst_item y dicc_xgenx para """
        if level==None and  retorno==None:     # 1ª ENTRADA
            level=-1            
            retorno=[]
            self.pasos=0
            tituloMaster=menu_dvd.titulo
        level += 1
        self.pasos+=1
        lst_hijos = self.get_lst_dict_hijosX(titulo=menu_dvd.titulo)        
        if  lst_hijos:         
            bmatch=-1
            for i in range(len(menu_dvd.lst_item)):
                strFila=menu_dvd.get_strRow_Body(row=i, esNumerado=True)
                retorno.append((menu_dvd.titulo, 
                                strFila, 
                                level, 
                                self.get_padre(titulo=menu_dvd.titulo),  
                                self.get_ind_en_padre(titulo=menu_dvd.titulo)))
                # print(fila)
                for hijo in lst_hijos:
                    if hijo['ind_en_padre'] == i:                        
                        self.Mystyca_XgenX(menu_dvd=hijo['menuDvd'] , level=level, tituloMaster=menu_dvd.titulo, retorno=retorno)
        elif not lst_hijos:
            for i in range(len(menu_dvd.lst_item)):
                retorno.append((menu_dvd.titulo, 
                                menu_dvd.get_strRow_Body(row=i, esNumerado=True), 
                                level, 
                                self.get_padre(titulo=menu_dvd.titulo), 
                                self.get_ind_en_padre(titulo=menu_dvd.titulo)
                                ))
                # print(menu_dvd.get_strRow_Body(row=i, esNumerado=True))

        return retorno

    # RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # R C R S V   PATH-PADRE , NOMBRE HIJO
    # -----------------------------------------------------------------------------------------------
    def mystyca_ScannerXgenX(self, menu_dvd, level=None,  retorno=None, apellido=None):
        if level==None and retorno==None:     # 1ª ENTRADA
            level=-1 ; retorno=[]  ;  apellido='' 
        level += 1 
        """ Contadores """
        lst_hijos = self.get_lst_dict_hijosX(titulo=menu_dvd.titulo)      
        """ Tengo al padre(menu_dvd, y a los hijos(lst_hijos)) 
        """  
        if  lst_hijos:         
            apellido += str(level) + '.'
            for i in range(len(menu_dvd.lst_item)):
                item = menu_dvd.get_item_row_body(i)
                retorno.append(( menu_dvd.titulo ,                                  
                                item , 
                                level , 
                                apellido , 
                                menu_dvd.get_numRltv_row_body(i) ,
                                self.get_padre(titulo_menu=menu_dvd.titulo) , 
                                self.get_ind_en_padre(titulo_menu=menu_dvd.titulo) ))
                                
                for hijo in lst_hijos:
                    if hijo['ind_en_padre'] == i:                        
                        self.mystyca_ScannerXgenX(menu_dvd=hijo['menuDvd'] , level=level,  retorno=retorno, apellido=apellido)
                    pass
        elif not lst_hijos:
            apellido += str(level) + '.'
            aux = apellido
            for i, item in enumerate(menu_dvd.lst_item):
                # apellido += str(level) + '.'
                # retorno.append(( apellido , menu_dvd.get_numRltv_row_body(i) ))
                retorno.append(( menu_dvd.titulo ,                                  
                                item , 
                                level , 
                                apellido , 
                                menu_dvd.get_numRltv_row_body(i) ,
                                self.get_padre(titulo_menu=menu_dvd.titulo) , 
                                self.get_ind_en_padre(titulo_menu=menu_dvd.titulo)  ))
                apellido = aux
        return retorno    
    
    # ________________________________________________________________________
    # IMPRIME EL MENU SEGUN LA CONFIGURACION. TB SE LLAMA CUANDO SE PULSA '<'
    def ver_mystyca_transformacion(self, menu_dvd):
        """
        FROM.......Franky-Franky-Franky-Franky-Franky-Franky_Franky-Franky-Franky-Franky
        FROM.......Franky-Franky-Franky-Franky-Franky-Franky_Franky-Franky-Franky-Franky
        """   
        menu_dvd.style(num_char=self.total_length+1 , char_head='*',char_cuello='*')         
        print(menu_dvd.F_r_a_n_k_Y(bSombrero=True, bCabeza=True, bCuello=True, esNumerado=True)) 
        pass            
        # IMPRIME Mystyca_skin()::: lst_skin formateada en todas sus columnas
        for fila_mystyca_str in self.lst_Impresion:
            print(fila_mystyca_str)                
        pass
        menu_dvd.style(char_pie='~', num_char=self.total_length+1) 
        print(menu_dvd.F_r_a_n_k_Y(bPie=True))    
        pass
        menu_dvd.style(char_pie='~', num_char=self.total_length+1)         
        print(menu_dvd.F_r_a_n_k_Y(bPie=True, bSalir=True)) 
        pass
        """ 
        TO.........Franky-Franky-Franky-Franky-Franky-Franky_Franky-Franky-Franky-Franky-Fr
        TO.........Franky-Franky-Franky-Franky-Franky-Franky_Franky-Franky-Franky-Franky-Fr
        """
    # _____________________________________________________________________________
    # CUANDO SE PULSA '?' , IMPRIME EL MENU CON INFORMACION SOBRE LA CONFIGURACION 
    def get_mystyca_informacion(self, titulo_menu, lst_padres , lst_hijos, execAll, max_length):
        lst_setup=self.lst__men_itm_lev_ape_name_padr_ipadr
        
        menu_dvd_inicial=self.get_menudvd(titulo_menu).fraseHead

        lst_final_dir=[]
        lst_funcionExe=[]
        lst_barraFinal=[]
        for i, fila in enumerate(lst_setup):
            # _________________________________
            if execAll == True: 
                lst_final_dir.append (f'(D)' if fila[1] in lst_padres else f'(X)')
            else:
                lst_final_dir.append (f'(-)' if fila[1] in lst_padres else f'(X)')
            # _________________________________
            menu_dvd=self.get_menudvd(fila[0])
            funcion = menu_dvd.dicc_menu.get(fila[1])
            if callable(funcion):
                lst_funcionExe.append(f' ({str(funcion.__name__)})')
            else:
                lst_funcionExe.append(' ( - ) ')
            # __________________________
            lst_barraFinal.append('|')
        # _____________________________________
        # self.set_lst_columna_skin(menu_dvd=menu_dvd, lst_skin=self.lst_skin, columna=5, lst_newValues = lst_final_dir)
        # self.set_lst_columna_skin(menu_dvd=menu_dvd, lst_skin=self.lst_skin, columna=6, lst_newValues = lst_funcionExe)
        """ CREA una Lista de Strings con cada linea completa A IMPRIMIR....es la Transformacion"""
        lst_Mystyca_Transformacion = [''.join(mystyca_fila) for mystyca_fila in self.lst_skin]          
        # __________________________________________________________________________________________
        """ Calculo las longitudes al mm para que cuadre con las mismas diemnsiones que el menu-Ppal """
        length_lst_final_dir = 7
        length_barrafin = 1
        length_lst_funcion_exe = int(self.total_length) - int(max_length+10 + length_lst_final_dir + length_barrafin ) + 1

        # fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        formato_fila = "{:<" + str(max_length+10) + "}" + "{:>" + str(length_lst_final_dir) + "}"+ "{:<" + str(length_lst_funcion_exe) + "}" + "{:<" + str(length_barrafin) + "}"
        # _____________________________________________________________________________________________________________
        # Generar la lista de impresión. Esto es la pera. Puedo formatear con zip, que hace pares de valores en listas.
        lst_Impresion = [
            formato_fila.format(col1_skin, col2_mode, col3_func, col4_barrafin) 
            for col1_skin, col2_mode, col3_func, col4_barrafin in zip(
                lst_Mystyca_Transformacion, lst_final_dir, lst_funcionExe, lst_barraFinal
            )
        ]
        # ________________________________________________________
        aux = menu_dvd.fraseHead    # Guardo la frase original
        if execAll == True: 
            menu_dvd.fraseHead=str(menu_dvd_inicial) + "\tMODE ::: Exec All"
        else:
            menu_dvd.fraseHead=str(menu_dvd_inicial) + "\tMODE ::: Exec (X)"
            
        menu_dvd.style(num_char=self.total_length+1 , char_head='*',char_cuello='*')         
        print(menu_dvd.F_r_a_n_k_Y(bSombrero=True, bCabeza=True, bCuello=True, esNumerado=True)) 
        for fila_mystyca_str in lst_Impresion:
            print(fila_mystyca_str)                
        menu_dvd.style(char_pie='~', num_char=self.total_length+1) 
        print(menu_dvd.F_r_a_n_k_Y(bPie=True))    
        menu_dvd.style(char_pie='~', num_char=self.total_length+1)         
        print(menu_dvd.F_r_a_n_k_Y(bPie=True, bSalir=True)) 

        menu_dvd.fraseHead = aux    # Le devolvemos su valor.
    # _______________________________
    def get_lst_item_funcion(self):
        """ >>> Devuelve una lista de diccionarios item_menu(str):funcion(func) """
        if not self.lst__men_itm_lev_ape_name_padr_ipadr: return None  
        lst_dicc_itmfunc=[]      
        for i, fila in enumerate(self.lst__men_itm_lev_ape_name_padr_ipadr):
            titulo_menu=fila[0]
            menu_dvd=self.get_menudvd(fila[0])
            item = fila[1]
            funcion = menu_dvd.dicc_menu.get(fila[1])
            if callable(funcion):
                lst_dicc_itmfunc.append({str(item):funcion})
            else:
                lst_dicc_itmfunc.append(None)

        return lst_dicc_itmfunc
       
    # _____________________________________
    # FROM nombre-titulo-Menu TO nombre-padre     
    def get_padre(self, titulo_menu):
        if self.dicc_xgenx:
            for tit, padre_index in self.dicc_xgenx.items():
                if titulo_menu == tit: 
                    if padre_index[PADRE_IND.PADRE.value]:
                        return padre_index[PADRE_IND.PADRE.value]
                    else:
                        return None
    # __________________________________________
    # FROM nombre-titulo TO indice en el padre
    def get_ind_en_padre(self, titulo_menu):
        if self.dicc_xgenx:
            for tit, padre_index in self.dicc_xgenx.items():
                if titulo_menu == tit: 
                    if padre_index[PADRE_IND.PADRE.value]:
                        return padre_index[PADRE_IND.INDEX.value]
                    else:
                        return None

    # ==============================================================================
    # SE EJECUTA Mystyca SIN CONFIGURACION.... MENU DE 1 NIVEL.
    # ==============================================================================
    def Mystyca_withOut(self, menu_dvd, execFunc):
        """ >>> Se ejecuta solo una vez. Puede ejecutar o retornar respuesta.
            es mision del programador recoger respuesta y tratarla. Son menus rápidos. """

        print(menu_dvd.F_r_a_n_k_Y(bSombrero=True, bCabeza=True, bCuello=True, esNumerado=True))
        
        for i in range(len(menu_dvd.lst_item)):
            print(menu_dvd.get_strRow_Body(row=i, esNumerado=True))
        
        print(menu_dvd.F_r_a_n_k_Y(bSalir=True, bPie=True))
        respuesta = menu_dvd.pide_data_usuario(menu_dvd=menu_dvd)        
        # return self.Terminator(titulo_menu=menu_dvd.titulo,  respuesta=respuesta, execFunc=execFunc )
        if respuesta == None: return None        
        if execFunc==False: 
            """ OPT RETORNA"""
            return respuesta
        else:
            """ OPT EXEC FUNC """                    
            # menu_dvd=self.get_menudvd(titulo_menu)            
            it=''
            for i, item in enumerate(menu_dvd.lst_item):
                if respuesta == i:
                    it=str(item)    

            if menu_dvd.dicc_menu[it] != None: 
                menu_dvd.dicc_menu[it]()
            else:
                key = next((k for k, v in menu_dvd.dicc_menu.items() if v == it), None)
                print(f"{key} está a None....shhhhh ;|" if key else f"{item} .... None Func")

            return True

    # ((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))
    # El Profesor Xavier lee la mente del Usuario y le saca un Dato por Teclado
    def Xavier_get_USUARIO(self, menu_dvd, lst_Valid, max_length, execAll=None, mystica_skin_str=None):
        """ >>> Def: Pide Un dato al Usuario y valida que da una respuesta valida con respecto a la geneticaX
        [menu_dvd] : el objeto MenuDvd (principal) sobre el que se trabaja. el punto de partida del analisis... Menu1
        [lst_Valid] : lista con las respuestas validas generadas en self.create_INDICEX()
        [max_length] : la longitud maxima de lst_skin en str.
        [execAll] : (bool) True = en todos los items intento ejecutar la funcion. False=Los directorios no se ejecutan.
        [mystica_skin_str] : (list), es lst_skin convertida linea a linea en str.

        Retorno: None, <<< salir | indice en lst_keys() y casi todos los lst_ de la clase.
        """
        pass
        """ 
        >>> LISTA DE LOS   P A D R E S   DEL MENU (  R C R S V  ) ....Usado para saber si tiene exec o son directorio."""
        lst_padres  = self.Mystyca_lst_padres(menu_dvd=menu_dvd)        
        lst_hijos   = [ hijo for hijo in self.lst_keys if hijo not in lst_padres]
        # print(lst_padres)
        # print(lst_hijos)
        """ 
        LISTAS DE   O P C I O N E S - V A L I D A S  """
        lst_valid_10 = [ ('').join(fila) for fila in lst_Valid   ]
        lst_valid_20 = [ ('.').join(fila) for fila in lst_Valid  ]
        lst_valid_25 = [ cadena+'.' for cadena in lst_valid_20   ]        
        lst_valid_30 = [ (',').join(fila) for fila in lst_Valid  ]
        lst_valid_35 = [ cadena+',' for cadena in lst_valid_30   ]
        lst_valid_40 = [ (' ').join(fila) for fila in lst_Valid  ]
        lst_valid_50 = [ ('-').join(fila) for fila in lst_Valid  ]
        lst_valid_55 = [ cadena+'-' for cadena in lst_valid_50   ]
        lst_valid_60 = [ (':').join(fila) for fila in lst_Valid  ]
        lst_valid_65 = [ cadena+':' for cadena in lst_valid_60   ]
        lst_valid_70 = [ (';').join(fila) for fila in lst_Valid  ]
        lst_valid_75 = [ cadena+';' for cadena in lst_valid_70   ]

        """ 
        888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        BUCLE HASTA OPCION VALIDA O SALIR +    A N A L I S I S   DE LAS R E S U P U E S T A S """
        respuesta=None
        while(True):
            respuesta_extraida =''
            pre_respuesta =''
            pos_respuesta =''
            respuesta=input(f"{menu_dvd.introData}").strip()
            try:
                if respuesta == SALIR:          # A PULSADO  '<<<' ....SALIR
                    """ RETORNO Y REPETICION DEL MENU :::: """
                    return None , None
                elif respuesta == '<':       
                    """ IMPRIME EL MENU Y VUELVE A PEDIR DATO AL USUARIO. """
                    os.system('cls')              
                    self.ver_mystyca_transformacion( menu_dvd=menu_dvd )
                    continue
                elif respuesta == '?':  # ver informacion del menu.                                        
                    lst_impr_info = self.get_mystyca_informacion( titulo_menu=menu_dvd.titulo, max_length=max_length, lst_padres = lst_padres, lst_hijos=lst_hijos , execAll=execAll)
                
                elif respuesta.startswith("<<") and respuesta.endswith(">>"):   
                    """ B a c k G r o u n d :   Acaba cuando yo me acabe (demonio) """
                    # Extraigo el contenido entre '<<' y '>>'
                    respuesta_extraida = str(respuesta[2:-2]).strip()
                    pre_respuesta  = respuesta[:2].strip()   # Desde el inicio(0) hasta 1(2-1) <<
                    post_respuesta = respuesta[2:].strip()   # Desde 2 hasta final >>
                    if pre_respuesta == '<<' and pos_respuesta == '>>':
                        print(f"Contenido extraído: {respuesta_extraida}")               
                        continue
                    print('m o d o   B a c k G r o u n d .... en proceso WIP')

                elif respuesta.startswith(">>"):       
                    """ i n t e r a c t i v o   (no demonio)(tkinter o si quieres que siga la ejecución aunque yo me acabe) """
                    respuesta_extraida = respuesta[2:].strip()   #Desde la posicion 2 hasta el final . respuesta!!.
                    pre_respuesta = respuesta[:2].strip()   # Desde el inicio(0) hasta 1(2-1) >>
                    print('m o d o   I n t e r a c t i v o  .... en proceso WIP')

                elif respuesta.startswith("**"):       
                    """  m o d o   d i r e c t o r y  """
                    respuesta_extraida = respuesta[2:].strip()   #Desde la posicion 2 hasta el final . respuesta!!.
                    pre_respuesta = respuesta[:2].strip()   # Desde el inicio(0) hasta 1(2-1) >>
                    print('m o d o   d i r e c t o r y .... en proceso WIP')

                # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
                """   V A L I D A C I O N    """
                # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
                
                """ Verifica/Valida que hay una respuesta y que se ha introducido '>>' """
                if respuesta_extraida != '' and pre_respuesta == '>>':
                    respuesta = respuesta_extraida

                """ Verifica/Valida que hay una respuesta y que se ha introducido '<<' """
                if respuesta_extraida != '' and pre_respuesta == '<<':
                    respuesta = respuesta_extraida    
                
                """ Verifica/Valida que hay una respuesta y que se ha introducido '**' """
                if respuesta_extraida != '' and pre_respuesta == '**':
                    respuesta = respuesta_extraida    
                

                # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
                """   E V A L U A C I O N   D E   L A   R E S P U E S TA    """
                # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
                listas_validas = [
                    lst_valid_10, lst_valid_20, lst_valid_25, lst_valid_30, 
                    lst_valid_35, lst_valid_40, lst_valid_50, lst_valid_55, 
                    lst_valid_60, lst_valid_65, lst_valid_70, lst_valid_75
                ]
                """  """
                bSalir=False # se pone a true para salir del bucle for.
                for lista in listas_validas:
                    if respuesta in lista:
                        for i, str_indice in enumerate(lista):
                            if respuesta == str_indice:
                                # print(f"Respuesta '{respuesta}' encontrada en el índice {i}")
                                # return i
                                elect, item_menu = self.separar_cadena(str(mystica_skin_str[i]).strip())
                                 # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
                                """ >>> MODO DE OPCION VALIDA( execAll = True | False =  solo HIJOS exec  """                                 
                                if execAll == None: 
                                    execAll = True
                                if isinstance(execAll, bool):
                                    if execAll == True:     # Todo son opciones validas.... responsabilidad del usuario meter funciones en directorios.
                                        return i , None           # ENCUENTRA Y RETORNA EL INDICE EN LST_KEYS!!!!!!!!!   :) 
                                    else:                   # Solo los Hijos son validos
                                        if item_menu in lst_padres:                                            
                                            print('(Directorio) ', end=' ')
                                            bSalir=True
                                            break        # Si encuentra un padre, no vale como respuesta valida y vuelve a preguntar.
                                        else:
                                            return i , pre_respuesta   # No es un padre.
                                        pass
                                else:
                                    execAll = True
                                pass                               
                    else:   # print("Respuesta no encontrada.")                        
                        pass                    
                    if bSalir == True:
                        bSalir = False
                        break
                pass
            except Exception as e:
                """ 
                SI ERROR, INFO Y SEGUIMOS :::: """
                print(e)
                continue
        pass
        if respuesta_extraida is not None and pre_respuesta is not None:
            if respuesta_extraida == respuesta: 
                return respuesta_extraida, pre_respuesta
            else:
                return respuesta , pre_respuesta
        else:
            return respuesta , None

    """ 
    [NUMERICA-JERARQUICA]
        1. Historia                         
        1.1. Historia antigua  
            1.1.1. Egipto  
            1.1.2. Mesopotamia  
        1.2. Historia moderna  
            1.2.1. Revolución Industrial  
            1.2.2. Guerras Mundiales  
        2. Ciencia  
        2.1. Física  
        2.2. Química
    """    
    # _________________
    # INDICEXXXX
    def create_INDICEX(self, lst__men_itm_lev_ape_name_padr_ipadr ): 
        """ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        ALGORITMO INFERNAL PARA SACAR LOS INDICES CORRECTOS EN LA FORMA [1, 0, 1, 2] (camino de levels)
        que se Corresponde con el level en la funcion recursiva. marca la posicion que va a tener y 
        la numeracion con respecto a esa posicion......una pesadilla que me ha llevado 6 días :()
        [lst__men_itm_lev_ape_name_padr_ipadr]: lst de datos que se saca de self.mystica_ScannerX()
        Retorno: None. Alimenta y llena los las listas de listas(que son la numeracion y posicion en el menu.):
        lst_opt_tipo_NUMERIC    |  lst_opt_tipo_ALF_MAX | lst_opt_tipo_ALF_MIN | lst_opt_tipo_MIXTO
        """

        MENU  = 0 ; ITEM  = 1 ; LEVEL = 2 ; APELL = 3 ; NAME = 4 ; PADRE = 5 ; ID_PADRE = 6
        # ________________
        import string
        import copy
        # ________________
        dicc_min =  {idx:letra for idx, letra in enumerate(string.ascii_lowercase)} 
        dicc_may =  {idx:letra for idx, letra in enumerate(string.ascii_uppercase)}        
        # ________________
        lst_name = [ ( int(lst_a[NAME]) + 1 ) for lst_a in self.lst__men_itm_lev_ape_name_padr_ipadr ]
        """ >>> Lista de los nombres relativos de cada Item + 1 """
        # ________________
        lst_split_apellido = [ str(lst_a[3]).split(sep='.')  for lst_a in self.lst__men_itm_lev_ape_name_padr_ipadr ]
        """ >>> Lista de apellidos en forma de lista. """
        # ..... del split sale con una dimensión de más(la del '.') y así lo ajusto a su dimension:
        for lst_apellido in lst_split_apellido:
            lst_apellido.pop()
        
        for lst_apellido in lst_split_apellido:
            for apellido in lst_apellido:
                apellido = int(apellido)

        # .... (La long de la list lst_apellido y  el level del item son directmnt proporcionales).
        """ ::::::: N U M E R I C O  LISTA DEL NOMBRE-FINAL-TOTAL :  """
        lst_opt_tipo_NUMERIC=[]
        ind_Master=1
        ind_Sub = 1

        for i, lst_apellido in enumerate(lst_split_apellido):
            if len(lst_apellido) == 1 and i == 0:           
                """ 1ª VEZ Menu PPal = fija ind_Master.   """
                pass
                lst_opt_tipo_NUMERIC.append([ind_Master])   # Add
                ind_Master += 1  ; ind_Sub     = 1          # Aumento el Master  y Re-inicio para los subMenus                                             
            else:
                actual = self.lst__men_itm_lev_ape_name_padr_ipadr[i]
                anterior = self.lst__men_itm_lev_ape_name_padr_ipadr[i-1]            
                if len(lst_apellido) == 1:                  # solo Masters ... actual[PADRE]=='-'
                    lst_opt_tipo_NUMERIC.append([ind_Master])
                    ind_Master += 1  ;    ind_Sub     = 1 
                    continue
                # ______________
                if actual[LEVEL] != anterior[LEVEL]:    
                    """ cambio de nivel """
                    ind_Sub = 1                     # 1º reinicio sub
                    if actual[LEVEL] > anterior[LEVEL]:   
                        """ Hacia Abajo(Hijo) """
                        lst_opt_tipo_NUMERIC.append(lst_opt_tipo_NUMERIC[i-1] + [ind_Sub] )
                        ind_Sub += 1    
                        pass
                    else:       
                        """ Hacia Arriba( padre, abuelo... pero NO el master). """                            
                        lvl_ref = int(actual[LEVEL] ) + 1
                        for j, path in enumerate(lst_opt_tipo_NUMERIC[::-1]):        
                            if len(path) == lvl_ref:
                                nuevo_path = path[:-1] + [path[-1] + 1]                         
                                # print(f'{path} -> {nuevo_path}')
                                lst_opt_tipo_NUMERIC.append( nuevo_path )
                                break
                        pass
                else:
                    """ mismo nivel """
                    ant=lst_opt_tipo_NUMERIC[i-1]
                    lst_opt_tipo_NUMERIC.append( ant[:-1] + [ant[-1]+1]  )
                    # Al anterior elemento. Lo empiezo por el final, le quito 1 y le sumo uno al ultimo elemento.

        """  
        ::::::: A L F - M A X   """
        lst_opt_tipo_ALF_MAX = copy.deepcopy(lst_opt_tipo_NUMERIC)
        for lst_path in lst_opt_tipo_ALF_MAX:
            lst_path[0] = dicc_may[int(lst_path[0])-1]
        """ 
        ::::::: A L F - M I N  """
        lst_opt_tipo_ALF_MIN = copy.deepcopy(lst_opt_tipo_NUMERIC)
        for lst_path in lst_opt_tipo_ALF_MIN:
            lst_path[0] = dicc_min[int(lst_path[0])-1]
        """  
        ::::::: M I X T O """
        lst_opt_tipo_MIXTO = copy.deepcopy(lst_opt_tipo_NUMERIC)
        for lst_path in lst_opt_tipo_MIXTO:
            lst_path[0] = dicc_may[int(lst_path[0])-1]
            try:                
                lst_path[2] = dicc_min[int(lst_path[2])-1]
            except:
                continue
        
        lst_opt_tipo_NUMERIC = [[str(element) for element in sublist] for sublist in lst_opt_tipo_NUMERIC]
        lst_opt_tipo_ALF_MAX = [[str(element) for element in sublist] for sublist in lst_opt_tipo_ALF_MAX]
        lst_opt_tipo_ALF_MIN = [[str(element) for element in sublist] for sublist in lst_opt_tipo_ALF_MIN]
        lst_opt_tipo_MIXTO   = [[str(element) for element in sublist] for sublist in lst_opt_tipo_MIXTO]
        # ____________________________________________________________
        # Asignacion a las variables de clase y objetivo cumplido ;)
        self.lst_opt_tipo_NUMERIC = lst_opt_tipo_NUMERIC
        self.lst_opt_tipo_ALF_MAX = lst_opt_tipo_ALF_MAX
        self.lst_opt_tipo_ALF_MIN = lst_opt_tipo_ALF_MIN
        self.lst_opt_tipo_MIXTO   = lst_opt_tipo_MIXTO

    # __________________________________________
    # Entra una cadena tipo   1.2.2. Guerras Mundiales  y devuelve un list[1,2,2] y 'Guerras Mundiales'  
    # (la uso para recuperar el item(Guerras Mundiales, pero se puede usar para recuperar la numeracion tb))
    def separar_cadena(self, cadena):
        patron = r'^([\w.]+?)\s+(.*)'
        path_item = re.match(patron, cadena.strip())
        if path_item:
            path  = path_item.group(1).strip('.').split('.')
            texto = path_item.group(2)
            return path, texto
        return None, None
    # ____________________________
    def set_tipos_indice_validos(self, type_XindeX=TYPEX.NUMERIC):
        if isinstance(type_XindeX, str):
            if type_XindeX == 'A':
                return self.lst_opt_tipo_ALF_MAX
            elif type_XindeX == 'a':
                return self.lst_opt_tipo_ALF_MIN
            elif type_XindeX == '1':
                return self.lst_opt_tipo_NUMERIC
            elif type_XindeX == 'a1':
                return self.lst_opt_tipo_MIXTO
            elif type_XindeX == '1a':
                return self.lst_opt_tipo_MIXTO
            elif type_XindeX == '1A':
                return self.lst_opt_tipo_MIXTO
            elif type_XindeX == 'A1':
                return self.lst_opt_tipo_MIXTO
            else:
                return self.lst_opt_tipo_NUMERIC           
            pass
        elif type_XindeX == TYPEX.NUMERIC:
            return self.lst_opt_tipo_NUMERIC
        elif type_XindeX == TYPEX.ALF_MAX:
            return self.lst_opt_tipo_ALF_MAX
        elif type_XindeX == TYPEX.ALF_MIN:
            return self.lst_opt_tipo_ALF_MIN
        elif type_XindeX == TYPEX.MIXTO:
            return self.lst_opt_tipo_MIXTO
        else:
            return self.lst_opt_tipo_NUMERIC
    # ____________________________________
    # Llamada desde Mystyca. imprime una linea 
    def print_row_Mystyca(self, menu_dvd, level, fila, esNumerado, x_n):
        menu_dvd.style( X__num = menu_dvd.get_TAB()*(level) + str(menu_dvd.X__num) )                    
        print(menu_dvd.get_strRow_Body(row=fila, esNumerado=esNumerado))
        menu_dvd.style( X__num = x_n )        
    # ____________________________________
    # 1ª VALIDACION DEL METODO SELF.View
    def validacion_show(self, titulo, configurado):
        if titulo not in self.lst_titulosXX: 
            print(f'ERR-VAL:: {titulo}  no esta en self.lst_titulosXX')
            return False                
        if titulo not in self.dicc_xgenx and configurado==True: 
            print(f'ERR-VAL:: {titulo} no esta en self.dicc_xgenx')
            return False
        return True
    # _______________________________________________________________
    # TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
    # Analiza las respuestas y toma una opcion en funcion de execFunc
    def Terminator(self, titulo_menu, item, respuesta, execFunc, pre_respuesta=None):
        """ Def: Tenemos la mision de crear una lista de [item , funcion, respuesta antigua, respuesta nueva]
        [titulo_menu] :(str): El titulo de menu_dvd.
        [respuesta]:(int): es el indice en cualquier lista de items(): lst_keys(), lst_item_func.... 1, 0, 12, 5
        [item]: (str): El nombre del Elemento del menu
        [execFunc]: (bool): True = ejecuta funcion | False = Devuelve respuesta
        [pre_respuesta]: (str): No se usa pero se pasa por parametro. es para que la vida sea mas sencilla. Si quieres usar un prefijo (>> , >>>) en este caso, para registrar las acciones del menu(a1, a, b11)
        """
        """
        SALIR """
        if respuesta == None: return None
        
        if execFunc==False: 
            """ OPT RETORNA"""
            return respuesta
        else:
            """ OPT EXEC FUNC """                    
            if self.lst_item_func:
                for i in range(len(self.lst_item_func)):
                    if i==respuesta:
                        if self.lst_item_func[i]:       # Si estuviera a None aquí casca... se podría hacer por try except ...mmmm
                            if self.lst_item_func[i][item]:
                                self.lst_item_func[i][item]()
                        else:
                            print(f'None')
                    else:
                        pass
            else:
                print('Sin Data :( .... llama a mystyca a ver que hace')
            """ 
            otra forma de acceder a la funcion(la idea original, pero se queda la mas intuitiva y facil de manejar.) """
            # menu_dvd=self.get_menudvd(titulo_menu)            
            # if menu_dvd.dicc_menu[item] != None: 
            #     menu_dvd.dicc_menu[item]()
            # else:                
            #     pass

            return True
    # _____________________________________________________
    # DEVUELVE UN LIST DE HIJOS COMPROBANDO EN DICC_XGENX
    def get_lst_dict_hijosX(self, titulo):
        """ >>> LISTA CON MIS HIJOS DE PRIMERA GENERACION. Recorre el dicc_xgenx y recoge 
        [Retorno]: una lista de diccionarios con los datos sobre mis hijos en dicc_xgenx :
        (key):'titulo' (value):'titulo1'
        (key):'menuDvd' (value):(MenuDvd)menudvd_hijo
        (key):'padre' (value):'Menu_Titulos'
        (key):'ind_en_padre' (value): 2         (El lugar que ocupa en el padre)         
        """
        lst_hijos=[]
        for tit, padre_index in self.dicc_xgenx.items():
            if titulo == padre_index[PADRE_IND.PADRE.value]:
                menudvd_hijo = self.get_menudvd(titulo=tit)
                lst_hijos.append({  'titulo':tit,
                                    'menuDvd':menudvd_hijo, 
                                    'padre':titulo,
                                    'ind_en_padre':padre_index[PADRE_IND.INDEX.value]
                                })                
            pass
        pass    
        if lst_hijos: 
            return lst_hijos
        else: 
            return None        
    
    # ____________________________
    # DEVUELVE LAS LISTAS XA WEB
    def get_web_lsts_lens_linea(self, titulo, configurado=False, execFunc=True, tipo_marcador=0, execAll=True, Loop=True, padX=30):
        """ Devuelve lo que necesita la web para representarse 
        [titulo](str): El titulo del menu. (obligatorio                   )
        [configurado](bool): Si usa la configuración o muestra un menu simple de 1 nivel.
        [execFunc](bool): True, Se ejecutan las funciones. False, devuelve la resupuesta al usuario
        [tipo_marcador](0, 'a', 'A', 'A0')
        [execAll](bool)
        [Loop](bool)
        [padX](int)
        """
        # Valida Titulo Repetido y Existencia en la genetica(Config)
        if self.validacion_show(titulo=titulo, configurado=configurado) == False : return None
        """ C A C H A  EL  M E N U  """
        menu_dvd=self.get_menudvd(titulo=titulo)

        """ CONFIGURACION APLICADA? """
        if configurado == True and self.get_lst_dict_hijosX(titulo=menu_dvd.titulo):        #  PRINT SUB-MENUS 
            
            """ >>> GENERA LA  M A T R I Z   D E   I M P R E S I O N   """
            lst_skin = self.Mystyca_Skin(menu_dvd=menu_dvd)
            if not lst_skin: return None
            
            """ >>> IIIIIIIIIIIIIIIIIIIIIIIIII - CONFIGURACION GENETICA DE MySTyCA - IIIIIIIIIIIIIIIIIIIIIIII"""
            lst__men_itm_lev_ape_name_padr_ipadr = self.mystyca_ScannerXgenX(menu_dvd=menu_dvd)

            lst_level = [fila[2] for fila in lst__men_itm_lev_ape_name_padr_ipadr]
            """ >>> Lista de indentacion """

            """ CREACION DE LOS INDICES QUE SE PUEDEN MOSTRAR """
            (self.lst_opt_tipo_NUMERIC, 
            self.lst_opt_tipo_ALF_MAX, 
            self.lst_opt_tipo_ALF_MIN, 
            self.lst_opt_tipo_MIXTO) = self.create_INDICEX(lst__men_itm_lev_ape_name_padr_ipadr=lst__men_itm_lev_ape_name_padr_ipadr  )
            
            """ >>> L I S T A   DE  las  O P C I O N E S   V A L I D A S  en formato Texto para lst_skin """
            lst_Lst_Valid_Opt = self.set_tipos_indice_validos(tipo_marcador)            
            if not lst_Lst_Valid_Opt: return None
            lst_Str_Valid_Opt = [('.').join(lst_V) for lst_V in lst_Lst_Valid_Opt]
            pass          
            """ >>> El Remate del Punto Final.... es sólo Estética, superficialidad....pero tan necesaria en su justa medida :) """
            lst_Str_Valid_Opt_REMAT = [cadena+'.' for cadena in lst_Str_Valid_Opt]
            pass          
            self.set_lst_columna_skin(menu_dvd=menu_dvd, lst_skin=lst_skin, columna=2, lst_newValues=lst_Str_Valid_Opt_REMAT)            
            lst_mystyca_skin_result = [''.join(mystyca_fila) for mystyca_fila in lst_skin]
            """ >>> Lista de str que contiene: ALF + ' ' + Item_menu """
            pass
            # rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
            return lst_level , lst_mystyca_skin_result

        elif configurado == False:            
            """ >>> MUESTRA UN MENU DEL TIRON """            
            self.Mystyca_withOut(menu_dvd=menu_dvd, execFunc=execFunc)
        pass

    # _______________________________________________________________
    # IMPRIME LIST DE LIST DE STR (....para pruebas del desarrollo)
    def print_lst_List(self, lst_skin, numSP=16 , lst_titulos=None , titulo=''):
        if titulo: print(titulo)        
        # =====================================================
        # Configura el formato ______________________
        # lst_titulos=["-0-","-1-","-2-","-3-","-4-","-5-"]
        if not lst_titulos:
            lst_titulos = [f'-{i}-' for i in range(len(lst_skin[0]))]

        lst_titulos=self.igualarListas(listaKeys=lst_skin[0], listaToReLong=lst_titulos, valorRelleno='-Loren-')
        formato_fila=''
        # for i in range (len(lst_titulos)):
        for i in range (len(lst_skin[0])):
            formato_fila += "{:<" + str(numSP) + "}"    
        # Imprime titulos kernel ________________
        print(formato_fila.format(*lst_titulos))    
        print(f'{'-'*(len(lst_skin[0])*numSP)}')   
        # Imprime kernel ________________
        for lst_impr in lst_skin:
            print(formato_fila.format(*lst_impr))
        pass    
    
    # _____________________________________________________________________
    # OBTIENE UNA LISTA DE LOS VALORES DE LA COLUMNA PASADA en Mystyca-Skin.... DESDE 0.
    # Mystyca_Skin es una lista de lst_str <<lst_skin[fila][columna]>> Es una matriz.
    def get_lst_columna_skin(self, lst_skin, columna):
        """ lst_skin    = self.Mystyca_Skin(menu_dvd=menu_dvd) """
        # lst_rtrn = []
        # for fila in lst_skin:
        #     for i, col in enumerate(fila):
        #         if i == columna:
        #             lst_rtrn.append(col)
        #             break
        lst_rtrn=[ col  for fila in lst_skin for i, col in enumerate(fila) if i == columna]
        if lst_rtrn: return lst_rtrn

    # Pone valores de una lista en una columna.
    # .....para poner el nuevo indice en Mystyca_skin, que es la que se va a imprimir.
    # ......ese mismo nuevo indice es la numeracion absoluta que se tiene que checkear en Terminator.
    def set_lst_columna_skin(self, menu_dvd, lst_skin, columna, lst_newValues):
        lst_rtrn = []
        for i, lst_fila in enumerate(lst_skin):
            for j in range(len(lst_fila)):
                if j == columna:
                    lst_skin[i][j]=lst_newValues[i]
                    break        
    # ___________________________________________________________________
    # Cambia un valor en lst_skin(....no usada, pero la dejo pq me gusta.)
    def setV_skin(self, lst_skin ,fila,  columna, valor):
        lst_rtrn = []
        for i, lst_fila in enumerate(lst_skin):
            for j in range(len(lst_fila)):
                if i == fila and j == columna:
                    lst_skin[i][j]=valor
                    return valor
                    
# ============================================================================================
# ============================================================================================
# ============================================================================================
import threading        
import time         
from functools import partial    
# ============================================================================================
class Over_Main(XindeX):
    """ AMPLIA XindeX Añadiendo la ejecución en hilos separados.... >>> interactivo(tkinter) , 
                                                                    >> segundo plano demonio(flask) """
    def __init__(self):        
        super().__init__()
        self.hilos={}
        pass

    def Terminator(self, titulo_menu, item, respuesta, execFunc, pre_respuesta=None, post_respuesta=None):
        if pre_respuesta == None:
            super().Terminator(titulo_menu=titulo_menu, item=item, respuesta=respuesta, execFunc=execFunc)
        else:
            if pre_respuesta=='<<':
                self.ejecutar_background(titulo_menu=titulo_menu, item=item, respuesta=respuesta, execFunc=execFunc)

            elif pre_respuesta == '>>':
                self.ejecutar_interactivo(titulo_menu=titulo_menu, item=item, respuesta=respuesta, execFunc=execFunc)

            else:   
                try:
                    super().Terminator(titulo_menu=titulo_menu, item=item, respuesta=respuesta, execFunc=execFunc)
                except Exception as e:
                    print(f"Error en Terminator Over_Main: titulo_menu: {titulo_menu} -item: {item} -respuesta: {respuesta} -execFunc: {execFunc}, -pre_respuesta: {pre_respuesta} \n{e}")
            
    # ______________________________________
    """ >>> """
    def ejecutar_interactivo(self, titulo_menu, item, respuesta, execFunc):
        """ >>> Logica Interactiva: Tkinter por ejemplo (demon=False)  """
        print(f"Interacción activa con {respuesta}...")
        """ 
        CONFIGURO EL HILO LO GUARDO Y LO LANZO """
        hilo = threading.Thread(target=partial(super().Terminator, titulo_menu, item, respuesta, execFunc, None)
                                , daemon=False
                                )
        self.hilos[respuesta] = hilo
        hilo.start()

    # ______________________________________
    """ >> """
    def ejecutar_background(self, titulo_menu, item, respuesta, execFunc):
        """ >>> servidor Flask por ejemplo (demon=True) 
        """
        
        print(f"Tarea en segundo plano: item: {item} - index: '{respuesta}' ...... ejecutada.")

        """ 
        CONFIGURO EL HILO LO GUARDO Y LO LANZO """
        hilo = threading.Thread(target=self.ejecutar, kwargs={'titulo_menu': titulo_menu, 'item': item, 'respuesta':respuesta, 'execFunc':execFunc}
                                , daemon=True
                                )
        self.hilos[respuesta] = hilo
        hilo.start()

    # ______________________________________
    def ejecutar(self, titulo_menu, item, respuesta, execFunc):
        pass
        super().Terminator(titulo_menu=titulo_menu, item=item, respuesta=respuesta, execFunc=execFunc, pre_respuesta=None)
    
    # ______________________________________
    def detener_hilo(self, respuesta):
        if respuesta in self.hilos and self.hilos[respuesta].is_alive():

            # ?????????? cambiar por msgbox
            print(f"Deteniendo hilo '{respuesta}'...")
            # Aquí podrías implementar una señal de parada segura si es necesario
            del self.hilos[respuesta]
        else:
            print(f"Hilo '{respuesta}' no está en ejecución.")

    # ______________________________________
    def listar_hilos(self):
        print("Hilos en ejecución:")
        for opcion, hilo in self.hilos.items():
            estado = "activo" if hilo.is_alive() else "detenido"
            print(f"  - {opcion}: {estado}")
            aux = input(f'\nPulsa Cualquier tecla para continuar.... ')



