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
            [fraseHead](str)(list)(matriz)  : titulo del Menu            
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
        
               
        # ■■ LA FRASE QUE SE PONE EN LA IMPRESION DEL MENU(POR DEFECTO, EL TITULO):
        self.fraseHead = fraseHead if fraseHead != '' else self.titulo
        
        # ■■ MENSAJE DE PEDIDA DE DATO AL USUARIO
        self.intradilla_data_user = '\nIntro Opt (XindeX)..... '     
    
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
    def style(self, intradilla_data_user='\nIntro Opt (XindeX)..... '):
        pass
    
    # Retorna 4 espacios
    def get_TAB(self):
        return self.TAB
    
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
    
    NUMERO_COLUMNAS = 9     # NUMERO DE COLUMNAS DE XINDEX. ES CTE. 

    def __init__(self, tipo_index:str='a', b_mode_all:bool=True, b_loop:bool=True ):
        """ ■■ Crea un menu Principal y gestiona una lista de menus secundarios que dependen del principal.
        [b_loop]: True=circular hasta Salida. | False=Sólo una ejecucion FALTA IMPLEMENTAR
        [head_datapush](list, str, matriz) : datos de la cabecera, None si no quieres cabecera.
        [pie_datapush](list, str, matriz): datos de pie, None si no quieres pie.

        ■ [tipo_index]  █  '1' = Numerico(byDef) █  'a' = Alfabetico Min █ 'A' = Alfabetico May  █ 'A1', '1A', a1, 1a =  Mixto
                           o bien: TIPEX.NUMERIC = 0 | TIPEX.ALF_MAX = 10 | TIPEX.ALF_MIN = 20 | TIPEX.MIXTO = 15
        ■ [b_mode_all] (bool)   True  ::: Solo se ejecutan ( o solo es OPCION-VALIDA) los subMenus Finales (no padres) 
                                False ::: Se ejecuta ( o solo es opcion valida) tanto padres como hijos.
        ■ [b_loop] (bool)       True  ::: SALES DEL MENÚ INTRODUCIENDO '<<<' 
                                False ::: SE PRESENTA EL MENU 1 VEZ Y SALE A MAIN.

        ejemplo: xindex = XindeX(head_datapush = ['fila 1 head'] , pie_datapush = [['fila 1 pie'],['fila 2 pie']] , b_loop=True) 

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
        self.matriz_opt_ok=[]   # ■■ Listado de Opciones Validas(a.1, b.2.3...). Se tiene que pasar a ■ get_dicc_xavier_into_user()
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
        # LISTA DE LAS OPCIONES QUE PUEDE INTRODUCIR EL USUARIO
        self.lst_opts_ok = None    
        # CABECERA Y PIE: 
        # self.head_datapush  = head_datapush
        # self.pie_datapush   = pie_datapush
        # self.pie_datapush   = f'(Salir).... <<<  ■  (Help).... ?  ■  (Repeat).... <  ■  (Begin).... *opcion'
        self.pie_datapush   = f'(Salir).... <<<  ■  (Help).... ?  ■  (Repeat).... < '
        # self.head_datapush  = " XINDEX - OVER-MAIN "
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # RESPUESTAS ■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■ DIRECTAS ... Se evalua cada uno: 
        self.lst_resp_ACCION = ['<','?','<<<']
        # ■ PREFIJO + RESPUESTA ... Se evalua cada uno: 
        self.lst_resp_BEGINERS = ['**', '=>']
        # ■ ENVUELTAS... Se evalua la lista como una unidad, (pre y pos)(envoltorio) : 
        self.lst_resp_PACK_1 = ['<<','>>']        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■ MENU PRINCIPAL(SE ESTABLECE EN MYSTYCA)
        self.menu_dvd = None
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # PREPARA IMPRESION ██████████████████        
        self.F_RANK_Y = None        
        self.F_RANK_Y_DEF = None
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■ LONGITUD MAXIMA DEL MENU (INCLUYE XINDEX E ITEMS)
        self.longitud_max_xindex=0
    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    def set_style(self, b_loop: bool = None, sp1: int = None, sp2: int = None, sp3: int = None, franky=None, franky_def=None):
        if b_loop is not None:
            setattr(self, "b_loop", b_loop)
        if sp1 is not None:
            setattr(self, "sp1", sp1)
        if sp2 is not None:
            setattr(self, "sp2", sp2)
        if sp3 is not None:
            setattr(self, "sp3", sp3)
        if franky is not None:
            setattr(self, "F_RANK_Y", franky)
        if franky_def is not None:
            setattr(self, "F_RANK_Y_DEF", franky_def)

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

    # ███████████████████████████████████████████████████████████████████████████████
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
            new_menu = MenuDvd(titulo=titulo, lst_items=lst_itemX, lst_funciones=lst_funcX, fraseHead=fraseHead)
            """ ■■ Se crea un objeto MenuDvd """
            # print(new_menu)
        except Exception as e:
            print(e)
            return None
        
        # Añade a la lista de titulos y a la lista de menus de XindeX
        self.lst_titulosXX.append(titulo)
        self.lst_menuXX.append(new_menu)
        
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
    def get_menudvd(self, titulo:str=None):
        """ ■■ Retorna un objeto MenuDvd x su str titulo. 
        [titulo](str) => Titulo del menú a devolver.
            None => devuelve todos los menus en lst_menuXX ( añadidos geneticamente con self.addX() )
        """
        if titulo is None:
            return [menu for menu in self.lst_menuXX]      # LISTA CON TODOS LOS MENUS 
        else:                    
            if titulo in self.lst_titulosXX:
                for menu in self.lst_menuXX:
                    if str(menu.titulo) == str(titulo):
                        return menu
    
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
    
    # ████████████████████████████████████████████████████████████████████████████████████████████████
    # █████ MUESTRA UN XINDEX.  (Imprime el menu con subMenus - Toma Control - Ejecuta Funciones) ████
    # def mystyca(self, titulo:str, tipo_index:str='a', b_mode_all:bool=True, b_loop:bool=True, pad_x:int=15):
    def mystyca(self, titulo:str, head_datapush:list=None, pad_x:int=15):
        """ 
        ■ [titulo]      Id del Menu Añadido/Configurado/Mostrados sus Items.
        
        ■ [pad_x] (int)      Distancia entre el punto final del str del menu y el marco final.
        
        ■ Ejemplos:
            1.  retorno = The_X_Men.mystyca(titulo='Menu1', b_mode_all=False, b_loop=True)
            2.  retorno = The_X_Men.mystyca(titulo='Menu1' )
            3.  retorno = The_X_Men.mystyca(titulo='Menu1', tipo_index='1', b_mode_all=False, b_loop=True)
        """    

        # ■■ VALIDA TITULO REPETIDO Y EXISTENCIA EN LA GENETICA(CONFIG)
        if titulo not in self.lst_titulosXX or titulo not in self.dicc_xgenx: 
            print(f'ERR-VAL:: {titulo} NO REGISTRADO EN XGENX')
            return None

        self.head_datapush=head_datapush
        self.pad_x = pad_x

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ███ CACHA EL MENU A IMPRIMIR...es la BASE GENETICA de trabajo
        # ████████████████████████████████████████████████████████████████████
        
        menu_dvd = self.get_menudvd(titulo = titulo)
        if not menu_dvd: return None
        self.menu_dvd = menu_dvd
        print(f'■ MENU: {self.menu_dvd.titulo}')
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ███ MODULO GENETICO 
        # ████████████████████████████████████████████████████████████████████

        # ■■ LISTADO DE LOS ITEMS QUE APARECEN EN EL MENU GENETICO. en orden de aparicion en el menu.... de arriba a abajo.
        # ■■ GENERICA DE NUMERO DE FILAS           
        self.lst_keys = self.mystyca_keys( menu_dvd = self.menu_dvd )
        
        # ■■■■■■■■■■■■■ CONFIGURACION DE LA GENETICA 
        self.lst__men_itm_lev_ape_name_padr_ipadr_func = self.mystyca_scaner_genetico( menu_dvd = self.menu_dvd )            

        # ■■■■■■■■■■■■■ CREACION DE LOS INDICES GENETICOS POSIBLES
        self.lst_idx_NUMERIC, self.lst_idx_ALF_MAX, self.lst_idx_ALF_MIN, self.lst_idx_MIXTO = self.crear_xindicex(lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func  )
        # ■■■■■■■■■■■■■ MATRIZ DE XINDEX VALIDOS X USER 
        self.matriz_opt_ok = self.get_lst_xindex_ok(tipo_index = self.tipo_index)
        if not self.matriz_opt_ok: return None

        # ■■ LISTA de las OPCIONES VALIDAS ...necesaria para self.get_matriz_impresion_literal
        self.lst_opts_ok = [('.').join(fila) for fila in self.matriz_opt_ok]

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ███ MODULO IMPRESION 
        # ████████████████████████████████████████████████████████████████████
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # TABLERO DE XINDEX 
        
        # ■■ MATRIZ DE IMPRESION: ■■■
        # ■■ b_definicion = False > sin incluir las columnas de definicion
        self.matriz_impresion_xindex = self.get_matriz_impresion_literal(menu_dvd = self.menu_dvd , 
                                                                        lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func , 
                                                                        lst_keys = self.lst_keys, 
                                                                        lst_opts_ok = self.lst_opts_ok, 
                                                                        b_definicion = False)        
        if not self.matriz_impresion_xindex: 
            print('ERROR :::: EN MATRIZ IMPRESION')
            return None        

        # ■■ LISTA DE STRING PARA IMPRIMIR 
        lst_mystyca_impresion = [''.join(mystyca_fila) for mystyca_fila in self.matriz_impresion_xindex]

        # ■■ LONGITUD MAXIMA DEL MENU..... usado para calcular el ancho de la columna.
        self.longitud_max_xindex = max(len(line) for line in lst_mystyca_impresion)
        
        # ■■ SACO LAS FILAS Y COLUMNAS DE ESTA GENETICA PARA PODER SACAR UNA DIMENSION PARA CREAR EL TABLERO DE IMPRESION FRANKY
        filas = len(self.matriz_impresion_xindex)
        columnas = len(self.matriz_impresion_xindex[0])

        self.F_RANK_Y = F_r_a_n_k_y( dimension = f'{filas}X{columnas}', head_datapush = self.head_datapush , pie_datapush=self.pie_datapush , pad_x = self.pad_x )
        self.F_RANK_Y.push(data_push=lst_mystyca_impresion, eje='Y')
        self.F_RANK_Y.imprimir(sp_between = 2, ancho_columna = None )

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        #  TABLERO DE INFORMACION ? 
        #  ■ PREPARO OTRO TABLERO PARALELO(F_RANK_Y_DEF) CON LA INFORMACION DE DEFINICION

        self.F_RANK_Y_DEF = F_r_a_n_k_y( dimension = f'{filas}X{columnas}', head_datapush = self.head_datapush , pie_datapush=self.pie_datapush , pad_x = self.pad_x )
        self.F_RANK_Y_DEF.push(data_push=lst_mystyca_impresion, eje='Y')
        
        # ■■ LISTA DE DEFINICIONES DE MENU GENETICO
        lst_definicion_item  = self.get_lst_definiciones( menu_dvd = self.menu_dvd, 
                                                            lista_m_i_l_a_n_p_i_f =self.lst__men_itm_lev_ape_name_padr_ipadr_func, 
                                                            b_mode_all = self.b_mode_all )
        # ■■ LISTA DE FUNCIONES DE MENU GENETICO
        lst_funcion_item = self.get_lst_funciones( lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func )
        
        # ■■■ CARGA EL TABLERO PERO NO LO IMPRIME, SOLO LO PREPARA.
        self.F_RANK_Y_DEF.push( data_push=lst_definicion_item, celda_inicio='D:0',  eje='Y' )
        self.F_RANK_Y_DEF.push( data_push=lst_funcion_item, celda_inicio='E:0',  eje='Y' )

        # ████████████████████████████████████████████████████████████████████████████████████████████████████████████
        # MODULO RESPUESTA ███████████████████████████████████████████████████████████████████████████████████████████
        # ████████████████████████████████████████████████████████████████████████████████████████████████████████████  
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ████ LOOP = FALSE, 1 SOLA RESPUESTA Y VUELVES ████
            # ■■ lo gestiona el main( .... cualquier llamada ) 
            # ■■ [respuesta] es el indice lineal en lst_keys o self.lst__men_itm_lev_ape_name_padr_ipadr_func
        if self.b_loop == False:   
            while(True):    # SI EL USUARIO INTRODUCE ? O < TIENE QUE REPETIRSE Y VUELVE CUANDO EL USUARIO RESPONDE SALIR U OPT-OK
                #  ■■■ XAVIER - OBTIENE RESPUESTA DE USUARIO ■■■
                dicc_xavier = self.get_dicc_xavier_into_user(menu_dvd = self.menu_dvd , lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func )    
                if dicc_xavier == None:         # SALIR... ha pulsado '<<<'. Esto anula el menu, pq se ejecuta una sola vez.
                    return None                 # Sale por Main(....por donde es llamada)
                
                # ■ OBTIENE EL INDICE EN M_I_L_A_N_P_I_F SI LO ENCUENTRA Y SI NO DEVUELVE NONE
                xindex = self.__get_xindex(menu_dvd = self.menu_dvd , dicc_respuesta = dicc_xavier, lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func)
                if  xindex != None:
                    dicc_xavier['xindex'] = xindex                    
                    return dicc_xavier['xindex']
                
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ████ LOOP = TRUE, SOLO SALES POR <<< ████
        while(True):
            # ■■■ XAVIER - OBTIENE RESPUESTA VALIDA DEL USUARIO, O SALIR ■■■
            dicc_xavier = self.get_dicc_xavier_into_user( menu_dvd = self.menu_dvd , lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func)   
            
            # ■■■ SALIR... ha pulsado '<<<' ■■■
            if not dicc_xavier:       
                return True                       
            
            # ■■■ TERMINATOR - EJECUTA LA RESPUESTA DEL USUARIO ■■■
            self.Terminator(dicc_respuesta = dicc_xavier, titulo_menu = self.menu_dvd.titulo)
            continue

    # █████████████████████████████████████████████████████████████
    # RCRSV: LISTA con Todos los items en orden de impresion.██████
    def mystyca_keys(self, menu_dvd, level=None, retorno=None):
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

    # █████████████████████████████████████████████████████████████
    # ████████████ RCRSV:  DATOS POR FILA DE IMPRESION  ███████████
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

                funcion_name = self.get_funcion_name(menu_dvd = menu_dvd, item=item)
                retorno.append(( menu_dvd.titulo ,                                  
                                item , 
                                level , 
                                apellido , 
                                menu_dvd.get_numRltv_row_body(i) ,
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
                                menu_dvd.get_numRltv_row_body(i) ,
                                self.get_padre(titulo_menu = menu_dvd.titulo) , 
                                self.get_ind_en_padre(titulo_menu = menu_dvd.titulo)  , 
                                # funcion_name
                                menu_dvd.dicc_menu.get(item, None)
                                ))
                apellido = aux
        return retorno    
    
    # OBTIENE EL NOMBRE DE LA FUNCION DE UN ITEM DE UN MENU
    def get_funcion_name(self, menu_dvd, item):
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
    
    # ■■■ CUANDO PULSA   '?' 
    def get_mystyca_informacion(self, titulo_menu, b_mode_all):
        """ CUANDO SE PULSA '?' , IMPRIME EL MENU CON INFORMACION SOBRE LA CONFIGURACION 
        [titulo_menu], 
        [b_mode_all], 
        RETORNO:
        """
        if self.F_RANK_Y_DEF.head:
            if b_mode_all == True: 
                # self.F_RANK_Y_DEF.head.push(data_push = ['  '] , celda_inicio='D:0')
                self.F_RANK_Y_DEF.head.push(data_push =['  '*2, " ■  MODE ::: Exec All"], celda_inicio='E:0', b_lineal=True)
            else:
                self.F_RANK_Y_DEF.head.push(data_push =['  '*2, " ■  MODE ::: Exec (X)"], celda_inicio='E:0', b_lineal=True)

        # ■■ IMPRIMIR EL TABLERO DE DEFINICION.
        self.F_RANK_Y_DEF.imprimir(lista=[self.longitud_max_xindex], sp_between = 3 , ancho_columna = None )
    
    # ■■■ OBTIENE LA LISTA DE DEFINICIONES (B_EXEC_ALL)    
    def get_lst_definiciones( self, menu_dvd, lista_m_i_l_a_n_p_i_f:list, b_mode_all:bool ):
        """ ■■ Devuelve LA Lista de Definicion (padre or hijo)(directorio or punta)
        [lista_m_i_l_a_n_p_i_f](list) , self.lst__men_itm_lev_ape_name_padr_ipadr_func
        [b_mode_all](bool), self.b_mode_all
        """
        # OBTENEMOS LA LISTA DE PADRES GENETICOS
        lst_padres  = self.get_list_padres_mystyca(menu_dvd = menu_dvd)
        lst_definicion_item=[]
        for i, fila_genetica in enumerate(lista_m_i_l_a_n_p_i_f):
            # ■ DEFINICION
            if b_mode_all == True: 
                lst_definicion_item.append (f'(D)' if fila_genetica[1] in lst_padres else f'(X)')
            else:
                lst_definicion_item.append (f'(-)' if fila_genetica[1] in lst_padres else f'(X)')
        
        # RETORNO
        return lst_definicion_item if lst_definicion_item else None
    
    # ■■■ OBTIENE LA LISTA DE LAS FUNCIONES SEGÚN EL ORDEN GENETICO
    def get_lst_funciones( self, lista_m_i_l_a_n_p_i_f:list ):
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
       
    # ■■■ FROM nombre-titulo-Menu TO nombre-padre     
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

    # ■■■ FROM nombre-titulo TO indice en el padre
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

    # ███████████████████████████████████████████████████████████████████████████████████
    # ████████████ XAVIER  pide datos al Usuario y le saca un Dato por Teclado ██████████
    def get_dicc_xavier_into_user(self, menu_dvd, lista_m_i_l_a_n_p_i_f:list=None):
        """ ■■ Def: Pide Un dato al Usuario y valida (self.__get_xindex ) que da una respuesta valida('b2' pejemp) con respecto a la geneticaX
        [menu_dvd] : el objeto MenuDvd (principal) sobre el que se trabaja. el punto de partida del analisis... Menu1
        [b_mode_all] : (bool) True = en todos los items intento ejecutar la funcion. False=Los directorios no se ejecutan.

        Retorno: None, <<< salir | 
                diccionario respuesta.keys = ('pre','respuesta','pos','xindex') de los elementos en lst_keys()

        """
        MONO_FROM   = 0
        MONO_TO     = 1
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # BUCLE HASTA OPCION VALIDA or SALIR +  DESEMPAQUETA LAS  RESUPUESTAS
        respuesta=None
        dicc_xavier = {}

        while(True):
            dicc_xavier['pre'] = None
            dicc_xavier['respuesta'] = None
            dicc_xavier['pos'] = None
            dicc_xavier['xindex'] = None
            
            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            # ██ PIDE RESPUESTA AL USER ██
            respuesta = input(f"{menu_dvd.intradilla_data_user}").strip()

            # ACCION DIRECTA
            if respuesta in self.lst_resp_ACCION:
                # ■■ SI HAY ALGUNA RESPUESTA DE ACCION DIRECTA NO HAY XINDEX, SOLO RESPUESTA.... para Terminator
                if respuesta == SALIR:
                    return None
                else:
                    dicc_xavier['pre'] = None
                    dicc_xavier['respuesta'] = respuesta
                    dicc_xavier['pos'] = None
                    dicc_xavier['xindex'] = None
                    
                    return dicc_xavier      # RETORNO LA ACCION ? , < , <<< PARA QUE LA EVALUE TERMINATOR.            
            elif any(respuesta.startswith(monomio) for monomio in self.lst_resp_BEGINERS):
                # ■■ BUSCA SI HAY ALGUNA RESPUESTA DEL USUARIO QUE EMPIECE POR UN BEGINER 
                
                # ENCUENTA EL INDICE QUE CUMPLE LA CONDICION EN EL ITERADOR self.lst_resp_BEGINERS('**', '=>')
                indice = next((i for i, monomio in enumerate(self.lst_resp_BEGINERS) if respuesta.startswith(monomio)), None)
                if indice is None: 
                    continue
                
                # CACHA EL MONOMIO 
                monomio = self.lst_resp_BEGINERS[indice]                                
                dicc_xavier['pre']       = monomio
                
                # A PARTIR DEL MONOMIO PUEDO CACHAR LA RESPUESTA. 
                dicc_xavier['respuesta'] = respuesta[len(monomio):]
                dicc_xavier['pos']       = None

                # ■ OBTIENE EL INDICE EN self.lst__men_itm_lev_ape_name_padr_ipadr_func
                xindex = self.__get_xindex(menu_dvd = menu_dvd , dicc_respuesta = dicc_xavier, lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f)
                if  xindex != None:
                    dicc_xavier['xindex'] = xindex
                    return dicc_xavier

                continue    # ■ SI NO ENCUENTRA UN INDICE VALIDO VUELVO A PREGUNTAR... USUARIO CONFUSO ;)
            
            elif respuesta.startswith(self.lst_resp_PACK_1[MONO_FROM]) and respuesta.endswith(self.lst_resp_PACK_1[MONO_TO]):       
                # ■■ LOS PACKS HAY QUE TRATARLOS INDIVIDUALMENTE, PERO CON ESTE PATRON SE PUEDE HACER COPY-PASTE
                dicc_xavier['pre']       = respuesta[ :len(self.lst_resp_PACK_1[MONO_FROM]) ]                                    # Desde el inicio(0) hasta 1(2-1) <<
                dicc_xavier['respuesta'] = respuesta[ len(dicc_xavier['pre']) : -len(self.lst_resp_PACK_1[MONO_TO]) ]
                dicc_xavier['pos']       = respuesta[ len(dicc_xavier['pre'])+len(dicc_xavier['respuesta']): ]      # Desde 2 hasta final >>
                
                # ■ OBTIENE EL INDICE EN self.lst__men_itm_lev_ape_name_padr_ipadr_func
                # ■ SI NO ENCUENTRA EL INDICE VUELVE A PREGUNTAR
                xindex = self.__get_xindex(menu_dvd = menu_dvd , dicc_respuesta = dicc_xavier, lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f)
                if  xindex is not None:
                    dicc_xavier['xindex'] = xindex
                    return dicc_xavier
                continue
            else:
                # ██ XINDEX: OPCION BUENA
                dicc_xavier['pre']       = None
                dicc_xavier['respuesta'] = respuesta
                dicc_xavier['pos']       = None
                xindex = self.__get_xindex(menu_dvd = menu_dvd , dicc_respuesta = dicc_xavier, lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f)
                if  xindex is None:
                    continue
                else:
                    dicc_xavier['xindex'] = xindex
                    return dicc_xavier

        # RETORNO ██████ evaluo si hay una respuesta o varias y las devuelvo.
        return dicc_xavier if dicc_xavier else None

    def __get_xindex(self, menu_dvd , dicc_respuesta:dict, lista_m_i_l_a_n_p_i_f:list):
        """ DEVUELVE EL INDICE DEL ITEM EN LA LISTA GENETICA O NONE  SI LA RESPUESTA ESTA EN EL XINDEX y COORDINA CON b_mode_all.
        [dicc_respuesta]:(dict), diccionario dicc_xavier que se carga en self.get_dicc_xavier_into_user()
            ■ contiene las keys: 'pre' , 'respuesta', 'pos' =► dicc_respuesta.['respuesta'] OR dicc_respuesta.get('respuesta', '')
        [b_mode_all]:(bool),True  =► Se ejecutan tanto los PADRES, como los HIJOS.
                            False =► Sólo se ejecutan los HIJOS
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
                            # item_menu = , lista_m_i_l_a_n_p_i_f:list[i][1]
                                
                            # ■■■■■■■■■■■■■■■■■■■■■■■■■
                            # ■■ MODO DE OPCION VALIDA ( b_mode_all = True, ejecuta todo. ■ b_mode_all = False, ejecuta solo hijos.                            
                            if self.b_mode_all == True:     
                                # ■■ Todo son opciones validas(HIJOS Y PADRES).... responsabilidad del usuario meter funciones en directorios.
                                return i      # ■■ ENCUENTRA Y RETORNA EL INDICE EN LST_KEYS!!!!!!!!!   :) 
                            else:             
                                # ■■ Solo los Hijos son validos. Los Directorios No se pueden Ejecutar en b_mode_all==False
                                if item_menu in lst_padres:                                            
                                    print(f'{item_menu} ■ (Directorio)')
                                    return None
                                else:
                                    return i
            
        except Exception as e:      # SI ERROR, INFO Y SEGUIMOS ::::
            print(f'ERROR EVALUACION ::: {e}')
            return None
            # continue
        pass

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # CREAR INDICEXXXX ████████████████████████
    def crear_xindicex(self, lista_m_i_l_a_n_p_i_f ): 
        """ 
        ALGORITMO INFERNAL PARA SACAR LOS INDICES CORRECTOS EN LA FORMA [1, 0, 1, 2] (camino de levels)
        ■ Este retorno Se Corresponde con el level sacado de en la funcion recursiva. 
        ■ Marca la posicion que va a tener y la numeracion con respecto a esa posicion.
        ■ Se basa en la creación de la lista del indice numerico y a partir de él crea los otros índices.
        ......una pesadilla que me ha llevado días :()

        ■ [lista_m_i_l_a_n_p_i_f]: lst de de datos geneticos que se saca de self.mystica_ScannerX()
        
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
    
    # SEGUN EL TIPO DE INDICE, DEVUELVE LAS OPCIONES CORRECTAS
    def get_lst_xindex_ok(self, tipo_index=TYPEX.NUMERIC):
        """ De todas las listas de indices creadas (lst_idx_NUMERIC, lst_idx_ALF_MAX, lst_idx_ALF_MIN, lst_idx_MIXTO ), 
        tipo_index indica cual es con la que nos quedamos.

        [tipo_index]:(str, int) ■ str => '1' , 'A', 'a' , '1a' 'a1'  ■ int => Enum TYPEX
        [lista_tipos_created]:(listr) => lista de los tipos creados usados que van a ser devueltos. esto hace que pueda personalizar los indices y crear sub-menus dentro de mystyca.
                                         ■ ES FUNDAMENTAL PASARLOS EN EL ORDEN DE DICC_OK
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
    def Terminator(self, dicc_respuesta:dict, titulo_menu:str):
        """ Def: Tenemos la mision de crear una lista de [item , funcion, respuesta antigua, respuesta nueva]
        [respuesta]:(dict): diccionario respuesta que se evalua en self.get_dicc_xavier_into_user(U)
        """        
        # VALIDACION
        if not isinstance(dicc_respuesta, dict): return None
        mono_from = dicc_respuesta.get('pre', None)
        respuesta = dicc_respuesta.get('respuesta', None)
        mono_to = dicc_respuesta.get('pos', None)
        xindex = dicc_respuesta.get('xindex', None)

        lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func
        COLUMNA_FUNCION = 7        

        # EMPIEZA LA EVALUACION DE LA RESPUESTA
        if not mono_from and not mono_to and respuesta and not xindex:      # ■■■ ACCION DIRECCTA ? , < , <<< ■■■ 
            if respuesta == '?':                                            # ■ INFO
                os.system('cls')              
                self.get_mystyca_informacion(titulo_menu=titulo_menu, b_mode_all=self.b_mode_all)
            
            elif respuesta == '<':                                          # ■ REPETIR MENU
                os.system('cls')              
                self.F_RANK_Y.imprimir(sp_between = 2, ancho_columna = None )
            else:                                                           # MONO NOT FOUND
                return False

        elif not mono_from and not mono_to and respuesta and xindex:        # ■■■ XINDEX ■■■ 
            # ██ EJECUTA LA FUNCIONN            
            lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_FUNCION]() if lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_FUNCION] else None
        
        else:                                               # ■■■ NOT FOUND ■■■
            print('EXEC NOT FOUND')                
            return

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
    
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # DEVUELVE LAS LISTAS XA WEB ■■■■■■■■■■■■■
    def get_web_lsts_lens_linea(self, titulo,  tipo_index=0, b_mode_all=True, b_loop=True, pad_x=15):
        """ Devuelve lo que necesita la web para representarse 
        [titulo](str): El titulo del menu. (obligatorio                   )
        [tipo_index](0, 'a', 'A', 'A0')
        [b_mode_all](bool)
        [b_loop](bool)
        [pad_x](int)
        """
        # ■■■■ VALIDA SI EL TITULO ESTA REPETIDO Y LA EXISTENCIA EN LA GENETICA(self.config())        
        if titulo not in self.lst_titulosXX or titulo not in self.dicc_xgenx: 
            print(f'ERR-VAL:: {titulo} NO REGISTRADO EN XGENX')
            return None        
        
        # ■■■■ MODULO CONFIG    
        # ■■■■ MODULO GENETICO     ■ lista_m_i_l_a_n_p_i_f  ■ lst_keys  ■ lst_opciones_ok  ■ crear_xindicex
        # ■■■■ MODULO IMPRESION    ■ get_matriz_impresion_literal   
        # ■■■■ MODULO RESPUESTA
        pass
        
    # DEVUELVE UNA MATRIZ DEL BODY DEL MENU. RECONFIGURACION PARA IMPRIMIR
    def get_matriz_impresion_literal(self, menu_dvd, lista_m_i_l_a_n_p_i_f:list, lst_keys:list, lst_opts_ok:list,b_definicion:bool=False ):
        """ DEVUELVE LA MATRIZ DE IMPRESION GENETICA RELLENA.
        [menu_dvd]:(MenuDvd), 
        [b_mode_all]:(bool), 
        [matriz_opt_ok](list), 
        [b_definicion]:(bool)=False
        """
        # VALIDACION
        # if not lst_keys: return None
        
        # ■■ CADA LISTA REPRESENTA UNA COLUMNA. LUEGO SE MONTA
        # ■■ La impresion trabaja linea a linea, al trabajar con lista de lista de str, puedo trabajar como matriz y alterar las columnas antes de ser impreso todo como lineas.
        lst_col_0_lvl        = [f'{ int(row[2]) * self.TAB }' for row in lista_m_i_l_a_n_p_i_f]        
        lst_col_1_xindex     = [f'{ xindex }'  for xindex in lst_opts_ok]
        lst_col_2_pto        = [f'{ '.' }'     for i in range(len(lst_keys))]            
        lst_col_3_sp1        = [f'{ ' ' * self.sp1}' for i in range(len(lst_keys))]            
        lst_col_4_item       = [f'{ row[1] }'  for row in lista_m_i_l_a_n_p_i_f]
        lst_col_5_sp2        = [f'{' ' * self.sp2}' for i in range(len(lst_keys))]            
        lst_col_6_definicion = self.get_lst_definiciones(   menu_dvd = menu_dvd, 
                                                            lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f, 
                                                            b_mode_all = self.b_mode_all)            
        lst_col_7_sp3        = [f'{' ' * self.sp3}' for i in range(len(lst_keys))]                    
        lst_col_8_funcion    = [f'{ self.get_funcion_name(menu_dvd=self.get_menudvd(titulo=row[0]), item = row[1]) }' 
                                        for row in lista_m_i_l_a_n_p_i_f]

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
                
            matriz_impresion_xindex.append(fila) if fila else None
        
        # ■ RETORNO:
        return matriz_impresion_xindex if matriz_impresion_xindex else None
    

    # █████████████████████████████████████████████████████████
    # ███ REALIZA TODAS LAS ACCIONES DE GENERACION GENETICA ███
    def load_modulo_gentico_x(self, titulo:str):
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
                
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■  TABLERO DE XINDEX 
        # ■■ MATRIZ DE IMPRESION: ■■■
        # ■■ b_definicion = False > sin incluir las columnas de definicion
        self.matriz_impresion_xindex = self.get_matriz_impresion_literal(menu_dvd = menu_dvd , 
                                                                        lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f , 
                                                                        lst_keys = lst_keys, 
                                                                        lst_opts_ok = lst_opts_ok,
                                                                        b_definicion = False
                                                                        )        
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
        self.F_RANK_Y = F_r_a_n_k_y( dimension = f'{filas}X{columnas}', head_datapush = self.head_datapush , pie_datapush=self.pie_datapush , pad_x = self.pad_x )
        self.F_RANK_Y.push(data_push=lst_mystyca_impresion, eje='Y')
        self.F_RANK_Y.imprimir(sp_between = 2, ancho_columna = None )
        
        # ■ TABLERO DE INFORMACION ? ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■  
        # ■ PREPARO OTRO TABLERO PARALELO(F_RANK_Y_DEF) CON LA INFORMACION DE DEFINICION
        self.F_RANK_Y_DEF = F_r_a_n_k_y( dimension = f'{filas}X{columnas}', head_datapush = self.head_datapush , pie_datapush=self.pie_datapush , pad_x = self.pad_x )
        self.F_RANK_Y_DEF.push(data_push=lst_mystyca_impresion, eje='Y')
        # ■■ LISTA DE DEFINICIONES DE MENU GENETICO
        lst_definicion_item  = self.get_lst_definiciones( menu_dvd = menu_dvd, 
                                                        lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f, 
                                                        b_mode_all = self.b_mode_all )
        # ■■ LISTA DE FUNCIONES DE MENU GENETICO
        lst_funcion_item = self.get_lst_funciones( lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f )
        # ■■■ CARGA EL TABLERO PERO NO LO IMPRIME, SOLO LO PREPARA.
        self.F_RANK_Y_DEF.push( data_push=lst_definicion_item, celda_inicio='D:0',  eje='Y' )
        self.F_RANK_Y_DEF.push( data_push=lst_funcion_item, celda_inicio='E:0',  eje='Y' )
        pass
    
    # ████████████████████████████████████████████████████████
    # ███ REALIZA TODAS LAS ACCIONES DE RESPUESTA GENETICA ███
    def load_modulo_respuesta_x(self, menu_dvd, lista_m_i_l_a_n_p_i_f:list):
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■■ LOOP = FALSE, 1 SOLA RESPUESTA Y VUELVES ■■■
            # ■■ lo gestiona el main( .... cualquier llamada ) 
            # ■■ [respuesta] es el indice lineal en lst_keys o self.lst__men_itm_lev_ape_name_padr_ipadr_func
        if self.b_loop == False:   
            while(True):    # SI EL USUARIO INTRODUCE ? O < TIENE QUE REPETIRSE Y VUELVE CUANDO EL USUARIO RESPONDE SALIR U OPT-OK
                #  ■■■ XAVIER - OBTIENE RESPUESTA DE USUARIO ■■■
                dicc_xavier = self.get_dicc_xavier_into_user(menu_dvd = menu_dvd , lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f )    
                if dicc_xavier == None:         # SALIR... ha pulsado '<<<'. Esto anula el menu, pq se ejecuta una sola vez.
                    return None                 # Sale por Main(....por donde es llamada)
                
                # ■ OBTIENE EL INDICE EN M_I_L_A_N_P_I_F SI LO ENCUENTRA Y SI NO DEVUELVE NONE
                xindex = self.__get_xindex(menu_dvd = menu_dvd , dicc_respuesta = dicc_xavier, lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f)
                if  xindex != None:
                    dicc_xavier['xindex'] = xindex                    
                    return dicc_xavier['xindex']
                
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■■■ LOOP = TRUE, SOLO SALES POR <<< ■■■■
        while(True):
            # ■■■ XAVIER - OBTIENE RESPUESTA VALIDA DEL USUARIO, O SALIR ■■■
            dicc_xavier = self.get_dicc_xavier_into_user( menu_dvd = menu_dvd , lista_m_i_l_a_n_p_i_f = lista_m_i_l_a_n_p_i_f)   
            
            # ■■■ SALIR... ha pulsado '<<<' ■■■
            if not dicc_xavier:       
                return True                       
            
            # ■■■ TERMINATOR - EJECUTA LA RESPUESTA DEL USUARIO ■■■
            self.Terminator(dicc_respuesta = dicc_xavier, titulo_menu = menu_dvd.titulo)
            continue
        pass


