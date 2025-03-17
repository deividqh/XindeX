import os
import re
from Franky import F_r_a_n_k_y

""" 
    VARIABLES GLOBALES Y CONSTANTES 
"""
from enum import Enum as TYPE_XINDEX
class TYPEX(TYPE_XINDEX):
    NUMERIC = 0
    ALF_MAX = 10
    ALF_MIN = 20
    MIXTO   = 30

#Cte para cuando se pide la opcion al usuario.
SALIR='<<<'
REPETIR='<'
from enum import Enum as Column
class COL(Column):    
    LEVEL       = 0 ; A = 0      # (oblig) level genX
    APELL       = 1 ; B = 1      # (oblig) apellidos genX
    NOMBR       = 2 ; C = 2      # (oblig) nombre genX -
    PUNTO       = 3 ; D = 3      # (oblig) cte '.'
    SP_1        = 4 ; E = 4      # (oblig) espacio entre el index y el item. config en style
    ITEM        = 5 ; F = 5      # (oblig) Item - Contenido del Menu.
    SP_2        = 6 ; G = 6      # (opt) espacio mas grande entre el item y su definicion(hijo ó padre)
    DEFINITION  = 7 ; H = 7      # (opt) define si es hijo o padre - si es padre, en modo exec_all == False, no se ejecuta, solo se ejecutan los hijos.
    SP_3        = 8 ; I = 8      # (opt) Espacio entre la definicion y el nombre de la funcion a ejecutar.
    FUNCTION    = 9 ; J = 9      # (opt) str de la funcion a ejecutar.(opcional)

# ============================================================================================
# ============================================================================================
class MenuDvd():
    """ 
    Def: Define las partes esenciales de un menu Simple:  Head | Titulo | Cuello | Filas Body | Pie    
    Fila Body:  X_n__ | __n__ | __n_X | X_item__ | item | __item_X 
    """
    TAB = '    '        # CTE TABULADO.... usado para los LEVELS

    def __init__(self, titulo:str, lst_items:list, lst_funciones:list=None, fraseHead:str=''):               
        """ 
        CREA UN MENU. 
        UN MENU ESTÁ DEFINIDO POR:
            [titulo](str)
            [lst_items](list)  : Los Items(Elementos Visibles) del menu que el usuario tiene que seleccionar.
            [lst_funciones](list)  : Lista de Funciones asociadas a cada lst_items... pueden ser None si no tiene funcion asociada.
            [fraseHead](str)  : la frase que aparecerá en el titulo del Menu            
        """
        # ■■ RECOGE TITULO
        self.titulo     = titulo      # El titulo e indice del menu. aparece por defecto en el HEAD es el id del menu.

        # ■■ RECOGE LISTA DE ITEMS
        self.lst_items = lst_items      # cada item(str) es el contenido del Menu. CUERPO 
        
        # ■■ SI NO PASAS LST_FUNC (LAS FUNCIONES DE CADA ITEM), LAS INICIALIZO A NONE....DON'T WORRY :)
        if lst_funciones==None:
            self.lst_funciones=[None for i in range(len(self.lst_items))]
        else:
            self.lst_funciones   = lst_funciones              # La funcion que se pasa asociada por posicion al Item de lst_items
        
        # ■■ GENERA LA LISTA DE NUMERACION RELATIVA ( del ZERO al n )
        self.lst_index_rltv = [i for i in range(len(self.lst_items))]
        
        # ■■ VALIDACION DE TAMAÑO DE LISTAS. IGUALAR TODAS A:  self.lst_items      
        self.igualarListas(listaKeys=self.lst_items, listaToReLong=self.lst_funciones)
         
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■
        # DICCIONARIO RESULTADO ████  
        #   ■ {'titulo_menu': list( 'item_1_menu' , func_item_1 )  }   ==> Se genera 1 por Menu. 
        #   ■ Es de donde tiene que coger ■■► Terminator ◄■■ la informacion para ejecutar al funcion.
        self.dicc_menu = dict(zip(self.lst_items, self.lst_funciones))
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # PREPARA IMPRESION █████████████████████████████████████████████████████        
        self.F_RANK_Y = None        
        
        # ■■ LA FRASE QUE SE PONE EN LA IMPRESION DEL MENU(POR DEFECTO, EL TITULO):
        self.fraseHead = fraseHead if fraseHead != '' else self.titulo
        
        # ■■ MENSAJE DE PEDIDA DE DATO AL USUARIO
        self.introData = '\nIntro Opt (XindeX)..... '     
        
        
        # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        # CARGA LAS LISTAS DE BEFORE-AFTER
        self.lst__X_num=[]          # Lista de los caracteres que van antes del Numero del item.
        self.lst__num_X=[]          # Lista de los caracteres que van depues del Numero del item.
        self.lst__X_item=[]         # Lista de los caracteres que van antes del Item
        self.lst__item_X=[]         # Lista de los caracteres que van Despues del Item        
        
        for i in range(len(lst_items)):
            self.lst__X_num.append('')
            self.lst__num_X.append('')
            self.lst__X_item.append('')
            self.lst__item_X.append('')
    
    def __str__(self):                
        pass
    
    # VALIDA LA ESTRUCTURA DE ENTRADA (...llamada desde AddX)
    def valid_unpack(self, lst_items):
        """  
        ■■ Opcion 1:
        lst_titulos = ["Tit-1", "Tit-2" , "Tit-3" ]
        lst_FNC    = ["func-1", "func-2" , "func-3" ]

        ■■ Opcion 2:
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
    
    # CAMBIA EL ESTILO(CARACTERES DE CABECERA, PIE, PRE-NUM , POST-NUM)
    def style(self, introData='\nIntro Opt (XindeX)..... '):
        pass
    
    # Retorna 4 espacios
    def get_TAB(self):
        return self.TAB
    
    # STRING DEL CUERPO EN LINEA
    def get_str_Body(self):
        """ ■■ Def: Devuelve una cadena de impresion con el menu. un menu con cabecera, cuerpo y pie.
        [esNumerado]: Si quieres un menú numerado o no.
        """
        cuerpo=f''
        for i,item_menu in enumerate(self.lst_items):      
            cuerpo += (f'{ self.lst__X_num[i] }')           # 'Opt-'
            cuerpo += (f'{ self.lst_index_rltv[i] }')       # 1            
            cuerpo += (f'{ str(self.lst__num_X[i]) }')      # '-'
            cuerpo += (f'{ str(self.lst__X_item[i]) }')     # TAB('    ')
            cuerpo += (f'{ item_menu }')                    # 'Casa'
            cuerpo += (f'{ str(self.lst__item_X[i]) }')     # TAB + "Loren ipsum"
            """
            ■
            ■ la última iteracion no imprime el \n """
            cuerpo += (f'{'\n'}')  if i<(len(self.lst_items)-1) else ''

        return cuerpo
    
    # DEVUELVE UNA FILA DEL MENU
    def get_strRow_Body(self, row):
        """ ■■ Def: Devuelve una fila del menu. la que le pases. En formato f'' para poder ser impreso o .format()
        No incluye salir, Opt-0. La numeracion empieza en 1, pero la lista en 0 
        Opt-1-  Casa    Def:Loren ipsum
        """
        fila_menu=f''
        if 0 <= row < len(self.lst_items):
            for i , item_menu in enumerate(self.lst_items):            
                if i == row :
                    fila_menu += f'{ self.lst__X_num[i]}'         # 'Opt-'                   
                    fila_menu += f'{ self.lst_index_rltv[i] }'    # 1         
                    fila_menu += f'{ str(self.lst__num_X[i])  }'  # '-'
                    fila_menu += f'{ str(self.lst__X_item[i]) }'  # TAB('    ')
                    
                    fila_menu += f'{ item_menu }'                 # 'Casa'

                    fila_menu += f'{ str(self.lst__item_X[i]) }'  # TAB + 'Def: Loren ipsum'
                    
                    return fila_menu
            pass
    
    # El item de una fila
    def get_item_row_body(self, row):
        """ ■■ Def: Devuelve el ITEM de una fila  """
        fila_menu=f''
        if 0 <= row < len(self.lst_items):
            for i , item_menu in enumerate(self.lst_items):            
                if i == row :
                    return f'{ item_menu }'      
    
    # El item de una fila
    def get_numRltv_row_body(self, row):
        """ ■■ Def: Devuelve el ITEM de una fila  """
        fila_menu=f''
        if 0 <= row < len(self.lst_items):
            for i , numRltv in enumerate(self.lst_index_rltv):            
                if i == row :
                    return f'{ numRltv }'                    
    
    # ██ DEVUELVE UNA FILA self.lst_items... En formato lista(columnas).... llamada desde mystyca_skin
    def get_lst_row_body(self, row):
        """ ■■ Def: Devuelve una fila del menu. la que le pases. En formato f'' para poder ser impreso o .format()
        No incluye salir, Opt-0. La numeracion empieza en 1, pero la lista en 0 
        Opt-1-  Casa    Def:Loren ImprSkinpsum
        """
        fila_menu=[]
        if 0 <= row < len(self.lst_items):
            for i , item_menu in enumerate(self.lst_items):            
                if i == row :
                    fila_menu.append ( f'') 
                    fila_menu.append ( f'') 
                    fila_menu.append ( f'') 
                    fila_menu.append ( f'') 
                    fila_menu.append ( f'') 
                    fila_menu.append ( f'') 
                    fila_menu.append ( f'') 
                    fila_menu.append ( f'') 

                    return fila_menu
            pass
        pass
    
    # IGUALA LAS LISTAS
    def igualarListas(self, listaKeys, listaToReLong, valorRelleno='Loren'):
        """             
        Trata las longitudes de las listas y las igualo según listaKeys como referencia.
        La que se Re-dimensiona creciendo o decreciendo para igualarse con listaKeys.
        [valorRelleno]: en caso de que listaKeys>listaToRelong, hay que rellenar con un nuevo valor. en caso de funciones, None(by Def)
        [Ejemplo de uso]:
        ■■ listTOdict_byTcld_ToString.igualarListas(listaKeys=listaKeys, listaToReLong=listaTipos)        
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

