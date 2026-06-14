import os
import re
from colorama import Fore, Style, init
from .Franky import F_r_a_n_k_y
# import pyfiglet                               # ■ LETRAS GRANDES.
from .Sdata import Sdata     # Clase de complemento de Over_Main para cachar datos (permite NULL, valores por defecto, validacion de tipos...) por teclado.

""" 
    VARIABLES GLOBALES Y CONSTANTES 
"""
from enum import Enum as TYPE_XINDEX
class TYPEX(TYPE_XINDEX):
    NUMERIC = 0
    ALF_MAX = 10
    ALF_MIN = 20
    MIXTO   = 15

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
    Def: Define las partes esenciales de un menu Simple: Asociando item a funcion y dando un orden y un índice.  
    """
    TAB = '    '        # CTE TABULADO.... usado para los LEVELS

    def __init__(self, titulo:str, lst_items:list, lst_funciones:list=None):               
        """ 
        ■ CREA UN MENU. 
        UN MENU ESTÁ DEFINIDO POR:
            [titulo](str)
            [lst_items](list)  : Los Items(Elementos Visibles) del menu que el usuario tiene que seleccionar.
            [lst_funciones](list)  : Lista de Funciones asociadas a cada lst_items... pueden ser None si no tiene funcion asociada.        
        """
        # ■■ RECOGE TITULO
        self.titulo     = titulo      # El titulo e indice del menu. aparece por defecto en el HEAD es el id del menu.

        # ■■ RECOGE LISTA DE ITEMS
        self.lst_items = lst_items      # cada item(str) es el contenido del Menu. CUERPO 
        
        if lst_funciones == None:
            # ■■ SI NO PASAS LST_FUNC (LAS FUNCIONES DE CADA ITEM), LAS INICIALIZO A NONE....DON'T WORRY :)
            self.lst_funciones = [None for i in range(len(self.lst_items))]
        else:
            # ■■ La funcion que se pasa asociada por posicion al Item de lst_items
            self.lst_funciones   = lst_funciones              
        
        # ■■ GENERA LA LISTA DE NUMERACION RELATIVA ( del ZERO al n )
        self.lst_index_rltv = [i for i in range(len(self.lst_items))]
        
        # ■■ VALIDACION DE TAMAÑO DE LISTAS. IGUALAR TODAS A:  self.lst_items      
        self.igualar_listas(listaKeys=self.lst_items, listaToReLong=self.lst_funciones)
         
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■
        # DICCIONARIO RESULTADO ████  
        #   ■ {'titulo_menu': list( 'item_1_menu' , func_item_1 )  }   ==> Se genera 1 por Menu. 
        #   ■ Es de donde tiene que coger ■terminator_executor_■ la informacion para ejecutar al funcion.
        self.dicc_menu = dict(zip(self.lst_items, self.lst_funciones))
        
        # ■■ MENSAJE DE PEDIDA DE DATO AL USUARIO
        # self.entradilla_data_user = '\nIntro Opcion '     
        self.entradilla_data_user = 'Intro Opcion '     
    
    def __str__(self):  
        """ ■ Cuando se imprime la clase """              
        return f'Titulo=> {self.titulo} Items =>{self.lst_items}'
    
    def valid_unpack(self, lst_items):
        """  
        ■ VALIDA LA ESTRUCTURA DE ENTRADA 
        • CALLED: ...llamada desde self.AddX()
        [lst_items] 
            [('F_RANK_Y', <function info_TABLERO at 0x000001E02A476340>), ('IMPRIMIR', <function info_IMPRIMIR at 0x000001E02A4765C0>), ('GET', <function info_GETTING at 0x000001E02A476A20>), ('PUSH', <function info_push at 0x000001E02A477420>), ('DEL', <function info_DEL at 0x000001E02A476DE0>), ('RANGOS', <function info_RANGO at 0x000001E02A477060>), ('MISCELANEA', None)]
        • SALIDA: 
            lst_ITM • ['F_RANK_Y', 'IMPRIMIR', 'GET', 'PUSH', 'DEL', 'RANGOS', 'MISCELANEA']
            lst_FNC • [<function info_TABLERO at 0x000001E02A476340>, <function info_IMPRIMIR at 0x000001E02A4765C0>, <function info_GETTING at 0x000001E02A476A20>, <function info_push at 0x000001E02A477420>, <function info_DEL at 0x000001E02A476DE0>, <function info_RANGO at 0x000001E02A477060>, None]
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
                    if not callable(funcion):       # ► IF NOT funcion ►
                        if funcion is None:             # ► PERMITE NONE como Funcion.
                            lst_FNC.append(None)    
                        else:                           # ► Aqui se puede valorar meter otro tipo de datos que no sea ejecutable(callable) o None.    
                            return None, None           
                    else:                           # ► IF FUNCION ►
                        lst_FNC.append(funcion)
            else:
                return None, None
            
            return lst_ITM, lst_FNC
        except:
            return None, None
        pass
    
    # CAMBIA EL ESTILO(CARACTERES DE CABECERA, PIE, PRE-NUM , POST-NUM)
    def style(self, entradilla_data_user:str='\nIntro Opt (XindeX)..... '):
        """ ■■ Pone un Nuevo mensaje de entrada de Usuario.
        ■ EJEMPLO: 
            The_X_Men.style( entradilla_data_user = '\n Mete Opcion... ' )
        """
        if isinstance(entradilla_data_user, str):
            self.entradilla_data_user = entradilla_data_user
        else:
            self.entradilla_data_user = '\nIntro Opt (XindeX)..... '

    
    # El item de una fila
    def get_item(self, indice):
        """ ■■ Devuelve el ITEM de un Menu. 
        [row](int): Numero de POSICION (posicion secuencial) del item a recuperar
        ► CALLED::: ► mystyca_scaner_genetico ► get_list_padres_mystyca ► mystyca_keys
        ■ EJEMPLO:  
            item = menu_dvd.get_item(indice=i)
        ■ RETORNO:
            1• El nombre del item. Pejemplo 'Matematicas' 
            2• None, si no encuentra resultado.
        """
        fila_menu=f''
        if 0 <= indice < len(self.lst_items):
            for i , item_menu in enumerate(self.lst_items):            
                if i == indice :
                    return f'{ item_menu }'      
    
    # IGUALA LAS LISTAS
    def igualar_listas(self, listaKeys:list, listaToReLong:list, valorRelleno = ''):
        """ ■■ Trata las longitudes de las listas e iguala sus longitudes según •listaKeys como referencia.
        La que se Re-dimensiona tiene que creccer o decrecer •listaToReLong para igualarse con •listaKeys.
        [listaKeys](list): Lista de referencia a copiar su dimension.
        [listaToReLong](list): lista a cambiar de dimension.
        [valorRelleno](any): en caso de que listaKeys>listaToRelong, hay que rellenar con un nuevo valor. en caso de funciones, None(by Def)
        
        ■ EJEMPLO: 
            self.igualar_listas(listaKeys=self.lst_items, listaToReLong=self.lst_funciones)
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
    
# ███████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████
# ██                                             XindeX                                                ██
# ███████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████
class XindeX(MenuDvd):
    """ 
    ■■ Def: GESTIONA UNA LISTA DE MENUS Y SUB-MENUS Y LOS MUESTRA POR TERMINAL.    
    """ 
    
    NUMERO_COLUMNAS = 9     # NUMERO DE COLUMNAS DE XINDEX. ES CTE. 

    def __init__(self, tipo_index:str='a', b_mode_all:bool=True, b_loop:bool=True ):
        """ ■■ Crea un Menu Principal y gestiona una lista de Menus Secundarios que dependen del principal por su configuración Genética.
        [tipo_index]  ►'1' = Numerico(byDef)  ►'a' = Alfabetico Min  ►'A' = Alfabetico May  ►'A1', '1A', a1, 1a = Mixto
                      OR en Modo CTE ► TIPEX.NUMERIC = 0 | TIPEX.ALF_MAX = 10 | TIPEX.ALF_MIN = 20 | TIPEX.MIXTO = 15
        [b_mode_all] (bool)   ► True  ::: Solo se ejecutan ( o solo es OPCION-VALIDA) los subMenus Finales (no padres) 
                              ► False ::: Se ejecuta ( o solo es opcion valida) tanto padres como hijos.
        
        [b_loop] (bool)       ► True  ::: SALES DEL MENÚ INTRODUCIENDO '<<<' 
                              ► False ::: SE PRESENTA EL MENU 1 VEZ Y SALE A MAIN.

        ■ EJEMPLO: 
            ■ ■ xindex = XindeX(tipo_index = 'a', b_mode_all = True , b_loop=True)
              ■ ■ ■ tipo_index = 'a'    ► Indice tipo Alfabético minusculas
              ■ ■ ■ b_mode_all = True   ► Se ejecuta todo(sin directorios) 
              ■ ■ ■ b_loop=True         ► Se Sale por '<<<'
            
            ■ ■ xindex = XindeX(tipo_index = 1, b_mode_all = False , b_loop=True)
              ■ ■ ■ tipo_index = 1      ► Indice tipo Numérico.
              ■ ■ ■ b_mode_all = False  ► Sólo se ejecutan los extremos, no los Directorios.
              ■ ■ ■ b_loop=True         ► Se Sale por '<<<'
        """        
        # ■■■■■■■■■■■■■■■■■■■■■■■■ RELACIONADASA CON LA LA LOGICA DE LA APLICACION
        self.tipo_index = tipo_index
        self.b_mode_all = b_mode_all
        self.b_loop = b_loop    # ■■ Define si se sale por <<< o nos vale sólo para una ejecución...tb para definir mas adelante una última vuelta. 
        # ■■■■■■■■■■■■■■■■■■■■■■■■
        self.pasos=0            # ■■ Para las funciones recursivas mystyca. Define las veces que se llama a la recursividad.
        self.lst_menuXX=[]      # ■■ Lista de objetos MenuDvd que mantiene un lst_items,  dicc_menu(num_n:[strMenu_n, func_n])  ... se carga en addX
        self.lst_titulosXX=[]   # ■■ Lista de titulos de menu introducidos. Me permite validar rapido                           ... se carga en addX
        self.lst_keys=[]        # ■■ Lista de items de menu introducidos. Me permite validar rapido                             ... se carga en addX
        # INFORMACION GENETICA ■■■■■■■■■■■■■■■■■■■■■■■■
        self.lst__men_itm_lev_ape_name_padr_ipadr_func=[]    # ██ Lista de lista de str. Invocada desde Mystica. Funcion Recursiva
        self.dicc_xgenx={}      # ■■ diccionario que mantiene la genealogía de los menus. ■ titulo:[master, index_en_master]  
        self.matriz_opt_ok=[]   # ■■ Listado de Opciones Validas(a.1, b.2.3...). Se tiene que pasar a ■ xavier_get_dicc__respuesta()
        # LA MATRIZ A IMPRIMIR ■■■■■■■■■■■■■■■■■■■■■■■
        self.matriz_impresion_xindex=[]   # ■■ Lista de lista de str. llamada desde Mystica en ■ self.Mystica_Skin(). Funcion Recursiva        
        # TIPOS DE FORMATOS DE MENU ... se forman en ■ self.crear_xindicex() 
        self.lst_idx_NUMERIC=[]     # ■ numerico
        self.lst_idx_ALF_MAX=[]     # ■ alfanumerico mayusculas
        self.lst_idx_ALF_MIN=[]     # ■ alfanumerico minusculas
        self.lst_idx_MIXTO=[]       # ■ mixto. mayusculas(A1, 1A); minusculas(a1, 1a)
        # ESPACIOS DEL FORMATO DE LINEA
        self.sp1 = 1    # separa index de item
        self.sp2 = 1    # separa item de definicion.... mejor largo que corto.... tiene que cambiar en funcion del maximo.
        self.sp3 = 2    # separa definicion de funcion
        # LISTA DE LAS OPCIONES QUE PUEDE INTRODUCIR EL USUARIO ■■■■■■■■■■■■■■■■■■■■■■■
        self.lst_opts_ok = None    
        # CABECERA Y PIE: 
        # self.head_datapush  = head_datapush
        # self.pie_datapush   = pie_datapush
        # self.pie_datapush   = f'(Salir).... <<<  ■  (Help).... ?  ■  (Repeat).... <  ■  (Begin).... *opcion'
        self.pie_datapush   = f'Salir "<<<"  ■  Help-Exec "?"  ■  Repeat  "<"   ■ (Info)  "??" '
        
        # self.head_datapush  = " XINDEX - OVER-MAIN "
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # RESPUESTAS ■■■■■■■■■■■■■■■■■■■■■■■■■

        # ■ DIRECTAS ... Se evalua cada uno: 
        self.RESP_ACCION_DIRECTA = ['<' , '?' , '??' , 'help', '<<<']
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■ MENU PRINCIPAL(SE ESTABLECE EN MYSTYCA)
        self.menu_dvd = None
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # PREPARA IMPRESION ██████████████████        
        self.F_RANK_Y = None        
        self.F_RANK_Y_DEF = None
        self.color_marco = Fore.WHITE
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■ LONGITUD MAXIMA DEL MENU (INCLUYE XINDEX E ITEMS)
        self.longitud_max_xindex=0

        self.DICC_CELDA={
            'inicio':'A:0',
            'definiciones':'D:0', 
            'funciones':'E:0'
        }
    
    def get_tipo_index(self):
        """ Getter Retorna el tipo de index """
        return self.tipo_index
    def get_b_mode_all(self):
        """ Getter Retorna el modo de index """
        return self.b_mode_all
    def get_b_loop(self):
        """ Getter Retorna el modo de loop """
        return self.b_loop

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    def set_style(self, tipo_index:str=None, 
                        b_mode_all:bool=True, 
                        b_loop:bool=None, 
                        sp1:int=None, 
                        sp2:int=None, 
                        sp3:int=None, 
                        franky=None, 
                        franky_def=None
                        ):
        """ ■ ESTABLECE LOS ATRIBUTOS SOBRE EL TIPO DE IMPRESION Y MODO. Desde aquí se pueden cambiar dinámicamente la configuración Pppal.

        [tipo_index]:(str)='a', tipo de formato de indice que se muestra y que se responde... pejemplo: 'a' = genera un indice con  a.1. , b.2.1, etc
        [b_mode_all]:(bool)=True, Se ejecutan todos los items de xindex, ■ False, se ejecutan sólo los hijos.
        [b_loop]:(bool)=True, sale por '<<<' ■ False, da una respuesta y sale.
        [sp1]:int, espacio entre 
        [sp2]:int, espacio entre
        [sp3]:int, espacio entre
        [franky](F_r_a_n_k_y__) = Objeto Franky del xindex, 
        [franky_def](F_r_a_n_k_y__) = Objeto Franky de xindex con definicion.
        """
        if tipo_index is not None:
            setattr(self, "tipo_index", tipo_index)
        if b_mode_all is not None:
            setattr(self, "b_mode_all", b_mode_all)
        if b_loop is not None:
            setattr(self, "b_loop", b_loop)
        if sp1 is not None:
            setattr(self, "sp1", sp1)
        if sp2 is not None:
            setattr(self, "sp2", sp2)
        if sp3 is not None:
            setattr(self, "sp3", sp3)
        if franky is not None:
            setattr(self, "F_RANK_Y", franky) if isinstance(franky, F_r_a_n_k_y) else setattr(self, "F_RANK_Y", None)
        if franky_def is not None:
            setattr(self, "F_RANK_Y_DEF", franky_def) if isinstance(franky_def, F_r_a_n_k_y) else setattr(self, "F_RANK_Y_DEF", None)

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # 1-AÑADE UN MENU AL GESTOR Genético... en forma lst_items=[it1, it2, ...]  lst_funciones=[f1, f2, ....] (no usar) (Crea un MenuDvd)
    def add(self, titulo:str, lst_items:list, lst_funciones:list=None):     
        """  Crea un Objeto MenuDvd 
        [titulo](str): Id del menú.
        [lst_items](list): lista de Items que se imprimiran junto con sus indices
        [lst_funciones](list): lista de funciones(objetos callables) asociadas por posición a los items.

        ■ EJEMPLO:
            he_X_Men.add(titulo='SUB_IMPR' , 
                         lst_items = [f"IMPRIMIR Modo  {Fore.YELLOW}Max", f"IMPRIMIR Modo Literal", f"IMPRIMIR Modo Fixed"] , 
                         lst_funciones = [func_max, func_literal, func_fixed] )
        ■ SALIDA:
            Objeto Menú Creado ( Asociación de items con funciones con un titulo como identificador)
        """
        if titulo in self.lst_titulosXX: 
            return False
        try:
            new_menu = MenuDvd(titulo=titulo, lst_items=lst_items, lst_funciones=lst_funciones)
        except Exception as e:
            print(e)
            return None
        self.lst_titulosXX.append(titulo)
        self.lst_menuXX.append(new_menu)
        return new_menu
    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # 2-CONFIGURA LA RELACION PADRE HIJO(INDICE) DEL MENU (dicc_xgenx)
    def config(self, titulo:str, nombre_padre:str=None, i_padre=None): 
        """ ■■ Añade una relacion Genética de los menus. ■■        
        ► Añade elementos a dicc_xgenx que es el diccionario que gestiona la genetica de XindeX

        [titulo](str): titulo, nombre del menu. Nombre identificativo del Menú a configurar.
        [nombre_padre](str): titulo del menu que será el padre.
        [i_padre](int, str): indice en el padre o Nombre de Item en el padre.
        EJEMPLO: 
            1• Menu.config(titulo = 'Derivadas' , nombre_padre='Asignaturas', 'Matematicas')    ► asigna el menú 'Derivadas'  al Menú 'Asignaturas' en el índice Matemáticas en Asignaturas.
            2• Menu.config(titulo = 'Integrales', nombre_padre='Asignaturas', 2)                ► asigna el menú 'Integrales' al Menú 'Asignaturas' en el índice 2 en el Menú Asignaturas(si existe).
        """
        # VALIDA LA EXISTENCIA DEL TITULO .... self.lst_titulosXX   se carga   en self.addX()  antes 
        if not titulo in self.lst_titulosXX:   return None
        
        # ■■■ EN CASO DE QUE META UN INDICE DE CADENA DE TEXTO
        if isinstance(i_padre, str):
            b_match = False
            """ Puede ser que meta un item del menu al que quiere ir(item del padre) """
            menu_padre=self.get_menudvd(titulo = nombre_padre)
            if not menu_padre: 
                return None
            for i, item_en_padre in enumerate(menu_padre.lst_items):
                if str(item_en_padre).strip().upper() == str(i_padre).strip().upper():
                    i_padre = i
                    b_match = True
                    break
            pass
            if b_match == False: return None
        
        # ████████████████████████████████████████████████
        # ANALISIS DE LA GENETICA  ███████████████████████        
        if nombre_padre == None and i_padre == None:
            self.dicc_xgenx[titulo]=['-', '-']
            """ ■■ Es un puro Master!!!  """

        elif nombre_padre == None and i_padre != None:
            self.dicc_xgenx[titulo]=['-', '-']            
            """ ■■ Es un Master Fuerte pero confundido, le sobra el index """

        elif nombre_padre != None and i_padre == None:
            newIndex=self.__busca_index_free(master_buscado=nombre_padre)            
            """ ■■ Es un Sub Puro ????? esta machacando al anterior pq no da con el index libre"""
            if newIndex:
                self.dicc_xgenx[titulo]=[nombre_padre, newIndex]
            else:
                return False

        elif nombre_padre != None and i_padre != None and str(i_padre).isdigit():
            """ ■■ es un Sub Selector Puro y machaca todo lo que pilla."""
            self.dicc_xgenx[titulo]=[nombre_padre, i_padre]
        
        else:
            """ ■■ Error No posible, pero lo dejo por legible.....o no ;) """        
            pass

    # ███████████████████████████████████████████████████████████████████████████████
    # -AÑADE UN MENU AL GESTOR Y LO CONFIGURA.... ES ADD Y CONFIG EN LA MISMA FUNCION.
    # en forma (item_menu, funcion) (Crea un MenuDvd) (y si metes padre e ipadre se configura la genetica)
    def addX(self, titulo:str, lst_items:list=None, padre:str=False, ipadre:str=None):             
        """ 
        [titulo]: Es el identificador del menu y sirve para la genetica.
        [lst_items](tuple)•(str, func) -> str es una cadena que será el texto en el menu. func puede ser None o el nombre de una funcion sin los parentesis(callable).
        [padre](str):  False, Nombre del Menu Padre. Si se escribe, un Menu se declara como Hijo.
        [ipadre](str): None, indice en el padre. puede ser int o str, pero recomiendo por claridad que sea el nombre del indice str.
        ■ EJEMPLO:
            The_X_Men.addX( titulo='MenuPpal',  
                            padre=None,         # MASTER
                            ipadre=None ,       # MASTER
                            lst_items=[ 
                                        ("F_RANK_Y" , info_TABLERO) ,      # ... ITEM = F_RANK_Y ; FUNCION = info_TABLERO
                                        ('IMPRIMIR', info_IMPRIMIR) , 
                                        ("GET", info_GETTING), 
                                        ("PUSH" , info_push), 
                                        ("DEL" , info_DEL), 
                                        ("RANGOS" , info_RANGO) , 
                                        ('MISCELANEA', None)
                            ])
        ► SALIDA:  
            El MenuDvd Creado y Configurado geneticamente.
        """
        # Desempaquetado:
        lst_itemX, lst_funcX = self.valid_unpack(lst_items=lst_items)
        if not lst_itemX and not lst_funcX:
            print(f'Error:: Estructura NO Valida: {lst_items} ')
            print(f'.... Recuerda: (item) Tiene que ser un String y de momento sin repetidos y (funcion) se escribe sin los parentesis y None es un valor Válido ')                
            return None
        if titulo in self.lst_titulosXX: 
            return False
        try:
            new_menu = MenuDvd(titulo=titulo, lst_items=lst_itemX, lst_funciones=lst_funcX)
            """ ■■ Se crea un objeto MenuDvd """
            # print(new_menu)
        except Exception as e:
            print(e)
            return None
        
        # Añade a la lista de titulos y a la lista de menus de XindeX
        self.lst_titulosXX.append(titulo)
        self.lst_menuXX.append(new_menu)
        
        # .... llama a config desde la addX !!!!!! Todo en 1.
        if padre==False:
            """ No introduce padre, no hago nada, salgo por donde vine """
            pass
        elif padre==None:
            if ipadre==None:
                """ es el Master"""
                self.config(titulo=titulo, nombre_padre=None, i_padre=None)
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
                    self.config(titulo=titulo, nombre_padre=padre, i_padre=ipadre)
        # ______________
        # Retorno:
        return new_menu

    # RETORNA UN OBJ MENUDVD POR MEDIO DE SU TITULO             (obtiene el MenuDvd )
    def get_menudvd(self, titulo:str=None):
        """ ■■ Retorna un objeto MenuDvd x su str titulo. 
        [titulo](str) ► Titulo(Id) del menú a devolver.
        ■ EJEMPLO:
            menu_dvd = self.get_menudvd(titulo = 'Asignaturas')
        ► SALIDA:
            Objeto MenuDvd encontrado o None si no encuentra el menu en self.lst_titulosXX
        """
        if titulo is None:
            return [menudvd for menudvd in self.lst_menuXX]      # LISTA CON TODOS LOS MENUS 
        else:                    
            if titulo in self.lst_titulosXX:
                for menudvd in self.lst_menuXX:
                    if str(menudvd.titulo) == str(titulo):
                        return menudvd
    
    # BUSCA INDEX FREE.                                         (Busca un indice libre)
    def __busca_index_free(self,  master_buscado ):
        """ ■■ Busca en el diccionario de configuracion << self.dicc_xgenx >> , un index libre(el siguiente). 
        [master_buscado](str): Nombre del menu a buscar. ► 'Asignaturas'
        ■ EJEMPLO: 
            newIndex=self.__busca_index_free(master_buscado='Asignaturas') 
        ► SALIDA: None si Error | indice para insertar si todo OK 
        """
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
                new_index=max_index + 1
                if new_index>len(self.dicc_xgenx.keys()): 
                    return None
                return new_index
            except Exception as e:
                print(f'Error: {e} ')
                return None    
        else:
            return 1    #Todos los menus empiezan las opciones en 1 y el 0 es Salir.
    
    # ████████████████████████████████████████████████████████████████████████████████████████████████
    # █████ MUESTRA UN XINDEX.  (Imprime el menu con subMenus - Toma Control - Ejecuta Funciones) ████
    def mystyca(self, titulo:str, head_datapush:list=None, pad_x:int=15):
        """ ■ MUESTRA UN XINDEX.  (Imprime el menu con subMenus - Toma Control - Ejecuta Funciones) ■

        [titulo](str):      Id del Menu Añadido/Configurado/Mostrados sus Items.
        [pad_x] (int):      Distancia entre el punto final del str del menu y el marco final.
        [head_datapush](any): Opcional, es la Cabecera del Menu. Se va a Imprimir desde la celda 'A:0' de la Head.
                            IF None, Crea un Tablero Franky sin Cabecera.
        ■ EJEMPLOS:
            retorno = The_X_Men.mystyca( titulo='MenuPpal' )                ► Sin Head y pad_x = 3(ByDef)
            retorno = The_X_Men.mystyca( titulo='MenuPpal' , pad_x=5 )      ► Sin Head y pad_x = 5
            retorno = The_X_Men.mystyca( titulo='MenuPpal' , head_datapush  = " XINDEX - {Fore.CYAN}OVER-FRANKY{Style.RESET_ALL}" , pad_x=5 )  ► texto (en A:0) y pad_x = 5 
            retorno = The_X_Men.mystyca( titulo='MenuPpal' , head_datapush  = [['FILA 1 CABECERA'], ['FILA 2 CABECERA'] ] , pad_x=5 )           ► matriz en la cabecera y pad_x = 5 (desde A:0)
        ■ SALIDA:
            ■ ■ ES LA FUNCION A EJECUTAR PARA QUE SE PRODUZCA UN XINDEX. TOMA EL CONTROL ■ ■
        """    

        # ■■ VALIDA TITULO REPETIDO Y EXISTENCIA EN LA GENETICA(CONFIG)
        if titulo not in self.lst_titulosXX or titulo not in self.dicc_xgenx: 
            print(f'ERR-VAL:: {titulo} NO REGISTRADO EN XGENX')
            return None

        self.head_datapush=head_datapush
        self.pad_x = pad_x

        # ■■ CACHA EL MENU A IMPRIMIR...es la BASE GENETICA de trabajo
        menu_dvd = self.get_menudvd(titulo = titulo)
        if not menu_dvd: 
            return None
        self.menu_dvd = menu_dvd
        print(f'■ MENU: {self.menu_dvd.titulo}')
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ███ MODULO GENETICO 
        self.load_modulo_gentico_x(titulo=titulo)

        # VALIDACION
        if (not self.lst__men_itm_lev_ape_name_padr_ipadr_func or 
            not self.lst_keys or 
            not self.lst_opts_ok): 
            print(f'ERR-VAL:: {titulo} NO REGISTRADO EN XGENX')
            return None
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ███ MODULO IMPRESION 
        self.load_modulo_impresion_x(menu_dvd = self.menu_dvd, 
                                    lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func, 
                                    lst_keys = self.lst_keys,
                                    lst_opts_ok = self.lst_opts_ok)
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ███ MODULO RESPUESTA        
        # ███ LOOP = FALSE, 1 SOLA RESPUESTA Y VUELVES ███
            # ■■ lo gestiona el main( .... cualquier llamada ) 
            # ■■ [respuesta] es el indice lineal en lst_keys o self.lst__men_itm_lev_ape_name_padr_ipadr_func
        if self.b_loop == False:   
            while(True):    # SI EL USUARIO INTRODUCE ? O < TIENE QUE REPETIRSE Y VUELVE CUANDO EL USUARIO RESPONDE SALIR U OPT-OK
                #  ■■■ XAVIER - OBTIENE RESPUESTA DE USUARIO ■■■
                dicc_xavier = self.xavier_get_dicc_respuesta(menu_dvd = self.menu_dvd , lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func )    
                if dicc_xavier == None:         # SALIR... ha pulsado '<<<'. Esto anula el menu, pq se ejecuta una sola vez.
                    return None                 # Sale por Main(....por donde es llamada)
                
                # ■ OBTIENE EL INDICE EN M_I_L_A_N_P_I_F SI LO ENCUENTRA Y SI NO DEVUELVE NONE
                xindex = self.get_xindex(menu_dvd = self.menu_dvd , dicc_respuesta = dicc_xavier, lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func)
                if  xindex != None:
                    dicc_xavier['xindex'] = xindex                    
                    return dicc_xavier['xindex']
                
        # ████ LOOP = TRUE, SOLO SALES POR <<< ████
        while(True):
            # ■■■ XAVIER - OBTIENE RESPUESTA VALIDA DEL USUARIO, O SALIR ■■■
            dicc_xavier = self.xavier_get_dicc_respuesta( menu_dvd = self.menu_dvd , lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func)   
            
            # ■■■ SALIR... ha pulsado '<<<' ■■■
            if not dicc_xavier:       
                return True                       
            
            # ■■■ TERMINATOR - EJECUTA LA RESPUESTA DEL USUARIO ■■■
            self.terminator_executor(dicc_respuesta = dicc_xavier, titulo_menu = self.menu_dvd.titulo)
            continue

    # █████████████████████████████████████████████████████████████
    # RCRSV: LISTA con Todos los items en orden de impresion.██████
    def mystyca_keys(self, menu_dvd, level=None, retorno=None):
        """ ■ FUNCION RECURSIVA QUE JUNTA EN UNA LISTA TODOS LOS ITEMS DE LA GENETICA DE MENU PASADO COMO ARGUMENTO.

        [menu_dvd](MenuDvd): Instancia del Objeto Menu. <classIndeX.classXindeX.MenuDvd object at 0x0000020E07AD23C0>
        [level](int)=None,      No se toca ni se pasa, es para propositos recursivos.
        [retorno](list)=None,   No se toca ni se pasa, es para propositos recursivos.

        ► CALLED: load_modulo_gentico_x
        ► EJEMPLO:
            self.lst_keys = self.mystyca_keys( menu_dvd = self.menu_dvd )
        ■ SALIDA:
            ['F_RANK_Y', '\x1b[92mCOMO\x1b[39m \x1b[31mEMPEZAR\x1b[39m / \x1b[92mHOW\x1b[39m \x1b[31mBEGIN', '\x1b[33mCREAR FRANKY\x1b[0m... Crea un Tablero ', '\x1b[33mINICIALIZA\x1b[0m Tablero (default)', '\x1b[92mMODE \x1b[31m(EXCEL)', 'IMPRIMIR', 'IMPRIMIR Modo  \x1b[33mMax', 'IMPRIMIR Modo Literal /  \x1b[33mMosaico\x1b[0m', 'IMPRIMIR Modo  \x1b[33mFixed', 'IMPRIMIR Modo  \x1b[33mLista', 'IMPRIMIR \x1b[33mALL IN ONE\x1b[0m (FROM-TO)', 'GET', 'GETTING \x1b[36mFila', 'GETTING \x1b[36mColumna', 'GETTING Valor By \x1b[36mFila-Columna\x1b[0m', 'GETTING Valor By \x1b[36mCelda\x1b[0m(A:0)', 'GETTING \x1b[36mMatriz Values', 'PUSH', 'PUSH \x1b[32mMATRIZ', 'PUSH \x1b[32mLISTA', 'PUSH OVER \x1b[32mFila', 'PUSH OVER \x1b[32mColumn', 'PUSH Valor \x1b[32mBy Celda (C:3)', 'PUSH valor \x1b[32mBy fila / columna', 'DEL', 'DEL \x1b[36mFila\x1b[0m Over F_RANK_Y', 'Del \x1b[36mColumn\x1b[0m', 'Del \x1b[36mCelda\x1b[0m', 'RANGOS', '\x1b[32mCREAR\x1b[0m Rango', '\x1b[32mBUSCAR\x1b[0m Rango', '\x1b[32mELIMINAR\x1b[0m Rango', '\x1b[32mIMPRIMIR x \x1b[33mNombre Rango', '\x1b[32mVER\x1b[0m INFO Rangos Tablero', '\x1b[32mPULL TO\x1b[0m \x1b[33mRANGO', 'MISCELANEA', '\x1b[33mPUSH \x1b[31mMASIVO', 'Prueba \x1b[35mIMPRESION MASIVA', 'Get \x1b[32m General Data \x1b[0m', 'Cambia \x1b[35mHEAD', 'Cambia \x1b[35mPIE', '\x1b[33mSet \x1b[35mColor\x1b[0m Marco', 'Set  \x1b[35mTipo de Marco', '\x1b[33mCambia \x1b[35mColor\x1b[0m MODE EXCEL']
        """
        if level==None and retorno==None:     # 1ª ENTRADA
            level=-1 ; retorno=[] ; self.pasos=0 
        level += 1 ; self.pasos += 1
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        lst_hijos = self.get_lst_dict_hijosX(titulo=menu_dvd.titulo)        
        if  lst_hijos:         
            for i in range(len(menu_dvd.lst_items)):                
                retorno.append(menu_dvd.get_item(indice=i))                
                for hijo in lst_hijos:
                    if hijo['ind_en_padre'] == i:                        
                        self.mystyca_keys(menu_dvd=hijo['menuDvd'] , level=level, retorno=retorno)
                        break    
        elif not lst_hijos:    
           for i, item in enumerate(menu_dvd.lst_items):                    
                retorno.append(item)
                
        # ___________________________________
        return retorno

    # █████████████████████████████████████████████████████████████
    # RCRSV: IDENTIFICA PADRES DE HIJOS 
    def get_list_padres_mystyca(self, menu_dvd, level=None, retorno=None ):
        """ ■ Funcion Recursiva que Devuelve una lista de los padres del menú pasado como argumento.
        [menu_dvd](MenuDvd): Instancia de un objeto MenuDvd. <classIndeX.classXindeX.MenuDvd object at 0x0000020E07AD23C0>
        [level](int): None,     No se toca ni se pasa, es para propositos recursivos.
        [retorno](list): None , No se toca ni se pasa, es para propositos recursivos.
        
        ► CALLED: ►get_lst_definiciones() ► get_xindex() ► terminator__executor() ► terminator__executor() SOBRE-ESCRITO.
        ■ EJEMPLO: 
            lst_padres  = self.get_list_padres_mystyca(menu_dvd = menu_dvd)
        ■ SALIDA: 
            ['F_RANK_Y', 'IMPRIMIR', 'GET', 'PUSH', 'DEL', 'RANGOS', 'MISCELANEA']
        """
        if level==None and retorno==None:     # 1ª ENTRADA
            level=-1   ; retorno=[] ; self.pasos=0 
        level += 1
        self.pasos+=1
        # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        lst_hijos = self.get_lst_dict_hijosX(titulo=menu_dvd.titulo)        
        if  lst_hijos:         
            for i in range(len(menu_dvd.lst_items)):
                for hijo in lst_hijos:
                    if hijo['ind_en_padre'] == i:                        
                        retorno.append(menu_dvd.get_item(indice=i))                
                        self.get_list_padres_mystyca(menu_dvd=hijo['menuDvd'] , level=level, retorno=retorno)
                    pass
        elif not lst_hijos:
           for i, item in enumerate(menu_dvd.lst_items):
                pass 
        return retorno

    # █████████████████████████████████████████████████████████████
    # ████████████ RCRSV:  DATOS POR FILA DE IMPRESION  ███████████
    def mystyca_scaner_genetico(self, menu_dvd, level=None,  retorno=None, apellido=None):
        """ ■ Funcion Recursiva que devuelve una lista radiografíca de la genética de un Menú pasado como argumento.
        Devuelve una lista donde cada item tiene: 1•titulo menu, 2•item del menu , 3•level, 4•apellidos,  5•name_padr , 6•indice en el padre , 7•funcion
        [menu_dvd],     Instancia de un Objeto Menú. ► <classIndeX.classXindeX.MenuDvd object at 0x0000020E07AD23C0>
        [level]=None,    No se pasa en la llamada. se pasa en la recursividad
        [retorno]=None,  No se pasa en la llamada. se pasa en la recursividad
        [apellido]=None, No se pasa en la llamada. se pasa en la recursividad
        
        ► CALLED: ►self.get_matriz_impresion_literal() ►self.load_modulo_gentico_x()
        ■ EJEMPLO: 
            ►self.lst__men_itm_lev_ape_name_padr_ipadr_func = self.mystyca_scaner_genetico( menu_dvd = self.menu_dvd )
            ►lst__m_i_l_a_n_p_i_f = self.mystyca_scaner_genetico( menu_dvd = self.menu_dvd )
        ■ SALIDA: 
            [('MenuPpal', 'F_RANK_Y', 0, '0.', 0, '-', '-', <function info_TABLERO at 0x000001AC308A13A0>), 
            ('SUB_CREAR', '\x1b[92mCOMO\x1b[39m \x1b[31mEMPEZAR\x1b[39m / \x1b[92mHOW\x1b[39m \x1b[31mBEGIN', 1, '0.1.', 0, 'MenuPpal', 0, <function info_begin at 0x000001AC308A1300>), 
            ('SUB_CREAR', '\x1b[33mCREAR FRANKY\x1b[0m... Crea un Tablero ', 1, '0.1.', 1, 'MenuPpal', 0, <function crear_tablero at 0x000001AC308A1440>), 
            ('SUB_CREAR', '\x1b[33mINICIALIZA\x1b[0m Tablero (default)', 1, '0.1.', 2, 'MenuPpal', 0, <function iniciar_tablero at 0x000001AC308A14E0>), 
            ('SUB_CREAR', '\x1b[92mMODE \x1b[31m(EXCEL)', 1, '0.1.', 3, 'MenuPpal', 0, <function mode_excel at 0x000001AC308A1580>), 
            ('MenuPpal', 'IMPRIMIR', 0, '0.', 1, '-', '-', <function info_IMPRIMIR at 0x000001AC308A1620>), 
            ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mMax', 1, '0.1.', 0, 'MenuPpal', 1, <function print_max at 0x000001AC308A16C0>), 
            ('SUB_IMPR', 'IMPRIMIR Modo Literal /  \x1b[33mMosaico\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 1, <function print_literal at 0x000001AC308A1760>), 
            ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mFixed', 1, '0.1.', 2, 'MenuPpal', 1, <function print_fixed at 0x000001AC308A1800>), 
            ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mLista', 1, '0.1.', 3, 'MenuPpal', 1, <function print_personal at 0x000001AC308A18A0>), 
            ('SUB_IMPR', 'IMPRIMIR \x1b[33mALL IN ONE\x1b[0m (FROM-TO)', 1, '0.1.', 4, 'MenuPpal', 1, <function print_from_to at 0x000001AC308A19E0>), 
            ('MenuPpal', 'GET', 0, '0.', 2, '-', '-', <function info_GETTING at 0x000001AC308A1A80>),
            ('SUB_GET', 'GETTING \x1b[36mFila', 1, '0.1.', 0, 'MenuPpal', 2, <function get_fila at 0x000001AC308A1C60>), 
            ('SUB_GET', 'GETTING \x1b[36mColumna', 1, '0.1.', 1, 'MenuPpal', 2, <function get_columna at 0x000001AC308A1D00>), 
            ('SUB_GET', 'GETTING Valor By \x1b[36mFila-Columna\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 2, <function get_fila_columna at 0x000001AC308A1BC0>), 
            ('SUB_GET', 'GETTING Valor By \x1b[36mCelda\x1b[0m(A:0)', 1, '0.1.', 3, 'MenuPpal', 2, <function get_celda at 0x000001AC308A1B20>), 
            ('SUB_GET', 'GETTING \x1b[36mMatriz Values', 1, '0.1.', 4, 'MenuPpal', 2, <function get_matriz_values at 0x000001AC308A1DA0>), 
            • • • • • 
        """
        if not isinstance(menu_dvd, MenuDvd): 
            print('ERROR: mystyca_scaner_genetico menu_dvd no es una Instacia de Objeto válida.')
            return None
        if level==None and retorno==None:     # 1ª ENTRADA
            level=-1 ; retorno=[]  ;  apellido='' 
        level += 1 
        """ Contadores """
        lst_dict_hijosX = self.get_lst_dict_hijosX(titulo=menu_dvd.titulo)      
        """ Tengo al padre(menu_dvd, y a los hijos(lst_dict_hijosX)) 
        """  
        if  lst_dict_hijosX:         
            apellido += str(level) + '.'
            for i in range(len(menu_dvd.lst_items)):
                item = menu_dvd.get_item(indice=i)

                funcion_name = self.get_funcion_name(menu_dvd = menu_dvd, item=item)
                retorno.append(( menu_dvd.titulo ,                                  
                                item , 
                                level , 
                                apellido , 
                                i ,
                                self.get_padre(titulo_menu=menu_dvd.titulo) , 
                                self.get_ind_en_padre(titulo_menu = menu_dvd.titulo) , 
                                # funcion_name 
                                menu_dvd.dicc_menu.get(item, None)
                                ))
                                
                for hijo in lst_dict_hijosX:
                    if hijo['ind_en_padre'] == i:                        
                        # ■■■■■■■■■■■■■■■■■■■■■■■■
                        self.mystyca_scaner_genetico(menu_dvd=hijo['menuDvd'] , level = level,  retorno = retorno, apellido = apellido)
                    pass
        elif not lst_dict_hijosX:
            apellido += str(level) + '.'
            aux = apellido
            for i, item in enumerate(menu_dvd.lst_items):
                
                funcion_name = self.get_funcion_name(menu_dvd=menu_dvd, item=item)

                retorno.append(( menu_dvd.titulo ,                                  
                                item , 
                                level , 
                                apellido , 
                                i ,
                                self.get_padre(titulo_menu = menu_dvd.titulo) , 
                                self.get_ind_en_padre(titulo_menu = menu_dvd.titulo)  , 
                                # funcion_name
                                menu_dvd.dicc_menu.get(item, None)
                                ))
                apellido = aux
        return retorno    
    
    # OBTIENE EL NOMBRE DE LA FUNCION DE UN ITEM DE UN MENU
    def get_funcion_name(self, menu_dvd, item:str):
        """  ■ Devuelve el nombre de la funcion asociada al item de un menuDvd
        [menu_dvd](MenuDvd): Instancia de un objeto MenuDvd. <classIndeX.classXindeX.MenuDvd object at 0x0000020E07AD23C0>
        [item](str): nombre del item del que se quiere buscar su función asociada.
        ► CALLED: ►self.get_matriz_impresion_literal() ►self.mystyca_scaner_genetico()
        ■ EJEMPLO: 
            funcion_name = self.get_funcion_name(menu_dvd = obj_menu_dvd, item='Matemáticas')
        ■ SALIDA: Podemos encontrar 3 tipos de salida:::
            1• str del nombre de la funcion .... todo va OK
            2• f'(-)'   IF funcion == None  .... todo OK
            3• str(funcion) .................... no OK pq funcion no es calable ni None, hace esta opción para no retornar None y admitir otros tipos de datos.
        """
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
    
    # ■■■ CUANDO PULSA   '?' ... Llamada desde terminator__executor
    def imprimir_mystyca_definiciones(self, menu_dvd, lista_m_i_l_a_n_p_i_f:list):
        """ ■■ CUANDO SE PULSA '?'  ► Imprime el Menú con los Items y las Funciones , definiciones y el modo de ejecución.
        [menu_dvd](MenuDvd) : Objeto MenuDvd que se va a imprimir. ► <classIndeX.classXindeX.MenuDvd object at 0x0000020E07AD23C0>
        [lista_m_i_l_a_n_p_i_f](list) : Lista de listas con la configuracion genetica de los menus. ►[('MenuPpal', 'F_RANK_Y', 0, '0.', 0, '-', '-', <function info_TABLERO at 0x0000020F388C9440>), ('SUB_CREAR', '\x1b[92mCOMO\x1b[39m \x1b[31mEMPEZAR\x1b[39m / \x1b[92mHOW\x1b[39m \x1b[31mBEGIN', 1, '0.1.', 0, 'MenuPpal', 0, <function info_begin at 0x0000020F388C93A0>), ('SUB_CREAR', '\x1b[33mCREAR FRANKY\x1b[0m... Crea un Tablero ', 1, '0.1.', 1, 'MenuPpal', 0, <function crear_tablero at 0x0000020F388C94E0>), ('SUB_CREAR', '\x1b[33mINICIALIZA\x1b[0m Tablero (default)', 1, '0.1.', 2, 'MenuPpal', 0, <function iniciar_tablero at 0x0000020F388C9580>), ('SUB_CREAR', '\x1b[92mMODE \x1b[31m(EXCEL)', 1, '0.1.', 3, 'MenuPpal', 0, <function mode_excel at 0x0000020F388C9620>), ('MenuPpal', 'IMPRIMIR', 0, '0.', 1, '-', '-', <function info_IMPRIMIR at 0x0000020F388C96C0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mMax', 1, '0.1.', 0, 'MenuPpal', 1, <function print_max at 0x0000020F388C9760>), ('SUB_IMPR', 'IMPRIMIR Modo Literal /  \x1b[33mMosaico\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 1, <function print_literal at 0x0000020F388C9800>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mFixed', 1, '0.1.', 2, 'MenuPpal', 1, <function print_fixed at 0x0000020F388C98A0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mLista', 1, '0.1.', 3, 'MenuPpal', 1, <function print_personal at 0x0000020F388C9940>), ('SUB_IMPR', 'IMPRIMIR \x1b[33mALL IN ONE\x1b[0m (FROM-TO)', 1, '0.1.', 4, 'MenuPpal', 1, <function print_from_to at 0x0000020F388C9A80>), ('MenuPpal', 'GET', 0, '0.', 2, '-', '-', <function info_GETTING at 0x0000020F388C9B20>), ('SUB_GET', 'GETTING \x1b[36mFila', 1, '0.1.', 0, 'MenuPpal', 2, <function get_fila at 0x0000020F388C9D00>), ('SUB_GET', 'GETTING \x1b[36mColumna', 1, '0.1.', 1, 'MenuPpal', 2, <function get_columna at 0x0000020F388C9DA0>), ('SUB_GET', 'GETTING Valor By \x1b[36mFila-Columna\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 2, <function get_fila_columna at 0x0000020F388C9C60>), ('SUB_GET', 'GETTING Valor By \x1b[36mCelda\x1b[0m(A:0)', 1, '0.1.', 3, 'MenuPpal', 2, <function get_celda at 0x0000020F388C9BC0>), ('SUB_GET', 'GETTING \x1b[36mMatriz Values', 1, '0.1.', 4, 'MenuPpal', 2, <function get_matriz_values at 0x0000020F388C9E40>), ('MenuPpal', 'PUSH', 0, '0.', 3, '-', '-', <function info_push at 0x0000020F388CA520>), ('SUB_PUSH', 'PUSH \x1b[32mMATRIZ', 1, '0.1.', 0, 'MenuPpal', 3, <function matriz_to_tablero at 0x0000020F388CA5C0>), ('SUB_PUSH', 'PUSH \x1b[32mLISTA', 1, '0.1.', 1, 'MenuPpal', 3, <function push_lista at 0x0000020F388CA8E0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mFila', 1, '0.1.', 2, 'MenuPpal', 3, <function push_valor_over_fila at 0x0000020F388CA7A0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mColumn', 1, '0.1.', 3, 'MenuPpal', 3, <function push_valor_over_columna at 0x0000020F388CA840>), ('SUB_PUSH', 'PUSH Valor \x1b[32mBy Celda (C:3)', 1, '0.1.', 4, 'MenuPpal', 3, <function push_celda at 0x0000020F388CA700>), ('SUB_PUSH', 'PUSH valor \x1b[32mBy fila / columna', 1, '0.1.', 5, 'MenuPpal', 3, <function push_fila_columna at 0x0000020F388CA660>), ('MenuPpal', 'DEL', 0, '0.', 4, '-', '-', <function info_DEL at 0x0000020F388C9EE0>), ('SUB_DEL', 'DEL \x1b[36mFila\x1b[0m Over F_RANK_Y', 1, '0.1.', 0, 'MenuPpal', 4, <function del_fila at 0x0000020F388CA020>), ('SUB_DEL', 'Del \x1b[36mColumn\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 4, <function del_columna at 0x0000020F388CA0C0>), ('SUB_DEL', 'Del \x1b[36mCelda\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 4, <function del_celda at 0x0000020F388C9F80>), ('MenuPpal', 'RANGOS', 0, '0.', 5, '-', '-', <function info_RANGO at 0x0000020F388CA160>), ('SUB_RANGOS', '\x1b[32mCREAR\x1b[0m Rango', 1, '0.1.', 0, 'MenuPpal', 5, <function crear_rango at 0x0000020F388CA200>), ('SUB_RANGOS', '\x1b[32mBUSCAR\x1b[0m Rango', 1, '0.1.', 1, 'MenuPpal', 5, <function buscar_rango at 0x0000020F388CA2A0>), ('SUB_RANGOS', '\x1b[32mELIMINAR\x1b[0m Rango', 1, '0.1.', 2, 'MenuPpal', 5, <function delete_rango at 0x0000020F388CA340>), ('SUB_RANGOS', '\x1b[32mIMPRIMIR x \x1b[33mNombre Rango', 1, '0.1.', 3, 'MenuPpal', 5, <function print_rango at 0x0000020F388C99E0>), ('SUB_RANGOS', '\x1b[32mVER\x1b[0m INFO Rangos Tablero', 1, '0.1.', 4, 'MenuPpal', 5, <function ver_info_rangos at 0x0000020F388CA3E0>), ('SUB_RANGOS', '\x1b[32mPULL TO\x1b[0m \x1b[33mRANGO', 1, '0.1.', 5, 'MenuPpal', 5, <function pull at 0x0000020F388CA480>), ('MenuPpal', 'MISCELANEA', 0, '0.', 6, '-', '-', None), ('SUB_MISC', '\x1b[33mPUSH \x1b[31mMASIVO', 1, '0.1.', 0, 'MenuPpal', 6, <function push_masivo at 0x0000020F388CA980>), ('SUB_MISC', 'Prueba \x1b[35mIMPRESION MASIVA', 1, '0.1.', 1, 'MenuPpal', 6, <function impresion_masiva at 0x0000020F388CAAC0>), ('SUB_MISC', 'Get \x1b[32m General Data \x1b[0m', 1, '0.1.', 2, 'MenuPpal', 6, <function get_datos_generales at 0x0000020F388CAA20>), ('SUB_MISC', 'Cambia \x1b[35mHEAD', 1, '0.1.', 3, 'MenuPpal', 6, <function cambia_cabecera at 0x0000020F388CAB60>), ('SUB_MISC', 'Cambia \x1b[35mPIE', 1, '0.1.', 4, 'MenuPpal', 6, <function cambia_pie at 0x0000020F388CAC00>), ('SUB_MISC', '\x1b[33mSet \x1b[35mColor\x1b[0m Marco', 1, '0.1.', 5, 'MenuPpal', 6, <function set_color_marco at 0x0000020F388CAD40>), ('SUB_MISC', 'Set  \x1b[35mTipo de Marco', 1, '0.1.', 6, 'MenuPpal', 6, <function set_estilo_marco at 0x0000020F388CACA0>), ('SUB_MISC', '\x1b[33mCambia \x1b[35mColor\x1b[0m MODE EXCEL', 1, '0.1.', 7, 'MenuPpal', 6, <function set_color_excel at 0x0000020F388CADE0>)]
        ► CALLED: self.terminator__executor() y self.terminator__executor() sobre-escrito de Over-Main
        ■ EJEMPLO: 
            self.imprimir_mystyca_definiciones( menu_dvd = self.menu_dvd , lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func )
        ■ SALIDA: 
            1• None si no se puede imprimir.
            2• Salida por terminal del XindeX con los Items y las Funciones asociadas o (-) en caso de que funcion == None.
        """
        # ■■ VALIDA TITULO Y EXISTENCIA EN LA GENETICA(CONFIG)
        if not menu_dvd or not lista_m_i_l_a_n_p_i_f: 
            return None

        lst_definicion_item  = self.get_lst_definiciones( menu_dvd = menu_dvd, lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f )
        # ■■■ CARGA EL TABLERO CON LA NUEVA DEFINICION DE ITEM, PERO NO LO IMPRIME, SOLO LO PREPARA. LAS FUNCIONES NO SE CARGAN.
        self.F_RANK_Y_DEF.push( data_push=lst_definicion_item, celda_inicio=self.DICC_CELDA['definiciones'],  eje='Y' )

        if self.F_RANK_Y_DEF.head:
            if self.b_mode_all == True: 
                self.F_RANK_Y_DEF.head.push(data_push =['  ', " ■  Se ejecutan Padres e Hijos"], celda_inicio=self.DICC_CELDA['definiciones'] , b_lineal=True)
            else:
                self.F_RANK_Y_DEF.head.push(data_push =['  ', " ■  Sólo se ejecutan los Hijos"], celda_inicio=self.DICC_CELDA['definiciones'], b_lineal=True)

        lst_max_columnas = self.F_RANK_Y_DEF.get_lst_max_columnas()
        if not lst_max_columnas: return None

        # ■■ IMPRIMIR EL TABLERO DE DEFINICION.
        # self.F_RANK_Y_DEF.imprimir(lista=lst_max_columnas, sp_between = 3 , ancho_columna = None )
        self.F_RANK_Y_DEF.imprimir(sp_between = 3 , ancho_columna = None )
    
    # ■■■ OBTIENE LA LISTA DE DEFINICIONES (B_EXEC_ALL)    
    def get_lst_definiciones( self, menu_dvd, lista_m_i_l_a_n_p_i_f:list ):
        """ ■■ Devuelve LA Lista de Definicion (padre/directorio or hijo) ═ (D)' y '(X)'
        [menu_dvd](MenuDvd) : Objeto MenuDvd que se va a imprimir.
        [lista_m_i_l_a_n_p_i_f](list) = self.lst__men_itm_lev_ape_name_padr_ipadr_func() ► es la lista genética del MenuDvd.
        ► CALLED: ►self.get_matriz_impresion_literal()  ►self.imprimir_mystyca_definiciones()
        ■ EJEMPLO: 
            lst_definicion_item  = self.get_lst_definiciones( menu_dvd = menu_dvd, lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f )
        ■ SALIDA: 
            ['(D)', '(X)', '(X)', '(X)', '(X)', '(D)', '(X)', '(X)', '(X)', • • • •  '(X)']
        """
        ITEM = 1
        # OBTENEMOS LA LISTA DE PADRES GENETICOS
        lst_padres  = self.get_list_padres_mystyca(menu_dvd = menu_dvd)
        lst_definicion_item=[]
        for i, fila_genetica in enumerate(lista_m_i_l_a_n_p_i_f):
            # ■ DEFINICION
            if self.b_mode_all == True: 
                lst_definicion_item.append (f'(D)' if fila_genetica[ITEM] in lst_padres else f'(X)')
            else:
                lst_definicion_item.append (f'(-)' if fila_genetica[ITEM] in lst_padres else f'(X)')
        
        # RETORNO
        return lst_definicion_item if lst_definicion_item else None
    
    # ■■■ OBTIENE LA LISTA DE LAS FUNCIONES SEGÚN EL ORDEN GENETICO
    def get_lst_funciones( self, lista_m_i_l_a_n_p_i_f:list ):
        """ ■ Devuelve una lista con los nombres de las funciones del Menú ordenadas por indice.
        [lista_m_i_l_a_n_p_i_f](list) Lista Genetica x filas  ►[('MenuPpal', 'F_RANK_Y', 0, '0.', 0, '-', '-', <function info_TABLERO at 0x0000020F388C9440>), ('SUB_CREAR', '\x1b[92mCOMO\x1b[39m \x1b[31mEMPEZAR\x1b[39m / \x1b[92mHOW\x1b[39m \x1b[31mBEGIN', 1, '0.1.', 0, 'MenuPpal', 0, <function info_begin at 0x0000020F388C93A0>), ('SUB_CREAR', '\x1b[33mCREAR FRANKY\x1b[0m... Crea un Tablero ', 1, '0.1.', 1, 'MenuPpal', 0, <function crear_tablero at 0x0000020F388C94E0>), ('SUB_CREAR', '\x1b[33mINICIALIZA\x1b[0m Tablero (default)', 1, '0.1.', 2, 'MenuPpal', 0, <function iniciar_tablero at 0x0000020F388C9580>), ('SUB_CREAR', '\x1b[92mMODE \x1b[31m(EXCEL)', 1, '0.1.', 3, 'MenuPpal', 0, <function mode_excel at 0x0000020F388C9620>), ('MenuPpal', 'IMPRIMIR', 0, '0.', 1, '-', '-', <function info_IMPRIMIR at 0x0000020F388C96C0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mMax', 1, '0.1.', 0, 'MenuPpal', 1, <function print_max at 0x0000020F388C9760>), ('SUB_IMPR', 'IMPRIMIR Modo Literal /  \x1b[33mMosaico\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 1, <function print_literal at 0x0000020F388C9800>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mFixed', 1, '0.1.', 2, 'MenuPpal', 1, <function print_fixed at 0x0000020F388C98A0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mLista', 1, '0.1.', 3, 'MenuPpal', 1, <function print_personal at 0x0000020F388C9940>), ('SUB_IMPR', 'IMPRIMIR \x1b[33mALL IN ONE\x1b[0m (FROM-TO)', 1, '0.1.', 4, 'MenuPpal', 1, <function print_from_to at 0x0000020F388C9A80>), ('MenuPpal', 'GET', 0, '0.', 2, '-', '-', <function info_GETTING at 0x0000020F388C9B20>), ('SUB_GET', 'GETTING \x1b[36mFila', 1, '0.1.', 0, 'MenuPpal', 2, <function get_fila at 0x0000020F388C9D00>), ('SUB_GET', 'GETTING \x1b[36mColumna', 1, '0.1.', 1, 'MenuPpal', 2, <function get_columna at 0x0000020F388C9DA0>), ('SUB_GET', 'GETTING Valor By \x1b[36mFila-Columna\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 2, <function get_fila_columna at 0x0000020F388C9C60>), ('SUB_GET', 'GETTING Valor By \x1b[36mCelda\x1b[0m(A:0)', 1, '0.1.', 3, 'MenuPpal', 2, <function get_celda at 0x0000020F388C9BC0>), ('SUB_GET', 'GETTING \x1b[36mMatriz Values', 1, '0.1.', 4, 'MenuPpal', 2, <function get_matriz_values at 0x0000020F388C9E40>), ('MenuPpal', 'PUSH', 0, '0.', 3, '-', '-', <function info_push at 0x0000020F388CA520>), ('SUB_PUSH', 'PUSH \x1b[32mMATRIZ', 1, '0.1.', 0, 'MenuPpal', 3, <function matriz_to_tablero at 0x0000020F388CA5C0>), ('SUB_PUSH', 'PUSH \x1b[32mLISTA', 1, '0.1.', 1, 'MenuPpal', 3, <function push_lista at 0x0000020F388CA8E0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mFila', 1, '0.1.', 2, 'MenuPpal', 3, <function push_valor_over_fila at 0x0000020F388CA7A0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mColumn', 1, '0.1.', 3, 'MenuPpal', 3, <function push_valor_over_columna at 0x0000020F388CA840>), ('SUB_PUSH', 'PUSH Valor \x1b[32mBy Celda (C:3)', 1, '0.1.', 4, 'MenuPpal', 3, <function push_celda at 0x0000020F388CA700>), ('SUB_PUSH', 'PUSH valor \x1b[32mBy fila / columna', 1, '0.1.', 5, 'MenuPpal', 3, <function push_fila_columna at 0x0000020F388CA660>), ('MenuPpal', 'DEL', 0, '0.', 4, '-', '-', <function info_DEL at 0x0000020F388C9EE0>), ('SUB_DEL', 'DEL \x1b[36mFila\x1b[0m Over F_RANK_Y', 1, '0.1.', 0, 'MenuPpal', 4, <function del_fila at 0x0000020F388CA020>), ('SUB_DEL', 'Del \x1b[36mColumn\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 4, <function del_columna at 0x0000020F388CA0C0>), ('SUB_DEL', 'Del \x1b[36mCelda\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 4, <function del_celda at 0x0000020F388C9F80>), ('MenuPpal', 'RANGOS', 0, '0.', 5, '-', '-', <function info_RANGO at 0x0000020F388CA160>), ('SUB_RANGOS', '\x1b[32mCREAR\x1b[0m Rango', 1, '0.1.', 0, 'MenuPpal', 5, <function crear_rango at 0x0000020F388CA200>), ('SUB_RANGOS', '\x1b[32mBUSCAR\x1b[0m Rango', 1, '0.1.', 1, 'MenuPpal', 5, <function buscar_rango at 0x0000020F388CA2A0>), ('SUB_RANGOS', '\x1b[32mELIMINAR\x1b[0m Rango', 1, '0.1.', 2, 'MenuPpal', 5, <function delete_rango at 0x0000020F388CA340>), ('SUB_RANGOS', '\x1b[32mIMPRIMIR x \x1b[33mNombre Rango', 1, '0.1.', 3, 'MenuPpal', 5, <function print_rango at 0x0000020F388C99E0>), ('SUB_RANGOS', '\x1b[32mVER\x1b[0m INFO Rangos Tablero', 1, '0.1.', 4, 'MenuPpal', 5, <function ver_info_rangos at 0x0000020F388CA3E0>), ('SUB_RANGOS', '\x1b[32mPULL TO\x1b[0m \x1b[33mRANGO', 1, '0.1.', 5, 'MenuPpal', 5, <function pull at 0x0000020F388CA480>), ('MenuPpal', 'MISCELANEA', 0, '0.', 6, '-', '-', None), ('SUB_MISC', '\x1b[33mPUSH \x1b[31mMASIVO', 1, '0.1.', 0, 'MenuPpal', 6, <function push_masivo at 0x0000020F388CA980>), ('SUB_MISC', 'Prueba \x1b[35mIMPRESION MASIVA', 1, '0.1.', 1, 'MenuPpal', 6, <function impresion_masiva at 0x0000020F388CAAC0>), ('SUB_MISC', 'Get \x1b[32m General Data \x1b[0m', 1, '0.1.', 2, 'MenuPpal', 6, <function get_datos_generales at 0x0000020F388CAA20>), ('SUB_MISC', 'Cambia \x1b[35mHEAD', 1, '0.1.', 3, 'MenuPpal', 6, <function cambia_cabecera at 0x0000020F388CAB60>), ('SUB_MISC', 'Cambia \x1b[35mPIE', 1, '0.1.', 4, 'MenuPpal', 6, <function cambia_pie at 0x0000020F388CAC00>), ('SUB_MISC', '\x1b[33mSet \x1b[35mColor\x1b[0m Marco', 1, '0.1.', 5, 'MenuPpal', 6, <function set_color_marco at 0x0000020F388CAD40>), ('SUB_MISC', 'Set  \x1b[35mTipo de Marco', 1, '0.1.', 6, 'MenuPpal', 6, <function set_estilo_marco at 0x0000020F388CACA0>), ('SUB_MISC', '\x1b[33mCambia \x1b[35mColor\x1b[0m MODE EXCEL', 1, '0.1.', 7, 'MenuPpal', 6, <function set_color_excel at 0x0000020F388CADE0>)]
        
        ► CALLED: ► self.load_modulo_impresion_x()
        ■ EJEMPLO: 
            lst_funcion_item = self.get_lst_funciones( lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f )
        ■ SALIDA: 
            1• [' (info_TABLERO)', ' (info_begin)', ' (crear_tablero)', ' (iniciar_tablero)', • • • ' ( - ) ', ' (push_masivo)', • • •, ' (set_color_excel)']
            2• None, si no ecuentra o error.
        """
        try:
            lst_funcion_item=[]
            for i, fila_genetica in enumerate(lista_m_i_l_a_n_p_i_f):
                # ■ FUNCIONES EXE
                menu_dvd = self.get_menudvd(titulo = fila_genetica[0])
                funcion = menu_dvd.dicc_menu.get(fila_genetica[1])

                if callable(funcion):
                    lst_funcion_item.append(f' ({str(funcion.__name__)})')
                else:
                    lst_funcion_item.append(' ( - ) ')

            # RETORNO
            return lst_funcion_item if lst_funcion_item else None

        except Exception as e:
            print(f'{e}')
            return None
       
    # ■■■ FROM nombre-titulo-Menu TO nombre-padre     
    def get_padre(self, titulo_menu):
        """ Devuelve el (str)nombre del padre de un menú dado su titulo(id)
        [titulo_menu](str): Titulo de un MenuDvd. pejemplo 'SUB_IMPR'
        ► CALLED: mystyca_scaner_genetico
        ■ EJEMPLO: 
            retorno.append( 'SUB_IMPR' ,x,x,x,x, self.get_padre(titulo_menu = menu_dvd.titulo) ,x,x )
        ■ SALIDA: 
            1• None si no encuentra Padre   
            2• Nombre(str) del MenuDvd padre ['-', '-'] or ['MenuPpal', 0] or ['MenuPpal', 1] • • • • 
        """
        PADRE=0
        INDEX=1
        if self.dicc_xgenx:
            for tit, padre_index in self.dicc_xgenx.items():
                if titulo_menu == tit: 
                    if padre_index[PADRE]:
                        return padre_index[PADRE]
                    else:
                        return None

    # ■■■ FROM nombre-titulo TO indice en el padre
    def get_ind_en_padre(self, titulo_menu):
        """ Retorna una lista con [Nombre-del-padre , indice-en-el-padre] dado un MenuDvd según su Genética.
        ► CALLED: ► self.mystyca_scaner_genetico()
        ■ EJEMPLO: 
            retorno.append( 'SUB_IMPR' , x,x,x,x,x,self.get_ind_en_padre(titulo_menu = 'SUB_IMPR'),x )
        ■ SALIDA: 
            1•  ['-', '-']                                  ► Sin Padre, es el MenuDvd maestro.
                ['MenuPpal', 0] • • • • ['MenuPpal', 2]     ► Nombre del padre , indice en el padre.
            2• None
        """
        PADRE=0     # cte para la tupla padre/index
        INDEX=1     # cte para la tupla padre/index
        if self.dicc_xgenx:
            for tit, padre_index in self.dicc_xgenx.items():
                if titulo_menu == tit: 
                    if padre_index[PADRE]:
                        return padre_index[INDEX]
                    else:
                        return None

    # ENTRA UN ITEM Y DEVULEVO EL MENU EN EL QUE ESTÁ ?????????????????????????????????????????????????????????????
    def get_menudvd_from_item(self,menu:str, item:str, xindicex:int, lista_m_i_l_a_n_p_i_f:list ):
        """ ■■ Devuelve un MenuDvd.titulo hijo.
        [menu](str): titulo del objeto MenuDvd.                     ►'MenuPpal'
        [item](str): item por el cual se busca el objeto MenuDvd.   ►'IMPRIMIR'
        [xindicex]                                                  ►5
        [lista_m_i_l_a_n_p_i_f]: Lista genetica del XindeX.         ►[('MenuPpal', 'F_RANK_Y', 0, '0.', 0, '-', '-', <function info_TABLERO at 0x0000020F388C9440>), ('SUB_CREAR', '\x1b[92mCOMO\x1b[39m \x1b[31mEMPEZAR\x1b[39m / \x1b[92mHOW\x1b[39m \x1b[31mBEGIN', 1, '0.1.', 0, 'MenuPpal', 0, <function info_begin at 0x0000020F388C93A0>), ('SUB_CREAR', '\x1b[33mCREAR FRANKY\x1b[0m... Crea un Tablero ', 1, '0.1.', 1, 'MenuPpal', 0, <function crear_tablero at 0x0000020F388C94E0>), ('SUB_CREAR', '\x1b[33mINICIALIZA\x1b[0m Tablero (default)', 1, '0.1.', 2, 'MenuPpal', 0, <function iniciar_tablero at 0x0000020F388C9580>), ('SUB_CREAR', '\x1b[92mMODE \x1b[31m(EXCEL)', 1, '0.1.', 3, 'MenuPpal', 0, <function mode_excel at 0x0000020F388C9620>), ('MenuPpal', 'IMPRIMIR', 0, '0.', 1, '-', '-', <function info_IMPRIMIR at 0x0000020F388C96C0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mMax', 1, '0.1.', 0, 'MenuPpal', 1, <function print_max at 0x0000020F388C9760>), ('SUB_IMPR', 'IMPRIMIR Modo Literal /  \x1b[33mMosaico\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 1, <function print_literal at 0x0000020F388C9800>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mFixed', 1, '0.1.', 2, 'MenuPpal', 1, <function print_fixed at 0x0000020F388C98A0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mLista', 1, '0.1.', 3, 'MenuPpal', 1, <function print_personal at 0x0000020F388C9940>), ('SUB_IMPR', 'IMPRIMIR \x1b[33mALL IN ONE\x1b[0m (FROM-TO)', 1, '0.1.', 4, 'MenuPpal', 1, <function print_from_to at 0x0000020F388C9A80>), ('MenuPpal', 'GET', 0, '0.', 2, '-', '-', <function info_GETTING at 0x0000020F388C9B20>), ('SUB_GET', 'GETTING \x1b[36mFila', 1, '0.1.', 0, 'MenuPpal', 2, <function get_fila at 0x0000020F388C9D00>), ('SUB_GET', 'GETTING \x1b[36mColumna', 1, '0.1.', 1, 'MenuPpal', 2, <function get_columna at 0x0000020F388C9DA0>), ('SUB_GET', 'GETTING Valor By \x1b[36mFila-Columna\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 2, <function get_fila_columna at 0x0000020F388C9C60>), ('SUB_GET', 'GETTING Valor By \x1b[36mCelda\x1b[0m(A:0)', 1, '0.1.', 3, 'MenuPpal', 2, <function get_celda at 0x0000020F388C9BC0>), ('SUB_GET', 'GETTING \x1b[36mMatriz Values', 1, '0.1.', 4, 'MenuPpal', 2, <function get_matriz_values at 0x0000020F388C9E40>), ('MenuPpal', 'PUSH', 0, '0.', 3, '-', '-', <function info_push at 0x0000020F388CA520>), ('SUB_PUSH', 'PUSH \x1b[32mMATRIZ', 1, '0.1.', 0, 'MenuPpal', 3, <function matriz_to_tablero at 0x0000020F388CA5C0>), ('SUB_PUSH', 'PUSH \x1b[32mLISTA', 1, '0.1.', 1, 'MenuPpal', 3, <function push_lista at 0x0000020F388CA8E0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mFila', 1, '0.1.', 2, 'MenuPpal', 3, <function push_valor_over_fila at 0x0000020F388CA7A0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mColumn', 1, '0.1.', 3, 'MenuPpal', 3, <function push_valor_over_columna at 0x0000020F388CA840>), ('SUB_PUSH', 'PUSH Valor \x1b[32mBy Celda (C:3)', 1, '0.1.', 4, 'MenuPpal', 3, <function push_celda at 0x0000020F388CA700>), ('SUB_PUSH', 'PUSH valor \x1b[32mBy fila / columna', 1, '0.1.', 5, 'MenuPpal', 3, <function push_fila_columna at 0x0000020F388CA660>), ('MenuPpal', 'DEL', 0, '0.', 4, '-', '-', <function info_DEL at 0x0000020F388C9EE0>), ('SUB_DEL', 'DEL \x1b[36mFila\x1b[0m Over F_RANK_Y', 1, '0.1.', 0, 'MenuPpal', 4, <function del_fila at 0x0000020F388CA020>), ('SUB_DEL', 'Del \x1b[36mColumn\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 4, <function del_columna at 0x0000020F388CA0C0>), ('SUB_DEL', 'Del \x1b[36mCelda\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 4, <function del_celda at 0x0000020F388C9F80>), ('MenuPpal', 'RANGOS', 0, '0.', 5, '-', '-', <function info_RANGO at 0x0000020F388CA160>), ('SUB_RANGOS', '\x1b[32mCREAR\x1b[0m Rango', 1, '0.1.', 0, 'MenuPpal', 5, <function crear_rango at 0x0000020F388CA200>), ('SUB_RANGOS', '\x1b[32mBUSCAR\x1b[0m Rango', 1, '0.1.', 1, 'MenuPpal', 5, <function buscar_rango at 0x0000020F388CA2A0>), ('SUB_RANGOS', '\x1b[32mELIMINAR\x1b[0m Rango', 1, '0.1.', 2, 'MenuPpal', 5, <function delete_rango at 0x0000020F388CA340>), ('SUB_RANGOS', '\x1b[32mIMPRIMIR x \x1b[33mNombre Rango', 1, '0.1.', 3, 'MenuPpal', 5, <function print_rango at 0x0000020F388C99E0>), ('SUB_RANGOS', '\x1b[32mVER\x1b[0m INFO Rangos Tablero', 1, '0.1.', 4, 'MenuPpal', 5, <function ver_info_rangos at 0x0000020F388CA3E0>), ('SUB_RANGOS', '\x1b[32mPULL TO\x1b[0m \x1b[33mRANGO', 1, '0.1.', 5, 'MenuPpal', 5, <function pull at 0x0000020F388CA480>), ('MenuPpal', 'MISCELANEA', 0, '0.', 6, '-', '-', None), ('SUB_MISC', '\x1b[33mPUSH \x1b[31mMASIVO', 1, '0.1.', 0, 'MenuPpal', 6, <function push_masivo at 0x0000020F388CA980>), ('SUB_MISC', 'Prueba \x1b[35mIMPRESION MASIVA', 1, '0.1.', 1, 'MenuPpal', 6, <function impresion_masiva at 0x0000020F388CAAC0>), ('SUB_MISC', 'Get \x1b[32m General Data \x1b[0m', 1, '0.1.', 2, 'MenuPpal', 6, <function get_datos_generales at 0x0000020F388CAA20>), ('SUB_MISC', 'Cambia \x1b[35mHEAD', 1, '0.1.', 3, 'MenuPpal', 6, <function cambia_cabecera at 0x0000020F388CAB60>), ('SUB_MISC', 'Cambia \x1b[35mPIE', 1, '0.1.', 4, 'MenuPpal', 6, <function cambia_pie at 0x0000020F388CAC00>), ('SUB_MISC', '\x1b[33mSet \x1b[35mColor\x1b[0m Marco', 1, '0.1.', 5, 'MenuPpal', 6, <function set_color_marco at 0x0000020F388CAD40>), ('SUB_MISC', 'Set  \x1b[35mTipo de Marco', 1, '0.1.', 6, 'MenuPpal', 6, <function set_estilo_marco at 0x0000020F388CACA0>), ('SUB_MISC', '\x1b[33mCambia \x1b[35mColor\x1b[0m MODE EXCEL', 1, '0.1.', 7, 'MenuPpal', 6, <function set_color_excel at 0x0000020F388CADE0>)]
        ► CALLED: terminator_executor_() de XindeX
        ■ EJEMPLO:  
            titulo_menu = self.get_menudvd_from_item(item = 'IMPRIMIR', menu = 'MenuPpal' , xindicex = 5, lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f)
        ■ SALIDA: 
            str titulo del MenuDvd. ► 'SUB_IMPR'
        """
        PADRE=0
        lst_hijos=[]
        menu_dvd = self.get_menudvd(titulo=menu)

        # print(lista_m_i_l_a_n_p_i_f)
        for tit, padre_index in self.dicc_xgenx.items():
            if menu == padre_index[PADRE]:
                menudvd_hijo = self.get_menudvd( titulo = tit )
                lst_hijos.append(menudvd_hijo)
        

        indice_en_menu_hijos = int(lista_m_i_l_a_n_p_i_f[xindicex][4])
        return lst_hijos[indice_en_menu_hijos].titulo
                
    # ███████████████████████████████████████████████████████████████████████████████████
    # ████████████ XAVIER  pide datos al Usuario y le saca un Dato por Teclado ██████████
    def xavier_get_dicc_respuesta(self, menu_dvd, lista_m_i_l_a_n_p_i_f:list=None):
        """ ■■ Def: Pide Un dato al Usuario y valida (self.get_xindex ) que da una respuesta valida('b2' pejemp) con respecto a la geneticaX
        [menu_dvd] : el objeto MenuDvd (principal) sobre el que se trabaja. <classIndeX.classXindeX.MenuDvd object at 0x0000020E07AD23C0>
        [lista_m_i_l_a_n_p_i_f](list): lista genetica.  ►[('MenuPpal', 'F_RANK_Y', 0, '0.', 0, '-', '-', <function info_TABLERO at 0x0000020F388C9440>), ('SUB_CREAR', '\x1b[92mCOMO\x1b[39m \x1b[31mEMPEZAR\x1b[39m / \x1b[92mHOW\x1b[39m \x1b[31mBEGIN', 1, '0.1.', 0, 'MenuPpal', 0, <function info_begin at 0x0000020F388C93A0>), ('SUB_CREAR', '\x1b[33mCREAR FRANKY\x1b[0m... Crea un Tablero ', 1, '0.1.', 1, 'MenuPpal', 0, <function crear_tablero at 0x0000020F388C94E0>), ('SUB_CREAR', '\x1b[33mINICIALIZA\x1b[0m Tablero (default)', 1, '0.1.', 2, 'MenuPpal', 0, <function iniciar_tablero at 0x0000020F388C9580>), ('SUB_CREAR', '\x1b[92mMODE \x1b[31m(EXCEL)', 1, '0.1.', 3, 'MenuPpal', 0, <function mode_excel at 0x0000020F388C9620>), ('MenuPpal', 'IMPRIMIR', 0, '0.', 1, '-', '-', <function info_IMPRIMIR at 0x0000020F388C96C0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mMax', 1, '0.1.', 0, 'MenuPpal', 1, <function print_max at 0x0000020F388C9760>), ('SUB_IMPR', 'IMPRIMIR Modo Literal /  \x1b[33mMosaico\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 1, <function print_literal at 0x0000020F388C9800>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mFixed', 1, '0.1.', 2, 'MenuPpal', 1, <function print_fixed at 0x0000020F388C98A0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mLista', 1, '0.1.', 3, 'MenuPpal', 1, <function print_personal at 0x0000020F388C9940>), ('SUB_IMPR', 'IMPRIMIR \x1b[33mALL IN ONE\x1b[0m (FROM-TO)', 1, '0.1.', 4, 'MenuPpal', 1, <function print_from_to at 0x0000020F388C9A80>), ('MenuPpal', 'GET', 0, '0.', 2, '-', '-', <function info_GETTING at 0x0000020F388C9B20>), ('SUB_GET', 'GETTING \x1b[36mFila', 1, '0.1.', 0, 'MenuPpal', 2, <function get_fila at 0x0000020F388C9D00>), ('SUB_GET', 'GETTING \x1b[36mColumna', 1, '0.1.', 1, 'MenuPpal', 2, <function get_columna at 0x0000020F388C9DA0>), ('SUB_GET', 'GETTING Valor By \x1b[36mFila-Columna\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 2, <function get_fila_columna at 0x0000020F388C9C60>), ('SUB_GET', 'GETTING Valor By \x1b[36mCelda\x1b[0m(A:0)', 1, '0.1.', 3, 'MenuPpal', 2, <function get_celda at 0x0000020F388C9BC0>), ('SUB_GET', 'GETTING \x1b[36mMatriz Values', 1, '0.1.', 4, 'MenuPpal', 2, <function get_matriz_values at 0x0000020F388C9E40>), ('MenuPpal', 'PUSH', 0, '0.', 3, '-', '-', <function info_push at 0x0000020F388CA520>), ('SUB_PUSH', 'PUSH \x1b[32mMATRIZ', 1, '0.1.', 0, 'MenuPpal', 3, <function matriz_to_tablero at 0x0000020F388CA5C0>), ('SUB_PUSH', 'PUSH \x1b[32mLISTA', 1, '0.1.', 1, 'MenuPpal', 3, <function push_lista at 0x0000020F388CA8E0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mFila', 1, '0.1.', 2, 'MenuPpal', 3, <function push_valor_over_fila at 0x0000020F388CA7A0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mColumn', 1, '0.1.', 3, 'MenuPpal', 3, <function push_valor_over_columna at 0x0000020F388CA840>), ('SUB_PUSH', 'PUSH Valor \x1b[32mBy Celda (C:3)', 1, '0.1.', 4, 'MenuPpal', 3, <function push_celda at 0x0000020F388CA700>), ('SUB_PUSH', 'PUSH valor \x1b[32mBy fila / columna', 1, '0.1.', 5, 'MenuPpal', 3, <function push_fila_columna at 0x0000020F388CA660>), ('MenuPpal', 'DEL', 0, '0.', 4, '-', '-', <function info_DEL at 0x0000020F388C9EE0>), ('SUB_DEL', 'DEL \x1b[36mFila\x1b[0m Over F_RANK_Y', 1, '0.1.', 0, 'MenuPpal', 4, <function del_fila at 0x0000020F388CA020>), ('SUB_DEL', 'Del \x1b[36mColumn\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 4, <function del_columna at 0x0000020F388CA0C0>), ('SUB_DEL', 'Del \x1b[36mCelda\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 4, <function del_celda at 0x0000020F388C9F80>), ('MenuPpal', 'RANGOS', 0, '0.', 5, '-', '-', <function info_RANGO at 0x0000020F388CA160>), ('SUB_RANGOS', '\x1b[32mCREAR\x1b[0m Rango', 1, '0.1.', 0, 'MenuPpal', 5, <function crear_rango at 0x0000020F388CA200>), ('SUB_RANGOS', '\x1b[32mBUSCAR\x1b[0m Rango', 1, '0.1.', 1, 'MenuPpal', 5, <function buscar_rango at 0x0000020F388CA2A0>), ('SUB_RANGOS', '\x1b[32mELIMINAR\x1b[0m Rango', 1, '0.1.', 2, 'MenuPpal', 5, <function delete_rango at 0x0000020F388CA340>), ('SUB_RANGOS', '\x1b[32mIMPRIMIR x \x1b[33mNombre Rango', 1, '0.1.', 3, 'MenuPpal', 5, <function print_rango at 0x0000020F388C99E0>), ('SUB_RANGOS', '\x1b[32mVER\x1b[0m INFO Rangos Tablero', 1, '0.1.', 4, 'MenuPpal', 5, <function ver_info_rangos at 0x0000020F388CA3E0>), ('SUB_RANGOS', '\x1b[32mPULL TO\x1b[0m \x1b[33mRANGO', 1, '0.1.', 5, 'MenuPpal', 5, <function pull at 0x0000020F388CA480>), ('MenuPpal', 'MISCELANEA', 0, '0.', 6, '-', '-', None), ('SUB_MISC', '\x1b[33mPUSH \x1b[31mMASIVO', 1, '0.1.', 0, 'MenuPpal', 6, <function push_masivo at 0x0000020F388CA980>), ('SUB_MISC', 'Prueba \x1b[35mIMPRESION MASIVA', 1, '0.1.', 1, 'MenuPpal', 6, <function impresion_masiva at 0x0000020F388CAAC0>), ('SUB_MISC', 'Get \x1b[32m General Data \x1b[0m', 1, '0.1.', 2, 'MenuPpal', 6, <function get_datos_generales at 0x0000020F388CAA20>), ('SUB_MISC', 'Cambia \x1b[35mHEAD', 1, '0.1.', 3, 'MenuPpal', 6, <function cambia_cabecera at 0x0000020F388CAB60>), ('SUB_MISC', 'Cambia \x1b[35mPIE', 1, '0.1.', 4, 'MenuPpal', 6, <function cambia_pie at 0x0000020F388CAC00>), ('SUB_MISC', '\x1b[33mSet \x1b[35mColor\x1b[0m Marco', 1, '0.1.', 5, 'MenuPpal', 6, <function set_color_marco at 0x0000020F388CAD40>), ('SUB_MISC', 'Set  \x1b[35mTipo de Marco', 1, '0.1.', 6, 'MenuPpal', 6, <function set_estilo_marco at 0x0000020F388CACA0>), ('SUB_MISC', '\x1b[33mCambia \x1b[35mColor\x1b[0m MODE EXCEL', 1, '0.1.', 7, 'MenuPpal', 6, <function set_color_excel at 0x0000020F388CADE0>)]
        ► CALLED: ► self.mystyca()  en XindeX
        ■ EJEMPLO: 
            dicc_xavier = self.xavier_get_dicc__respuesta(menu_dvd = menu_dvd , lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f )
        ■ SALIDA: 
                1• {'pre': None, 'respuesta': 'a1', 'pos': None, 'xindex': 1} 
                2• {'pre': None, 'respuesta': '?', 'pos': None, 'xindex': None}
                3• {'pre': None, 'respuesta': '<', 'pos': None, 'xindex': None}
                4• None, <<< salir
        """
        MONO_FROM   = 0
        MONO_TO     = 1
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # BUCLE HASTA OPCION VALIDA or SALIR +  DESEMPAQUETA LAS  RESUPUESTAS
        respuesta_user=None
        dicc_xavier = {}

        while(True):
            dicc_xavier['pre'] = None
            dicc_xavier['respuesta'] = None
            dicc_xavier['pos'] = None
            dicc_xavier['xindex'] = None
            
            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            # ██ PIDE RESPUESTA AL USER ██
            respuesta_user = input(f"{menu_dvd.entradilla_data_user}").strip()

            # ACCION DIRECTA
            if respuesta_user in self.RESP_ACCION_DIRECTA:
                # ■■ SI HAY ALGUNA RESPUESTA DE ACCION DIRECTA NO HAY XINDEX, SOLO RESPUESTA.... para terminator_executor_
                if respuesta_user == SALIR:
                    return None
                else:
                    dicc_xavier['pre'] = None
                    dicc_xavier['respuesta'] = respuesta_user
                    dicc_xavier['pos'] = None
                    dicc_xavier['xindex'] = None
                    
                    return dicc_xavier      # RETORNO LA ACCION ? , < , <<< PARA QUE LA EVALUE TERMINATOR.            
            else:
                # ██ XINDEX: OPCION BUENA
                dicc_xavier['pre']       = None
                dicc_xavier['respuesta'] = respuesta_user
                dicc_xavier['pos']       = None
                xindex = self.get_xindex(menu_dvd = menu_dvd , dicc_respuesta = dicc_xavier, lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f)
                if  xindex is None:
                    continue
                else:
                    dicc_xavier['xindex'] = xindex
                    return dicc_xavier

        # RETORNO ██████ evaluo si hay una respuesta o varias y las devuelvo.
        return dicc_xavier if dicc_xavier else None

    def get_xindex(self, menu_dvd , dicc_respuesta:dict, lista_m_i_l_a_n_p_i_f:list):
        """ DEVUELVE EL INDICE DEL ITEM EN LA LISTA GENETICA O NONE  SI LA RESPUESTA ESTA EN EL XINDEX y COORDINA CON b_mode_all.
        
        [dicc_respuesta]:(dict), diccionario dicc_xavier que se carga en self.xavier_get_dicc__respuesta()
            Intro Opt (XindeX)..... a1    ► {'pre': None, 'respuesta': 'a1', 'pos': None, 'xindex': None}
        [lista_m_i_l_a_n_p_i_f](list): Lista de configuración genética.
            ► [('MenuPpal', 'F_RANK_Y', 0, '0.', 0, '-', '-', <function info_TABLERO at 0x0000020F388C9440>), ('SUB_CREAR', '\x1b[92mCOMO\x1b[39m \x1b[31mEMPEZAR\x1b[39m / \x1b[92mHOW\x1b[39m \x1b[31mBEGIN', 1, '0.1.', 0, 'MenuPpal', 0, <function info_begin at 0x0000020F388C93A0>), ('SUB_CREAR', '\x1b[33mCREAR FRANKY\x1b[0m... Crea un Tablero ', 1, '0.1.', 1, 'MenuPpal', 0, <function crear_tablero at 0x0000020F388C94E0>), ('SUB_CREAR', '\x1b[33mINICIALIZA\x1b[0m Tablero (default)', 1, '0.1.', 2, 'MenuPpal', 0, <function iniciar_tablero at 0x0000020F388C9580>), ('SUB_CREAR', '\x1b[92mMODE \x1b[31m(EXCEL)', 1, '0.1.', 3, 'MenuPpal', 0, <function mode_excel at 0x0000020F388C9620>), ('MenuPpal', 'IMPRIMIR', 0, '0.', 1, '-', '-', <function info_IMPRIMIR at 0x0000020F388C96C0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mMax', 1, '0.1.', 0, 'MenuPpal', 1, <function print_max at 0x0000020F388C9760>), ('SUB_IMPR', 'IMPRIMIR Modo Literal /  \x1b[33mMosaico\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 1, <function print_literal at 0x0000020F388C9800>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mFixed', 1, '0.1.', 2, 'MenuPpal', 1, <function print_fixed at 0x0000020F388C98A0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mLista', 1, '0.1.', 3, 'MenuPpal', 1, <function print_personal at 0x0000020F388C9940>), ('SUB_IMPR', 'IMPRIMIR \x1b[33mALL IN ONE\x1b[0m (FROM-TO)', 1, '0.1.', 4, 'MenuPpal', 1, <function print_from_to at 0x0000020F388C9A80>), ('MenuPpal', 'GET', 0, '0.', 2, '-', '-', <function info_GETTING at 0x0000020F388C9B20>), ('SUB_GET', 'GETTING \x1b[36mFila', 1, '0.1.', 0, 'MenuPpal', 2, <function get_fila at 0x0000020F388C9D00>), ('SUB_GET', 'GETTING \x1b[36mColumna', 1, '0.1.', 1, 'MenuPpal', 2, <function get_columna at 0x0000020F388C9DA0>), ('SUB_GET', 'GETTING Valor By \x1b[36mFila-Columna\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 2, <function get_fila_columna at 0x0000020F388C9C60>), ('SUB_GET', 'GETTING Valor By \x1b[36mCelda\x1b[0m(A:0)', 1, '0.1.', 3, 'MenuPpal', 2, <function get_celda at 0x0000020F388C9BC0>), ('SUB_GET', 'GETTING \x1b[36mMatriz Values', 1, '0.1.', 4, 'MenuPpal', 2, <function get_matriz_values at 0x0000020F388C9E40>), ('MenuPpal', 'PUSH', 0, '0.', 3, '-', '-', <function info_push at 0x0000020F388CA520>), ('SUB_PUSH', 'PUSH \x1b[32mMATRIZ', 1, '0.1.', 0, 'MenuPpal', 3, <function matriz_to_tablero at 0x0000020F388CA5C0>), ('SUB_PUSH', 'PUSH \x1b[32mLISTA', 1, '0.1.', 1, 'MenuPpal', 3, <function push_lista at 0x0000020F388CA8E0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mFila', 1, '0.1.', 2, 'MenuPpal', 3, <function push_valor_over_fila at 0x0000020F388CA7A0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mColumn', 1, '0.1.', 3, 'MenuPpal', 3, <function push_valor_over_columna at 0x0000020F388CA840>), ('SUB_PUSH', 'PUSH Valor \x1b[32mBy Celda (C:3)', 1, '0.1.', 4, 'MenuPpal', 3, <function push_celda at 0x0000020F388CA700>), ('SUB_PUSH', 'PUSH valor \x1b[32mBy fila / columna', 1, '0.1.', 5, 'MenuPpal', 3, <function push_fila_columna at 0x0000020F388CA660>), ('MenuPpal', 'DEL', 0, '0.', 4, '-', '-', <function info_DEL at 0x0000020F388C9EE0>), ('SUB_DEL', 'DEL \x1b[36mFila\x1b[0m Over F_RANK_Y', 1, '0.1.', 0, 'MenuPpal', 4, <function del_fila at 0x0000020F388CA020>), ('SUB_DEL', 'Del \x1b[36mColumn\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 4, <function del_columna at 0x0000020F388CA0C0>), ('SUB_DEL', 'Del \x1b[36mCelda\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 4, <function del_celda at 0x0000020F388C9F80>), ('MenuPpal', 'RANGOS', 0, '0.', 5, '-', '-', <function info_RANGO at 0x0000020F388CA160>), ('SUB_RANGOS', '\x1b[32mCREAR\x1b[0m Rango', 1, '0.1.', 0, 'MenuPpal', 5, <function crear_rango at 0x0000020F388CA200>), ('SUB_RANGOS', '\x1b[32mBUSCAR\x1b[0m Rango', 1, '0.1.', 1, 'MenuPpal', 5, <function buscar_rango at 0x0000020F388CA2A0>), ('SUB_RANGOS', '\x1b[32mELIMINAR\x1b[0m Rango', 1, '0.1.', 2, 'MenuPpal', 5, <function delete_rango at 0x0000020F388CA340>), ('SUB_RANGOS', '\x1b[32mIMPRIMIR x \x1b[33mNombre Rango', 1, '0.1.', 3, 'MenuPpal', 5, <function print_rango at 0x0000020F388C99E0>), ('SUB_RANGOS', '\x1b[32mVER\x1b[0m INFO Rangos Tablero', 1, '0.1.', 4, 'MenuPpal', 5, <function ver_info_rangos at 0x0000020F388CA3E0>), ('SUB_RANGOS', '\x1b[32mPULL TO\x1b[0m \x1b[33mRANGO', 1, '0.1.', 5, 'MenuPpal', 5, <function pull at 0x0000020F388CA480>), ('MenuPpal', 'MISCELANEA', 0, '0.', 6, '-', '-', None), ('SUB_MISC', '\x1b[33mPUSH \x1b[31mMASIVO', 1, '0.1.', 0, 'MenuPpal', 6, <function push_masivo at 0x0000020F388CA980>), ('SUB_MISC', 'Prueba \x1b[35mIMPRESION MASIVA', 1, '0.1.', 1, 'MenuPpal', 6, <function impresion_masiva at 0x0000020F388CAAC0>), ('SUB_MISC', 'Get \x1b[32m General Data \x1b[0m', 1, '0.1.', 2, 'MenuPpal', 6, <function get_datos_generales at 0x0000020F388CAA20>), ('SUB_MISC', 'Cambia \x1b[35mHEAD', 1, '0.1.', 3, 'MenuPpal', 6, <function cambia_cabecera at 0x0000020F388CAB60>), ('SUB_MISC', 'Cambia \x1b[35mPIE', 1, '0.1.', 4, 'MenuPpal', 6, <function cambia_pie at 0x0000020F388CAC00>), ('SUB_MISC', '\x1b[33mSet \x1b[35mColor\x1b[0m Marco', 1, '0.1.', 5, 'MenuPpal', 6, <function set_color_marco at 0x0000020F388CAD40>), ('SUB_MISC', 'Set  \x1b[35mTipo de Marco', 1, '0.1.', 6, 'MenuPpal', 6, <function set_estilo_marco at 0x0000020F388CACA0>), ('SUB_MISC', '\x1b[33mCambia \x1b[35mColor\x1b[0m MODE EXCEL', 1, '0.1.', 7, 'MenuPpal', 6, <function set_color_excel at 0x0000020F388CADE0>)]
        [menu_dvd](MenuDvd): Instancia de un objeto MenuDvd.
            <classIndeX.classXindeX.MenuDvd object at 0x0000020E07AD23C0>
        ► CALLED: 
            ►self.xavier_get_dicc__respuesta() ►self.mystyca()
        ■ EJEMPLO: 
            xindex = self.get_xindex(menu_dvd = menu_dvd , dicc_respuesta = dicc_xavier, lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f)
        ■ SALIDA: 
            xindex = 1
        """
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # LISTA DE LOS   P A D R E S   DEL MENU (RCRSV) ■■■■■■■ ....Usado para saber si tiene exec o son directorio.
        lst_padres  = self.get_list_padres_mystyca(menu_dvd = menu_dvd)        
        lst_hijos   = [ hijo for hijo in self.lst_keys if hijo not in lst_padres]

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # RESPUESTAS DE LISTAS DE OPCIONES - VALIDAS : b2, b:2, b-2 , b 2 , b.2. , b.2
        lst_valid_free          = [ ('').join(fila) for fila in self.matriz_opt_ok   ]   # FREE ( 'a1' )
        lst_valid_punto         = [ ('.').join(fila) for fila in self.matriz_opt_ok  ]   # PTO ( 'a.1' )
        lst_valid_punto_remat   = [ cadena+'.' for cadena in lst_valid_punto   ]                   # REMATE PTO ( 'a.1.' )
        lst_valid_sp            = [ (' ').join(fila) for fila in self.matriz_opt_ok  ]   # ESPACIO ( 'a 1' ) 
        lst_valid_guion         = [ ('-').join(fila) for fila in self.matriz_opt_ok  ]   # GUION ( 'a-1' )
        lst_valid_dos_puntos    = [ (':').join(fila) for fila in self.matriz_opt_ok  ]   # DOS PTOS ( 'a:1' )

        try:
            listas_validas = [ lst_valid_free, lst_valid_punto, lst_valid_punto_remat, lst_valid_sp, lst_valid_guion, lst_valid_dos_puntos ]
            
            # RECORRO TODAS LAS LISTAS VALIDAS EN BUSCA DE UN MATCH CON RESPUESTA
            for lista in listas_validas:
                # if respuesta in lista:
                if dicc_respuesta['respuesta'] in lista:
                    for i, xindex in enumerate(lista):
                        if dicc_respuesta['respuesta'] == xindex:                                                 # ■■ MATCH DE FILA

                            # ■ CON LA FILA , CACHO EL ITEM DEL MENU ■ para saber si es hijo o padre
                            item_menu = lista_m_i_l_a_n_p_i_f[i][1]
                            return i      # ■■ ENCUENTRA Y RETORNA EL INDICE EN LST_KEYS!!!!!!!!!   :) 
            
        except Exception as e:      # SI ERROR, INFO Y SEGUIMOS ::::
            print(f'ERROR EVALUACION ::: {e}')
            return None
            # continue
        pass

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # CREAR INDICEXXXX ████████████████████████
    def crear_xindicex(self, lista_m_i_l_a_n_p_i_f ): 
        """ 
        ■ ALGORITMO INFERNAL PARA SACAR LOS INDICES CORRECTOS EN LA FORMA [1, 0, 1, 2] (camino de levels)
        ■ Este retorno Se Corresponde con el level sacado de en la funcion recursiva. 
        ■ Marca la posicion que va a tener y la numeracion con respecto a esa posicion.
        ■ Se basa en la creación de la lista del indice numerico y a partir de él crea los otros índices.
        ......una pesadilla que me ha llevado días :(

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

        ■ [lista_m_i_l_a_n_p_i_f]: lst de de datos geneticos que se saca de self.mystica_ScannerX()
            ► [('MenuPpal', 'F_RANK_Y', 0, '0.', 0, '-', '-', <function info_TABLERO at 0x0000020F388C9440>), ('SUB_CREAR', '\x1b[92mCOMO\x1b[39m \x1b[31mEMPEZAR\x1b[39m / \x1b[92mHOW\x1b[39m \x1b[31mBEGIN', 1, '0.1.', 0, 'MenuPpal', 0, <function info_begin at 0x0000020F388C93A0>), ('SUB_CREAR', '\x1b[33mCREAR FRANKY\x1b[0m... Crea un Tablero ', 1, '0.1.', 1, 'MenuPpal', 0, <function crear_tablero at 0x0000020F388C94E0>), ('SUB_CREAR', '\x1b[33mINICIALIZA\x1b[0m Tablero (default)', 1, '0.1.', 2, 'MenuPpal', 0, <function iniciar_tablero at 0x0000020F388C9580>), ('SUB_CREAR', '\x1b[92mMODE \x1b[31m(EXCEL)', 1, '0.1.', 3, 'MenuPpal', 0, <function mode_excel at 0x0000020F388C9620>), ('MenuPpal', 'IMPRIMIR', 0, '0.', 1, '-', '-', <function info_IMPRIMIR at 0x0000020F388C96C0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mMax', 1, '0.1.', 0, 'MenuPpal', 1, <function print_max at 0x0000020F388C9760>), ('SUB_IMPR', 'IMPRIMIR Modo Literal /  \x1b[33mMosaico\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 1, <function print_literal at 0x0000020F388C9800>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mFixed', 1, '0.1.', 2, 'MenuPpal', 1, <function print_fixed at 0x0000020F388C98A0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mLista', 1, '0.1.', 3, 'MenuPpal', 1, <function print_personal at 0x0000020F388C9940>), ('SUB_IMPR', 'IMPRIMIR \x1b[33mALL IN ONE\x1b[0m (FROM-TO)', 1, '0.1.', 4, 'MenuPpal', 1, <function print_from_to at 0x0000020F388C9A80>), ('MenuPpal', 'GET', 0, '0.', 2, '-', '-', <function info_GETTING at 0x0000020F388C9B20>), ('SUB_GET', 'GETTING \x1b[36mFila', 1, '0.1.', 0, 'MenuPpal', 2, <function get_fila at 0x0000020F388C9D00>), ('SUB_GET', 'GETTING \x1b[36mColumna', 1, '0.1.', 1, 'MenuPpal', 2, <function get_columna at 0x0000020F388C9DA0>), ('SUB_GET', 'GETTING Valor By \x1b[36mFila-Columna\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 2, <function get_fila_columna at 0x0000020F388C9C60>), ('SUB_GET', 'GETTING Valor By \x1b[36mCelda\x1b[0m(A:0)', 1, '0.1.', 3, 'MenuPpal', 2, <function get_celda at 0x0000020F388C9BC0>), ('SUB_GET', 'GETTING \x1b[36mMatriz Values', 1, '0.1.', 4, 'MenuPpal', 2, <function get_matriz_values at 0x0000020F388C9E40>), ('MenuPpal', 'PUSH', 0, '0.', 3, '-', '-', <function info_push at 0x0000020F388CA520>), ('SUB_PUSH', 'PUSH \x1b[32mMATRIZ', 1, '0.1.', 0, 'MenuPpal', 3, <function matriz_to_tablero at 0x0000020F388CA5C0>), ('SUB_PUSH', 'PUSH \x1b[32mLISTA', 1, '0.1.', 1, 'MenuPpal', 3, <function push_lista at 0x0000020F388CA8E0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mFila', 1, '0.1.', 2, 'MenuPpal', 3, <function push_valor_over_fila at 0x0000020F388CA7A0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mColumn', 1, '0.1.', 3, 'MenuPpal', 3, <function push_valor_over_columna at 0x0000020F388CA840>), ('SUB_PUSH', 'PUSH Valor \x1b[32mBy Celda (C:3)', 1, '0.1.', 4, 'MenuPpal', 3, <function push_celda at 0x0000020F388CA700>), ('SUB_PUSH', 'PUSH valor \x1b[32mBy fila / columna', 1, '0.1.', 5, 'MenuPpal', 3, <function push_fila_columna at 0x0000020F388CA660>), ('MenuPpal', 'DEL', 0, '0.', 4, '-', '-', <function info_DEL at 0x0000020F388C9EE0>), ('SUB_DEL', 'DEL \x1b[36mFila\x1b[0m Over F_RANK_Y', 1, '0.1.', 0, 'MenuPpal', 4, <function del_fila at 0x0000020F388CA020>), ('SUB_DEL', 'Del \x1b[36mColumn\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 4, <function del_columna at 0x0000020F388CA0C0>), ('SUB_DEL', 'Del \x1b[36mCelda\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 4, <function del_celda at 0x0000020F388C9F80>), ('MenuPpal', 'RANGOS', 0, '0.', 5, '-', '-', <function info_RANGO at 0x0000020F388CA160>), ('SUB_RANGOS', '\x1b[32mCREAR\x1b[0m Rango', 1, '0.1.', 0, 'MenuPpal', 5, <function crear_rango at 0x0000020F388CA200>), ('SUB_RANGOS', '\x1b[32mBUSCAR\x1b[0m Rango', 1, '0.1.', 1, 'MenuPpal', 5, <function buscar_rango at 0x0000020F388CA2A0>), ('SUB_RANGOS', '\x1b[32mELIMINAR\x1b[0m Rango', 1, '0.1.', 2, 'MenuPpal', 5, <function delete_rango at 0x0000020F388CA340>), ('SUB_RANGOS', '\x1b[32mIMPRIMIR x \x1b[33mNombre Rango', 1, '0.1.', 3, 'MenuPpal', 5, <function print_rango at 0x0000020F388C99E0>), ('SUB_RANGOS', '\x1b[32mVER\x1b[0m INFO Rangos Tablero', 1, '0.1.', 4, 'MenuPpal', 5, <function ver_info_rangos at 0x0000020F388CA3E0>), ('SUB_RANGOS', '\x1b[32mPULL TO\x1b[0m \x1b[33mRANGO', 1, '0.1.', 5, 'MenuPpal', 5, <function pull at 0x0000020F388CA480>), ('MenuPpal', 'MISCELANEA', 0, '0.', 6, '-', '-', None), ('SUB_MISC', '\x1b[33mPUSH \x1b[31mMASIVO', 1, '0.1.', 0, 'MenuPpal', 6, <function push_masivo at 0x0000020F388CA980>), ('SUB_MISC', 'Prueba \x1b[35mIMPRESION MASIVA', 1, '0.1.', 1, 'MenuPpal', 6, <function impresion_masiva at 0x0000020F388CAAC0>), ('SUB_MISC', 'Get \x1b[32m General Data \x1b[0m', 1, '0.1.', 2, 'MenuPpal', 6, <function get_datos_generales at 0x0000020F388CAA20>), ('SUB_MISC', 'Cambia \x1b[35mHEAD', 1, '0.1.', 3, 'MenuPpal', 6, <function cambia_cabecera at 0x0000020F388CAB60>), ('SUB_MISC', 'Cambia \x1b[35mPIE', 1, '0.1.', 4, 'MenuPpal', 6, <function cambia_pie at 0x0000020F388CAC00>), ('SUB_MISC', '\x1b[33mSet \x1b[35mColor\x1b[0m Marco', 1, '0.1.', 5, 'MenuPpal', 6, <function set_color_marco at 0x0000020F388CAD40>), ('SUB_MISC', 'Set  \x1b[35mTipo de Marco', 1, '0.1.', 6, 'MenuPpal', 6, <function set_estilo_marco at 0x0000020F388CACA0>), ('SUB_MISC', '\x1b[33mCambia \x1b[35mColor\x1b[0m MODE EXCEL', 1, '0.1.', 7, 'MenuPpal', 6, <function set_color_excel at 0x0000020F388CADE0>)]        
        
        ► CALLED: self.load_modulo_gentico_x()
        ■ EJEMPLO: 
            self.lst_idx_NUMERIC, self.lst_idx_ALF_MAX, self.lst_idx_ALF_MIN, self.lst_idx_MIXTO = self.crear_xindicex( lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func  )
        ■ SALIDA: 
            lst_idx_NUMERIC ► [['1'], ['1', '1'], ['1', '2'], ['1', '3'], ['1', '4'], ['2'], ['2', '1'], ['2', '2'], ['2', '3'], ['2', '4'], ['2', '5'], ['3'], ['3', '1'], ['3', '2'], ['3', '3'], ['3', '4'], ['3', '5'], ['4'], ['4', '1'], ['4', '2'], ['4', '3'], ['4', '4'], ['4', '5'], ['4', '6'], ['5'], ['5', '1'], ['5', '2'], ['5', '3'], ['6'], ['6', '1'], ['6', '2'], ['6', '3'], ['6', '4'], ['6', '5'], ['6', '6'], ['7'], ['7', '1'], ['7', '2'], ['7', '3'], ['7', '4'], ['7', '5'], ['7', '6'], ['7', '7'], ['7', '8']]
            lst_idx_ALF_MIN ► [['a'], ['a', '1'], ['a', '2'], ['a', '3'], ['a', '4'], ['b'], ['b', '1'], ['b', '2'], ['b', '3'], ['b', '4'], ['b', '5'], ['c'], ['c', '1'], ['c', '2'], ['c', '3'], ['c', '4'], ['c', '5'], ['d'], ['d', '1'], ['d', '2'], ['d', '3'], ['d', '4'], ['d', '5'], ['d', '6'], ['e'], ['e', '1'], ['e', '2'], ['e', '3'], ['f'], ['f', '1'], ['f', '2'], ['f', '3'], ['f', '4'], ['f', '5'], ['f', '6'], ['g'], ['g', '1'], ['g', '2'], ['g', '3'], ['g', '4'], ['g', '5'], ['g', '6'], ['g', '7'], ['g', '8']]
            lst_idx_ALF_MAX ► [['A'], ['A', '1'], ['A', '2'], ['A', '3'], ['A', '4'], ['B'], ['B', '1'], ['B', '2'], ['B', '3'], ['B', '4'], ['B', '5'], ['C'], ['C', '1'], ['C', '2'], ['C', '3'], ['C', '4'], ['C', '5'], ['D'], ['D', '1'], ['D', '2'], ['D', '3'], ['D', '4'], ['D', '5'], ['D', '6'], ['E'], ['E', '1'], ['E', '2'], ['E', '3'], ['F'], ['F', '1'], ['F', '2'], ['F', '3'], ['F', '4'], ['F', '5'], ['F', '6'], ['G'], ['G', '1'], ['G', '2'], ['G', '3'], ['G', '4'], ['G', '5'], ['G', '6'], ['G', '7'], ['G', '8']]
            lst_idx_MIXTO   ► [['A'], ['A', '1'], ['A', '2'], ['A', '3'], ['A', '4'], ['B'], ['B', '1'], ['B', '2'], ['B', '3'], ['B', '4'], ['B', '5'], ['C'], ['C', '1'], ['C', '2'], ['C', '3'], ['C', '4'], ['C', '5'], ['D'], ['D', '1'], ['D', '2'], ['D', '3'], ['D', '4'], ['D', '5'], ['D', '6'], ['E'], ['E', '1'], ['E', '2'], ['E', '3'], ['F'], ['F', '1'], ['F', '2'], ['F', '3'], ['F', '4'], ['F', '5'], ['F', '6'], ['G'], ['G', '1'], ['G', '2'], ['G', '3'], ['G', '4'], ['G', '5'], ['G', '6'], ['G', '7'], ['G', '8']]
        """
        import string
        import copy

        MENU  = 0 ; ITEM  = 1 ; LEVEL = 2 ; APELL = 3 ; NAME = 4 ; PADRE = 5 ; ID_PADRE = 6
        
        dicc_min =  {idx:letra for idx, letra in enumerate(string.ascii_lowercase)} 
        dicc_may =  {idx:letra for idx, letra in enumerate(string.ascii_uppercase)}        
        
        lst_name = [ ( int(lst_a[NAME]) + 1 ) for lst_a in lista_m_i_l_a_n_p_i_f ]
        """ ■■ Lista de los nombres relativos de cada Item + 1 """
        
        # ■■ LISTA DE APELLIDOS (INDEXACION ANTERIOR A LA SUYA.)
        lst_split_apellido = [ str(lst_a[APELL]).split(sep='.')  for lst_a in lista_m_i_l_a_n_p_i_f ]        

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
                actual = lista_m_i_l_a_n_p_i_f[i]
                anterior = lista_m_i_l_a_n_p_i_f[i-1]            
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
    
    # SEGUN EL TIPO DE INDICE, DEVUELVE LAS OPCIONES CORRECTAS
    def get_lst_xindex_ok(self, tipo_index=TYPEX.NUMERIC):
        """ De todas las listas de indices creadas (lst_idx_NUMERIC, lst_idx_ALF_MAX, lst_idx_ALF_MIN, lst_idx_MIXTO ), 
        tipo_index indica cual es con la que nos quedamos.

        [tipo_index]:(str, int) ■ str => '1' , 'A', 'a' , '1a' 'a1'  ■ int => Enum TYPEX
        [lista_tipos_created]:(listr) => lista de los tipos creados usados que van a ser devueltos. esto hace que pueda personalizar los indices y crear sub-menus dentro de mystyca.
                                         ■ ES FUNDAMENTAL PASARLOS EN EL ORDEN DE DICC_OK
        ► CALLED: ► self.load_modulo_gentico_x()
        ■ EJEMPLO: 
            self.matriz_opt_ok = self.get_lst_xindex_ok(tipo_index = 'a')               
        ■ SALIDA: 
            lst_idx_ALF_MIN ► [['a'], ['a', '1'], ['a', '2'], ['a', '3'], ['a', '4'], ['b'], ['b', '1'], ['b', '2'], ['b', '3'], ['b', '4'], ['b', '5'], ['c'], ['c', '1'], ['c', '2'], ['c', '3'], ['c', '4'], ['c', '5'], ['d'], ['d', '1'], ['d', '2'], ['d', '3'], ['d', '4'], ['d', '5'], ['d', '6'], ['e'], ['e', '1'], ['e', '2'], ['e', '3'], ['f'], ['f', '1'], ['f', '2'], ['f', '3'], ['f', '4'], ['f', '5'], ['f', '6'], ['g'], ['g', '1'], ['g', '2'], ['g', '3'], ['g', '4'], ['g', '5'], ['g', '6'], ['g', '7'], ['g', '8']]
        """
        if isinstance(tipo_index, str):
            if tipo_index == 'A':
                return self.lst_idx_ALF_MAX
            elif tipo_index == 'a':
                return self.lst_idx_ALF_MIN
            elif tipo_index == '1':
                return self.lst_idx_NUMERIC
            elif str(tipo_index).upper() == '1A':
                return self.lst_idx_MIXTO
            elif str(tipo_index).upper() == 'A1':
                return self.lst_idx_MIXTO
            else:
                return self.lst_idx_NUMERIC           
            pass
        else:                                       # PERMITE NUMERICO (Clase Enum TYPEX)
            if tipo_index == TYPEX.NUMERIC:
                return self.lst_idx_NUMERIC
            elif tipo_index == TYPEX.ALF_MAX:
                return self.lst_idx_ALF_MAX
            elif tipo_index == TYPEX.ALF_MIN:
                return self.lst_idx_ALF_MIN
            elif tipo_index == TYPEX.MIXTO:
                return self.lst_idx_MIXTO
            else:               # EN CASO DE QUE NINGUNO VALGA...(byDef)
                return self.lst_idx_NUMERIC

    # ███████████████████████████████████████
    # ████████████ EJECUTADOR  ██████████████
    def terminator_executor(self, dicc_respuesta:dict, titulo_menu:str):
        """ ■ EJECUTA LA RESPUESTA INTRODUCIDA POR EL USUARIO.
        [dicc_respuesta]:(dict): diccionario respuesta que se evalua en self.xavier_get_dicc__respuesta()
            Intro Opt (XindeX)..... a1    ► {'pre': None, 'respuesta': 'a1', 'pos': None, 'xindex': None}
        [titulo_menu](str): Titulo del menú sobre el que se quiere ejecutar la respuesta.
            titulo_menu = 'SUB_IMPR'
        ► CALLED: self.mystyca() en Class XindeX. Si trabajas con la clase Over-Main esta función no se ejecuta.
        ■ EJEMPLO: 
            self.terminator__executor(dicc_respuesta = dicc_xavier, titulo_menu = self.menu_dvd.titulo)
        ■ SALIDA: 
            Ejecuta la funcion asignada al indice o Sale por <<<
        """        
        # VALIDACION
        if not isinstance(dicc_respuesta, dict): return None
        _iniciador = dicc_respuesta.get('pre', None)
        respuesta = dicc_respuesta.get('respuesta', None)
        _terminador = dicc_respuesta.get('pos', None)
        xindex = dicc_respuesta.get('xindex', None)

        COLUMNA_MENU = 0       
        COLUMNA_ITEM = 1       
        COLUMNA_FUNCION = 7        

        # ■■■■ MENU DEL TITULO
        menu_dvd = self.get_menudvd(titulo=titulo_menu)
        # ■■■■ LISTA DE LOS   P A D R E S   DEL MENU (RCRSV) ■■■■■■■ ....Usado para saber si es un menu de directorio o no.
        lst_padres  = self.get_list_padres_mystyca(menu_dvd = menu_dvd)
        
        lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func
        
        # ■■■ ACCION DIRECCTA ? , < , <<< ■■■ 
        if _iniciador is None and _terminador is None and respuesta is not None and xindex is not None:      
            
            # ■ INFO (FRANKY_DEF)
            if respuesta == '?':                                            
                os.system('cls')              
                self.imprimir_mystyca_definiciones(menu_dvd=self.menu_dvd, lista_m_i_l_a_n_p_i_f=self.lst__men_itm_lev_ape_name_padr_ipadr_func)
            
            # ■ REPETIR MENU
            elif respuesta == '<':                                          
                os.system('cls')              
                self.F_RANK_Y.imprimir(sp_between = 2, ancho_columna = None )
            
            # ■ ACCION DIRECTA  NOT FOUND
            else:                                                           
                return False
        
        # ██ INTRODUCE INDICE 
        elif _iniciador is None and _terminador is None and respuesta is not None and xindex is not None:        # ■■■ XINDEX ■■■             

            # EN MODO DIRECTORIO NO PUEDO EJECUTAR SOBRE UN PADRE
            if self.b_mode_all == False and lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_ITEM] in lst_padres:
                print(f'(DIRECTORY)')
                return      # ■ MODO DIRECTORIO Y ESTÁ ENTRE LOS PADRES EN UNA RESPUESTA DE XINDEX
            else:
                # █████████████ EJECUTA LA FUNCIONN █████████████
                lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_FUNCION]() if lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_FUNCION] else None
        
        # ■■■ NOT FOUND ■■■
        else:                                               
            return False
        
        return True

    # DEVUELVE UN LIST DE HIJOS COMPROBANDO dicc_xgenx
    def get_lst_dict_hijosX(self, titulo:str):
        """ ■■ LISTA CON MIS HIJOS DE PRIMERA GENERACION. Recorre el dicc_xgenx y recoge 
        [titulo](str) ► Título del Menú del que se quieren cachar los hijos. ►'MenuPpal'
        ► CALLED: 
            ►self.mystyca_scaner_genetico() 
            ►self.mystyca_keys() 
            ►self.get_list_padres_mystyca() 
        ■ EJEMPLO: 
            lst_hijos = self.get_lst_dict_hijosX(titulo='MenuPpal')
        ■ SALIDA: Una lista de diccionarios con los datos sobre mis hijos en dicc_xgenx :
            [{'titulo': 'SUB_CREAR', 'menuDvd': <classIndeX.classXindeX.MenuDvd object at 0x0000016D1FA991D0>, 'padre': 'MenuPpal', 'ind_en_padre': 0}, 
            {'titulo': 'SUB_IMPR', 'menuDvd': <classIndeX.classXindeX.MenuDvd object at 0x0000016D1FA99450>, 'padre': 'MenuPpal', 'ind_en_padre': 1}, 
            {'titulo': 'SUB_GET', 'menuDvd': <classIndeX.classXindeX.MenuDvd object at 0x0000016D1FA8D350>, 'padre': 'MenuPpal', 'ind_en_padre': 2}, 
            {'titulo': 'SUB_PUSH', 'menuDvd': <classIndeX.classXindeX.MenuDvd object at 0x0000016D1FA8D480>, 'padre': 'MenuPpal', 'ind_en_padre': 3}, 
            {'titulo': 'SUB_DEL', 'menuDvd': <classIndeX.classXindeX.MenuDvd object at 0x0000016D1FA260F0>, 'padre': 'MenuPpal', 'ind_en_padre': 4}, 
            {'titulo': 'SUB_RANGOS', 'menuDvd': <classIndeX.classXindeX.MenuDvd object at 0x0000016D1FA9D370>, 'padre': 'MenuPpal', 'ind_en_padre': 5}, 
            {'titulo': 'SUB_MISC', 'menuDvd': <classIndeX.classXindeX.MenuDvd object at 0x0000016D1FA9D6A0>, 'padre': 'MenuPpal', 'ind_en_padre': 6}]
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
        
    # DEVUELVE UNA MATRIZ DEL BODY DEL MENU. RECONFIGURACION PARA IMPRIMIR
    def get_matriz_impresion_literal(self, menu_dvd, lista_m_i_l_a_n_p_i_f:list, lst_keys:list, lst_opts_ok:list ):
        """ DEVUELVE LA MATRIZ DE IMPRESION GENETICA RELLENA.
        
        [menu_dvd](MenuDvd): instancia del objeto MenuDvd. ► <classIndeX.classXindeX.MenuDvd object at 0x0000020E07AD23C0>
        [lista_m_i_l_a_n_p_i_f](list): Lista Genética del menu_dvd.
            ► [('MenuPpal', 'F_RANK_Y', 0, '0.', 0, '-', '-', <function info_TABLERO at 0x0000020F388C9440>), ('SUB_CREAR', '\x1b[92mCOMO\x1b[39m \x1b[31mEMPEZAR\x1b[39m / \x1b[92mHOW\x1b[39m \x1b[31mBEGIN', 1, '0.1.', 0, 'MenuPpal', 0, <function info_begin at 0x0000020F388C93A0>), ('SUB_CREAR', '\x1b[33mCREAR FRANKY\x1b[0m... Crea un Tablero ', 1, '0.1.', 1, 'MenuPpal', 0, <function crear_tablero at 0x0000020F388C94E0>), ('SUB_CREAR', '\x1b[33mINICIALIZA\x1b[0m Tablero (default)', 1, '0.1.', 2, 'MenuPpal', 0, <function iniciar_tablero at 0x0000020F388C9580>), ('SUB_CREAR', '\x1b[92mMODE \x1b[31m(EXCEL)', 1, '0.1.', 3, 'MenuPpal', 0, <function mode_excel at 0x0000020F388C9620>), ('MenuPpal', 'IMPRIMIR', 0, '0.', 1, '-', '-', <function info_IMPRIMIR at 0x0000020F388C96C0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mMax', 1, '0.1.', 0, 'MenuPpal', 1, <function print_max at 0x0000020F388C9760>), ('SUB_IMPR', 'IMPRIMIR Modo Literal /  \x1b[33mMosaico\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 1, <function print_literal at 0x0000020F388C9800>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mFixed', 1, '0.1.', 2, 'MenuPpal', 1, <function print_fixed at 0x0000020F388C98A0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mLista', 1, '0.1.', 3, 'MenuPpal', 1, <function print_personal at 0x0000020F388C9940>), ('SUB_IMPR', 'IMPRIMIR \x1b[33mALL IN ONE\x1b[0m (FROM-TO)', 1, '0.1.', 4, 'MenuPpal', 1, <function print_from_to at 0x0000020F388C9A80>), ('MenuPpal', 'GET', 0, '0.', 2, '-', '-', <function info_GETTING at 0x0000020F388C9B20>), ('SUB_GET', 'GETTING \x1b[36mFila', 1, '0.1.', 0, 'MenuPpal', 2, <function get_fila at 0x0000020F388C9D00>), ('SUB_GET', 'GETTING \x1b[36mColumna', 1, '0.1.', 1, 'MenuPpal', 2, <function get_columna at 0x0000020F388C9DA0>), ('SUB_GET', 'GETTING Valor By \x1b[36mFila-Columna\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 2, <function get_fila_columna at 0x0000020F388C9C60>), ('SUB_GET', 'GETTING Valor By \x1b[36mCelda\x1b[0m(A:0)', 1, '0.1.', 3, 'MenuPpal', 2, <function get_celda at 0x0000020F388C9BC0>), ('SUB_GET', 'GETTING \x1b[36mMatriz Values', 1, '0.1.', 4, 'MenuPpal', 2, <function get_matriz_values at 0x0000020F388C9E40>), ('MenuPpal', 'PUSH', 0, '0.', 3, '-', '-', <function info_push at 0x0000020F388CA520>), ('SUB_PUSH', 'PUSH \x1b[32mMATRIZ', 1, '0.1.', 0, 'MenuPpal', 3, <function matriz_to_tablero at 0x0000020F388CA5C0>), ('SUB_PUSH', 'PUSH \x1b[32mLISTA', 1, '0.1.', 1, 'MenuPpal', 3, <function push_lista at 0x0000020F388CA8E0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mFila', 1, '0.1.', 2, 'MenuPpal', 3, <function push_valor_over_fila at 0x0000020F388CA7A0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mColumn', 1, '0.1.', 3, 'MenuPpal', 3, <function push_valor_over_columna at 0x0000020F388CA840>), ('SUB_PUSH', 'PUSH Valor \x1b[32mBy Celda (C:3)', 1, '0.1.', 4, 'MenuPpal', 3, <function push_celda at 0x0000020F388CA700>), ('SUB_PUSH', 'PUSH valor \x1b[32mBy fila / columna', 1, '0.1.', 5, 'MenuPpal', 3, <function push_fila_columna at 0x0000020F388CA660>), ('MenuPpal', 'DEL', 0, '0.', 4, '-', '-', <function info_DEL at 0x0000020F388C9EE0>), ('SUB_DEL', 'DEL \x1b[36mFila\x1b[0m Over F_RANK_Y', 1, '0.1.', 0, 'MenuPpal', 4, <function del_fila at 0x0000020F388CA020>), ('SUB_DEL', 'Del \x1b[36mColumn\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 4, <function del_columna at 0x0000020F388CA0C0>), ('SUB_DEL', 'Del \x1b[36mCelda\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 4, <function del_celda at 0x0000020F388C9F80>), ('MenuPpal', 'RANGOS', 0, '0.', 5, '-', '-', <function info_RANGO at 0x0000020F388CA160>), ('SUB_RANGOS', '\x1b[32mCREAR\x1b[0m Rango', 1, '0.1.', 0, 'MenuPpal', 5, <function crear_rango at 0x0000020F388CA200>), ('SUB_RANGOS', '\x1b[32mBUSCAR\x1b[0m Rango', 1, '0.1.', 1, 'MenuPpal', 5, <function buscar_rango at 0x0000020F388CA2A0>), ('SUB_RANGOS', '\x1b[32mELIMINAR\x1b[0m Rango', 1, '0.1.', 2, 'MenuPpal', 5, <function delete_rango at 0x0000020F388CA340>), ('SUB_RANGOS', '\x1b[32mIMPRIMIR x \x1b[33mNombre Rango', 1, '0.1.', 3, 'MenuPpal', 5, <function print_rango at 0x0000020F388C99E0>), ('SUB_RANGOS', '\x1b[32mVER\x1b[0m INFO Rangos Tablero', 1, '0.1.', 4, 'MenuPpal', 5, <function ver_info_rangos at 0x0000020F388CA3E0>), ('SUB_RANGOS', '\x1b[32mPULL TO\x1b[0m \x1b[33mRANGO', 1, '0.1.', 5, 'MenuPpal', 5, <function pull at 0x0000020F388CA480>), ('MenuPpal', 'MISCELANEA', 0, '0.', 6, '-', '-', None), ('SUB_MISC', '\x1b[33mPUSH \x1b[31mMASIVO', 1, '0.1.', 0, 'MenuPpal', 6, <function push_masivo at 0x0000020F388CA980>), ('SUB_MISC', 'Prueba \x1b[35mIMPRESION MASIVA', 1, '0.1.', 1, 'MenuPpal', 6, <function impresion_masiva at 0x0000020F388CAAC0>), ('SUB_MISC', 'Get \x1b[32m General Data \x1b[0m', 1, '0.1.', 2, 'MenuPpal', 6, <function get_datos_generales at 0x0000020F388CAA20>), ('SUB_MISC', 'Cambia \x1b[35mHEAD', 1, '0.1.', 3, 'MenuPpal', 6, <function cambia_cabecera at 0x0000020F388CAB60>), ('SUB_MISC', 'Cambia \x1b[35mPIE', 1, '0.1.', 4, 'MenuPpal', 6, <function cambia_pie at 0x0000020F388CAC00>), ('SUB_MISC', '\x1b[33mSet \x1b[35mColor\x1b[0m Marco', 1, '0.1.', 5, 'MenuPpal', 6, <function set_color_marco at 0x0000020F388CAD40>), ('SUB_MISC', 'Set  \x1b[35mTipo de Marco', 1, '0.1.', 6, 'MenuPpal', 6, <function set_estilo_marco at 0x0000020F388CACA0>), ('SUB_MISC', '\x1b[33mCambia \x1b[35mColor\x1b[0m MODE EXCEL', 1, '0.1.', 7, 'MenuPpal', 6, <function set_color_excel at 0x0000020F388CADE0>)]
        [lst_keys](list), 
            ['F_RANK_Y', '\x1b[92mCOMO\x1b[39m \x1b[31mEMPEZAR\x1b[39m / \x1b[92mHOW\x1b[39m \x1b[31mBEGIN', '\x1b[33mCREAR FRANKY\x1b[0m... Crea un Tablero ', '\x1b[33mINICIALIZA\x1b[0m Tablero (default)', '\x1b[92mMODE \x1b[31m(EXCEL)', 'IMPRIMIR', 'IMPRIMIR Modo  \x1b[33mMax', 'IMPRIMIR Modo Literal /  \x1b[33mMosaico\x1b[0m', 'IMPRIMIR Modo  \x1b[33mFixed', 'IMPRIMIR Modo  \x1b[33mLista', 'IMPRIMIR \x1b[33mALL IN ONE\x1b[0m (FROM-TO)', 'GET', 'GETTING \x1b[36mFila', 'GETTING \x1b[36mColumna', 'GETTING Valor By \x1b[36mFila-Columna\x1b[0m', 'GETTING Valor By \x1b[36mCelda\x1b[0m(A:0)', 'GETTING \x1b[36mMatriz Values', 'PUSH', 'PUSH \x1b[32mMATRIZ', 'PUSH \x1b[32mLISTA', 'PUSH OVER \x1b[32mFila', 'PUSH OVER \x1b[32mColumn', 'PUSH Valor \x1b[32mBy Celda (C:3)', 'PUSH valor \x1b[32mBy fila / columna', 'DEL', 'DEL \x1b[36mFila\x1b[0m Over F_RANK_Y', 'Del \x1b[36mColumn\x1b[0m', 'Del \x1b[36mCelda\x1b[0m', 'RANGOS', '\x1b[32mCREAR\x1b[0m Rango', '\x1b[32mBUSCAR\x1b[0m Rango', '\x1b[32mELIMINAR\x1b[0m Rango', '\x1b[32mIMPRIMIR x \x1b[33mNombre Rango', '\x1b[32mVER\x1b[0m INFO Rangos Tablero', '\x1b[32mPULL TO\x1b[0m \x1b[33mRANGO', 'MISCELANEA', '\x1b[33mPUSH \x1b[31mMASIVO', 'Prueba \x1b[35mIMPRESION MASIVA', 'Get \x1b[32m General Data \x1b[0m', 'Cambia \x1b[35mHEAD', 'Cambia \x1b[35mPIE', '\x1b[33mSet \x1b[35mColor\x1b[0m Marco', 'Set  \x1b[35mTipo de Marco', '\x1b[33mCambia \x1b[35mColor\x1b[0m MODE EXCEL']
        [lst_opts_ok]:(list): Lista de las opciones validas que tiene que coincidir con la dimensión de lst_keys.
            ['a', 'a.1', 'a.2', 'a.3', 'a.4', 'b', 'b.1', 'b.2', 'b.3', 'b.4', 'b.5', 'c', 'c.1', 'c.2', 'c.3', 'c.4', 'c.5', 'd', 'd.1', 'd.2', 'd.3', 'd.4', 'd.5', 'd.6', 'e', 'e.1', 'e.2', 'e.3', 'f', 'f.1', 'f.2', 'f.3', 'f.4', 'f.5', 'f.6', 'g', 'g.1', 'g.2', 'g.3', 'g.4', 'g.5', 'g.6', 'g.7', 'g.8']            
        
        ► CALLED: self.load_modulo_impresion_x()
        ■ EJEMPLO: 
            self.matriz_impresion_xindex = self.get_matriz_impresion_literal(menu_dvd = <classIndeX.classXindeX.MenuDvd object at 0x0000020E07AD23C0> , 
                                                                        lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f , 
                                                                        lst_keys = lst_keys, 
                                                                        lst_opts_ok = lst_opts_ok )
        ■ SALIDA: 
            [['', 'a', '.', ' ', 'F_RANK_Y', '', '', '', ''], ['    ', 'a.1', '.', ' ', '\x1b[92mCOMO\x1b[39m \x1b[31mEMPEZAR\x1b[39m / \x1b[92mHOW\x1b[39m \x1b[31mBEGIN', '', '', '', ''], ['    ', 'a.2', '.', ' ', '\x1b[33mCREAR FRANKY\x1b[0m... Crea un Tablero ', '', '', '', ''], ['    ', 'a.3', '.', ' ', '\x1b[33mINICIALIZA\x1b[0m Tablero (default)', '', '', '', ''], ['    ', 'a.4', '.', ' ', '\x1b[92mMODE \x1b[31m(EXCEL)', '', '', '', ''], ['', 'b', '.', ' ', 'IMPRIMIR', '', '', '', ''], ['    ', 'b.1', '.', ' ', 'IMPRIMIR Modo  \x1b[33mMax', '', '', '', ''], ['    ', 'b.2', '.', ' ', 'IMPRIMIR Modo Literal /  \x1b[33mMosaico\x1b[0m', '', '', '', ''], ['    ', 'b.3', '.', ' ', 'IMPRIMIR Modo  \x1b[33mFixed', '', '', '', ''], ['    ', 'b.4', '.', ' ', 'IMPRIMIR Modo  \x1b[33mLista', '', '', '', ''], ['    ', 'b.5', '.', ' ', 'IMPRIMIR \x1b[33mALL IN ONE\x1b[0m (FROM-TO)', '', '', '', ''], ['', 'c', '.', ' ', 'GET', '', '', '', ''], ['    ', 'c.1', '.', ' ', 'GETTING \x1b[36mFila', '', '', '', ''], ['    ', 'c.2', '.', ' ', 'GETTING \x1b[36mColumna', '', '', '', ''], ['    ', 'c.3', '.', ' ', 'GETTING Valor By \x1b[36mFila-Columna\x1b[0m', '', '', '', ''], ['    ', 'c.4', '.', ' ', 'GETTING Valor By \x1b[36mCelda\x1b[0m(A:0)', '', '', '', ''], ['    ', 'c.5', '.', ' ', 'GETTING \x1b[36mMatriz Values', '', '', '', ''], ['', 'd', '.', ' ', 'PUSH', '', '', '', ''], ['    ', 'd.1', '.', ' ', 'PUSH \x1b[32mMATRIZ', '', '', '', ''], ['    ', 'd.2', '.', ' ', 'PUSH \x1b[32mLISTA', '', '', '', ''], ['    ', 'd.3', '.', ' ', 'PUSH OVER \x1b[32mFila', '', '', '', ''], ['    ', 'd.4', '.', ' ', 'PUSH OVER \x1b[32mColumn', '', '', '', ''], ['    ', 'd.5', '.', ' ', 'PUSH Valor \x1b[32mBy Celda (C:3)', '', '', '', ''], ['    ', 'd.6', '.', ' ', 'PUSH valor \x1b[32mBy fila / columna', '', '', '', ''], ['', 'e', '.', ' ', 'DEL', '', '', '', ''], ['    ', 'e.1', '.', ' ', 'DEL \x1b[36mFila\x1b[0m Over F_RANK_Y', '', '', '', ''], ['    ', 'e.2', '.', ' ', 'Del \x1b[36mColumn\x1b[0m', '', '', '', ''], ['    ', 'e.3', '.', ' ', 'Del \x1b[36mCelda\x1b[0m', '', '', '', ''], ['', 'f', '.', ' ', 'RANGOS', '', '', '', ''], ['    ', 'f.1', '.', ' ', '\x1b[32mCREAR\x1b[0m Rango', '', '', '', ''], ['    ', 'f.2', '.', ' ', '\x1b[32mBUSCAR\x1b[0m Rango', '', '', '', ''], ['    ', 'f.3', '.', ' ', '\x1b[32mELIMINAR\x1b[0m Rango', '', '', '', ''], ['    ', 'f.4', '.', ' ', '\x1b[32mIMPRIMIR x \x1b[33mNombre Rango', '', '', '', ''], ['    ', 'f.5', '.', ' ', '\x1b[32mVER\x1b[0m INFO Rangos Tablero', '', '', '', ''], ['    ', 'f.6', '.', ' ', '\x1b[32mPULL TO\x1b[0m \x1b[33mRANGO', '', '', '', ''], ['', 'g', '.', ' ', 'MISCELANEA', '', '', '', ''], ['    ', 'g.1', '.', ' ', '\x1b[33mPUSH \x1b[31mMASIVO', '', '', '', ''], ['    ', 'g.2', '.', ' ', 'Prueba \x1b[35mIMPRESION MASIVA', '', '', '', ''], ['    ', 'g.3', '.', ' ', 'Get \x1b[32m General Data \x1b[0m', '', '', '', ''], ['    ', 'g.4', '.', ' ', 'Cambia \x1b[35mHEAD', '', '', '', ''], ['    ', 'g.5', '.', ' ', 'Cambia \x1b[35mPIE', '', '', '', ''], ['    ', 'g.6', '.', ' ', '\x1b[33mSet \x1b[35mColor\x1b[0m Marco', '', '', '', ''], ['    ', 'g.7', '.', ' ', 'Set  \x1b[35mTipo de Marco', '', '', '', ''], ['    ', 'g.8', '.', ' ', '\x1b[33mCambia \x1b[35mColor\x1b[0m MODE EXCEL', '', '', '', '']]
        """
        # VALIDACION
        # if not lst_keys: return None
        ITEM = 1
        LEVEL = 2
        # ■■ CADA LISTA REPRESENTA UNA COLUMNA. LUEGO SE MONTA
        # ■■ La impresion trabaja linea a linea, al trabajar con lista de lista de str, puedo trabajar como matriz y alterar las columnas antes de ser impreso todo como lineas.
        lst_col_0_lvl        = [f'{ int(row[LEVEL]) * self.TAB }' for row in lista_m_i_l_a_n_p_i_f]     # 1-LEVEL   
        lst_col_1_xindex     = [f'{ xindex }'  for xindex in lst_opts_ok]                               # 2-XINDEX
        lst_col_2_pto        = [f'{ '.' }'     for i in range(len(lst_keys))]                           # 3-PUNTO
        lst_col_3_sp1        = [f'{ ' ' * self.sp1}' for i in range(len(lst_keys))]                     # 4-ESPACIO
        lst_col_4_item       = [f'{ row[ITEM] }'  for row in lista_m_i_l_a_n_p_i_f]                     # 5-ITEM
        lst_col_5_sp2        = [f'{' ' * self.sp2}' for i in range(len(lst_keys))]                      # 6-ESPACIO          
        lst_col_6_definicion = self.get_lst_definiciones( menu_dvd = menu_dvd, lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f)    # 7-DEFINICION
        lst_col_7_sp3        = [f'{' ' * self.sp3}' for i in range(len(lst_keys))]                      # 8-ESPACIO
        lst_col_8_funcion    = [f'{ self.get_funcion_name(menu_dvd=self.get_menudvd(titulo=row[0]), item = row[1]) }' 
                                        for row in lista_m_i_l_a_n_p_i_f]                               # 9-FUNCION

        # ■ GENERO UNA MATRIZ VACIA ... que va a ser el molde sobre el que construir self.matriz_index
        matriz_vacia = [[0] * self.NUMERO_COLUMNAS for _ in range(len(lst_keys))]
        
        # ■ GENERA LA MATRIZ DE IMPRESION ASIGNANDO LOS DATOS DE LAS COLUMNAS
        matriz_impresion_xindex = []
        for i, lst_fila in enumerate(matriz_vacia):
            fila = []
            for j in range(len(lst_fila)):
                if j == 0:      fila.append( lst_col_0_lvl[i] )
                elif j == 1:    fila.append( lst_col_1_xindex[i] )
                elif j == 2:    fila.append( lst_col_2_pto[i] )
                elif j == 3:    fila.append( lst_col_3_sp1[i] )
                elif j == 4:    fila.append( lst_col_4_item[i])
                elif j == 5:    fila.append( '' )                
                # elif j == 5:    fila.append( lst_col_5_sp2[i] )                
                elif j == 6:    fila.append( '' )                
                elif j == 7:    fila.append( '' )                
                elif j == 8:    fila.append( '' )                
                
            matriz_impresion_xindex.append(fila) if fila else None
        
        # ■ RETORNO:
        return matriz_impresion_xindex if matriz_impresion_xindex else None

    # █████████████████████████████████████████████████████████
    # ███ REALIZA TODAS LAS ACCIONES DE GENERACION GENETICA ███
    def load_modulo_gentico_x(self, titulo:str):
        """  Carga las variables genéticas necesareas para la impresión y respuesta: 
        [titulo](str): titulo del menu sobre el que se quiere hacer el MODULO GENETICO(Relación de Menu-Items entre padres e hijos)
        ► CALLED: ► begin_asterisco() ► mystyca()
        ■ EJEMPLO: 
            self.load_modulo_gentico_x(titulo = self.menu_dvd.titulo)
        ■ SALIDA:
            None, sólo carga las variables genéticas necesareas para la impresión y respuesta: 
            self.menu_dvd, self.lst_keys, self.lst__men_itm_lev_ape_name_padr_ipadr_func, self.lst_idx_NUMERIC, self.lst_idx_ALF_MAX, self.lst_idx_ALF_MIN, self.lst_idx_MIXTO, self.matriz_opt_ok, self.lst_opts_ok
        """
        # ■■ VALIDA TITULO REPETIDO Y EXISTENCIA EN LA GENETICA(CONFIG)
        if titulo not in self.lst_titulosXX or titulo not in self.dicc_xgenx: 
            print(f'ERR-VAL:: {titulo} NO REGISTRADO EN XGENX')
            return None
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ███ CACHA EL MENU A IMPRIMIR...es la BASE GENETICA de trabajo
        menu_dvd = self.get_menudvd(titulo = titulo)
        if not menu_dvd: return None
        self.menu_dvd = menu_dvd
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ███ MODULO GENETICO 
        # ■■ LISTADO DE LOS ITEMS QUE APARECEN EN EL MENU GENETICO. en orden de aparicion en el menu.... de arriba a abajo.
        self.lst_keys = self.mystyca_keys( menu_dvd = self.menu_dvd )
        # ■■■■■■■■■■■■■ CONFIGURACION DE LA GENETICA 
        self.lst__men_itm_lev_ape_name_padr_ipadr_func = self.mystyca_scaner_genetico( menu_dvd = self.menu_dvd )            
        # ■■■■■■■■■■■■■ CREACION DE LOS INDICES GENETICOS POSIBLES
        self.lst_idx_NUMERIC, self.lst_idx_ALF_MAX, self.lst_idx_ALF_MIN, self.lst_idx_MIXTO = self.crear_xindicex( lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func  )
        # ■■■■■■■■■■■■■ MATRIZ DE XINDEX VALIDOS X USER 
        self.matriz_opt_ok = self.get_lst_xindex_ok(tipo_index = self.tipo_index)
        if not self.matriz_opt_ok: return None
        # ■■ LISTA de las OPCIONES VALIDAS ...necesaria para self.get_matriz_impresion_literal
        self.lst_opts_ok = [('.').join(fila) for fila in self.matriz_opt_ok]
        pass
    
    # ████████████████████████████████████████████████████████
    # ███ REALIZA TODAS LAS ACCIONES DE IMPRESION GENETICA ███
    def load_modulo_impresion_x(self, menu_dvd, lista_m_i_l_a_n_p_i_f:list, lst_keys:list,lst_opts_ok:list):
        """ ■■ Crea 2 Tableros, el normal(F_RANK_Y) con las opciones y los items y el de INFORMACION(F_RANK_Y_DEF) e lo imprime F_RANK_Y.
        ES LA FUNCION QUE INTERACTUA CON LA CLASE FRANKY PARA HACER LA IMPRESION DEL XINDEX Y XINDEX-FUNCIONES.
        
        [menu_dvd]:(MenuDvd), Objeto MenuDvd que contiene el menu a imprimir y ejecutar. 
            ► <classIndeX.classXindeX.MenuDvd object at 0x0000020E07AD23C0>
        [lista_m_i_l_a_n_p_i_f](list): lista de datos geneticos que se saca de self.mystica_ScannerX()
            ► [('MenuPpal', 'F_RANK_Y', 0, '0.', 0, '-', '-', <function info_TABLERO at 0x0000020F388C9440>), ('SUB_CREAR', '\x1b[92mCOMO\x1b[39m \x1b[31mEMPEZAR\x1b[39m / \x1b[92mHOW\x1b[39m \x1b[31mBEGIN', 1, '0.1.', 0, 'MenuPpal', 0, <function info_begin at 0x0000020F388C93A0>), ('SUB_CREAR', '\x1b[33mCREAR FRANKY\x1b[0m... Crea un Tablero ', 1, '0.1.', 1, 'MenuPpal', 0, <function crear_tablero at 0x0000020F388C94E0>), ('SUB_CREAR', '\x1b[33mINICIALIZA\x1b[0m Tablero (default)', 1, '0.1.', 2, 'MenuPpal', 0, <function iniciar_tablero at 0x0000020F388C9580>), ('SUB_CREAR', '\x1b[92mMODE \x1b[31m(EXCEL)', 1, '0.1.', 3, 'MenuPpal', 0, <function mode_excel at 0x0000020F388C9620>), ('MenuPpal', 'IMPRIMIR', 0, '0.', 1, '-', '-', <function info_IMPRIMIR at 0x0000020F388C96C0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mMax', 1, '0.1.', 0, 'MenuPpal', 1, <function print_max at 0x0000020F388C9760>), ('SUB_IMPR', 'IMPRIMIR Modo Literal /  \x1b[33mMosaico\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 1, <function print_literal at 0x0000020F388C9800>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mFixed', 1, '0.1.', 2, 'MenuPpal', 1, <function print_fixed at 0x0000020F388C98A0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mLista', 1, '0.1.', 3, 'MenuPpal', 1, <function print_personal at 0x0000020F388C9940>), ('SUB_IMPR', 'IMPRIMIR \x1b[33mALL IN ONE\x1b[0m (FROM-TO)', 1, '0.1.', 4, 'MenuPpal', 1, <function print_from_to at 0x0000020F388C9A80>), ('MenuPpal', 'GET', 0, '0.', 2, '-', '-', <function info_GETTING at 0x0000020F388C9B20>), ('SUB_GET', 'GETTING \x1b[36mFila', 1, '0.1.', 0, 'MenuPpal', 2, <function get_fila at 0x0000020F388C9D00>), ('SUB_GET', 'GETTING \x1b[36mColumna', 1, '0.1.', 1, 'MenuPpal', 2, <function get_columna at 0x0000020F388C9DA0>), ('SUB_GET', 'GETTING Valor By \x1b[36mFila-Columna\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 2, <function get_fila_columna at 0x0000020F388C9C60>), ('SUB_GET', 'GETTING Valor By \x1b[36mCelda\x1b[0m(A:0)', 1, '0.1.', 3, 'MenuPpal', 2, <function get_celda at 0x0000020F388C9BC0>), ('SUB_GET', 'GETTING \x1b[36mMatriz Values', 1, '0.1.', 4, 'MenuPpal', 2, <function get_matriz_values at 0x0000020F388C9E40>), ('MenuPpal', 'PUSH', 0, '0.', 3, '-', '-', <function info_push at 0x0000020F388CA520>), ('SUB_PUSH', 'PUSH \x1b[32mMATRIZ', 1, '0.1.', 0, 'MenuPpal', 3, <function matriz_to_tablero at 0x0000020F388CA5C0>), ('SUB_PUSH', 'PUSH \x1b[32mLISTA', 1, '0.1.', 1, 'MenuPpal', 3, <function push_lista at 0x0000020F388CA8E0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mFila', 1, '0.1.', 2, 'MenuPpal', 3, <function push_valor_over_fila at 0x0000020F388CA7A0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mColumn', 1, '0.1.', 3, 'MenuPpal', 3, <function push_valor_over_columna at 0x0000020F388CA840>), ('SUB_PUSH', 'PUSH Valor \x1b[32mBy Celda (C:3)', 1, '0.1.', 4, 'MenuPpal', 3, <function push_celda at 0x0000020F388CA700>), ('SUB_PUSH', 'PUSH valor \x1b[32mBy fila / columna', 1, '0.1.', 5, 'MenuPpal', 3, <function push_fila_columna at 0x0000020F388CA660>), ('MenuPpal', 'DEL', 0, '0.', 4, '-', '-', <function info_DEL at 0x0000020F388C9EE0>), ('SUB_DEL', 'DEL \x1b[36mFila\x1b[0m Over F_RANK_Y', 1, '0.1.', 0, 'MenuPpal', 4, <function del_fila at 0x0000020F388CA020>), ('SUB_DEL', 'Del \x1b[36mColumn\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 4, <function del_columna at 0x0000020F388CA0C0>), ('SUB_DEL', 'Del \x1b[36mCelda\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 4, <function del_celda at 0x0000020F388C9F80>), ('MenuPpal', 'RANGOS', 0, '0.', 5, '-', '-', <function info_RANGO at 0x0000020F388CA160>), ('SUB_RANGOS', '\x1b[32mCREAR\x1b[0m Rango', 1, '0.1.', 0, 'MenuPpal', 5, <function crear_rango at 0x0000020F388CA200>), ('SUB_RANGOS', '\x1b[32mBUSCAR\x1b[0m Rango', 1, '0.1.', 1, 'MenuPpal', 5, <function buscar_rango at 0x0000020F388CA2A0>), ('SUB_RANGOS', '\x1b[32mELIMINAR\x1b[0m Rango', 1, '0.1.', 2, 'MenuPpal', 5, <function delete_rango at 0x0000020F388CA340>), ('SUB_RANGOS', '\x1b[32mIMPRIMIR x \x1b[33mNombre Rango', 1, '0.1.', 3, 'MenuPpal', 5, <function print_rango at 0x0000020F388C99E0>), ('SUB_RANGOS', '\x1b[32mVER\x1b[0m INFO Rangos Tablero', 1, '0.1.', 4, 'MenuPpal', 5, <function ver_info_rangos at 0x0000020F388CA3E0>), ('SUB_RANGOS', '\x1b[32mPULL TO\x1b[0m \x1b[33mRANGO', 1, '0.1.', 5, 'MenuPpal', 5, <function pull at 0x0000020F388CA480>), ('MenuPpal', 'MISCELANEA', 0, '0.', 6, '-', '-', None), ('SUB_MISC', '\x1b[33mPUSH \x1b[31mMASIVO', 1, '0.1.', 0, 'MenuPpal', 6, <function push_masivo at 0x0000020F388CA980>), ('SUB_MISC', 'Prueba \x1b[35mIMPRESION MASIVA', 1, '0.1.', 1, 'MenuPpal', 6, <function impresion_masiva at 0x0000020F388CAAC0>), ('SUB_MISC', 'Get \x1b[32m General Data \x1b[0m', 1, '0.1.', 2, 'MenuPpal', 6, <function get_datos_generales at 0x0000020F388CAA20>), ('SUB_MISC', 'Cambia \x1b[35mHEAD', 1, '0.1.', 3, 'MenuPpal', 6, <function cambia_cabecera at 0x0000020F388CAB60>), ('SUB_MISC', 'Cambia \x1b[35mPIE', 1, '0.1.', 4, 'MenuPpal', 6, <function cambia_pie at 0x0000020F388CAC00>), ('SUB_MISC', '\x1b[33mSet \x1b[35mColor\x1b[0m Marco', 1, '0.1.', 5, 'MenuPpal', 6, <function set_color_marco at 0x0000020F388CAD40>), ('SUB_MISC', 'Set  \x1b[35mTipo de Marco', 1, '0.1.', 6, 'MenuPpal', 6, <function set_estilo_marco at 0x0000020F388CACA0>), ('SUB_MISC', '\x1b[33mCambia \x1b[35mColor\x1b[0m MODE EXCEL', 1, '0.1.', 7, 'MenuPpal', 6, <function set_color_excel at 0x0000020F388CADE0>)]
        [lst_keys](list): lista de los keys que aparecen en el menu genetico.
            ► ['F_RANK_Y', '\x1b[92mCOMO\x1b[39m \x1b[31mEMPEZAR\x1b[39m / \x1b[92mHOW\x1b[39m \x1b[31mBEGIN', '\x1b[33mCREAR FRANKY\x1b[0m... Crea un Tablero ', '\x1b[33mINICIALIZA\x1b[0m Tablero (default)', '\x1b[92mMODE \x1b[31m(EXCEL)', 'IMPRIMIR', 'IMPRIMIR Modo  \x1b[33mMax', 'IMPRIMIR Modo Literal /  \x1b[33mMosaico\x1b[0m', 'IMPRIMIR Modo  \x1b[33mFixed', 'IMPRIMIR Modo  \x1b[33mLista', 'IMPRIMIR \x1b[33mALL IN ONE\x1b[0m (FROM-TO)', 'GET', 'GETTING \x1b[36mFila', 'GETTING \x1b[36mColumna', 'GETTING Valor By \x1b[36mFila-Columna\x1b[0m', 'GETTING Valor By \x1b[36mCelda\x1b[0m(A:0)', 'GETTING \x1b[36mMatriz Values', 'PUSH', 'PUSH \x1b[32mMATRIZ', 'PUSH \x1b[32mLISTA', 'PUSH OVER \x1b[32mFila', 'PUSH OVER \x1b[32mColumn', 'PUSH Valor \x1b[32mBy Celda (C:3)', 'PUSH valor \x1b[32mBy fila / columna', 'DEL', 'DEL \x1b[36mFila\x1b[0m Over F_RANK_Y', 'Del \x1b[36mColumn\x1b[0m', 'Del \x1b[36mCelda\x1b[0m', 'RANGOS', '\x1b[32mCREAR\x1b[0m Rango', '\x1b[32mBUSCAR\x1b[0m Rango', '\x1b[32mELIMINAR\x1b[0m Rango', '\x1b[32mIMPRIMIR x \x1b[33mNombre Rango', '\x1b[32mVER\x1b[0m INFO Rangos Tablero', '\x1b[32mPULL TO\x1b[0m \x1b[33mRANGO', 'MISCELANEA', '\x1b[33mPUSH \x1b[31mMASIVO', 'Prueba \x1b[35mIMPRESION MASIVA', 'Get \x1b[32m General Data \x1b[0m', 'Cambia \x1b[35mHEAD', 'Cambia \x1b[35mPIE', '\x1b[33mSet \x1b[35mColor\x1b[0m Marco', 'Set  \x1b[35mTipo de Marco', '\x1b[33mCambia \x1b[35mColor\x1b[0m MODE EXCEL']
        [lst_opts_ok](list): lista de las opciones validas que aparecen en el menu genetico.
            ► ['a', 'a.1', 'a.2', 'a.3', 'a.4', 'b', 'b.1', 'b.2', 'b.3', 'b.4', 'b.5', 'c', 'c.1', 'c.2', 'c.3', 'c.4', 'c.5', 'd', 'd.1', 'd.2', 'd.3', 'd.4', 'd.5', 'd.6', 'e', 'e.1', 'e.2', 'e.3', 'f', 'f.1', 'f.2', 'f.3', 'f.4', 'f.5', 'f.6', 'g', 'g.1', 'g.2', 'g.3', 'g.4', 'g.5', 'g.6', 'g.7', 'g.8']            
        ► CALLED: ► begin_asterisco() ► mystyca()
        ■ EJEMPLO: 
            self.load_modulo_impresion_x(menu_dvd = ► <classIndeX.classXindeX.MenuDvd object at 0x0000020E07AD23C0>, 
                                    lista_m_i_l_a_n_p_i_f = ► [('MenuPpal', 'F_RANK_Y', 0, '0.', 0, '-', '-', <function info_TABLERO at 0x0000020F388C9440>), ('SUB_CREAR', '\x1b[92mCOMO\x1b[39m \x1b[31mEMPEZAR\x1b[39m / \x1b[92mHOW\x1b[39m \x1b[31mBEGIN', 1, '0.1.', 0, 'MenuPpal', 0, <function info_begin at 0x0000020F388C93A0>), ('SUB_CREAR', '\x1b[33mCREAR FRANKY\x1b[0m... Crea un Tablero ', 1, '0.1.', 1, 'MenuPpal', 0, <function crear_tablero at 0x0000020F388C94E0>), ('SUB_CREAR', '\x1b[33mINICIALIZA\x1b[0m Tablero (default)', 1, '0.1.', 2, 'MenuPpal', 0, <function iniciar_tablero at 0x0000020F388C9580>), ('SUB_CREAR', '\x1b[92mMODE \x1b[31m(EXCEL)', 1, '0.1.', 3, 'MenuPpal', 0, <function mode_excel at 0x0000020F388C9620>), ('MenuPpal', 'IMPRIMIR', 0, '0.', 1, '-', '-', <function info_IMPRIMIR at 0x0000020F388C96C0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mMax', 1, '0.1.', 0, 'MenuPpal', 1, <function print_max at 0x0000020F388C9760>), ('SUB_IMPR', 'IMPRIMIR Modo Literal /  \x1b[33mMosaico\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 1, <function print_literal at 0x0000020F388C9800>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mFixed', 1, '0.1.', 2, 'MenuPpal', 1, <function print_fixed at 0x0000020F388C98A0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mLista', 1, '0.1.', 3, 'MenuPpal', 1, <function print_personal at 0x0000020F388C9940>), ('SUB_IMPR', 'IMPRIMIR \x1b[33mALL IN ONE\x1b[0m (FROM-TO)', 1, '0.1.', 4, 'MenuPpal', 1, <function print_from_to at 0x0000020F388C9A80>), ('MenuPpal', 'GET', 0, '0.', 2, '-', '-', <function info_GETTING at 0x0000020F388C9B20>), ('SUB_GET', 'GETTING \x1b[36mFila', 1, '0.1.', 0, 'MenuPpal', 2, <function get_fila at 0x0000020F388C9D00>), ('SUB_GET', 'GETTING \x1b[36mColumna', 1, '0.1.', 1, 'MenuPpal', 2, <function get_columna at 0x0000020F388C9DA0>), ('SUB_GET', 'GETTING Valor By \x1b[36mFila-Columna\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 2, <function get_fila_columna at 0x0000020F388C9C60>), ('SUB_GET', 'GETTING Valor By \x1b[36mCelda\x1b[0m(A:0)', 1, '0.1.', 3, 'MenuPpal', 2, <function get_celda at 0x0000020F388C9BC0>), ('SUB_GET', 'GETTING \x1b[36mMatriz Values', 1, '0.1.', 4, 'MenuPpal', 2, <function get_matriz_values at 0x0000020F388C9E40>), ('MenuPpal', 'PUSH', 0, '0.', 3, '-', '-', <function info_push at 0x0000020F388CA520>), ('SUB_PUSH', 'PUSH \x1b[32mMATRIZ', 1, '0.1.', 0, 'MenuPpal', 3, <function matriz_to_tablero at 0x0000020F388CA5C0>), ('SUB_PUSH', 'PUSH \x1b[32mLISTA', 1, '0.1.', 1, 'MenuPpal', 3, <function push_lista at 0x0000020F388CA8E0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mFila', 1, '0.1.', 2, 'MenuPpal', 3, <function push_valor_over_fila at 0x0000020F388CA7A0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mColumn', 1, '0.1.', 3, 'MenuPpal', 3, <function push_valor_over_columna at 0x0000020F388CA840>), ('SUB_PUSH', 'PUSH Valor \x1b[32mBy Celda (C:3)', 1, '0.1.', 4, 'MenuPpal', 3, <function push_celda at 0x0000020F388CA700>), ('SUB_PUSH', 'PUSH valor \x1b[32mBy fila / columna', 1, '0.1.', 5, 'MenuPpal', 3, <function push_fila_columna at 0x0000020F388CA660>), ('MenuPpal', 'DEL', 0, '0.', 4, '-', '-', <function info_DEL at 0x0000020F388C9EE0>), ('SUB_DEL', 'DEL \x1b[36mFila\x1b[0m Over F_RANK_Y', 1, '0.1.', 0, 'MenuPpal', 4, <function del_fila at 0x0000020F388CA020>), ('SUB_DEL', 'Del \x1b[36mColumn\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 4, <function del_columna at 0x0000020F388CA0C0>), ('SUB_DEL', 'Del \x1b[36mCelda\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 4, <function del_celda at 0x0000020F388C9F80>), ('MenuPpal', 'RANGOS', 0, '0.', 5, '-', '-', <function info_RANGO at 0x0000020F388CA160>), ('SUB_RANGOS', '\x1b[32mCREAR\x1b[0m Rango', 1, '0.1.', 0, 'MenuPpal', 5, <function crear_rango at 0x0000020F388CA200>), ('SUB_RANGOS', '\x1b[32mBUSCAR\x1b[0m Rango', 1, '0.1.', 1, 'MenuPpal', 5, <function buscar_rango at 0x0000020F388CA2A0>), ('SUB_RANGOS', '\x1b[32mELIMINAR\x1b[0m Rango', 1, '0.1.', 2, 'MenuPpal', 5, <function delete_rango at 0x0000020F388CA340>), ('SUB_RANGOS', '\x1b[32mIMPRIMIR x \x1b[33mNombre Rango', 1, '0.1.', 3, 'MenuPpal', 5, <function print_rango at 0x0000020F388C99E0>), ('SUB_RANGOS', '\x1b[32mVER\x1b[0m INFO Rangos Tablero', 1, '0.1.', 4, 'MenuPpal', 5, <function ver_info_rangos at 0x0000020F388CA3E0>), ('SUB_RANGOS', '\x1b[32mPULL TO\x1b[0m \x1b[33mRANGO', 1, '0.1.', 5, 'MenuPpal', 5, <function pull at 0x0000020F388CA480>), ('MenuPpal', 'MISCELANEA', 0, '0.', 6, '-', '-', None), ('SUB_MISC', '\x1b[33mPUSH \x1b[31mMASIVO', 1, '0.1.', 0, 'MenuPpal', 6, <function push_masivo at 0x0000020F388CA980>), ('SUB_MISC', 'Prueba \x1b[35mIMPRESION MASIVA', 1, '0.1.', 1, 'MenuPpal', 6, <function impresion_masiva at 0x0000020F388CAAC0>), ('SUB_MISC', 'Get \x1b[32m General Data \x1b[0m', 1, '0.1.', 2, 'MenuPpal', 6, <function get_datos_generales at 0x0000020F388CAA20>), ('SUB_MISC', 'Cambia \x1b[35mHEAD', 1, '0.1.', 3, 'MenuPpal', 6, <function cambia_cabecera at 0x0000020F388CAB60>), ('SUB_MISC', 'Cambia \x1b[35mPIE', 1, '0.1.', 4, 'MenuPpal', 6, <function cambia_pie at 0x0000020F388CAC00>), ('SUB_MISC', '\x1b[33mSet \x1b[35mColor\x1b[0m Marco', 1, '0.1.', 5, 'MenuPpal', 6, <function set_color_marco at 0x0000020F388CAD40>), ('SUB_MISC', 'Set  \x1b[35mTipo de Marco', 1, '0.1.', 6, 'MenuPpal', 6, <function set_estilo_marco at 0x0000020F388CACA0>), ('SUB_MISC', '\x1b[33mCambia \x1b[35mColor\x1b[0m MODE EXCEL', 1, '0.1.', 7, 'MenuPpal', 6, <function set_color_excel at 0x0000020F388CADE0>)], 
                                    lst_keys = ► ['F_RANK_Y', '\x1b[92mCOMO\x1b[39m \x1b[31mEMPEZAR\x1b[39m / \x1b[92mHOW\x1b[39m \x1b[31mBEGIN', '\x1b[33mCREAR FRANKY\x1b[0m... Crea un Tablero ', '\x1b[33mINICIALIZA\x1b[0m Tablero (default)', '\x1b[92mMODE \x1b[31m(EXCEL)', 'IMPRIMIR', 'IMPRIMIR Modo  \x1b[33mMax', 'IMPRIMIR Modo Literal /  \x1b[33mMosaico\x1b[0m', 'IMPRIMIR Modo  \x1b[33mFixed', 'IMPRIMIR Modo  \x1b[33mLista', 'IMPRIMIR \x1b[33mALL IN ONE\x1b[0m (FROM-TO)', 'GET', 'GETTING \x1b[36mFila', 'GETTING \x1b[36mColumna', 'GETTING Valor By \x1b[36mFila-Columna\x1b[0m', 'GETTING Valor By \x1b[36mCelda\x1b[0m(A:0)', 'GETTING \x1b[36mMatriz Values', 'PUSH', 'PUSH \x1b[32mMATRIZ', 'PUSH \x1b[32mLISTA', 'PUSH OVER \x1b[32mFila', 'PUSH OVER \x1b[32mColumn', 'PUSH Valor \x1b[32mBy Celda (C:3)', 'PUSH valor \x1b[32mBy fila / columna', 'DEL', 'DEL \x1b[36mFila\x1b[0m Over F_RANK_Y', 'Del \x1b[36mColumn\x1b[0m', 'Del \x1b[36mCelda\x1b[0m', 'RANGOS', '\x1b[32mCREAR\x1b[0m Rango', '\x1b[32mBUSCAR\x1b[0m Rango', '\x1b[32mELIMINAR\x1b[0m Rango', '\x1b[32mIMPRIMIR x \x1b[33mNombre Rango', '\x1b[32mVER\x1b[0m INFO Rangos Tablero', '\x1b[32mPULL TO\x1b[0m \x1b[33mRANGO', 'MISCELANEA', '\x1b[33mPUSH \x1b[31mMASIVO', 'Prueba \x1b[35mIMPRESION MASIVA', 'Get \x1b[32m General Data \x1b[0m', 'Cambia \x1b[35mHEAD', 'Cambia \x1b[35mPIE', '\x1b[33mSet \x1b[35mColor\x1b[0m Marco', 'Set  \x1b[35mTipo de Marco', '\x1b[33mCambia \x1b[35mColor\x1b[0m MODE EXCEL'] ,
                                    lst_opts_ok = ['a', 'a.1', 'a.2', 'a.3', 'a.4', 'b', 'b.1', 'b.2', 'b.3', 'b.4', 'b.5', 'c', 'c.1', 'c.2', 'c.3', 'c.4', 'c.5', 'd', 'd.1', 'd.2', 'd.3', 'd.4', 'd.5', 'd.6', 'e', 'e.1', 'e.2', 'e.3', 'f', 'f.1', 'f.2', 'f.3', 'f.4', 'f.5', 'f.6', 'g', 'g.1', 'g.2', 'g.3', 'g.4', 'g.5', 'g.6', 'g.7', 'g.8'] )
        ■ SALIDA: 
            CREA E IMPRIME EL TABLERO FRANKY    ► self.F_RANK_Y.imprimir(sp_between = 2, ancho_columna = None )   # ■ Imprimir max-Columnas
            CREA EL TABLERO FRANKY-DEF          ► self.F_RANK_Y_DEF = F_r_a_n_k_y__( dimension = f'{filas}X{columnas}', head_datapush = self.head_datapush , pie_datapush=self.pie_datapush , pad_x = self.pad_x )
            None, si hay algún error en la carga de la matriz de impresión.

        """ 
            
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■  TABLERO DE XINDEX 
        # ■■ MATRIZ DE IMPRESION: ■■■
        # ■■ b_definicion = False > sin incluir las columnas de definicion
        self.matriz_impresion_xindex = self.get_matriz_impresion_literal(menu_dvd = menu_dvd , 
                                                                        lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f , 
                                                                        lst_keys = lst_keys, 
                                                                        lst_opts_ok = lst_opts_ok )        
        if not self.matriz_impresion_xindex: 
            print('ERROR :::: EN MATRIZ IMPRESION PPAL')
            return None      
        # ■■ LISTA DE STRING PARA IMPRIMIR 
        lst_mystyca_impresion = [''.join(mystyca_fila) for mystyca_fila in self.matriz_impresion_xindex]
        
        # ■■ LONGITUD MAXIMA DEL MENU..... usado para calcular el ancho de la columna.
        self.longitud_max_xindex = max(len(line) for line in lst_mystyca_impresion)
        
        # ■■ SACO LAS FILAS Y COLUMNAS DE ESTA GENETICA PARA PODER SACAR UNA DIMENSION PARA CREAR EL TABLERO DE IMPRESION FRANKY
        filas = len(self.matriz_impresion_xindex)
        columnas = len(self.matriz_impresion_xindex[0])

        self.F_RANK_Y = F_r_a_n_k_y(dimension = f'{filas}X{columnas}', 
                                    head_datapush = self.head_datapush , 
                                    pie_datapush=self.pie_datapush , 
                                    pad_x = self.pad_x )
        
        self.F_RANK_Y.push(data_push=lst_mystyca_impresion, eje='Y')    # ■ Ponemos en el Tablero la lista de Impresión.

        self.F_RANK_Y.imprimir(sp_between = 2, ancho_columna = None )   # ■ Imprimir max-Columnas
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■ TABLERO DE INFORMACION ? ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■  
        # ■ Preparo otro Tablero paralelo para la definicion de los items, que se va a imprimir al lado del menu.
        self.F_RANK_Y_DEF = F_r_a_n_k_y( dimension = f'{filas}X{columnas}', head_datapush = self.head_datapush , pie_datapush=self.pie_datapush , pad_x = self.pad_x )
        self.F_RANK_Y_DEF.push(data_push=lst_mystyca_impresion, eje='Y')
        
        # ■■ LISTA DE DEFINICIONES DE MENU GENETICO
        lst_definicion_item  = self.get_lst_definiciones( menu_dvd = menu_dvd, lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f )
        # lst_definicion_item = [f'{Fore.RED}{item}{Style.RESET_ALL}' for item in lst_definicion_item] if lst_definicion_item else None
        # ■■ LISTA DE FUNCIONES DE MENU GENETICO
        lst_funcion_item = self.get_lst_funciones( lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f )

        # ■■■ CARGA EL TABLERO PERO NO LO IMPRIME, SOLO LO PREPARA.
        self.F_RANK_Y_DEF.push( data_push=lst_definicion_item, celda_inicio=self.DICC_CELDA['definiciones'],  eje='Y' )
        self.F_RANK_Y_DEF.push( data_push=lst_funcion_item, celda_inicio=self.DICC_CELDA['funciones'],  eje='Y' )
        pass
        # ■■■ RETORNO 
        return True
    
    # ████████████████████████████████████████████████████████
    # ██████████████ DEVUELVE LAS LISTAS XA WEB ██████████████
    def get_web_lsts_lens_linea(self, titulo,  tipo_index=0, b_mode_all=True, b_loop=True, pad_x=15):
        """ Devuelve lo que necesita la web para representarse 
        [titulo](str): El titulo del menu. (obligatorio                   )
        [tipo_index](0, 'a', 'A', 'A0')
        [b_mode_all](bool)
        [b_loop](bool)
        [pad_x](int)
        ► CALLED: 
        ■ EJEMPLO: 
            
        ■ SALIDA: OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        """
        # ■■■■ VALIDA SI EL TITULO ESTA REPETIDO Y LA EXISTENCIA EN LA GENETICA(self.config())        
        if titulo not in self.lst_titulosXX or titulo not in self.dicc_xgenx: 
            print(f'ERR-VAL:: {titulo} NO REGISTRADO EN XGENX')
            return None
        print('En Construcción......')        
        
        # ■■■■ MODULO CONFIG    
        # ■■■■ MODULO GENETICO     ■ lista_m_i_l_a_n_p_i_f  ■ lst_keys  ■ lst_opciones_ok  ■ crear_xindicex
        # ■■■■ MODULO IMPRESION    ■ get_matriz_impresion_literal   
        # ■■■■ MODULO RESPUESTA
        pass


# █████████████████████████████████████████████████████████████████████████████████████████████████████████████
# ██████████████████████████████████████ OVER MAIN ████████████████████████████████████████████████████████████
# █████████████████████████████████████████████████████████████████████████████████████████████████████████████
import multiprocessing
import time
import sys
import os
import json
import subprocess
from collections import defaultdict
from colorama import Fore, Style
# ============================================================================================
class Over_Main(XindeX):
    """ AMPLIA XindeX Añadiendo la ejecución en hilos separados .... 
        ■■ EJECUTA Interactivo ( tkinter ) , 
        ■■ EJECUTA Segundo plano demonio( flask ) 
        ■■ IMPLEMENTA COLOR EN HEAD Y PIE... A TRAVES DE style().

        ■ EJEMPLO: 
            from classIndeX.classXindeX import Over_Main      # Versión de Lanzamiento de XindeX como Demonio y Background, Modo Like, Modo Sub-Menu.

            1• The_X_Men = Over_Main()                                              ► Crea un objeto Over_Main de alf min , Sólo se ejecutan los hijos(b_mode_all=False) y se sale por <<< (b_loop=True)            
            2• The_X_Men = Over_Main(tipo_index='a', b_mode_all=True, b_loop=True ) ► Crea un objeto Over_Main de alf min , Todo se ejecuta(b_mode_all=True) y se sale por <<< (b_loop=True)            
    """
    # Inicializa colorama (necesario para Windows)
    FROM_TO = '-'           # CARACTER USADO (PARA EL PATRON RE) PARA IMPRIMIR ■ FROM - TO 

    def __init__(self,  dicc_funciones=None, 
                        tipo_index:str='a', 
                        b_mode_all:bool=False, 
                        b_loop=True ,
                        b_config=None, 
                        ):                

        # ■■ LLAMADAA AL PADRE
        super().__init__(tipo_index=tipo_index, b_mode_all=b_mode_all, b_loop = b_loop )

        init(autoreset=True)      # Para usar colorama en Windows

        # self.pie_datapush = self.set_color(texto=self.pie_datapush)
        self.pie_datapush = f'Salir {self.set_color(texto="<<<", color=Fore.GREEN)}  ■  Help-Exec {self.set_color(texto="?")}  ■  Repeat  {self.set_color(texto="<")}   ■ (Info)  {self.set_color(texto="??")} '

        # ■■ DICCIONARIO PARA EL CONTROL DE HILOS CON LAS EJECUCIONES =>b2 (INDEPENDIENTE)(DEMONIO) Y <<b2>> (DEPENDIETE)
        self.dicc_procesos = {}

        self.RESP_ACCION_DIRECTA = ['<' , '?' , '??' , 'help', '<<<', '#' , '@', '$']
        """ ■ DIRECTAS ... SOBRE ESCRITO DE INDEX PARA INCLUIR 'list'( listar procesos) y 'kill'(parar procesos) """
        
        self.RESP_BEGINNERS = ['**', '=>', '=' ]
        """ ■ PREFIJO + RESPUESTA ... Se evalua cada uno:  """
        
        self.RESP_BACKGROUND = ['[',']']        
        """ ■ ENVUELTAS... Se evalua la lista como una unidad, (pre y pos)(envoltorio) :  """
        
        self.RESP_LIKE_STR = ['"','"']        
        """ ■ ENVUELTAS... Se evalua la lista como una unidad, (pre y pos)(envoltorio):  """

        self.RESP_PROCESOS = ['►', '■' , '■ ', 'list', 'stop', 'stop ', 'kill', 'listar']
        """ ■■ RESPUESTAS PARA CONTROL DE PROCESOS: '►' (Alt+16, listar procesos) y '■' (Alt+254, parar procesos) """
        
        # ████████████████████████████████
        # ■■■ Propiedades del Orquestador
        # 🧠 Archivos simples para hablar con Streamlit: config estable + retorno de la última ejecución.
        self.archivo_config = "config_menu.json"
        self.archivo_retorno_streamlit = "temp_menu_resultado.json"
        self.datos_streamlit = None
        self.dicc_funciones = dicc_funciones if dicc_funciones else {}
        
        # PARSEO AUTOMÁTICO DE CONSOLA (Si b_config es None, miramos si el usuario escribió --config)
        if b_config is None:
            self.b_config = "--config" in sys.argv
        else:
            self.b_config = b_config
            
        # INICIAR FLUJO DE ESTADOS
        self._gestionar_estados()

    def _gestionar_estados(self):
        # 🧠 Orquesta el flujo: si hace falta configurar, espera Streamlit y después usa sus datos.
        json_existe = os.path.exists(self.archivo_config)
        
        # Lanza la web si se fuerza configuración o si es la primera vez
        if not json_existe or self.b_config:
            self.datos_streamlit = self._lanzar_configurador()
            json_existe = os.path.exists(self.archivo_config)
            
        if not json_existe:
            print(f"{Fore.RED}❌ Error crítico: No hay configuración de menú guardada. Abortando.{Style.RESET_ALL}")
            sys.exit(1)
            
        # Si llegamos aquí, el JSON existe y es seguro construir el menú
        self._construir_desde_json()
        
    def _lanzar_configurador(self):
        # 🧠 Streamlit corre como subproceso; al guardar, la app escribe JSON y se cierra sola.
        print(f"{Fore.CYAN}⚙️  Abriendo el configurador visual en tu navegador...{Style.RESET_ALL}")
        
        if os.path.exists(self.archivo_retorno_streamlit):
            os.remove(self.archivo_retorno_streamlit)

        # Calculamos la ruta segura de Streamlit para lanzarlo
        ruta_st = os.path.join("XindeX", "xindex_st.py")
        entorno = os.environ.copy()
        entorno["XINDEX_CONFIG_DESDE_CERO"] = "1" if self.b_config or not os.path.exists(self.archivo_config) else "0"
        proc = subprocess.Popen(["streamlit", "run", ruta_st], env=entorno)
        
        print(f"{Fore.YELLOW}► El programa está esperando a que guardes o cierres Streamlit.{Style.RESET_ALL}")
        proc.wait()

        if os.path.exists(self.archivo_retorno_streamlit):
            with open(self.archivo_retorno_streamlit, "r", encoding="utf-8") as f:
                datos = json.load(f)
            os.remove(self.archivo_retorno_streamlit)
            print(f"{Fore.GREEN}✅ Datos recibidos desde Streamlit.{Style.RESET_ALL}")
            return datos

        print(f"{Fore.YELLOW}⚠️  Streamlit terminó sin devolver datos nuevos.{Style.RESET_ALL}")
        return None
            
    def _construir_desde_json(self):
        # 🧠 Construye el árbol desde memoria si venimos de Streamlit; si no, desde el JSON guardado.
        if self.datos_streamlit is not None:
            nodos = self.datos_streamlit
        else:
            with open(self.archivo_config, "r", encoding='utf-8') as f:
                nodos = json.load(f)

        padres_por_nivel = {}
        items_por_padre = defaultdict(list)
        info_submenus = {}

        for nodo in nodos:
            lvl = nodo.get('indentacion', 0)
            txt = nodo.get('texto', 'Sin Título')
            func_str = nodo.get('funcion')
            
            txt_padre = padres_por_nivel.get(lvl - 1) if lvl > 0 else None
            func_real = self.dicc_funciones.get(func_str) if func_str else None
            
            items_por_padre[txt_padre].append((txt, func_real))
            padres_por_nivel[lvl] = txt
            info_submenus[txt] = {'padre': txt_padre, 'ipadre': txt}

        # Generador de Árbol para Mystyca
        for nombre_menu, lista_items in items_por_padre.items():
            if nombre_menu is None:
                self.addX(titulo='MAIN_MENU', padre=None, ipadre=None, lst_items=lista_items)
            else:
                info = info_submenus[nombre_menu]
                padre_real = info['padre'] if info['padre'] is not None else 'MAIN_MENU'
                self.addX(titulo=nombre_menu, padre=padre_real, ipadre=info['ipadre'], lst_items=lista_items)

    # ██ SOBRE-ESCRIBE XAVIER de XindeX 
    def xavier_get_dicc_respuesta(self, menu_dvd, lista_m_i_l_a_n_p_i_f:list=None):
        """ ► SOBRE-ESCRIBE el método en MenuDvd.
        ■■ Pide Un dato al Usuario y valida (self.get_xindex) que da una respuesta_user valida('b2' pejemp) con respecto a la geneticaX. 

        [menu_dvd] : el objeto MenuDvd (principal) sobre el que se trabaja. el punto de partida del analisis
            ► <classIndeX.classXindeX.MenuDvd object at 0x0000020E07AD23C0>
        [lista_m_i_l_a_n_p_i_f]: 
            ► [('MenuPpal', 'F_RANK_Y', 0, '0.', 0, '-', '-', <function info_TABLERO at 0x0000020F388C9440>), ('SUB_CREAR', '\x1b[92mCOMO\x1b[39m \x1b[31mEMPEZAR\x1b[39m / \x1b[92mHOW\x1b[39m \x1b[31mBEGIN', 1, '0.1.', 0, 'MenuPpal', 0, <function info_begin at 0x0000020F388C93A0>), ('SUB_CREAR', '\x1b[33mCREAR FRANKY\x1b[0m... Crea un Tablero ', 1, '0.1.', 1, 'MenuPpal', 0, <function crear_tablero at 0x0000020F388C94E0>), ('SUB_CREAR', '\x1b[33mINICIALIZA\x1b[0m Tablero (default)', 1, '0.1.', 2, 'MenuPpal', 0, <function iniciar_tablero at 0x0000020F388C9580>), ('SUB_CREAR', '\x1b[92mMODE \x1b[31m(EXCEL)', 1, '0.1.', 3, 'MenuPpal', 0, <function mode_excel at 0x0000020F388C9620>), ('MenuPpal', 'IMPRIMIR', 0, '0.', 1, '-', '-', <function info_IMPRIMIR at 0x0000020F388C96C0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mMax', 1, '0.1.', 0, 'MenuPpal', 1, <function print_max at 0x0000020F388C9760>), ('SUB_IMPR', 'IMPRIMIR Modo Literal /  \x1b[33mMosaico\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 1, <function print_literal at 0x0000020F388C9800>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mFixed', 1, '0.1.', 2, 'MenuPpal', 1, <function print_fixed at 0x0000020F388C98A0>), ('SUB_IMPR', 'IMPRIMIR Modo  \x1b[33mLista', 1, '0.1.', 3, 'MenuPpal', 1, <function print_personal at 0x0000020F388C9940>), ('SUB_IMPR', 'IMPRIMIR \x1b[33mALL IN ONE\x1b[0m (FROM-TO)', 1, '0.1.', 4, 'MenuPpal', 1, <function print_from_to at 0x0000020F388C9A80>), ('MenuPpal', 'GET', 0, '0.', 2, '-', '-', <function info_GETTING at 0x0000020F388C9B20>), ('SUB_GET', 'GETTING \x1b[36mFila', 1, '0.1.', 0, 'MenuPpal', 2, <function get_fila at 0x0000020F388C9D00>), ('SUB_GET', 'GETTING \x1b[36mColumna', 1, '0.1.', 1, 'MenuPpal', 2, <function get_columna at 0x0000020F388C9DA0>), ('SUB_GET', 'GETTING Valor By \x1b[36mFila-Columna\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 2, <function get_fila_columna at 0x0000020F388C9C60>), ('SUB_GET', 'GETTING Valor By \x1b[36mCelda\x1b[0m(A:0)', 1, '0.1.', 3, 'MenuPpal', 2, <function get_celda at 0x0000020F388C9BC0>), ('SUB_GET', 'GETTING \x1b[36mMatriz Values', 1, '0.1.', 4, 'MenuPpal', 2, <function get_matriz_values at 0x0000020F388C9E40>), ('MenuPpal', 'PUSH', 0, '0.', 3, '-', '-', <function info_push at 0x0000020F388CA520>), ('SUB_PUSH', 'PUSH \x1b[32mMATRIZ', 1, '0.1.', 0, 'MenuPpal', 3, <function matriz_to_tablero at 0x0000020F388CA5C0>), ('SUB_PUSH', 'PUSH \x1b[32mLISTA', 1, '0.1.', 1, 'MenuPpal', 3, <function push_lista at 0x0000020F388CA8E0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mFila', 1, '0.1.', 2, 'MenuPpal', 3, <function push_valor_over_fila at 0x0000020F388CA7A0>), ('SUB_PUSH', 'PUSH OVER \x1b[32mColumn', 1, '0.1.', 3, 'MenuPpal', 3, <function push_valor_over_columna at 0x0000020F388CA840>), ('SUB_PUSH', 'PUSH Valor \x1b[32mBy Celda (C:3)', 1, '0.1.', 4, 'MenuPpal', 3, <function push_celda at 0x0000020F388CA700>), ('SUB_PUSH', 'PUSH valor \x1b[32mBy fila / columna', 1, '0.1.', 5, 'MenuPpal', 3, <function push_fila_columna at 0x0000020F388CA660>), ('MenuPpal', 'DEL', 0, '0.', 4, '-', '-', <function info_DEL at 0x0000020F388C9EE0>), ('SUB_DEL', 'DEL \x1b[36mFila\x1b[0m Over F_RANK_Y', 1, '0.1.', 0, 'MenuPpal', 4, <function del_fila at 0x0000020F388CA020>), ('SUB_DEL', 'Del \x1b[36mColumn\x1b[0m', 1, '0.1.', 1, 'MenuPpal', 4, <function del_columna at 0x0000020F388CA0C0>), ('SUB_DEL', 'Del \x1b[36mCelda\x1b[0m', 1, '0.1.', 2, 'MenuPpal', 4, <function del_celda at 0x0000020F388C9F80>), ('MenuPpal', 'RANGOS', 0, '0.', 5, '-', '-', <function info_RANGO at 0x0000020F388CA160>), ('SUB_RANGOS', '\x1b[32mCREAR\x1b[0m Rango', 1, '0.1.', 0, 'MenuPpal', 5, <function crear_rango at 0x0000020F388CA200>), ('SUB_RANGOS', '\x1b[32mBUSCAR\x1b[0m Rango', 1, '0.1.', 1, 'MenuPpal', 5, <function buscar_rango at 0x0000020F388CA2A0>), ('SUB_RANGOS', '\x1b[32mELIMINAR\x1b[0m Rango', 1, '0.1.', 2, 'MenuPpal', 5, <function delete_rango at 0x0000020F388CA340>), ('SUB_RANGOS', '\x1b[32mIMPRIMIR x \x1b[33mNombre Rango', 1, '0.1.', 3, 'MenuPpal', 5, <function print_rango at 0x0000020F388C99E0>), ('SUB_RANGOS', '\x1b[32mVER\x1b[0m INFO Rangos Tablero', 1, '0.1.', 4, 'MenuPpal', 5, <function ver_info_rangos at 0x0000020F388CA3E0>), ('SUB_RANGOS', '\x1b[32mPULL TO\x1b[0m \x1b[33mRANGO', 1, '0.1.', 5, 'MenuPpal', 5, <function pull at 0x0000020F388CA480>), ('MenuPpal', 'MISCELANEA', 0, '0.', 6, '-', '-', None), ('SUB_MISC', '\x1b[33mPUSH \x1b[31mMASIVO', 1, '0.1.', 0, 'MenuPpal', 6, <function push_masivo at 0x0000020F388CA980>), ('SUB_MISC', 'Prueba \x1b[35mIMPRESION MASIVA', 1, '0.1.', 1, 'MenuPpal', 6, <function impresion_masiva at 0x0000020F388CAAC0>), ('SUB_MISC', 'Get \x1b[32m General Data \x1b[0m', 1, '0.1.', 2, 'MenuPpal', 6, <function get_datos_generales at 0x0000020F388CAA20>), ('SUB_MISC', 'Cambia \x1b[35mHEAD', 1, '0.1.', 3, 'MenuPpal', 6, <function cambia_cabecera at 0x0000020F388CAB60>), ('SUB_MISC', 'Cambia \x1b[35mPIE', 1, '0.1.', 4, 'MenuPpal', 6, <function cambia_pie at 0x0000020F388CAC00>), ('SUB_MISC', '\x1b[33mSet \x1b[35mColor\x1b[0m Marco', 1, '0.1.', 5, 'MenuPpal', 6, <function set_color_marco at 0x0000020F388CAD40>), ('SUB_MISC', 'Set  \x1b[35mTipo de Marco', 1, '0.1.', 6, 'MenuPpal', 6, <function set_estilo_marco at 0x0000020F388CACA0>), ('SUB_MISC', '\x1b[33mCambia \x1b[35mColor\x1b[0m MODE EXCEL', 1, '0.1.', 7, 'MenuPpal', 6, <function set_color_excel at 0x0000020F388CADE0>)]
        
        ► CALLED: ►self.mystyca()
        ■ EJEMPLO: 
            dicc_xavier = self.xavier_get_dicc__respuesta( menu_dvd = menu_dvd , lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f)
        ■ SALIDA:   1• {'pre': None, 'respuesta': 'a1', 'pos': None, 'xindex': 1} 
                    2• {'pre': '=>', 'respuesta': 'a1', 'pos': None, 'xindex': 1}
                    3• {'pre': '[', 'respuesta': 'a1', 'pos': ']', 'xindex': 1}
                    4• {'pre': None, 'respuesta': '?', 'pos': None, 'xindex': None}
                    5• {'pre': None, 'respuesta': '<', 'pos': None, 'xindex': None}
                    6• None, <<< salir
        """
        MONO_FROM   = 0
        MONO_TO     = 1
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # BUCLE HASTA OPCION VALIDA or SALIR +  DESEMPAQUETA LAS  RESUPUESTAS
        respuesta_user=None
        dicc_xavier = {}

        while(True):
            dicc_xavier['pre'] = None
            dicc_xavier['respuesta'] = None
            dicc_xavier['pos'] = None
            dicc_xavier['xindex'] = None
            
            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            # ██ PIDE RESPUESTA AL USER ██
            # respuesta_user = input(f"\n• ({menu_dvd.titulo}) {menu_dvd.entradilla_data_user}.... ").strip()
            respuesta_user = input(f"■ ({menu_dvd.titulo}) INTRO___ ").strip()

            # ██ ACCION VACIO
            if respuesta_user == '':
                continue

            # ██ SI HAY ALGUNA RESPUESTA DE ACCION DIRECTA NO HAY XINDEX, SOLO RESPUESTA.... para terminator_executor_
            elif respuesta_user in self.RESP_ACCION_DIRECTA:
                if respuesta_user == SALIR:
                    return None
                else:
                    dicc_xavier['pre'] = None
                    dicc_xavier['respuesta'] = respuesta_user
                    dicc_xavier['pos'] = None
                    dicc_xavier['xindex'] = None
                    
                    return dicc_xavier      # RETORNO LA ACCION ? , < , <<< PARA QUE LA EVALUE TERMINATOR.      

            # ██ BUSCA SI HAY ALGUNA RESPUESTA DEL USUARIO QUE EMPIECE POR UN BEGINER 
            elif any(respuesta_user.startswith(monomio) for monomio in self.RESP_BEGINNERS):
                
                # ENCUENTA EL INDICE QUE CUMPLE LA CONDICION EN EL ITERADOR self.RESP_BEGINNERS('**', '=>')
                indice = next((i for i, monomio in enumerate(self.RESP_BEGINNERS) if respuesta_user.startswith(monomio)), None)
                if indice is None: 
                    continue
                
                # CACHA EL MONOMIO 
                monomio = self.RESP_BEGINNERS[indice]                                
                dicc_xavier['pre']       = monomio
                
                # A PARTIR DEL MONOMIO PUEDO CACHAR LA RESPUESTA. 
                dicc_xavier['respuesta'] = respuesta_user[len(monomio):]
                dicc_xavier['pos']       = None

                # ■ OBTIENE EL INDICE EN self.lst__men_itm_lev_ape_name_padr_ipadr_func
                xindex = self.get_xindex(menu_dvd = menu_dvd , dicc_respuesta = dicc_xavier , lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f)
                if  xindex is not None:
                    dicc_xavier['xindex'] = xindex
                    return dicc_xavier

                continue    # ■ SI NO ENCUENTRA UN INDICE VALIDO VUELVO A PREGUNTAR... USUARIO CONFUSO ;)
            
            elif any(respuesta_user.startswith(monomio) for monomio in self.RESP_PROCESOS):
                # ENCUENTA EL INDICE QUE CUMPLE LA CONDICION EN EL ITERADOR self.RESP_PROCESOS('P>>', 'P>', 'p>')
                indice = next((i for i, monomio in enumerate(self.RESP_PROCESOS) if respuesta_user.startswith(monomio)), None)
                if indice is None: 
                    continue
                
                # CACHA EL MONOMIO 
                monomio = self.RESP_PROCESOS[indice]                                
                dicc_xavier['pre'] = monomio                
                # A PARTIR DEL MONOMIO PUEDO CACHAR LA RESPUESTA. 
                dicc_xavier['respuesta'] = respuesta_user[len(monomio):]
                dicc_xavier['pos']    = None
                dicc_xavier['xindex'] = None
                
                # RETORNO LA RESPUESTA SIN HACER NADA MAS
                return dicc_xavier

            # ██ LOS PACKS HAY QUE TRATARLOS INDIVIDUALMENTE, PERO CON ESTE PATRON SE PUEDE HACER COPY-PASTE
            elif respuesta_user.startswith(self.RESP_BACKGROUND[MONO_FROM]) and respuesta_user.endswith(self.RESP_BACKGROUND[MONO_TO]):       
                dicc_xavier['pre']       = respuesta_user[ :len(self.RESP_BACKGROUND[MONO_FROM]) ]                                    # Desde el inicio(0) hasta 1(2-1) <<
                dicc_xavier['respuesta'] = respuesta_user[ len(dicc_xavier['pre']) : -len(self.RESP_BACKGROUND[MONO_TO]) ]
                dicc_xavier['pos']       = respuesta_user[ len(dicc_xavier['pre'])+len(dicc_xavier['respuesta']): ]      # Desde 2 hasta final >>
                
                # ■ OBTIENE EL INDICE EN self.lst__men_itm_lev_ape_name_padr_ipadr_func
                # ■ SI NO ENCUENTRA EL INDICE VUELVE A PREGUNTAR
                xindex = self.get_xindex(menu_dvd = menu_dvd , dicc_respuesta = dicc_xavier, lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f)
                if  xindex is not None:
                    dicc_xavier['xindex'] = xindex
                    return dicc_xavier
                
                continue
            
            elif respuesta_user.startswith(self.RESP_LIKE_STR[MONO_FROM]) and respuesta_user.endswith(self.RESP_LIKE_STR[MONO_TO]):       
                dicc_xavier['pre']       = respuesta_user[ :len(self.RESP_LIKE_STR[MONO_FROM]) ]                                    # Desde el inicio(0) hasta 1(2-1) <<
                dicc_xavier['respuesta'] = respuesta_user[ len(dicc_xavier['pre']) : -len(self.RESP_LIKE_STR[MONO_TO]) ]
                dicc_xavier['pos']       = respuesta_user[ len(dicc_xavier['pre'])+len(dicc_xavier['respuesta']): ]      # Desde 2 hasta final >>
                
                # ■ En esta accion(buscar entre-comillas) No hay que buscar indices para ejecutar.
                # xindex = self.get_xindex(menu_dvd = menu_dvd , dicc_respuesta = dicc_xavier, lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f)
                # dicc_xavier['xindex'] = xindex
                return dicc_xavier
                continue
            
            # ██ FROM-TO : '1-5' pejem.
            elif self.descomponer_cadena_guion(cadena=respuesta_user ) is not None:
                NUMERO_FROM = 0
                POSICION_GUION = 1
                NUMERO_TO = 2
                # ■■ DESCOMPONE LA CADENA CON EL PATRON DE GUION '-' Y DEVUELVE UNA TUPLA CON LOS VALORES CONVERTIDOS A INT
                #       ■■ '1-5' => (1, '-', 5)
                tupla = self.descomponer_cadena_guion(cadena=respuesta_user)
                if tupla is not None:
                    dicc_xavier['pre']       = tupla[0]     # YA VIENE COMO INT
                    dicc_xavier['respuesta'] = Over_Main.FROM_TO
                    dicc_xavier['pos']       = tupla[1]     # YA VIENE COMO INT
                    dicc_xavier['xindex'] = None            # NO TIENE XINDEX, SOLO RESPUESTA   
                    return dicc_xavier

            # ██ XINDEX: OPCION NATURAL
            else:
                dicc_xavier['pre']       = None
                dicc_xavier['respuesta'] = respuesta_user
                dicc_xavier['pos']       = None
                xindex = self.get_xindex(menu_dvd = menu_dvd , dicc_respuesta = dicc_xavier, lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f)
                if  xindex is None:
                    print(f'{dicc_xavier['respuesta']} NOT FOUND ❌') if dicc_xavier['respuesta'] != '' else None
                    continue
                else:
                    dicc_xavier['xindex'] = xindex
                    return dicc_xavier

        # RETORNO ██████ evaluo si hay una respuesta o varias y las devuelvo.
        return dicc_xavier if dicc_xavier else None

    def descomponer_cadena_guion(self, cadena):
        """  Separa una cadena por un guion('-'). No permite tener mas de un guión. con lo cual se optienen 3 partes:   a - b
        Lo que devuelve esta funcion es una tupla (a, b)
        ► CALLED: xavier_get_dicc__respuesta() de la Clase Over-Main
        ■ EJEMPLO: 
            tupla = self.descomponer_cadena_guion(cadena='5-8')
        ■ SALIDA: 
            tupla = (5,8)
        """
        # patron = re.compile(r'(\d+)(Over_Main.FROM_TO)(\d+)')
        patron = re.compile(r'(\d+)(-)(\d+)')
        resultado = patron.findall(cadena)
        if not resultado: 
            return None
        if len(resultado[0]) != 3: 
            return None
        try:
            lista = list(resultado[0])
            lista = [int(elemento)  for elemento in lista if elemento != Over_Main.FROM_TO] 
            return tuple(lista)
        except Exception as e:
            print(f'Error: {e}')
            return None

    # ████████████ SOBRE-ESCRIBE  TERMINATOR - (EJECUTADOR) 
    def terminator_executor(self, dicc_respuesta:dict, titulo_menu:str):
        """ 
        ■ EJECUTA LA FUNCION ASOCIADA AL XINDEX DEL ITEM RESPUESTA 
        ■ ■ SOBRE-ESCRIBE terminator_executor_ DE XindeX para ampliar las opciones de ejecutar demonio, background, modo like, modo sub-menú, modo from-to, lista de procesos y matar proceso.
        
        [dicc_respuesta]:(dict): diccionario respuesta que se evalua en self.xavier_get_dicc__respuesta()
            Intro Opt (XindeX)..... a1                          ► {'pre': None, 'respuesta': 'a1', 'pos': None, 'xindex': None}
        [titulo_menu]:(str) : El titulo del menu. (obligatorio) ► 'MenuPpal' 
            
        ► CALLED: ►self.mystyca()
        ■ EJEMPLO: 
            self.terminator__executor(dicc_respuesta = dicc_xavier, titulo_menu = self.menu_dvd.titulo)
        ■ SALIDA: 
            None, Ejecuta la Función y vuelve a preguntar hasta salir por '<<<'
        """        

        COLUMNA_MENU = 0       
        COLUMNA_ITEM = 1       
        COLUMNA_FUNCION = 7    

        MONO_FROM   = 0
        MONO_TO     = 1   
        
        # VALIDACION
        if not isinstance(dicc_respuesta, dict): return None
        _iniciador = dicc_respuesta.get('pre', None)
        respuesta = dicc_respuesta.get('respuesta', None)
        _terminador = dicc_respuesta.get('pos', None)
        xindex = dicc_respuesta.get('xindex', None)

        lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func

        # ■■■■ MENU DEL TITULO
        menu_dvd = self.get_menudvd(titulo=titulo_menu)
        
        # ■■■■ LISTA DE LOS   P A D R E S   DEL MENU (RCRSV) ■■■■■■■ ....Usado para saber si es un menu de directorio o no.
        lst_padres  = self.get_list_padres_mystyca(menu_dvd = menu_dvd)        
        lst_hijos   = [ hijo for hijo in self.lst_keys if hijo not in lst_padres] 
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■■■ EMPIEZA LA EVALUACION DE LA RESPUESTA ■■■■
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

        # █ █ █ █ █ █ ACCION DIRECCTA ? , < , <<< 
        if (_iniciador   is None     and  
            _terminador  is None     and                  
            respuesta   is not None and 
            respuesta   in self.RESP_ACCION_DIRECTA):      

            if respuesta == '?':                                            # ■ Muestra el menu de funciones y definiciones.
                os.system('cls')              
                self.imprimir_mystyca_definiciones(menu_dvd=self.menu_dvd, lista_m_i_l_a_n_p_i_f=self.lst__men_itm_lev_ape_name_padr_ipadr_func)            
            
            elif respuesta == '??':                                          # ■ Ayuda del XindeX
                os.system('cls')              
                Over_Main.ayuda_xindex()
            
            elif respuesta == 'help':                                       # ■ ayuda sobre la clase.
                os.system('cls')              
                Over_Main.ayuda_funciones()
            
            elif respuesta == '<':                                          # ■ REPETIR MENU
                os.system('cls')              
                self.F_RANK_Y.imprimir(sp_between = 2, ancho_columna = None )

            elif respuesta == '#':
                # os.system('cls')              
                self.set_style(b_mode_all = not self.b_mode_all)
            
            elif respuesta == '@':
                sdata = Sdata.get_data(key_dict='S', tipo=str, msg_entrada='Nombre Estilo(franky/default/unicode/doble/vacio/moderno/elegante)', permite_nulo=False)
                self.F_RANK_Y.style(estilo=sdata['S'])
                self.F_RANK_Y_DEF.style(estilo=sdata['S'])
                print(f'::: Estilo Marco cambiado a {sdata["S"]} ::: ')

            elif respuesta == '$':
                sdata = Sdata.get_data( key_dict='S', tipo=str, msg_entrada='Introduce color(■black ■red ■green ■yellow ■blue ■magenta ■cyan ■white ■lblack ■lred ■lgreen ■lyellow ■lblue ■lmagenta ■lcyan ■lwhite ■grey ■gray ■lgrey ■dgrey ■orange ■purple ■default ■reset ■none ■pink ■lime ■aqua)', permite_nulo=False)
                # self.F_RANK_Y.style(color=sdata['S'])
                # self.F_RANK_Y_DEF.style(color=sdata['S'])

                self.F_RANK_Y.color_marco(color=sdata['S'])    
                self.F_RANK_Y_DEF.color_marco(color=sdata['S'])    
                self.F_RANK_Y.imprimir()
                print(f'::: Color Marco cambiado a {sdata["S"]} ::: ')
            else:                                                           
                return False

        # █ █ █ █ █ █ RESPUESTA Directa 
        elif (_iniciador   is None     and 
              _terminador  is None     and               
              respuesta   is not None and   
              xindex      is not None):        
            
            # MODO DIRECTORIO?
            if self.b_mode_all == False and lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_ITEM] in lst_padres:
                print(f'b_mode_all == {self.b_mode_all} => (DIRECTORY)')
                return      # ■ MODO DIRECTORIO Y ESTÁ ENTRE LOS PADRES EN UNA RESPUESTA DE XINDEX

            # ██ EJECUTA LA FUNCIONN ██
            lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_FUNCION]() if lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_FUNCION] else None
        
        # █ █ █ █ █ █ BEGINNER'S 
        elif (_iniciador   is not None and 
              _terminador     is None     and               
              xindex      is not None and 
              _iniciador in self.RESP_BEGINNERS):         
            
            # ■ ■ ■ ■ ■ ■ ■  SUB-MENU INTERNO RECURSIVO
            if _iniciador == '**':                          
                # ■ SOLO PARA PADRES  
                if self.b_mode_all == False and lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_ITEM] in lst_hijos:
                    return

                # ■ xindex de la respuesta marca la fila de lista_m_i_l_a_n_p_i_f
                titulo_select = lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_MENU]
                item_select   = lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_ITEM]                
                
                # ■ SI EL ITEM NO ES UN PADRE DEL MENU RETORNA, ... ESTO NO ES PARA HIJOS
                if item_select not in lst_padres: 
                    return
                
                # DEVUELVE EL TITULO DEL MENU DESDE EL ITEM SELECCIONADO
                titulo_menu = self.get_menudvd_from_item(item = item_select, menu = titulo_select , xindicex = xindex, lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f)

                # ■ LLAMO A LA FUNCION RECURSIVA begin_asterisco CON EL MENU_DVD SELECCIONADO EN LA RESUPUESTA.
                self.begin_asterisco(titulo_menu = titulo_menu)
            
            # ■ ■ ■ ■ ■ ■ ■ INDEPENDIENTE - LANZA UN PROCESO INDEPENDIENTE (TKINTER pejem.) ■■■
            elif _iniciador == '=>':                         
                # ■■■■ SOLO PARA HIJOS ■■■■
                if self.b_mode_all == False and lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_ITEM] in lst_padres:
                    return

                funcion = lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_FUNCION]
                if funcion is None: return
                self.lanzar_proceso(proceso = funcion,  demonio=False)
                # os.system('cls')
            # ■ ■ ■ ■ ■ ■  LIKE =a1 
            elif _iniciador == '=':  

                if not self.matriz_impresion_xindex: return None      
                # ■■ LISTA DE STRING PARA IMPRIMIR 
                lst_mystyca_impresion = [''.join(mystyca_fila) for mystyca_fila in self.matriz_impresion_xindex]
                lst_mystyca_impresion = [linea.strip() for linea in lst_mystyca_impresion]
                lst_numero_fila = []
                for i, str_fila in enumerate(lst_mystyca_impresion):
                    if str_fila.startswith(respuesta):
                        lst_numero_fila.append(i)
                        # print(fila)
                if not lst_numero_fila: return None
                desde = min(lst_numero_fila)
                hasta = max(lst_numero_fila)
                pass
                self.F_RANK_Y_DEF.imprimir(sp_between = 2, ancho_columna = None , fila_from=desde, fila_to=hasta)                       
            
            # ■ ■ ■ ■ ■ ■ ESTYLE @moderno
            elif _iniciador == '@':  
                pass

            # ■■■ NOT FOUND ■■■ 
            else:                                        
                print(f'{_iniciador} - NOT FOUND ❌')                     

        # █ █ █ █ █ █ FROM - TO 
        elif (  _iniciador   is not None and
                _terminador     is not None and               
                respuesta   == Over_Main.FROM_TO and 
                xindex      is None):
            try:
                _iniciador = abs(int(_iniciador))
                _terminador = abs(int(_terminador))
                if _iniciador > _terminador:
                    _iniciador, _terminador = _terminador, _iniciador

                self.F_RANK_Y_DEF.imprimir(sp_between = 2, ancho_columna = None , fila_from=int(_iniciador), fila_to=_terminador) 
            except Exception as e:
                print(f'❌ ERR: {e}') 
                return None
        
        # █ █ █ █ █ █ PACK's TIPO [a1] 
        elif  ( _iniciador   is not None and 
                _terminador     is not None and             
                xindex      is not None and 
                respuesta   is not None):             
            
            # ■■■ DEPENDIENTE - PACK 1 - LANZA OVER-MAIN ■■■ SERVIDOR pjem.
            if _iniciador == '[' and _terminador == ']':       
                
                # SOLO PARA HIJOS: MODO DIRECTORIO y PADRE
                if self.b_mode_all == False and lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_ITEM] in lst_padres:
                    return

                funcion = lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_FUNCION]
                if funcion is None: return
                print('EXEC DEMONIO - DEPENDIENTE')                
                self.lanzar_proceso( proceso = funcion,  demonio=True)
                # os.system('cls')
            else:                                           # PACK NOT FOUND
                print('■ PACK NOT FOUND ❌')                

        # █ █ █ █ █ █ PACK's TIPO "pimienta"  # ■■■ LIKE STRING
        elif  ( _iniciador   is not None and 
                _terminador     is not None and             
                xindex      is None and 
                respuesta   is not None):                         
            
            if _iniciador == '"' and _terminador == '"':       
                self.api_buscar( respuesta )
        
        # █ █ █ █ █ █ PROCESO'S 
        elif (_iniciador   is not None and 
              _terminador     is None     and               
              xindex      is None     and 
              respuesta   is not None and
              _iniciador in self.RESP_PROCESOS):         
            
            # ■■■ SUB-MENU RECURSIVO ■■■
            if str(_iniciador).upper() == '►' or str(_iniciador).lower() == 'list':
                self.listar_procesos()
                
            elif (  str(_iniciador).upper() == '■' or 
                    str(_iniciador).lower() == 'kill' or 
                    str(_iniciador).lower() == 'stop'
                 ):
                print(f'... Intentando Parar el Proceso {respuesta}')                
                self.detener_proceso(proceso = str(respuesta).strip())

        else:                                               
            print('■ NOT FOUND ❌')
            return False

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ PROCESOS ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    def lanzar_proceso(self, proceso, demonio:bool=False, terminal=False, *args, **kwargs):
        """ ■ INICIA UN PROCESO Y LO ALMACENNA EN EL DICCIONARIO
        [proceso](callable), el objeto callable(funcion) que se ejecuta
        [demonio](bool), si se ejecuta como un demonio(dependiente)(para cuando se acaba esta ejecucion.) o como un background(independiente)(aunque muera el ppal el independiente sigue.)
        [args](dict),   los argumentos que se le pasan al objeto callable. Son necesareos para llamar a multiprocessing.Process(target=proceso, daemon=demonio, args=args, kwargs=kwargs)
        [kwargs],       los argumentos que se le pasan al objeto callable. Son necesareos para llamar a multiprocessing.Process(target=proceso, daemon=demonio, args=args, kwargs=kwargs)
        
        ► CALLED: ► terminator_executor_() de la clase Over_Main
        ■ EJEMPLO: 
            self.lanzar_proceso( proceso = funcion,  demonio = False)   ► Lanza un proceso en BackGround. Independiente del proceso que lo lanza.
            self.lanzar_proceso( proceso = funcion,  demonio = True)    ► Lanza un proceso dependiente del proceso que lo lanza.
        ■ SALIDA: 
            print(f"\nProceso '{nombre_funcion}' iniciado con PID... {8860}")
        """

        args = args or ()
        kwargs = kwargs or {}
        nombre_proceso = proceso.__name__
        try:
            if nombre_proceso in self.dicc_procesos and self.dicc_procesos[nombre_proceso].is_alive():
                print(f"El proceso '{nombre_proceso}' ya está en ejecución.")
                return
                
            p = multiprocessing.Process(target=proceso, daemon=demonio, args=args, kwargs=kwargs)
            p.start()
            self.dicc_procesos[nombre_proceso] = p
            print(f"\n✅ Proceso '{nombre_proceso}' iniciado con PID... {p.pid}.")
        except Exception as e:
            print(e)
            return None

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    def listar_procesos(self):
        """ MUESTRA LOS PROCESOS QUE ESTAN EN EJECUCION LANZADOS CON:  =>a1  ó  [a1]
        ► CALLED: self.terminator__executor()
        ■ EJEMPLO: 
            print(self.listar_procesos())
        ■ SALIDA: 
            None. Muestra por pantalla la lista de procesos lanzados.
        """
        # return {nombre: p.is_alive() for nombre, p in self.dicc_procesos.items()}
        # aux = input(f'\nPulsa Cualquier tecla para continuar.... ')
        print(f"\n{Fore.CYAN}■■■■■■{Fore.RESET} Listado de procesos {Fore.CYAN}■■■■■■■{Fore.RESET}")
        for nombre_proceso, p in self.dicc_procesos.items():
            estado = "🟢 Vivo" if p.is_alive() else "🔴 Terminado"
            print(f"• Nombre Proceso = {Fore.CYAN}{nombre_proceso}{Fore.RESET}: PID = {Fore.CYAN}{p.pid}{Fore.RESET} - Demonio = {f'{Fore.GREEN}Si{Fore.RESET}' if p.daemon else F'{Fore.RED}No{Fore.RESET}'} ESTADO = {estado}")
        print()
    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    def detener_proceso(self, proceso:str):
        """ DETIENE UN PROCESO Y LO ELIMINA DEL DICCIONARIO
        [proceso](str)(int), el nombre o el pid del proceso que se quiere detener.
        ► CALLED: self.terminator__executor()
        ■ EJEMPLO: 
            self.detener_proceso(proceso = 8860)
        ■ SALIDA: 
            print de confirmación de la acción.
        """
        # EN CASO DE QUE EL NOMBRE SEA UN PID, LO BUSCA EN EL DICCIONARIO 
        if str(proceso).isdigit():
            if any(int(proceso) == p.pid for p in self.dicc_procesos.values()):
                proceso = next(name for name, p in self.dicc_procesos.items() if p.pid == int(proceso))
            else:
                print(f"PID {proceso} NOT FOUND en la Lista de Procesos Lanzados.")
                return
        elif proceso == '':
            self.detener_all_procesos()
            return

        if proceso in self.dicc_procesos and self.dicc_procesos[proceso].is_alive():
            self.dicc_procesos[proceso].terminate()         # TERMINA EL PROCESO.
            self.dicc_procesos[proceso].join()              # Espera que termine la Terminación OK del proceso
            print(f"• Proceso {Fore.CYAN}{proceso}{Fore.RESET} ► PID {Fore.CYAN}{self.dicc_procesos[proceso].pid}{Fore.RESET} 🔴 Detenido.")
        else:
            if not proceso in self.dicc_procesos:
                print(f"• No se encontró el proceso {Fore.RED}{proceso}")
            elif not self.dicc_procesos[proceso].is_alive():
                print(f"• El Proceso '{proceso}' ya estaba {Fore.RED}Detenido.")

    def detener_all_procesos(self):
        """  
        ► CALLED: self.detener_proceso()
        ■ EJEMPLO: 
            self.detener_all_procesos()
        ■ SALIDA: 
        """
        respuesta = Sdata.get_data(key_dict='S', tipo=str, msg_entrada='¿Estás seguro de que quieres detener todos los procesos? (s/n)', permite_nulo=False)
        if respuesta['S'].lower() != 's':
            print("Operación cancelada. No se detendrán los procesos.")
            return

        print("\n🛑 Terminando todos los procesos...")
        for nombre_proceso, proceso in list(self.dicc_procesos.items()):
            self.detener_proceso(proceso = proceso.pid)
            # print(f"Proceso  {Fore.BLUE}{nombre_proceso}{Fore.RESET} - {Fore.CYAN}{proceso.pid}{Fore.RESET} 🔴 Detenido.")

    # ███████████████████████ SUB-MENUS - BEGINNERS 
    def begin_asterisco(self, titulo_menu:str):
        """ 
        ■ FUNCION QUE SE EJECUTA CUANDO SE HACE '**b' . 
            ■ ■ Crea un SUB-MENU del directorio.
            ■ ■ Se sale de este sub-Menu con <<< y vuelves al principal.
        
        [titulo_menu](str): titulo del menu Sobre el que se va a establecer el nuevo menu genetico.
        ► CALLED: self.terminator__executor() de Over_Main
        ■ EJEMPLO: 
            self.begin_asterisco(titulo_menu = titulo_menu)
        ■ SALIDA: 
            Crea un nuevo menu llamando a mystyca y cuando sale, sale hacia atrás en la pila y recompone los valores iniciales.
        """
        
        if not self.menu_dvd: return None   # Valida.
        
        # ■■■■■■■■ ME GUARDO EL MENU PPAL
        menu_dvd_aux = self.menu_dvd
        head_datapush_aux = self.head_datapush 
        color_marco_aux = self.color_marco
        
        # 
        # ■■■■■■■■ LLAMO A LA GENERACION DEL NUEVO MENU ■ ES RECURSIVA.
        self.mystyca(titulo=titulo_menu, head_datapush=self.set_color(texto=titulo_menu, color=Fore.RED), pad_x=self.pad_x)
        
        # ■ HA SALIDO POR <<< Y DEJO LAS COSAS COMO ESTABAN ANTES DEL **
        self.menu_dvd = menu_dvd_aux
        
        # CARGA GENETICA
        self.load_modulo_gentico_x(titulo = self.menu_dvd.titulo)
        if not self.lst__men_itm_lev_ape_name_padr_ipadr_func or not self.lst_keys or not self.lst_opts_ok: 
            return None
        
        # IMPRIME GENETICA
        self.head_datapush = head_datapush_aux
        self.load_modulo_impresion_x(menu_dvd = self.menu_dvd , 
                                    lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func , 
                                    lst_keys = self.lst_keys ,
                                    lst_opts_ok = self.lst_opts_ok)
        
        # self.F_RANK_Y.color_marco(color=Fore.CYAN)
        # self.F_RANK_Y_DEF.color_marco(color=Fore.CYAN)
        # NOTA: NO CARGO EL MODULO RESPUESTAA PQ CUANDO SALGA DE ESTA FUNCION TERMINATOR ME ENVIARÁ AL MODULO RESPUESTA.
        pass

    # ███████████████████████ 
    def api_buscar(self, str_like: str):
        """
        Busca una frase en las keys y values del índice y muestra las líneas
        en una lista plana en forma de columna (usando Franky) sin niveles de tabulación.
        Finalmente solicita la opción usando el prompt dinámico con el nombre del menú.
        """
        # 1. Limpiamos comillas y pasamos a minúsculas para una búsqueda tolerante
        busqueda = str_like.strip().strip('"').strip("'").lower()
        resultados = []
        
        if not self.matriz_impresion_xindex: 
            print(f"❌.....No hay menú cargado para buscar.")
            return None      
        # ■■ LISTA DE STRING PARA IMPRIMIR 
        lst_mystyca_impresion = [''.join(mystyca_fila) for mystyca_fila in self.matriz_impresion_xindex]
        lst_mystyca_impresion = [linea.strip() for linea in lst_mystyca_impresion]
        
        resultados = []
        for i, str_fila in enumerate(lst_mystyca_impresion):
            if busqueda in str_fila.lower():
                resultados.append(str_fila.strip())
        pass        
        # self.F_RANK_Y_DEF.imprimir(sp_between = 2, ancho_columna = None , fila_from=desde, fila_to=hasta)
        
        # 3. Dibujamos los resultados encapsulados en el marco Franky
        franky_busqueda = F_r_a_n_k_y(dimension = f'{len(resultados)}X{3}', 
                                    head_datapush = f"Resultados de Búsqueda: '{busqueda}'",  
                                    pie_datapush=self.pie_datapush , 
                                    pad_x = self.pad_x )
        # franky_busqueda.head.push(f"Resultados de Búsqueda para: '{busqueda}'")
        
        if resultados:
            franky_busqueda.push(resultados, eje='Y')
        else:
            franky_busqueda.push([f"No se encontraron coincidencias para '{str_like}'"], eje='Y')
            
        franky_busqueda.imprimir(sp_between=1)
        print(f"\n🔍 Búsqueda completada. {len(resultados)} resultado(s) encontrado(s).")

        
        

    # ██████████████████████████████████████████████████████████████████████
    # ██████████████████████████████ COLOR █████████████████████████████████ 
    # ██████████████████████████████████████████████████████████████████████

    def set_color(self, texto, color=None):
        """  Pone un color a un texto.
        ■ EJEMPLO: 
            self.mystyca(titulo=titulo_menu, head_datapush=self.set_color(texto=titulo_menu, color=Fore.RED), pad_x=self.pad_x)
        ■ SALIDA: el texto con el color asignado.
        """
        if color is None:
            # Devuelve el texto coloreado en azul.
            return f"{Fore.LIGHTCYAN_EX}{texto}{Style.RESET_ALL}"
        else:
            return f"{color}{texto}{Style.RESET_ALL}"

    # ██████████████████████████████████████████████████████████████████████
    # ██████████████████████████████ AYUDA █████████████████████████████████ 
    # ██████████████████████████████████████████████████████████████████████
    
    @staticmethod
    def ayuda_xindex():
        xindex = ['<<<', '<' , '?', '??', 'help']
        overmain = ['**P', '<< index >>' , '=>' , '=' , '2-5']
        """  
        ■ SALIDA: 
        """
        d = {
            '<<<' : f'{Fore.GREEN}<<<{Fore.RESET}',
            '?' : f'{Fore.GREEN}?{Fore.RESET}',
            '??' : f'{Fore.GREEN}??{Fore.RESET}',
            'help' : f'{Fore.GREEN}help{Fore.RESET}',
            '<' : f'{Fore.GREEN}<{Fore.RESET}', 
            '@' : f'{Fore.GREEN}@{Fore.RESET}',
            '$' : f'{Fore.GREEN}${Fore.RESET}',
            '=' : f'{Fore.GREEN}={Fore.RESET}',
            '#' : f'{Fore.GREEN}#{Fore.RESET}',
            '**' : f'{Fore.GREEN}**{Fore.RESET}',
            'GUION' : f'5{Fore.GREEN}-{Fore.RESET}12',
            '=>' : f'{Fore.GREEN}=>{Fore.RESET}',
            '[c12]' : f'{Fore.GREEN}[c12]{Fore.RESET}',
            '[a]' : f'{Fore.GREEN}[{Fore.RESET}a{Fore.GREEN}]{Fore.RESET}',
            'list' : f'{Fore.GREEN}list{Fore.RESET}',
            'listar' : f'{Fore.GREEN}listar{Fore.RESET}',
            'kill' : f'{Fore.GREEN}kill{Fore.RESET}',
            'stop' : f'{Fore.GREEN}stop{Fore.RESET}',
            'ERR' : f'{Fore.RED}ERROR :::: {Fore.RESET}',
        }
        print(Sdata.big_text(texto=f'Ayuda   X i n d e X', color=Fore.CYAN))
        ENE = '\n'
        txt = ''
        txt += f'■ ■ ■ ■ ■ ■ ■ ■ Clase XindeX'
        txt += ENE + f'{d['<<<']}\t SALIR'
        txt += ENE + f'{d['?']}\t Muestra el MENU de DEFINICION(la Funcion que se Ejecuta en cada Item) '
        txt += ENE + f'\t También muestra el modo de ejecución (En el Head):'
        txt += ENE + f'\t{' '*3}• Todos se ejecutan  (Exec All)'
        txt += ENE + f'\t{' '*3}• Solo se ejecutan los hijos (Mode Directory)'
        txt += ENE + f'{d['<']}\t Limpia la terminal e imprime el Indice'
        txt += ENE + f'{d['??']}\t Muestra la ayuda de las Acciones sobre el Indice(éste menu)'
        txt += ENE + f'{d['help']}\t Muestra la ayuda sobre los parámetros para la clase XindeX / Over_Main.'
        txt += ENE + f'\t la clase XindeX/Over_Main.'  
        txt += ENE + f'{d['#']}\t Switch al modo de ejecución(padres + hijos ó sólo hijos)'  
        txt += ENE + f'{d['@']}\t Cambia el estilo del Menu(default/franky/moderno/vacio/...)'  
        txt += ENE + f'{d['$']}\t Cambia el Color del Marco(red/lred/gray/cyan/yellow/...)'  
        txt += ENE + f'\n■ ■ ■ ■ ■ ■ ■ ■ Clase Over-Main'
        txt += ENE + f'{d['=']}a1\t Modo LIKE , Muestra todo lo que empieza por a.1 !!'  
        txt += ENE + f'\t ATENCION: Muestra el menu filtrado pero admite cualquier entrada al menu. '  
        txt += ENE + f'{d['=']}a.1\t {d['ERR']}NO muestra nada  pq hay que Ponerlo SIN PUNTO (a1)'  
        txt += ENE + f'\n{d['GUION']}\t Muestra el Menu desde la fila 1 hasta la fila 5 (ambas incluidas)'  
        txt += ENE + f'\n{d['**']}b\t Modo Sub-Menu . MUESTRA EL MENU SI b ES PADRE (DIRECTORY)'  
        txt += ENE + f'\t ATENCION: Genera otro nuevo menu y re-ordena los indices. Se sale con {d['<<<']} '
        txt += ENE + f'{d['**']}a1\t {d['ERR']}No está permitido SI  a.1 es HIJO. '  
        txt += ENE + f'\n{d['=>']}b11\t LANZA Un PROCESO En Modo INDEPENDIENTE del Proceso PPAL. Si el P'  
        txt += ENE + f'{d['=>']}a\t {d['ERR']}No Se ejecuta pq [a] es PADRE (DIRECTORY) si b_mode_all=False'  
        txt += ENE + f'\t Sin Sin embargo si b_mode_all=True, y tiene asignada una funcion, se ejecuta como Background.'  
        txt += ENE + f'\n{d['[c12]']}\t LANZA Un PROCESO En {Fore.CYAN}Modo DEPENDIENTE{Fore.RESET} (DEMONIO) DEL PROGRAMA PPAL.'  
        txt += ENE + f'\t Cuando el PPal Acaba, el demonio acaba abruptamente tb.'  
        txt += ENE + f'{d['[a]']}\t {d['ERR']}No Se ejecuta pq [a] es PADRE (DIRECTORY) SI b_mode_all=False. '  
        txt += ENE + f'\t Sin embargo si b_mode_all=True, y tiene asignada una funcion, se ejecuta como {Fore.CYAN}Demonio{Fore.RESET}.'  
        # txt += ENE + f'{Fore.GREEN}►{Fore.RESET}\t (Alt+16) IMPRIME LA {Fore.CYAN}LISTA DE PROCESOS{Fore.RESET} (con PID)'  
        txt += ENE + f'\n{d['list']}\t Imprime la LISTA DE PROCESOS (con PID)'  
        txt += ENE + f'{d['listar']}\t Imprime la LISTA DE PROCESOS (con PID)'  
        # txt += ENE + f'{Fore.GREEN}■ 886{Fore.RESET}\t (Alt+254) {Fore.CYAN}Detiene el Proceso{Fore.RESET} ( ■ 886 ) Si Existe'  
        txt += ENE + f'{d['kill']} 886\tDetiene el Proceso ( ■ 886 ) Si Existe'  
        txt += ENE + f'{d['stop']} 886\tDetiene el Proceso ( ■ 886 ) Si Existe'  

        print(f'{txt}')
    
    # DESCRIPCION DE LOS PARAMETROS
    @staticmethod
    def ayuda_funciones():        

        print(Sdata.big_text(texto=f'Ayuda Funciones XindeX', color=Fore.CYAN))
        ENE = '\n'
        txt = ''
        txt += ENE + f'{Fore.BLUE}■ ■ ■ ■ ■ {Style.RESET_ALL} Imports Usados '  
        txt += ENE + f'from {Fore.YELLOW}classXindeX{Style.RESET_ALL} import {Fore.YELLOW}XindeX{Style.RESET_ALL}'  
        txt += ENE + f'from {Fore.YELLOW}classXindeX{Style.RESET_ALL} import {Fore.YELLOW}Over_Main{Style.RESET_ALL}'  
        txt += ENE + f'from {Fore.YELLOW}Sdata{Style.RESET_ALL} import {Fore.YELLOW}Sdata{Style.RESET_ALL}'
        
        txt += ENE + f'\n{Fore.CYAN}■■■■■■■■■■■■■{Fore.RESET} PARAMETROS Over_Main'  
        txt += ENE + f'The_X_Men = {Fore.YELLOW}Over_Main{Fore.RESET}({Fore.GREEN}tipo_index{Fore.RESET} = a,{Fore.GREEN}b_mode_all{Fore.RESET} = True, {Fore.GREEN}b_loop{Fore.RESET} = True )'  
        txt += ENE
        txt += ENE + f'[{Fore.GREEN}tipo_index{Fore.RESET}] (str) ► Tipo de XindeX a crear, puede ser:'  
        txt += ENE + f'\t • Numerico(byDef): 1'  
        txt += ENE + f'\t • Alfabetico Min: a'  
        txt += ENE + f'\t • Alfabetico May: A'  
        txt += ENE + f'\t • Mixto May: A1, 1A'  
        txt += ENE + f'\t • Mixto Min: a1, 1a'  
        txt += ENE + f'[{Fore.GREEN}b_mode_all{Fore.RESET}] (bool)'  
        txt += ENE + f'\t • True: (byDef) Solo se ejecutan (o solo es opcion valida) los subMenus Finales (no padres). '  
        txt += ENE + f'\t • False: Se ejecuta (solo los que son opcion valida) todo lo que no sea None en func.'  
        txt += ENE + f'[{Fore.GREEN}b_loop{Fore.RESET}] (bool)        '  
        txt += ENE + f'\t • True: (byDef) Ejecuta Items del XindeX y solo sale por {Fore.GREEN}<<<{Fore.RESET}'  
        txt += ENE + f'\t • False: Solo ejecutamos una vez y retorna respuesta'  
        
        txt += ENE + f'\n{Fore.CYAN}■■■■■■■■■■■■■{Fore.RESET} PARAMETROS AddX'  
        txt += ENE + f'The_X_Men.{Fore.YELLOW}addX{Fore.RESET}( {Fore.GREEN}titulo{Fore.RESET} = sub-Xindex, {Fore.GREEN}padre{Fore.RESET} = Menu1, {Fore.GREEN}ipadre{Fore.RESET} = Info XindeX, {Fore.GREEN}lst_items{Fore.RESET} = [ (item_1, func_1), (item_n, func_n) ])'  
        txt += ENE
        txt += ENE + f'{Fore.GREEN}titulo{Fore.RESET}(str)::: Nombre e identificador Principal del menu.'  
        txt += ENE + f'{Fore.GREEN}padre{Fore.RESET}(str)::: Indice en el padre donde se añade el nuevo menu.'  
        txt += ENE + f'\t • Puede ser una posicion (entero) o el nombre del menu(str).'  
        txt += ENE + f'\t • Tb puede ser None en caso de un menu sin padre o Principal.'  
        txt += ENE + f'{Fore.GREEN}lst_items{Fore.RESET}(list[tuple]):::  Par nombre del item - funcion asociada.'  
        
        txt += ENE + f'\n{Fore.CYAN}■■■■■■■■■■■■■{Fore.RESET} PARAMETROS Mystyca'  
        txt += ENE + f'retorno = The_X_Men.{Fore.YELLOW}mystyca{Fore.RESET}( {Fore.GREEN}titulo{Fore.RESET} = Menu1, {Fore.GREEN}head_datapush{Fore.RESET} = XINDEX - OVER-MAIN,{Fore.GREEN}pad_x{Fore.RESET} = 50 )'  
        txt += ENE
        txt += ENE + f'[{Fore.GREEN}titulo{Fore.RESET}](str)'
        txt += ENE + f'\t • nombre / Id del Menu Añadido( con addX ) y Configurado (con padre e ipadre). '
        txt += ENE + f'\t • Tb puede ser None en caso de un menu sin padre o Principal.'        
        txt += ENE + f'[{Fore.GREEN}head_datapush{Fore.RESET}](str)'  
        txt += ENE + f'\t • Texto cabecera del Menu' 
        txt += ENE + f'\t • Si None, no lleva cabecera'
        txt += ENE + f'[{Fore.GREEN}pad_x{Fore.RESET}](int)::: Espacio entre el final del caracter más a la derecha y el marco derecho del XindeX'

        txt += ENE + f"""{Fore.YELLOW}
■ CONSEJO: COPIA , PEGA Y ADAPTA EL CODIGO VERDE A TUS NECESIDADES{Fore.RESET}"""
        
        txt += ENE + f""" {Fore.GREEN}

# 0 ■ ■ ■ ■ CREO UN ARCHIVO over_main.py y escribo en él el bloque de código siguiente 
#           para crear un XindeX básico. 
from XindeX.classXindeX import Over_Main       
from XindeX.Sdata import Sdata  # ■ (OPCIONAL PERO RECOMENDADO) Para pedir datos Seguros al usuario .
    
# 1 ■ ■ ■ ■ CREO LOS MENUS Y SUS FUNCIONES ASOCIADAS 
Menu1 = The_X_Men.addX(titulo='menu_principal', padre=None , ipadre=None, 
                lst_items = [ 
                    ("Tema 1" , func_tema_1) ,
                    ("Tema 2" , func_tema_2) , 
                    ("Tema 3" , None) , 
                    ("Tema 4" , None), 
                    ("Tema 5" , func_tema_5) , 
                ])

# 2 ■ ■ ■ ■ Creo un sub-menu dentro del menu_principal desde 'Tema 2'
The_X_Men.addX( titulo='sub_menu_1', padre='menu_principal' , ipadre='Tema 2' , 
                lst_items = [ 
                ("KNN", func_knn) , 
                ("SVM", func_svm) , 
                ("StandarSacale", None) , 
                ])    

# 3 ■ ■ ■ ■  LLAMO A MYSTYCA PARA VISUALIZAR EL MENU 
retorno = The_X_Men.mystyca( titulo='menu_principal', head_datapush  = " Formularios DVD " , pad_x=5 )
{Fore.RESET}"""
        
        txt += ENE + """ 
# 4 ■■■■■ RETORNO DE MYSTYCA (Opcional)
print(f"::: T H E   E N D  en MAIN() ::: '{'retorno if retorno else 'no retorno'} ")
""" 
        
        txt += ENE + f"""{Fore.LIGHTCYAN_EX}
... y luego tienes que definir las funciones en este mismo archivo o importarlas

• Si quieres usar el indice como motor de ejecución puedes usar un archivo de funciones aparte 
  ( para tener el código más limpio ).
• Si es un indice para realizar pruebas sobre clases puedes escribir las funciones en este mismo archivo 
  ( para mantener el orquestador centralizado en un mismo sitio ).
POR EJEMPLO: Si quiero usar un archivo de funciones aparte:
{Fore.RESET}"""

        txt += ENE + f""" {Fore.GREEN} 
import archivo_funciones as af 
The_X_Men.addX( titulo='fam', padre='menu_principal'   , ipadre='Tema 2' , 
                lst_items = [ 
                ("KNN", af.funcion_knn) , 
                ("SVM", af.funcion_svm) , 
                ("StandarSacale", None) , 
                ])    

{Fore.RESET}"""


        print(txt)