# █████████████████████████████████████████████████████████████████████████████████████████████████████████████
# ██████████████████████████████████████ OVER MAIN ████████████████████████████████████████████████████████████
# █████████████████████████████████████████████████████████████████████████████████████████████████████████████
import threading        
import time         
from functools import partial    
# ============================================================================================
class Over_Main(XindeX):
    """ AMPLIA XindeX Añadiendo la ejecución en hilos separados .... 
        ■■ Interactivo ( tkinter ) , 
        ■■ Segundo plano demonio( flask ) 
    """
    def __init__(self, tipo_index:str='a', b_mode_all:bool=False, b_loop=True ):        
        
        
        super().__init__(tipo_index='a', b_mode_all=False, b_loop = True )
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        
        # DICCIONARIO PARA EL CONTROL DE HILOS CON LAS EJECUCIONES =>b2 (INDEPENDIENTE)(DEMONIO) Y <<b2>> (DEPENDIETE)
        self.hilos={}
        
        # LISTADO DE TODOS LOS SUB-MENUS QUE DEPENDEN DE menu_dvd
        self.lista_sub_menus = None
        
        # OPCIONES VALIDAS DE CADA LISTA: matriz_submenus_ok_off
        self.matriz_submenus_ok_off=[]
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        pass
        
    # DEVUELVE XINDEX VALIDO SEGUN tipo_index. 
    # SE PUEDE ELEGIR LA LISTA DE OPCIONES VALIDAS.
    def get_lista_index_ok_off(self, tipo_index, lista_lst_indices_created:list):
        """ devuelve el indice indicado valido de entre los que se pasan como argumento.        
        [lista_lst_indices_created]:(list de list) => ■ LO MAS IMPORTANTE ES QUE SE PASEN TODOS LOS INDICES (NUMERICO, MIN, MAX , MIXTO) 
        ■ Y EN ESE ORDEN
        """
        if not lista_lst_indices_created: return None
        if len(lista_lst_indices_created) != 4: return None

        if lista_lst_indices_created is not None:
            DICC_OK={ 1 : lista_lst_indices_created[0], 
                    'a' : lista_lst_indices_created[1], 
                    'A' : lista_lst_indices_created[2], 
                    'a1': lista_lst_indices_created[3], 
                    '1a': lista_lst_indices_created[3], 
                    'A1': lista_lst_indices_created[3], 
                    '1A': lista_lst_indices_created[3]
                    }
            # ■ RETORNA LA LISTA OK SEGUN tipo_index
            return DICC_OK.get(tipo_index, None)

    def ejecutar_interactivo(self, titulo_menu, item, respuesta):
        """ ■■ Logica Interactiva: Tkinter por ejemplo (demon=False)  """
        """ CONFIGURO EL HILO LO GUARDO Y LO LANZO """
        print(f"Interacción activa con {respuesta}...")
        hilo = threading.Thread(target=partial(super().Terminator, titulo_menu, item, respuesta, None)
                                , daemon=False )
        self.hilos[respuesta] = hilo
        hilo.start()

    def ejecutar_background(self, titulo_menu, item, respuesta):
        """ >> """
        """ ■■ servidor Flask por ejemplo (demon=True) """
        

        """ CONFIGURO EL HILO LO GUARDO Y LO LANZO """
        hilo = threading.Thread(target=self.ejecutar, 
                                kwargs={'titulo_menu': titulo_menu, 'item': item, 'respuesta':respuesta} , 
                                daemon=True
                                )
        self.hilos[respuesta] = hilo
        hilo.start()
        print(f"Tarea en segundo plano: item: {item} - index: '{respuesta}' ...... ejecutada.")

    def listar_hilos(self):
        print("Hilos en ejecución:")
        for opcion, hilo in self.hilos.items():
            estado = "activo" if hilo.is_alive() else "detenido"
            print(f"  - {opcion}: {estado}")
            aux = input(f'\nPulsa Cualquier tecla para continuar.... ')

    # ███████████████████████████████████████
    # ████████████ EJECUTADOR  ██████████████
    def Terminator(self, dicc_respuesta:dict, titulo_menu:str):
        """ Def: EJECUTA LA RESPUESTA - SOBRE ESCRIBE TERMINATOR PARA AMPLIAR LAS OPCIONES.
        [respuesta]:(dict): diccionario respuesta que se evalua en self.get_dicc_xavier_into_user(U)
        """        
        # VALIDACION
        if not isinstance(dicc_respuesta, dict): return None
        mono_from = dicc_respuesta.get('pre', None)
        respuesta = dicc_respuesta.get('respuesta', None)
        mono_to = dicc_respuesta.get('pos', None)
        xindex = dicc_respuesta.get('xindex', None)

        lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func
        COLUMNA_FUNCION = 7        

        # EMPIEZA LA EVALUACION DE LA RESPUESTA
        if not mono_from and not mono_to and respuesta and not xindex:      # ■■■ ACCION DIRECCTA ? , < , <<< ■■■ 
            if respuesta == '?':                                            # ■ INFO
                os.system('cls')              
                self.get_mystyca_informacion(titulo_menu=titulo_menu, b_mode_all=self.b_mode_all)
            
            elif respuesta == '<':                                          # ■ REPETIR MENU
                os.system('cls')              
                self.F_RANK_Y.imprimir(sp_between = 2, ancho_columna = None )
            else:                                                           # MONO NOT FOUND
                return False

        elif not mono_from and not mono_to and respuesta and xindex:        # ■■■ XINDEX ■■■ 
            
            # ██ EJECUTA LA FUNCIONN █████████████████████████████████████████
            lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_FUNCION]() if lista_m_i_l_a_n_p_i_f[xindex][COLUMNA_FUNCION] else None
        
        elif  mono_from and not mono_to and xindex:         # ■■■ BEGINNER'S ■■■ 
            if mono_from == '**':                           # ■ BEGIN
                print(f'EXEC BEGI_N **')                
                # VEO DONDE ESTOY DESPUES
                titulo_select   = lista_m_i_l_a_n_p_i_f[xindex][0]
                item_select     = lista_m_i_l_a_n_p_i_f[xindex][1]
                print(f'Menú Select: {titulo_menu} sobre Item Select: {item_select}')
                # ■ LLAMO A LA FUNCION BEGIN ASTERISCOS CON EL MENU_DVD SELECCIONADO EN LA RESUPUESTA
                self.begin_asterisco(titulo_menu=titulo_select)
                # VEO DONDE ESTOY DESPUES
                titulo_select   = lista_m_i_l_a_n_p_i_f[xindex][0]
                item_select     = lista_m_i_l_a_n_p_i_f[xindex][1]
                print(f'Menú Select: {titulo_menu} sobre Item Select: {item_select}')
            
            elif mono_from == '=>':                         # ■ DEMONIO - LANZA OVER-MAIN
                print('EXEC DEMONIO >>')                
            
            else:                                           # PRE- NOT FOUND
                print(f'EXEC PRE- NOT FOUND')                     

        elif  mono_from and mono_to and xindex:             # ■■■ PACK ■■■ 
            if mono_from == '<<' and mono_to == '>>':       # ■ DEPENDIENTE - PACK 1 - LANZA OVER-MAIN
                print('EXEC DEPENDIENTE')
            
            else:                                           # PACK NOT FOUND
                print('EXEC PACK NOT FOUND')                
        else:                                               # ■■■ NOT FOUND ■■■
            print('EXEC NOT FOUND')                
            return

    def begin_asterisco(self, titulo_menu:str):
        if not self.menu_dvd: return None
        # ■ ME GUARDO EL MENU PPAL
        menu_dvd_aux = self.menu_dvd
        head_datapush_aux = self.head_datapush
        # ■ BUSCO EL TITULO DEL MENU QUE EL USUARIO HA SELECCIONADO
        
        # ■ LLAMO A LA GENERACION DEL NUEVO MENU
        self.mystyca(titulo=titulo_menu, head_datapush=titulo_menu)
        
        # ■ HA SALIDO POR <<< Y DEJO LAS COSAS COMO ESTABAN ANTES DEL **
        self.menu_dvd = menu_dvd_aux
        # CARGA GENETICA
        self.load_modulo_gentico_x(titulo = self.menu_dvd.titulo)
        if not self.lst__men_itm_lev_ape_name_padr_ipadr_func or not self.lst_keys or not self.lst_opts_ok: 
            return None
        # IMPRIME GENETICA
        self.F_RANK_Y.head.push(data_push=head_datapush_aux)
        self.load_modulo_impresion_x(menu_dvd = self.menu_dvd , 
                                    lista_m_i_l_a_n_p_i_f = self.lst__men_itm_lev_ape_name_padr_ipadr_func , 
                                    lst_keys = self.lst_keys ,
                                    lst_opts_ok = self.lst_opts_ok)
        
        
        # NOTA: NO CAGO EL MODULO RESPUESTAA PQ CUANDO SALGA DE ESTA FUNCION TERMINATOR ME ENVIARÁ AL MODULO RESPUESTA.
        pass
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    def obtener_texto_azul(self, texto):
        """Devuelve el texto coloreado en azul."""
        return f"{Fore.BLUE}{texto}{Style.RESET_ALL}"

    def obtener_longitud(self, texto):
        """Devuelve la longitud del texto con los caracteres de color incluidos."""
        texto_coloreado = self.obtener_texto_azul(texto=texto)
        return len(texto_coloreado)

    def obtener_longitud_real(self, texto):
        """Devuelve la longitud del texto sin los caracteres de color."""
        texto_coloreado = self.obtener_texto_azul(texto=texto)
        texto_limpio = re.sub(r'\x1B\[[0-9;]+m', '', texto_coloreado)  # Quita secuencias ANSI
        return len(texto_limpio)