class XindeX(MenuDvd):
    """ 
    ■■ Def: Gestiona una lista de menus y sub menus y los muestra por Terminal.
    instancia: ElMenuXX=XindiceX()
    add:    Añade un menu con dos listas, una de Titulos y otra Opcional de funciones a Exec con cada titulo en 1:1
    cofig:  Configura la Escalera del Indice: Menu|Padre|indice_en_el_padre
    View:   Muestra un Menu: 1-Con Genetica/Sin Genetica, 2-Vuelve/Se Ejecuta 3-Control Sobre Estilos 4-
    """ 

    def __init__(self, esLoop=True):
        """ ■■ Crea un menu Principal y gestiona una lista de menus secundarios que dependen del principal.
        [esLoop]: True=circular hasta Salida. | False=Sólo una ejecucion FALTA IMPLEMENTAR
        """        
        
        self.esLoop = esLoop  # ■■ Define si se sale por <<< o nos vale sólo para una ejecución...tb para definir mas adelante una última vuelta. 

        self.pasos=0    # ■■ Para las funciones recursivas Mystyca. Define las veces que se llama a la recursividad.

        self.lst_menuXX=[]  # ■■ Lista de objetos MenuDvd que mantiene un lst_items,  dicc_menu(num_n:[strMenu_n, func_n]) 
        self.lst_titulosXX=[]   # ■■ Lista de titulos de menu introducidos. Me permite validar rapido 
        self.lst_keys=[]    # ■■ Lista de items de menu introducidos. Me permite validar rapido 

        self.dicc_xgenx={}          # ■■ diccionario que mantiene la genealogía de los menus. titulo:[master, index_en_master]  
        self.lst__men_itm_lev_ape_name_padr_ipadr_func=[]    # ██ Lista de lista de str. Invocada desde Mystica. Funcion Recursiva
        self.matriz_opciones_validas=[]   # ■■ Listado de la pareja (item_en_mystica, respuesta valida). Se tiene que pasar a xavier_into_user()
        
        
        self.matriz_xindex=[]    # ES LA MATRIZ A IMPRIMIR.  # lista de lista de str. llamada desde Mystica en self.Mystica_Skin(). Funcion Recursiva
        
        # self.matriz_xindex = None  # matriz de filas x columnas de la impresion de mystyca.... para una impresion lst_max/csp [0,0,0,0,0] , ancho=None, sp_between = 0    

        self.lst_Impresion = []     # Lista de String con la impresion final de Mystyca. INCLUYE EL INDEXADO Y EL ITEM-MENU
        
        # TIPOS DE FORMATOS DE MENU.....  se forman en self.crear_xindicex() 
        self.lst_idx_NUMERIC=[]
        self.lst_idx_ALF_MAX=[]
        self.lst_idx_ALF_MIN=[]
        self.lst_idx_MIXTO=[]

        self.sp1 = 1    # separa index de item
        self.sp2 = 1    # separa item de definicion.... mejor largo que corto.... tiene que cambiar en funcion del maximo.
        self.sp3 = 2    # separa definicion de funcion

        self.lst_str_opciones_validas = None

        self.matriz_vacia = None  # ESTRUCTURA DE LA MATRIZ. 

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # 1-AÑADE UN MENU AL GESTOR... en forma lst_items=[it1, it2, ...]  lst_funciones=[f1, f2, ....] (no usar) (Crea un MenuDvd)
    def add(self, titulo, lst_items, lst_funciones=None):     
        """  Crea un Objeto MenuDvd"""
        if titulo in self.lst_titulosXX: 
            return False
        try:
            new_menu=MenuDvd(titulo=titulo, lst_items=lst_items, lst_funciones=lst_funciones)
        except Exception as e:
            print(e)
            return None
        self.lst_titulosXX.append(titulo)
        self.lst_menuXX.append(new_menu)
        # print(f'Load Menu {titulo} Ok ;)')
        return new_menu
    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # 2-CONFIGURA LA RELACION PADRE HIJO(INDICE) DEL MENU         (dicc_xgenx)
    def config(self, titulo, suPadre=None, indexInPadre=None): 
        """ ■■► Configura la relacion de los menus. ◄■■        
        Añade elementos a dicc_xgenx que es el diccionario que gestiona la genetica de XindeX

        [titulo](str): indice del menu. Nombre identificativo del Menú a configurar.
        [suPadre](str): 
        [indexInPadre](int, str): 
        """
        # VALIDA LA EXISTENCIA DEL TITULO .... self.lst_titulosXX   se carga   en self.addX()  antes 
        if not titulo in self.lst_titulosXX:   return None
        
        # ■■■ EN CASO DE QUE META UN INDICE DE CADENA DE TEXTO
        if isinstance(indexInPadre, str):
            b_match = False
            """ Puede ser que meta un item del menu al que quiere ir(item del padre) """
            menu_padre=self.get_menudvd(titulo = suPadre)
            if not menu_padre: 
                return None
            for i, item_en_padre in enumerate(menu_padre.lst_items):
                if str(item_en_padre).strip().upper() == str(indexInPadre).strip().upper():
                    indexInPadre = i
                    b_match = True
                    break
            pass
            if b_match == False: return None
        
        # ████████████████████████████████████████████████
        # ANALISIS DE LA GENETICA  ███████████████████████        
        if suPadre == None and indexInPadre == None:
            self.dicc_xgenx[titulo]=['-', '-']
            """ ■■ Es un puro Master!!!  """

        elif suPadre == None and indexInPadre != None:
            self.dicc_xgenx[titulo]=['-', '-']            
            """ ■■ Es un Master Fuerte pero confundido, le sobra el index """

        elif suPadre != None and indexInPadre == None:
            newIndex=self.__busca_index_free(titulo_key=titulo, master_buscado=suPadre)            
            """ ■■ Es un Sub Puro ????? esta machacando al anterior pq no da con el index libre"""
            if newIndex:
                self.dicc_xgenx[titulo]=[suPadre, newIndex]
            else:
                return False

        elif suPadre != None and indexInPadre != None and str(indexInPadre).isdigit():
            """ ■■ es un Sub Selector Puro y machaca todo lo que pilla."""
            self.dicc_xgenx[titulo]=[suPadre, indexInPadre]
        
        else:
            """ ■■ Error No posible, pero lo dejo por legible.....o no ;) """        


    # █████████████████████████████████████████████████████████████████████████████████
    # -AÑADE UN MENU AL GESTOR Y LO CONFIGURA.... ES ADD Y CONFIG EN LA MISMA FUNCION.
    # en forma (item_menu, funcion) (Crea un MenuDvd) (y si metes padre e ipadre se configura la genetica)
    def addX(self, titulo:str, lst_items:list=None, fraseHead:str='', padre:str=False, ipadre:str=None):             
        """ 
        [titulo]: Es el identificador del menu y sirve para la genetica.
        [lst_items]: (str, func) -> str es una cadena que será el texto en el menu. func puede ser None o el nombre de una funcion sin los parentesis.
        fraseHead:str='', El título del Menú.
        padre:str=False, Nombre del Menu Padre. Si se escribe, un Menu se declara como Hijo.
        ipadre:str=None, indice en el padre. puede ser int o str, pero recomiendo por claridad que sea el nombre del indice str.
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
            new_menu=MenuDvd(titulo=titulo, lst_items=lst_itemX, lst_funciones=lst_funcX, fraseHead=fraseHead)
            """ ■■ Se crea un objeto MenuDvd """
            # print(new_menu)
        except Exception as e:
            print(e)
            return None
        
        # Añade a la lista de titulos y a la lista de menus de XindeX
        self.lst_titulosXX.append(titulo)
        self.lst_menuXX.append(new_menu)
        # print(f'Load Menu {titulo} Ok ;)', end=' | ')

        
        # ■■ Code de: [padre] e [i_padre] como OPCIONALES
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

    # RETORNA UN OBJ MENUDVD POR MEDIO DE SU TITULO             (obtiene el MenuDvd )
    def get_menudvd(self, titulo:str):
        """ ■■ Retorna un objeto MenuDvd x su str titulo. """
        if titulo in self.lst_titulosXX:
            for menu in self.lst_menuXX:
                if str(menu.titulo) == str(titulo):
                    return menu
    # _________________
    # BUSCA INDEX FREE.                                         (Busca un indice libre)
    def __busca_index_free(self, titulo_key,  master_buscado ):
        """ ■■ Busca en el diccionario de configuracion << self.dicc_xgenx >> , un index libre(el siguiente). 
        Retorna: None si Error | indice para insertar si todo OK """
        lst_indexes=[]
        PADRE=0
        INDEX=1
        for tit_dicc, par_master_idx in self.dicc_xgenx.items():
            if master_buscado == par_master_idx[PADRE]:
                lst_indexes.append(par_master_idx[INDEX])
        
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
    
    # ███████████████████████████████████████████████████████████████████████████████
    # MUESTRA UN XINDEX.  (Imprime el menu con subMenus - Toma Control - Ejecuta Funciones)
    def Mystyca(self, titulo:str,  b_exe:bool=True, tipo_index:str=0, b_exec_all:bool=True, b_loop:bool=True, pad_x:int=30):
        """ 
        ■ [titulo]      Id del Menu Añadido/Configurado/Mostrados sus Items.

        ■ [b_exe]    True  ::: EJECUTA FUNCIONN .... en TERMINATOR  
                        False ::: RETORNA RESPUESTA

        ■ [tipo_index]  █  '1' = Numerico(byDef) █  'a' = Alfabetico Min █ 'A' = Alfabetico May  █ 'A1', '1A', a1, 1a =  Mixto
                           o bien: TIPEX.NUMERIC = 0 | TIPEX.ALF_MAX = 10 | TIPEX.ALF_MIN = 20 | TIPEX.MIXTO = 30

        ■ [b_exec_all] (bool)  True  ::: Solo se ejecutan ( o solo es OPCION-VALIDA) los subMenus Finales (no padres) 
                            False ::: Se ejecuta ( o solo es opcion valida) todo lo que no sea None en func.
                            ■ Si b_exe == False ::: No iterfiere pq b_exe se trata en TERMINATOR y b_exec_all se trata en Opcion_Valida(XAVIER)


        ■ [b_loop] (bool)     True  ::: SALES DEL MENÚ INTRODUCIENDO '<<<' 
                            False ::: SE PRESENTA EL MENU 1 VEZ Y SALE A MAIN.

        ■ [pad_x] (int)      Distancia entre el punto final del str del menu y el marco final.
        
        ■ Ejemplos:
            1.  retorno = The_X_Men.Mystyca(titulo='Menu1', b_exec_all=False, b_loop=True)
            2.  retorno = The_X_Men.Mystyca(titulo='Menu1', b_exe=True )
            3.  retorno = The_X_Men.Mystyca(titulo='Menu1', b_exe=True, tipo_index='1', b_exec_all=False, b_loop=True)
        """    
        # print('\n■■ MYSTYCA ■■')

        # ■■ VALIDA TITULO REPETIDO Y EXISTENCIA EN LA GENETICA(CONFIG)
        if titulo not in self.lst_titulosXX or titulo not in self.dicc_xgenx: 
            print(f'ERR-VAL:: {titulo} NO REGISTRADO EN XGENX')
            return None
        
        # ███ CACHA EL MENU A IMPRIMIR...es la base genetica sobre la que trabajamos1
        menu_dvd = self.get_menudvd(titulo = titulo)
        if not menu_dvd: return None
        
        # ████████████████████████████████████████████████████████████████████████████████████████████████████████████
        # ACTIONES GENETICAS █████████████████████████████████████████████████████████████████████████████████████████
        # ████████████████████████████████████████████████████████████████████████████████████████████████████████████  

        # ■■ listado de los items que aparecen en el menu genetico. en orden de aparicion en el menu.... de arriba a abajo.
        # ■■ GENERICA DE NUMERO DE FILAS           
        self.lst_keys = self.Mystyca_Keys( menu_dvd = menu_dvd )
        
        # CONFIGURACION DE MySTyCA ███████████████████████████████  
        self.lst__men_itm_lev_ape_name_padr_ipadr_func = self.mystyca_scaner_genetico( menu_dvd = menu_dvd )            

        # CREACION DE LOS INDICES ███████████████████████████████  
        self.lst_idx_NUMERIC, self.lst_idx_ALF_MAX, self.lst_idx_ALF_MIN, self.lst_idx_MIXTO = self.crear_xindicex(lst__men_itm_lev_ape_name_padr_ipadr_func = self.lst__men_itm_lev_ape_name_padr_ipadr_func  )
        """ ■■ Crea los diferentes TIPOS DE INDICE VALIDOS SEGÚN LA GENETICA: Alfabético, Numérico(by Def), Mixto """

        # MATRIZ DE OPCIONES VALIDAS ████████████████████████████
        # .... para llegar a obtener lst_Str_Valid_Opt_REMAT
        self.matriz_opciones_validas = self.__selecciona_xindex(type_XindeX = tipo_index)
        """ ■■ LISTA DE List de Str(Matriz) de las ■ OPCIONES OK!! 
            ...Esta lista hay que pasarla a  self.xavier_into_user() para las respuestas OK
            Es Lo que el usuario puede aceptar como entrada: pej ( 'a.1' , '1.1' , 'A.1' )
            
            [tipo_index]: '1' , 'A', 'a' , '1a' 'a1' + Enum TYPEX
        """            
        # ■■ LISTA  DE  las  OPCIONES  VALIDAS  en formato Texto para matriz_xindex
        if not self.matriz_opciones_validas: return None
        self.lst_str_opciones_validas = [('.').join(fila) for fila in self.matriz_opciones_validas]

        # ████████████████████████████████████████████████████████████████████████████████████████████████████████████
        # ACTIONES IMPRESION █████████████████████████████████████████████████████████████████████████████████████████
        # ████████████████████████████████████████████████████████████████████████████████████████████████████████████  
        
        numero_filas = len(self.lst_keys)
        numero_columnas = 9        
        
        # ■ Genero una matriz vacia que va a ser el molde sobre el que construir self.matriz_index
        self.matriz_vacia = [[0] * numero_columnas for _ in range(numero_filas)]

        # ██ MATRIZ DE IMPRESION
        self.matriz_xindex = self.get_matriz_impresion_literal(menu_dvd=menu_dvd, b_exec_all=b_exec_all, b_definicion=False)        
        if not self.matriz_xindex: return None        

        # LISTA DE STRING PARA IMPRIMIR 
        lst_mystyca_impresion = [''.join(mystyca_fila) for mystyca_fila in self.matriz_xindex]
        
        # ■■ LONGITUD MAXIMA DEL MENU
        longitud_max_xindex = max(len(line) for line in lst_mystyca_impresion)
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # IMPRIMIR XINDEX ■■■■■■■■■■■■■■■■■■■■■■■■■
        pie_datapush  = f'(Salir).... <<<  ■  (Help).... ?  ■  (Repeat).... <  ■  (Begin).... *opcion'
        head_datapush = " XINDEX - OVER-MAIN "

        filas = len(self.matriz_xindex)
        columnas = len(self.matriz_xindex[0])
        self.F_RANK_Y = F_r_a_n_k_y( dimension = f'{filas}X{columnas}', head_datapush = head_datapush , pie_datapush=pie_datapush , pad_x = 10 )
        # self.F_RANK_Y.push(data_push=self.matriz_xindex, blineal=False)
        self.F_RANK_Y.push(data_push=lst_mystyca_impresion, eje='Y')
        self.F_RANK_Y.imprimir(sp_between = 2, ancho_columna = None )


        # ████████████████████████████████████████████████████████████████████████████████████████████████████████████
        # ACTION RESPUESTA ███████████████████████████████████████████████████████████████████████████████████████████
        # ████████████████████████████████████████████████████████████████████████████████████████████████████████████  
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ████ LOOP = FALSE, 1 SOLA RESPUESTA Y VUELVES ████
        # ■■ lo gestiona el main( .... cualquier llamada ) 
        # ■■ [respuesta] es el indice lineal en lst_keys o self.lst__men_itm_lev_ape_name_padr_ipadr_func
        if b_loop == False:   
            # 
            #  XAVIER - OBTIENE RESPUESTA DE USUARIO █████████████████████████████████████
                # ■ respuesta es el indice en las listas de filas de xindex. 
                # ■ respuesta puede ser: 1- un index del menu ( a1 ), 2- una orden directa ( ? , <<<, < ) , 3- una respuesta envuelta( *a1 , <<a1>> )
            respuesta, pre_respuesta = self.xavier_into_user(menu_dvd = menu_dvd , 
                                                                lst_Valid = self.matriz_opciones_validas, 
                                                                longitud_max_xindex = longitud_max_xindex , 
                                                                b_exec_all=b_exec_all, 
                                                                mystica_skin_str=lst_mystyca_impresion )    
            if respuesta == None:       # SALIR... ha pulsado '<<<'. Esto anula el menu, pq se ejecuta una sola vez.
                return                  # Sale por Main(....por donde es llamada)
            else:
                # print(f'\nRespuesta encontrada en {respuesta}: {self.lst__men_itm_lev_ape_name_padr_ipadr_func[int(respuesta)][1]} ')                
                
                # TERMINATOR - EJECUTA ██████████████████████████████████████████████████
                titulo_menu = self.lst__men_itm_lev_ape_name_padr_ipadr_func[int(respuesta)][0]
                item_menu   = self.lst__men_itm_lev_ape_name_padr_ipadr_func[int(respuesta)][1]
                return self.Terminator(titulo_menu=titulo_menu, item=item_menu, pre_respuesta=pre_respuesta, respuesta=respuesta, b_exe=b_exe )    
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ████ LOOP = TRUE, SALES POR <<< ████
        while(True):
            # XAVIER - OBTIENE RESPUESTA VALIDA DEL USUARIO, O SALIR ████████████████████
            respuesta, pre_respuesta = self.xavier_into_user( menu_dvd = menu_dvd, 
                                                                lst_Valid = self.matriz_opciones_validas, 
                                                                longitud_max_xindex = longitud_max_xindex, 
                                                                b_exec_all = b_exec_all , 
                                                                mystica_skin_str = lst_mystyca_impresion
                                                                )   
            # ANALIZA LA RESPUESTA QUE VIENE DE XAVIER
            if respuesta == None and pre_respuesta==None:       # SALIR... ha pulsado '<<<'
                return True                                     # Sale por Main(....por donde es llamada)
            else:       
                # ■ IMPRIME EL ITEM DE LA RESPUESTA EN EL PROMPT
                print(f'   [{respuesta}] :) {self.lst__men_itm_lev_ape_name_padr_ipadr_func[int(respuesta)][1]} ', end='| -> ')
                
                # CACHA EL TITULO DEL MENU Y EL ITEM PARA PASARLO A TERMINATOR Y EJECUTAR LA FUNCION ASOCIADA.
                titulo_menu = self.lst__men_itm_lev_ape_name_padr_ipadr_func[int(respuesta)][0]
                item_menu   = self.lst__men_itm_lev_ape_name_padr_ipadr_func[int(respuesta)][1]
                
                # TERMINATOR - EJECUTA ██████████████████████████████████████████████████
                self.Terminator(titulo_menu = titulo_menu, 
                                item = item_menu, 
                                pre_respuesta = pre_respuesta, 
                                respuesta = respuesta, 
                                b_exe = b_exe
                                )    

    # █████████████████████████████████████████████████████████████
    # RCRSV: LISTA con Todos los items en orden de impresion.██████
    def Mystyca_Keys(self, menu_dvd, level=None, retorno=None):
        """  """
        if level==None and retorno==None:     # 1ª ENTRADA
            level=-1 ; retorno=[] ; self.pasos=0 
        level += 1 ; self.pasos += 1
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        lst_hijos = self.__get_lst_dict_hijosX(titulo=menu_dvd.titulo)        
        if  lst_hijos:         
            for i in range(len(menu_dvd.lst_items)):                
                retorno.append(menu_dvd.get_item_row_body(i))                
                for hijo in lst_hijos:
                    if hijo['ind_en_padre'] == i:                        
                        self.Mystyca_Keys(menu_dvd=hijo['menuDvd'] , level=level, retorno=retorno)
                        break    
        elif not lst_hijos:    
           for i, item in enumerate(menu_dvd.lst_items):                    
                retorno.append(item)
                
        # ___________________________________
        return retorno

    # █████████████████████████████████████████████████████████████████████
    # RCRSV: IDENTIFICA PADRES DE HIJOS ███████████████████████████████████
    def get_list_padres_mystyca(self, menu_dvd, level=None, retorno=None ):
        if level==None and retorno==None:     # 1ª ENTRADA
            level=-1   ; retorno=[] ; self.pasos=0 
        level += 1
        self.pasos+=1
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        lst_hijos = self.__get_lst_dict_hijosX(titulo=menu_dvd.titulo)        
        if  lst_hijos:         
            for i in range(len(menu_dvd.lst_items)):
                for hijo in lst_hijos:
                    if hijo['ind_en_padre'] == i:                        
                        retorno.append(menu_dvd.get_item_row_body(row=i))                
                        self.get_list_padres_mystyca(menu_dvd=hijo['menuDvd'] , level=level, retorno=retorno)
                    pass
        elif not lst_hijos:
           for i, item in enumerate(menu_dvd.lst_items):
                pass 
        return retorno

    # R C R S V •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• SIN USO
    def Mystyca_Skin(self, menu_dvd, level=None, retorno=None):
        """  """
        if level==None and retorno==None:     # 1ª ENTRADA
            level=-1 ;  retorno=[] ; self.pasos=0 
        level += 1
        self.pasos+=1
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        lst_hijos = self.__get_lst_dict_hijosX(titulo=menu_dvd.titulo)        
        if  lst_hijos:         
            bmatch=False
            for i, item in enumerate(menu_dvd.lst_items):
                retorno.append(menu_dvd.get_lst_row_body(row=i))
                for hijo in lst_hijos:
                    if hijo['ind_en_padre'] == i:                        
                        self.Mystyca_Skin(menu_dvd=hijo['menuDvd'] , level=level, retorno=retorno)
        elif not lst_hijos:
            for i, item in enumerate(menu_dvd.lst_items):
                retorno.append(menu_dvd.get_lst_row_body(row=i))
        return retorno
    
    # R C R S V •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• SIN USO
    def Mystyca_XgenX(self, menu_dvd, level=None, retorno=None, tituloMaster=None):
        """ Recorre el arbol de Menus y devuelve un lst [nombreMenu, lista impresion, level, nombrePadre, indice_en_Padre]
        Usa principalmente lst_items y dicc_xgenx para """
        if level==None and  retorno==None:     # 1ª ENTRADA
            level=-1            
            retorno=[]
            self.pasos=0
            tituloMaster=menu_dvd.titulo
        level += 1
        self.pasos+=1
        lst_hijos = self.__get_lst_dict_hijosX(titulo=menu_dvd.titulo)        
        if  lst_hijos:         
            bmatch=-1
            for i in range(len(menu_dvd.lst_items)):
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
            for i in range(len(menu_dvd.lst_items)):
                retorno.append((menu_dvd.titulo, 
                                menu_dvd.get_strRow_Body(row=i, esNumerado=True), 
                                level, 
                                self.get_padre(titulo=menu_dvd.titulo), 
                                self.get_ind_en_padre(titulo=menu_dvd.titulo)
                                ))
                # print(menu_dvd.get_strRow_Body(row=i, esNumerado=True))

        return retorno

    # █████████████████████████████████████████████████████████████████████████████████████
    # RCRSV:  DATOS POR FILA DE IMPRESION  ████████████████████████████████████████████████
    def mystyca_scaner_genetico(self, menu_dvd, level=None,  retorno=None, apellido=None):
        """ 
        [menu_dvd], 
        [level]=None,    No se pasa en la llamada. se pasa en la recursividad
        [retorno]=None,  No se pasa en la llamada. se pasa en la recursividad
        [apellido]=None, No se pasa en la llamada. se pasa en la recursividad
        """
        if level==None and retorno==None:     # 1ª ENTRADA
            level=-1 ; retorno=[]  ;  apellido='' 
        level += 1 
        """ Contadores """
        lst_dict_hijosX = self.__get_lst_dict_hijosX(titulo=menu_dvd.titulo)      
        """ Tengo al padre(menu_dvd, y a los hijos(lst_dict_hijosX)) 
        """  
        if  lst_dict_hijosX:         
            apellido += str(level) + '.'
            for i in range(len(menu_dvd.lst_items)):
                item = menu_dvd.get_item_row_body(i)

                funcion_name = self.__get_funcion_name(menu_dvd=menu_dvd, item=item)
                retorno.append(( menu_dvd.titulo ,                                  
                                item , 
                                level , 
                                apellido , 
                                menu_dvd.get_numRltv_row_body(i) ,
                                self.get_padre(titulo_menu=menu_dvd.titulo) , 
                                self.get_ind_en_padre(titulo_menu=menu_dvd.titulo) , 
                                # funcion_name 
                                menu_dvd.dicc_menu.get(item, None)
                                ))
                                
                for hijo in lst_dict_hijosX:
                    if hijo['ind_en_padre'] == i:                        
                        # ■■■■■■■■■■■■■■■■■■■■■■■■
                        self.mystyca_scaner_genetico(menu_dvd=hijo['menuDvd'] , level=level,  retorno=retorno, apellido=apellido)
                    pass
        elif not lst_dict_hijosX:
            apellido += str(level) + '.'
            aux = apellido
            for i, item in enumerate(menu_dvd.lst_items):
                
                funcion_name = self.__get_funcion_name(menu_dvd=menu_dvd, item=item)

                retorno.append(( menu_dvd.titulo ,                                  
                                item , 
                                level , 
                                apellido , 
                                menu_dvd.get_numRltv_row_body(i) ,
                                self.get_padre(titulo_menu=menu_dvd.titulo) , 
                                self.get_ind_en_padre(titulo_menu=menu_dvd.titulo)  , 
                                # funcion_name
                                menu_dvd.dicc_menu.get(item, None)
                                ))
                apellido = aux
        return retorno    
    
    def __get_funcion_name(self, menu_dvd, item):
        if not isinstance(menu_dvd, MenuDvd): return None
        funcion = menu_dvd.dicc_menu.get(item, None)
        if funcion:
            if callable(funcion):
                funcion_name = funcion.__name__
            else:
                funcion_name = str(funcion)
        else:
            funcion_name = f'( - )'
        # RETORNO
        return funcion_name
    
    # ██████████ CUANDO PULSA '?' , IMPRIME EL MENU CON INFORMACION SOBRE LA CONFIGURACION ████████
    def get_mystyca_informacion(self, titulo_menu, lst_padres , lst_hijos, b_exec_all, longitud_max_xindex):
        """ CUANDO SE PULSA '?' , IMPRIME EL MENU CON INFORMACION SOBRE LA CONFIGURACION 
        [titulo_menu], 
        [lst_padres] , 
        [lst_hijos], 
        [b_exec_all], 
        [longitud_max_xindex]
        RETORNO:

        """
        frase_head_aux = self.get_menudvd(titulo = titulo_menu).fraseHead
        menu_dvd = self.get_menudvd(titulo = titulo_menu)
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        lst_definicion_item  = self.get_lst_definiciones( menu_dvd = menu_dvd, lista_genetica_x_fila =self.lst__men_itm_lev_ape_name_padr_ipadr_func, b_exec_all = b_exec_all )
        lst_funcion_item = self.get_lst_funciones( lista_genetica_x_fila = self.lst__men_itm_lev_ape_name_padr_ipadr_func )
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

        # ██ MATRIZ DE IMPRESION
        matriz_xindex = self.get_matriz_impresion_literal(menu_dvd=menu_dvd, b_exec_all=b_exec_all, b_definicion=True)

        # CREA una Lista de Strings con cada linea completa A IMPRIMIR....es la Transformacion
        lst_mystyca_impresion = [''.join(mystyca_fila) for mystyca_fila in matriz_xindex]          
        
        # Calculo las longitudes al mm para que cuadre con las mismas diemnsiones que el menu-Ppal
        if b_exec_all == True: 
            self.F_RANK_Y.head.push(data_push="  ", celda_inicio='D:0')
            self.F_RANK_Y.head.push(data_push=["  ", " ■  MODE ::: Exec All"], celda_inicio='D:0', b_lineal=True)
        else:
            self.F_RANK_Y.head.push(data_push=["  ", " ■  MODE ::: Exec (X)"], celda_inicio='D:0', b_lineal=True)
        
        self.F_RANK_Y.iniciar()
        self.F_RANK_Y.push(data_push=lst_mystyca_impresion, eje='Y')
        self.F_RANK_Y.imprimir(sp_between = 2, ancho_columna = None )

        self.F_RANK_Y.iniciar()
        matriz_xindex = self.get_matriz_impresion_literal(menu_dvd=menu_dvd, b_exec_all=b_exec_all, b_definicion=False)
        lst_mystyca_impresion = [''.join(mystyca_fila) for mystyca_fila in matriz_xindex]          
        self.F_RANK_Y.push(data_push=lst_mystyca_impresion, eje='Y')
    
    # ■■■ OBTIENE LA LISTA DE DEFINICIONES (B_EXEC_ALL)    
    def get_lst_definiciones( self, menu_dvd, lista_genetica_x_fila:list, b_exec_all:bool ):
        """ ■■ Devuelve LA Lista de Definicion (padre or hijo)(directorio or punta)
        [lista_genetica_x_fila](list) , self.lst__men_itm_lev_ape_name_padr_ipadr_func
        [b_exec_all](bool), self.b_exec_all
        """
        # OBTENEMOS LA LISTA DE PADRES GENETICOS
        lst_padres  = self.get_list_padres_mystyca(menu_dvd = menu_dvd)
        lst_definicion_item=[]
        for i, fila_genetica in enumerate(lista_genetica_x_fila):
            # ■ DEFINICION
            if b_exec_all == True: 
                lst_definicion_item.append (f'(D)' if fila_genetica[1] in lst_padres else f'(X)')
            else:
                lst_definicion_item.append (f'(-)' if fila_genetica[1] in lst_padres else f'(X)')
        
        # RETORNO
        return lst_definicion_item if lst_definicion_item else None
    
    # ■■■ OBTIENE LA LISTA DE LAS FUNCIONES SEGÚN EL ORDEN GENETICO
    def get_lst_funciones( self, lista_genetica_x_fila:list ):
        lst_funcion_item=[]
        for i, fila_genetica in enumerate(lista_genetica_x_fila):
            # ■ FUNCIONES EXE
            menu_dvd = self.get_menudvd(titulo = fila_genetica[0])
            funcion = menu_dvd.dicc_menu.get(fila_genetica[1])

            if callable(funcion):
                lst_funcion_item.append(f' ({str(funcion.__name__)})')
            else:
                lst_funcion_item.append(' ( - ) ')

        # RETORNO
        return lst_funcion_item if lst_funcion_item else None
       
    # ████ FROM nombre-titulo-Menu TO nombre-padre     
    def get_padre(self, titulo_menu):
        PADRE=0
        INDEX=1
        if self.dicc_xgenx:
            for tit, padre_index in self.dicc_xgenx.items():
                if titulo_menu == tit: 
                    if padre_index[PADRE]:
                        return padre_index[PADRE]
                    else:
                        return None

    # ████ FROM nombre-titulo TO indice en el padre
    def get_ind_en_padre(self, titulo_menu):
        PADRE=0
        INDEX=1
        if self.dicc_xgenx:
            for tit, padre_index in self.dicc_xgenx.items():
                if titulo_menu == tit: 
                    if padre_index[PADRE]:
                        return padre_index[INDEX]
                    else:
                        return None

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # XAVIER  pide datos al Usuario y le saca un Dato por Teclado ██████████
    def xavier_into_user(self, menu_dvd, lst_Valid, longitud_max_xindex, b_exec_all=None, mystica_skin_str=None):
        """ ■■ Def: Pide Un dato al Usuario y valida que da una respuesta valida con respecto a la geneticaX
        [menu_dvd] : el objeto MenuDvd (principal) sobre el que se trabaja. el punto de partida del analisis... Menu1
        [lst_Valid] : lista con las respuestas validas generadas en self.crear_xindicex()
        [longitud_max_xindex] : la longitud maxima de matriz_xindex en str.
        [b_exec_all] : (bool) True = en todos los items intento ejecutar la funcion. False=Los directorios no se ejecutan.
        [mystica_skin_str] : (list), es matriz_xindex convertida linea a linea en str.

        Retorno: None, <<< salir | indice en lst_keys() y casi todos los lst_ de la clase.
        """
        pass
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # LISTA DE LOS   P A D R E S   DEL MENU (RCRSV) ■■■■■■■ ....Usado para saber si tiene exec o son directorio.
        lst_padres  = self.get_list_padres_mystyca(menu_dvd=menu_dvd)        
        lst_hijos   = [ hijo for hijo in self.lst_keys if hijo not in lst_padres]
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # LISTAS DE   O P C I O N E S - V A L I D A S 
        # .... Esto vale para que cualquier conbinacion sea valida: b2, b:2, b;2 b,2 b.2... por parte del usuario
        lst_valid_10 = [ ('').join(fila) for fila in lst_Valid   ]
        lst_valid_20 = [ ('.').join(fila) for fila in lst_Valid  ]
        lst_valid_25 = [ cadena+'.' for cadena in lst_valid_20   ]        
        lst_valid_40 = [ (' ').join(fila) for fila in lst_Valid  ]
        lst_valid_50 = [ ('-').join(fila) for fila in lst_Valid  ]
        lst_valid_55 = [ cadena+'-' for cadena in lst_valid_50   ]
        lst_valid_60 = [ (':').join(fila) for fila in lst_Valid  ]
        lst_valid_65 = [ cadena+':' for cadena in lst_valid_60   ]
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # BUCLE HASTA OPCION VALIDA O SALIR +  ANALISIS  DE LAS  RESUPUESTAS
        respuesta=None
        dicc_xavier = {}

        while(True):
            respuesta_extraida =''
            pre_respuesta =''
            pos_respuesta =''

            respuesta = input(f"{menu_dvd.introData}").strip()
            try:
                if respuesta == SALIR:          # ██ A PULSADO  '<<<' ....SALIR                    
                    dicc_xavier['pre'] = None
                    dicc_xavier['respuesta'] = None
                    dicc_xavier['pos'] = None

                    return None , None

                elif respuesta == '<':  # ██ IMPRIME EL MENU Y VUELVE A PEDIR DATO AL USUARIO.
                    
                    os.system('cls')              
                    self.F_RANK_Y.imprimir(sp_between = 2, ancho_columna = None )             

                elif respuesta == '?':  # ██ VER INFORMACION DE MENU - FUNCIONES QUE SE EJECUTAN.                                        

                    lst_impr_info = self.get_mystyca_informacion( titulo_menu   = menu_dvd.titulo , 
                                                                    longitud_max_xindex  = longitud_max_xindex , 
                                                                    lst_padres  = lst_padres , 
                                                                    lst_hijos   = lst_hijos , 
                                                                    b_exec_all  = b_exec_all
                                                                    )
                                    
                elif respuesta.startswith("<<") and respuesta.endswith(">>"):       # ██ BACKGROUND :   Acaba cuando yo me acabe (demonio)
                    # Extraigo el contenido entre '<<' y '>>'
                    dicc_xavier['pre'] =  respuesta[:2].strip()         # Desde el inicio(0) hasta 1(2-1) <<
                    dicc_xavier['respuesta'] = str(respuesta[2:-2]).strip()
                    dicc_xavier['pos'] = respuesta[2:].strip()          # Desde 2 hasta final >>

                    respuesta_extraida = str(respuesta[2:-2]).strip()
                    pre_respuesta  = respuesta[:2].strip()   # Desde el inicio(0) hasta 1(2-1) <<
                    post_respuesta = respuesta[2:].strip()   # Desde 2 hasta final >>

                    # if pre_respuesta == '<<' and pos_respuesta == '>>':
                    if dicc_xavier['pre'] == '<<' and dicc_xavier['pos'] == '>>':
                        print(f"Contenido extraído: {respuesta_extraida}")               
                    print('MODO BACKGROUND.... en proceso WIP')

                elif respuesta.startswith(">>"):        # ██ MODO INTERACTIVO   (no demonio)(tkinter o si quieres que siga la ejecución aunque yo me acabe)
                    respuesta_extraida = respuesta[2:].strip()                  #Desde la posicion 2 hasta el final . respuesta!!.
                    pre_respuesta = respuesta[:2].strip()                       # Desde el inicio(0) hasta 1(2-1) >>
                    print(' MODO INTERACTIVO  .... en proceso WIP')
                    
                    dicc_xavier['pre'] = respuesta[:2].strip()
                    dicc_xavier['respuesta'] = respuesta[2:].strip() 
                    dicc_xavier['pos'] = None

                elif respuesta.startswith('**'):        # ██ MODO REDUCIDO (FROM FILA TO FILA) (SOLO LOS QUE EMPIECEN POR ■ a ó ■ a1 ó ■ a1 y b1) 
                    
                    respuesta_extraida = respuesta[2:].strip()   #Desde la posicion 2 hasta el final . respuesta!!.
                    pre_respuesta = respuesta[:2].strip()   # Desde el inicio(0) hasta 1(2-1) >>
                    print('Modo Directorio .... en proceso WIP')

                    dicc_xavier['pre'] = pre_respuesta
                    dicc_xavier['respuesta'] = respuesta_extraida
                    dicc_xavier['pos'] = None
            except Exception as e:      # SI ERROR, INFO Y SEGUIMOS ::::
                print(f'ERROR RESPUESTA ::: {e}')
                continue
            try:
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                #   V A L I D A C I O N   ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                
                # Verifica/Valida que hay una respuesta y que se ha introducido '>>'
                if respuesta_extraida != '' and pre_respuesta == '>>':
                    respuesta = respuesta_extraida

                # Verifica/Valida que hay una respuesta y que se ha introducido '<<'
                if respuesta_extraida != '' and pre_respuesta == '<<':
                    respuesta = respuesta_extraida    
                
                # Verifica/Valida que hay una respuesta y que se ha introducido '**'
                if respuesta_extraida != '' and pre_respuesta == '**':
                    respuesta = respuesta_extraida    
                
            except Exception as e:  # SI ERROR, INFO Y SEGUIMOS ::::
                print(f'ERROR VALIDACION ::: {e}')
                continue
            try:
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                #   EVALUACION DE LA RESPUESTA ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                listas_validas = [
                    lst_valid_10, lst_valid_20, lst_valid_25, 
                    lst_valid_40, lst_valid_50, lst_valid_55, 
                    lst_valid_60, lst_valid_65
                ]
                
                bSalir=False                            # Se pone a True para salir del bucle FOR.
                # RECORRO TODAS LAS LISTAS VALIDAS EN BUSCA DE UN MATCH CON RESPUESTA
                for lista in listas_validas:
                    if respuesta in lista:
                        for i, str_indice in enumerate(lista):
                            if respuesta == str_indice:                 # ■■ MATCH

                                elect, item_menu = self.__separar_cadena(str(mystica_skin_str[i]).strip())
                                 
                                # ████████████████████████████████████████████████████████████████████
                                # ■■ MODO DE OPCION VALIDA( b_exec_all = True | False =  solo HIJOS exec                                  
                                if b_exec_all == None: 
                                    b_exec_all = True
                                if isinstance(b_exec_all, bool):
                                    if b_exec_all == True:     # ■■ Todo son opciones validas(HIJOS Y PADRES).... responsabilidad del usuario meter funciones en directorios.
                                        return i , None     # ■■ ENCUENTRA Y RETORNA EL INDICE EN LST_KEYS!!!!!!!!!   :) 
                                    else:                   # ■■ Solo los Hijos son validos. Los Directorios No se pueden Ejecutar en b_exec_all==False
                                        if item_menu in lst_padres:                                            
                                            print('(Directorio) ', end=' ')
                                            bSalir=True
                                            break        # Si encuentra un padre, no vale como respuesta valida y vuelve a preguntar.
                                        else:
                                            return i , pre_respuesta   # No es un padre.
                                        pass
                                else:
                                    b_exec_all = True
                                pass                               
                    else:   # print("Respuesta no encontrada.")                        
                        pass                    
                    if bSalir == True:
                        bSalir = False
                        break
                pass
            except Exception as e:      # SI ERROR, INFO Y SEGUIMOS ::::
                print(f'ERROR EVALUACION ::: {e}')
                continue

        # RETORNO ██████ 
        if respuesta_extraida is not None and pre_respuesta is not None:    # HAY RESPUESTA Y PRE-RESPUESTA: **b2, <<b2>>, >>b2
            if respuesta_extraida == respuesta: 

                return respuesta_extraida, pre_respuesta
            else:
                return respuesta , pre_respuesta
        else:                                           # SOLO HAY RESPUESTA: < , <<<, ? , b2, a11, ...
            return respuesta , None

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # INDICEXXXX █████████████████████████████████████████████████████
    def crear_xindicex(self, lst__men_itm_lev_ape_name_padr_ipadr_func ): 
        """ 
        ALGORITMO INFERNAL PARA SACAR LOS INDICES CORRECTOS EN LA FORMA [1, 0, 1, 2] (camino de levels)
        ■ Este retorno Se Corresponde con el level sacado de en la funcion recursiva. 
        ■ Marca la posicion que va a tener y la numeracion con respecto a esa posicion.
        ■ Se basa en la creación de la lista del indice numerico y a partir de él crea los otros índices.
        ......una pesadilla que me ha llevado días :()

        ■ [lst__men_itm_lev_ape_name_padr_ipadr_func]: lst de datos que se saca de self.mystica_ScannerX()
        
        ■ Retorno:  None. Alimenta y llena los las listas de listas(que son la numeracion y posicion en el menu.):
                    lst_idx_NUMERIC    |  lst_idx_ALF_MAX | lst_idx_ALF_MIN | lst_idx_MIXTO
        
        ■ [NUMERICA-JERARQUICA]
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
        ■ RESULTADO 
            [0,1,2,2,1,2,2,0,1,1]
        """
        import string
        import copy

        MENU  = 0 ; ITEM  = 1 ; LEVEL = 2 ; APELL = 3 ; NAME = 4 ; PADRE = 5 ; ID_PADRE = 6
        
        dicc_min =  {idx:letra for idx, letra in enumerate(string.ascii_lowercase)} 
        dicc_may =  {idx:letra for idx, letra in enumerate(string.ascii_uppercase)}        
        
        lst_name = [ ( int(lst_a[NAME]) + 1 ) for lst_a in self.lst__men_itm_lev_ape_name_padr_ipadr_func ]
        """ ■■ Lista de los nombres relativos de cada Item + 1 """
        
        # ■■ LISTA DE APELLIDOS (INDEXACION ANTERIOR A LA SUYA.)
        lst_split_apellido = [ str(lst_a[APELL]).split(sep='.')  for lst_a in self.lst__men_itm_lev_ape_name_padr_ipadr_func ]        

        # ..... del split sale con una dimensión de más(la del '.') y así lo ajusto a su dimension:
        for lst_apellido in lst_split_apellido:
            lst_apellido.pop()
        
        for lst_apellido in lst_split_apellido:
            for apellido in lst_apellido:
                apellido = int(apellido)
        # .... (La long de la list lst_apellido y  el level del item son directmnt proporcionales).

        # NUMERICO  LISTA DEL NOMBRE-FINAL-TOTAL ████████████ 
        lst_idx_NUMERIC=[]          # Lista resultado final
        ind_Master=1                     
        ind_Sub = 1

        for i, lst_apellido in enumerate(lst_split_apellido):

            if len(lst_apellido) == 1 and i == 0:           # 1ª VEZ Menu PPal = fija ind_Master.                  
                lst_idx_NUMERIC.append([ind_Master])   # Add
                ind_Master += 1  
                ind_Sub     = 1          # Aumento el Master  y Re-inicio para los subMenus                                             
            else:
                actual = self.lst__men_itm_lev_ape_name_padr_ipadr_func[i]
                anterior = self.lst__men_itm_lev_ape_name_padr_ipadr_func[i-1]            
                if len(lst_apellido) == 1:                  # solo Masters ... actual[PADRE]=='-'
                    lst_idx_NUMERIC.append([ind_Master])
                    ind_Master += 1  ;    ind_Sub     = 1 
                    continue
                # ______________
                if actual[LEVEL] != anterior[LEVEL]:    # ■■ CAMBIO DE NIVEL ■■■

                    ind_Sub = 1                         # 1º reinicio sub

                    if actual[LEVEL] > anterior[LEVEL]:     # .... Hacia Abajo(Hijo)                        
                        lst_idx_NUMERIC.append(lst_idx_NUMERIC[i-1] + [ind_Sub] )
                        ind_Sub += 1    
                    else:                                   # .... Hacia Arriba( padre, abuelo... pero NO el master).                                                    
                        lvl_ref = int(actual[LEVEL] ) + 1
                        
                        # RECORRO LA LISTA AL REVES ■
                        for j, path in enumerate(lst_idx_NUMERIC[::-1]):        
                            if len(path) == lvl_ref:
                                nuevo_path = path[:-1] + [path[-1] + 1]                         
                                lst_idx_NUMERIC.append( nuevo_path )
                                break
                        pass
                else:       # ■■■ MISMO NIVEL ■■■                                        
                    # AL ANTERIOR ELEMENTO(i-1): LO EMPIEZO POR EL FINAL(anterior_item[:-1]), LE QUITO 1 Y LE SUMO 1 AL ULTIMO ELEMENTO ( [anterior_item[-1] + 1] )
                    anterior_item = lst_idx_NUMERIC[i-1]
                    lst_idx_NUMERIC.append( anterior_item[:-1] + [anterior_item[-1]+1]  )

        """  
        ::::::: A L F - M A X   """
        lst_idx_ALF_MAX = copy.deepcopy(lst_idx_NUMERIC)
        for lst_path in lst_idx_ALF_MAX:
            lst_path[0] = dicc_may[int(lst_path[0])-1]
        """ 
        ::::::: A L F - M I N  """
        lst_idx_ALF_MIN = copy.deepcopy(lst_idx_NUMERIC)
        for lst_path in lst_idx_ALF_MIN:
            lst_path[0] = dicc_min[int(lst_path[0])-1]
        """  
        ::::::: M I X T O """
        lst_idx_MIXTO = copy.deepcopy(lst_idx_NUMERIC)
        for lst_path in lst_idx_MIXTO:
            lst_path[0] = dicc_may[int(lst_path[0])-1]
            try:                
                lst_path[2] = dicc_min[int(lst_path[2])-1]
            except:
                continue
        
        lst_idx_NUMERIC = [[str(element) for element in sublist] for sublist in lst_idx_NUMERIC]
        lst_idx_ALF_MAX = [[str(element) for element in sublist] for sublist in lst_idx_ALF_MAX]
        lst_idx_ALF_MIN = [[str(element) for element in sublist] for sublist in lst_idx_ALF_MIN]
        lst_idx_MIXTO   = [[str(element) for element in sublist] for sublist in lst_idx_MIXTO]
        
        # RETORNO TODOS LOS XINDEX POSIBLES
        return lst_idx_NUMERIC , lst_idx_ALF_MAX , lst_idx_ALF_MIN , lst_idx_MIXTO
    
    # Entra una cadena tipo   1.2.2. Guerras Mundiales  y devuelve un list[1,2,2] y 'Guerras Mundiales'  
    # (la uso para recuperar el item(Guerras Mundiales, pero se puede usar para recuperar la numeracion tb))
    def __separar_cadena(self, cadena):
        patron = r'^([\w.]+?)\s+(.*)'
        path_item = re.match(patron, cadena.strip())
        if path_item:
            path  = path_item.group(1).strip('.').split('.')
            texto = path_item.group(2)
            return path, texto
        return None, None
    
    def __selecciona_xindex(self, type_XindeX=TYPEX.NUMERIC):

        if isinstance(type_XindeX, str):
            if type_XindeX == 'A':
                return self.lst_idx_ALF_MAX
            elif type_XindeX == 'a':
                return self.lst_idx_ALF_MIN
            elif type_XindeX == '1':
                return self.lst_idx_NUMERIC
            elif type_XindeX == 'a1':
                return self.lst_idx_MIXTO
            elif type_XindeX == '1a':
                return self.lst_idx_MIXTO
            elif type_XindeX == '1A':
                return self.lst_idx_MIXTO
            elif type_XindeX == 'A1':
                return self.lst_idx_MIXTO
            else:
                return self.lst_idx_NUMERIC           
            pass
        
        # PERMITE NUMERICO
        elif type_XindeX == TYPEX.NUMERIC:
            return self.lst_idx_NUMERIC
        elif type_XindeX == TYPEX.ALF_MAX:
            return self.lst_idx_ALF_MAX
        elif type_XindeX == TYPEX.ALF_MIN:
            return self.lst_idx_ALF_MIN
        elif type_XindeX == TYPEX.MIXTO:
            return self.lst_idx_MIXTO
        else:               # EN CASO DE QUE NINGUNO VALGA...(byDef)
            return self.lst_idx_NUMERIC

    # █████████████████████████████████████████████████████████████████████████████
    # EJECUTADOR en funcion de b_exe ████████████████
    def Terminator(self, titulo_menu:str, item, respuesta:int, b_exe:bool, pre_respuesta:str=None):
        """ Def: Tenemos la mision de crear una lista de [item , funcion, respuesta antigua, respuesta nueva]
        [titulo_menu] :(str): El titulo de menu_dvd.
        [respuesta]:(int): es el indice en cualquier lista de items(): lst_keys()
        [item]: (str): El nombre del Elemento del menu
        [b_exe]: (bool): True = ejecuta funcion | False = Devuelve respuesta
        [pre_respuesta]: (str): No se usa pero se pasa por parametro. es para que la vida sea mas sencilla. Si quieres usar un prefijo (>> , ■■) en este caso, para registrar las acciones del menu(a1, a, b11)
        """        
        # SALIR
        if respuesta == None: 
            return None
        
        # OPT RETORNAR
        if b_exe==False:         
            return respuesta
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        for i, row in enumerate(self.lst__men_itm_lev_ape_name_padr_ipadr_func):
            if i == respuesta:
                row[7]() if row[7] else None
                return True

    
    # DEVUELVE UN LIST DE HIJOS COMPROBANDO dicc_xgenx
    def __get_lst_dict_hijosX(self, titulo):
        """ ■■ LISTA CON MIS HIJOS DE PRIMERA GENERACION. Recorre el dicc_xgenx y recoge 
        [Retorno]: una lista de diccionarios con los datos sobre mis hijos en dicc_xgenx :
        (key):'titulo' (value):'titulo1'
        (key):'menuDvd' (value):(MenuDvd)menudvd_hijo
        (key):'padre' (value):'Menu_Titulos'
        (key):'ind_en_padre' (value): 2         (El lugar que ocupa en el padre)         
        """
        PADRE=0
        INDEX=1
        lst_hijos=[]
        for tit, padre_index in self.dicc_xgenx.items():
            if titulo == padre_index[PADRE]:
                menudvd_hijo = self.get_menudvd( titulo = tit )
                lst_hijos.append({  'titulo':tit,
                                    'menuDvd':menudvd_hijo, 
                                    'padre':titulo,
                                    'ind_en_padre':padre_index[INDEX]
                                })                
            pass
        pass    
        if lst_hijos: 
            return lst_hijos
        else: 
            return None        
    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # DEVUELVE LAS LISTAS XA WEB ■■■■■■■■■■■■■■■■■■■■■■■■■■■
    def get_web_lsts_lens_linea(self, titulo, b_exe=True, tipo_index=0, b_exec_all=True, b_loop=True, pad_x=30):
        """ Devuelve lo que necesita la web para representarse 
        [titulo](str): El titulo del menu. (obligatorio                   )
        [b_exe](bool): True, Se ejecutan las funciones. False, devuelve la resupuesta al usuario
        [tipo_index](0, 'a', 'A', 'A0')
        [b_exec_all](bool)
        [b_loop](bool)
        [pad_x](int)
        """
        # ■■■■ VALIDA SI EL TITULO ESTA REPETIDO Y LA EXISTENCIA EN LA GENETICA(self.config())        
        if titulo not in self.lst_titulosXX or titulo not in self.dicc_xgenx: 
            print(f'ERR-VAL:: {titulo} NO REGISTRADO EN XGENX')
            return None        
        
        # ■■■■ CACHA EL MENU ■■■■
        menu_dvd = self.get_menudvd( titulo = titulo )
        
    # DEVUELVE UNA MATRIZ DEL BODY DEL MENU. RECONFIGURACION PARA IMPRIMIR
    # def get_matriz_impresion_literal(self, menu_dvd, b_exec_all:bool, lst_str_opciones_validas:list, b_definicion:bool=False):
    def get_matriz_impresion_literal(self, menu_dvd, b_exec_all:bool, b_definicion:bool=False):
        """ DEVUELVE LA MATRIZ DE IMPRESION GENETICA RELLENA.
        [menu_dvd]:(MenuDvd), 
        [b_exec_all]:(bool), 
        [matriz_opciones_validas](list), 
        [b_definicion]:(bool)=False
        """
        # ■■ CADA LISTA REPRESENTA UNA COLUMNA. LUEGO SE MONTA
        # ■■ La impresion trabaja linea a linea, al trabajar con lista de lista de str, puedo trabajar como matriz y alterar las columnas antes de ser impreso todo como lineas.
        lst_col_0_lvl        = [f'{ int(row[2]) * self.TAB }' for row in self.lst__men_itm_lev_ape_name_padr_ipadr_func]        
        lst_col_1_xindex     = [f'{ xindex }'  for xindex in self.lst_str_opciones_validas]
        lst_col_2_pto        = [f'{ '.' }'     for i in range(len(self.lst_keys))]            
        lst_col_3_sp1        = [f'{ ' ' * self.sp1}' for i in range(len(self.lst_keys))]            
        lst_col_4_item       = [f'{ row[1] }'  for row in self.lst__men_itm_lev_ape_name_padr_ipadr_func]
        lst_col_5_sp2        = [f'{' ' * self.sp2}' for i in range(len(self.lst_keys))]            
        lst_col_6_definicion = self.get_lst_definiciones(   menu_dvd = menu_dvd, 
                                                            lista_genetica_x_fila =self.lst__men_itm_lev_ape_name_padr_ipadr_func, 
                                                            b_exec_all = b_exec_all)            
        lst_col_7_sp3        = [f'{' ' * self.sp3}' for i in range(len(self.lst_keys))]                    
        lst_col_8_funcion    = [f'{ self.__get_funcion_name(menu_dvd=self.get_menudvd(titulo=row[0]), item = row[1]) }' 
                                        for row in self.lst__men_itm_lev_ape_name_padr_ipadr_func]
        
        # ■ GENERA LA MATRIZ DE IMPRESION ASIGNANDO LOS DATOS DE LAS COLUMNAS
        matriz_xindex = []
        for i, lst_fila in enumerate(self.matriz_vacia):
            fila = []
            for j in range(len(lst_fila)):
                if j == 0:      fila.append( lst_col_0_lvl[i] )
                elif j == 1:    fila.append( lst_col_1_xindex[i] )
                elif j == 2:    fila.append( lst_col_2_pto[i] )
                elif j == 3:    fila.append( lst_col_3_sp1[i] )
                elif j == 4:    fila.append( lst_col_4_item[i] )
                elif j == 5:    fila.append( lst_col_5_sp2[i] )
                
                # B_DEFINICION
                if j == 6 and b_definicion == True:    
                    fila.append( lst_col_6_definicion[i] )
                elif j == 6 and b_definicion == False:
                    fila.append( '' )
                   
                if j == 7 and b_definicion == True:    
                    fila.append( lst_col_7_sp3[i] )
                elif j == 7 and b_definicion == False:
                    fila.append( '' )

                if j == 8 and b_definicion == True:
                    fila.append( lst_col_8_funcion[i] )                
                elif j == 8 and b_definicion == False:
                    fila.append( '' )

            matriz_xindex.append(fila) if fila else None
        
        # ■ RETORNO:
        return matriz_xindex if matriz_xindex else None
    
# ============================================================================================
# ============================================================================================
# ============================================================================================
import threading        
import time         
from functools import partial    
# ============================================================================================
class Over_Main(XindeX):
    """ AMPLIA XindeX Añadiendo la ejecución en hilos separados.... ■■ interactivo(tkinter) , 
                                                                    >> segundo plano demonio(flask) """
    def __init__(self):        
        super().__init__()
        self.hilos={}
        pass

    def Terminator(self, titulo_menu, item, respuesta, b_exe, pre_respuesta=None, post_respuesta=None):
        if pre_respuesta == None:
            super().Terminator(titulo_menu=titulo_menu, item=item, respuesta=respuesta, b_exe=b_exe)
        else:
            if pre_respuesta=='<<':
                self.ejecutar_background(titulo_menu=titulo_menu, item=item, respuesta=respuesta, b_exe=b_exe)

            elif pre_respuesta == '>>':
                self.ejecutar_interactivo(titulo_menu=titulo_menu, item=item, respuesta=respuesta, b_exe=b_exe)

            else:   
                try:
                    super().Terminator(titulo_menu=titulo_menu, item=item, respuesta=respuesta, b_exe=b_exe)
                except Exception as e:
                    print(f"Error en Terminator Over_Main: titulo_menu: {titulo_menu} -item: {item} -respuesta: {respuesta} -b_exe: {b_exe}, -pre_respuesta: {pre_respuesta} \n{e}")
            
    # ______________________________________
    """ ■■ """
    def ejecutar_interactivo(self, titulo_menu, item, respuesta, b_exe):
        """ ■■ Logica Interactiva: Tkinter por ejemplo (demon=False)  """
        print(f"Interacción activa con {respuesta}...")
        """ 
        CONFIGURO EL HILO LO GUARDO Y LO LANZO """
        hilo = threading.Thread(target=partial(super().Terminator, titulo_menu, item, respuesta, b_exe, None)
                                , daemon=False
                                )
        self.hilos[respuesta] = hilo
        hilo.start()

    # ______________________________________
    """ >> """
    def ejecutar_background(self, titulo_menu, item, respuesta, b_exe):
        """ ■■ servidor Flask por ejemplo (demon=True) 
        """
        
        print(f"Tarea en segundo plano: item: {item} - index: '{respuesta}' ...... ejecutada.")

        """ 
        CONFIGURO EL HILO LO GUARDO Y LO LANZO """
        hilo = threading.Thread(target=self.ejecutar, kwargs={'titulo_menu': titulo_menu, 'item': item, 'respuesta':respuesta, 'b_exe':b_exe}
                                , daemon=True
                                )
        self.hilos[respuesta] = hilo
        hilo.start()

    # ______________________________________
    def ejecutar(self, titulo_menu, item, respuesta, b_exe):
        pass
        super().Terminator(titulo_menu=titulo_menu, item=item, respuesta=respuesta, b_exe=b_exe, pre_respuesta=None)
    
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



