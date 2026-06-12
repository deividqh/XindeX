# •••••••••  By David Quesada Heredia davidquesadaheredia@gmail.com ••••••••••

# ███████████████████████████████████████████████████████████████████████████████████████████████████████████████
                                # ■ DEFINICION DE LAS CLASES ■
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████████
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# STTS:     Def las funciones estaticas que se pueden usar en Celda , Rango, Tablero y Brackets

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# CELDA:    Define el cruce entre una fila y una columna. guarda el valor y la letra de la columna.
    # ►A:0  ►B:3  ►M:10. etc...

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# RANGO:    Def un Objeto virtual que se define por todas las celdas que existen en entre una celda de inicio y una celda Fin
    # A:0 -> A:10
    # A:0 -> B:10
    # A:0 -> M:10

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# TABLERO:  Define Un Rango que puede contener otros rangos. Y Sirve de 'Tablero' de Impresion
    #   Loren Ipsum que estas en los cielos                                                       
    #                                                                                            
    #                                        False  None  3333              Hidalgo Caballero     
    #                                        4      5.5   6     Ey You                            
    #                                        True   1     A0                Globus Palidus        

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# FRANKY :   CREA 3 TABLEROS: CABECERA / CUERPO / PIE ....y les pone un MARCO. Sobreescribe imprimir()
    # ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    # █  Mensaje Head: Opcional: str, list, matriz                                                 █
    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    # █  Loren Ipsum que estas en los cielos                                                       █
    # █                                                                                            █
    # █                                       False  None  3333              Hidalgo Caballero     █
    # █                                       4      5.5   6     Ey You                            █
    # █                                       True   1     A0                Globus Palidus        █
    # █                                                                                            █
    # ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    # █  Mensaje Pie: Salir <<<  ■ Help-Exec ?  ■ Repeat < ■ (Info)  ??                            █
    # ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
# 

# ███████████████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████████
"""  
                    :::  S T T S  :::  CELDA :::  RANGO  :::  TABLERO  :::  FRANKY  :::
"""
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████████

""" 
Para el alfabeto lowerstrig, upperstring. """
import string           

class SttS():

    """ DICCIONARIOS FUNDAMENTALES QUE DEFINEN LETRA:NUMERO Y NUMERO:LETRA EN MAYUSCULA Y MINUSCULA(4 DICCIONARIOS).
    USADOS PARA REFERENCIAR LAS COLUMNAS POR SU LETRA Y OBTENER SU NUMERO AUTOMATICAMENTE O VICEVERSA. """
    _min_ln = None      # minusculas letra - numero 
    _min_nl = None      # minusculas numero - letra

    _may_ln = None      # mayusculas letra - numero 
    _may_nl = None      # mayusculas numero - letra

    @staticmethod
    def inicializa_diccs_letra_numero():
        """ ■ Inicializa los diccionarios estáticos si aún no están inicializados. """
        if SttS._min_ln is None or SttS._min_nl is None: 
            SttS.set_dicc_columnas_min()

        if SttS._may_ln is None or SttS._may_nl is None:
            SttS.set_dicc_columnas_may()
      
    # [dicc1] ==>  'a':0, 'b':1, ... 'az'=702 |  [dicc2] ==>   0:'a', 1:'b', ... 702:'az'
    @staticmethod

    def set_dicc_columnas_min():
        try:
            SttS._min_ln = {letra: i for i, letra in enumerate(string.ascii_lowercase)}
            index = len(SttS._min_ln)
            for first in string.ascii_lowercase:
                for second in string.ascii_lowercase:
                    SttS._min_ln[f"{first}{second}"] = index
                    index += 1
            # Invertido____________________________________________
            SttS._min_nl = {v: k for k, v in SttS._min_ln.items()}

        except Exception as e:
            print(f"Error Grave set_dicc_columnas_min::: {e}")
            return None, None
        finally:
            return SttS._min_ln , SttS._min_nl
    #  [dicc1] ==> 'A':0, 'B':1, ... 'AZ':702  |  [dicc2] ==>   0:'A', 1:'B', ... 702:'AZ'

    @staticmethod
    def set_dicc_columnas_may():
        """ RETORNA 2 DICCIONARIOS => 'A':0, 'B':1, ... 'AZ':702  y otro invertido =>  0:'A', 1:'B', ... 702:'AZ' 
        SttS._may_ln , SttS._may_nl
        """
        try:
            SttS._may_ln = {letra: i for i, letra in enumerate(string.ascii_uppercase)}
            index = len(SttS._may_ln)
            for first in string.ascii_uppercase:
                for second in string.ascii_uppercase:
                    SttS._may_ln[f"{first}{second}"] = index
                    index += 1

            # El invertido lo hacemos facil con una lista de comprension :)
            SttS._may_nl = {v: k for k, v in SttS._may_ln.items()}

        except Exception as e:
            print(f"Error Grave set_dicc_columnas_may::: {e}")
            return None, None
        
        finally:
            return SttS._may_ln , SttS._may_nl 

    # Convierte una cadena del tipo 20x15 en (20,15)   ó   A:13 en (A,13)
    @staticmethod
    def desata_binomio(cadena:str, char:str=':'):
        """
        Descompone una cadena en dos partes separadas por un carácter dado.
            [cadena] (str): La cadena a descomponer (e.g., 'A:0', '20x15').
            [char] (str): El carácter que separa las dos partes de la cadena (por defecto ':').
        Retorno:
            tuple: (str, str) con las dos partes de la cadena. Devuelve (None, None) si la head es inválida.
        Ejemplo:
            >>> SttS.desata_binomio("A:0")
            ('A', '0')
            >>> SttS.desata_binomio("20x15", char='x')
            ('20', '15')
        """
        try:
            cadena = str(cadena).upper()
            lst_f_c = cadena.split( sep = char, maxsplit = -1 )
            if not lst_f_c: 
                return None, None
            if len(lst_f_c) != 2: return None, None
        except Exception as e:
            return None, None
        finally:
            pass
        # SIEMPRE ES F , C 
        try:
            primer_binomio = str(lst_f_c[0]).strip()
            segundo_binomio = str(lst_f_c[1]).strip()
        except Exception as e:
            print(f"Error::: desata_binomio::: {e}")
            return None, None
        finally:
            return primer_binomio, segundo_binomio

    # VALIDA UNA FILA ENTRE DOS VALORES POSIBLES FROM Y TO ________________
    @staticmethod
    def b_fila_valida(fila, from_incl , to_incl ):
        try:
            fila=int(fila)
            if from_incl <= fila <= to_incl:  
                return True
            else:
                return False
        except Exception as e:
            return False

    # VALIDA QUE UNA COLUMNA ESTA EN EL RANGO FROM - TO _________________
    @staticmethod
    def b_columna_valida(columna, from_incl , to_incl):
        """ >>> Valida que una columna puede estar dentro del rango total de columnas posibles(desde a hasta az) 
        """
        # __________________________________________
        # Si no existen los diccionarios, los crea.
        SttS.inicializa_diccs_letra_numero()

        """ Viene como [Letra] y esta entre las combinacioes posibles('az' maximo, 'bn' sería falso) """
        if columna in SttS._may_ln or columna in SttS._min_ln:            
            numero_letra = SttS.letra_to_numcol(columna)
            if numero_letra == None: 
                return False
            if from_incl <= numero_letra <= to_incl:  
                return True
            else:
                return False

        """ Viene como [Numero] y esta entre las combinacioes posibles. 
        Lo typeo para que de igual si viene como 1 o como '1'         """
        if int(columna) in SttS._may_nl or int(columna) in SttS._min_nl:
            if from_incl <= columna <= to_incl:  
                return True
            else:
                return False

        return False        
        
    # DE LETRA A NUMERO  ____________________________________________
    @staticmethod
    def letra_to_numcol(letra):
        """ Entra una 'C' y sale un 3  o None si no encuentra 
        >>> Ejemplo: numero_columna = self.letra_to_num_col('C') 
        >>> print(numero_columna) ==> 2
        """
        # __________________________________________
        # Si no existen los diccionarios, los crea.
        SttS.inicializa_diccs_letra_numero()       
        
        # Paso la letra a   m i n u s c u l a  para poder buscar solamente en un diccionario y no tener que buscar en los 2 
        letra = str(letra).strip().upper()
        if letra in SttS._may_ln:
            return SttS._may_ln[letra]            
        else: 
            return None
    
    # SUMA UNA CANTIDAD A UNA LETRA ____________________________________________
    @staticmethod
    def suma_letra(letra, cantidad_sumar):
        """ Suma una cantidad a una letra y devuelve la letra resultante """
        # resultado = None
        try:
            letra = str(letra).strip().upper()
            SttS.inicializa_diccs_letra_numero()                       

            numero_letra = SttS.letra_to_numcol(letra=letra)
            if 0 <= numero_letra < len(SttS._may_ln.keys()):
                resultado = int(numero_letra) + int(cantidad_sumar)  # -1 => pq se empieza a contar desde la letra de inicio
                if resultado in SttS._may_nl:
                    """ Letra encontrada """
                    return SttS._may_nl[resultado]            
                else: 
                    return None
        except Exception as e:
            print(f'Error suma_letra :::: {e}')
            return None

    # IGUALA LAS LISTAS ____________________________________________________
    @staticmethod
    def igualar_listas(lista_keys, lista_to_relong, valor_relleno='Loren'):
        """             
        Trata las longitudes de las listas y las igualo según lista_keys como referencia.
        La que se Re-dimensiona creciendo o decreciendo para igualarse con lista_keys.
        [valor_relleno]: en caso de que lista_keys>listaToRelong, hay que rellenar con un nuevo valor. en caso de funciones, None(by Def)
        [Ejemplo de uso]:
        >>> listTOdict_byTcld_ToString.igualar_listas(lista_keys=lista_keys, lista_to_relong=listaTipos)        
        lista_keys y listaTipos son inmutables, se pasan por referencia y no hay que retornar valor. Aun así se retorna
        """
        if len(lista_keys) == len(lista_to_relong):
            return lista_to_relong
        elif len(lista_keys) > len(lista_to_relong):
            listaNewTipos=[valor_relleno for i, (k) in enumerate(lista_keys) if i >= len(lista_to_relong)]
            lista_to_relong = lista_to_relong + listaNewTipos
        else:
            longListaTipos = len(lista_to_relong)
            longListaKeys  = len(lista_keys)
            for i in range(longListaKeys , longListaTipos ):
                lista_to_relong.pop()

        return lista_to_relong
        pass

    @staticmethod
    def es_matriz(matriz):
        """ >>> VALIDA QUE ES UNA LISTA DE LISTAS
        True: Es una lista de listas tipo: [[1,2],[3,4],[5,6]]
        False: No es una lista de listas o error
        """
        try:
            if not isinstance(matriz, list):
                return False                        
            for elemento in matriz:
                if not isinstance(elemento, list):
                    return False            
            return True
        except Exception as e:
            return False

    # Entra una cadena separada por un caracter (coma) y devuelve una l i s t a   c o n   c a d a   i t e m 
    @staticmethod
    def cadena_to_lista(cadena:str, char:str=','):  
        """ >>> Entra Una cadena separada por comaas, retorna una list de coma en coma 
        Entra: 'cadena, de , ejemplo' |   Sale: ['cadena', 'de', 'ejemplo'] """      
        try:
            if not isinstance(cadena, str): return None
            # Quita Espacios delante y detras_________________
            cadena = cadena.strip()
            # Eliminar comas al inicio o al final_____________
            if cadena.startswith(char) or cadena.endswith(char):
                cadena = cadena.strip(char)
            # Convierte la cadena en una lista________________
            lst_retorno = cadena.split(sep=char)
            if not lst_retorno: return 
            # Quita los espacios de delante y detras de cada item_______
            lst_to_tablero = [str(item).strip() for item in lst_retorno]
        except Exception as e:
            return None
        finally:
            return lst_retorno

    # 'frase ejemplo' en 'f r a s e  E j e m p l o' 
    @staticmethod
    def frase_to_char_espacio(frase:str, b_tipo_titulo:bool=False):
        try:
            frase = str(frase).strip()
            if b_tipo_titulo==True:
                frase=str(frase).title()
            # Convertir la cadena en una lista de caracteres, preservando espacios
            lista_caracteres = [char if char!=' ' else '  ' for char in frase]
            # Unir los caracteres con un espacio intercalado
        except Exception as e:
            return frase
        finally:
            return ' '.join(lista_caracteres)
    
    # ENTRA UNA CELDA (C:2) Y DEVUELVO   3 , 2 . HACE VALIDACIONES DE TIPO
    @staticmethod
    def fc_by_celda(celda:str):
        """ >>> From 'C:4' To fila 4, columna 3         """
        # Validaciones
        fila    = None
        columna = None
        try:
            if not isinstance(celda, str): return None, None
            letra_columna , fila = SttS.desata_binomio(cadena=celda, char=':')
            if not letra_columna: return None, None
            columna = SttS.letra_to_numcol(letra=letra_columna)               
            if  fila == None or columna == None: return None, None            
            
            fila = int(fila) 
            columna = int(columna)

        except Exception as e:
            print(f'Error en num_col_by_celda{e}')
            return None, None
        finally:
            return abs(fila), abs(columna)        

    # ENTRA UNA fila y columna (3 , 2) y devuelvo una celda (C:2)
    @staticmethod
    def celda_by_fc(fila:int, columna:int):
        try:        
            """ Lo trato como número.... si casca, es letra. """
            columna = int(columna)
            letra = SttS._may_nl[columna]
            celda = f'{letra}:{fila}'
        except Exception as e:
            """ viene como letra """
            celda = f'{columna}:{fila}'

        return celda

    # Convierte una dimension del tipo 20x15 en filas=20, columnas=15
    @staticmethod
    def filas_columnas_from_dimension(dimension:str):
        try:
            dimension = dimension.upper()
            filas , columnas = SttS.desata_binomio(cadena=dimension, char='X')
            if filas and columnas:
                filas    = int(filas)
                columnas = int(columnas)
            return filas, columnas
        except Exception as e:
            print(f"Error::: get_filas_columnas_from_dimension::: {e}")
            return None, None    

    
    # ██████████████████████  R E C U R S I V A S  █████████████████████████    

    # Busqueda recursiva por un iterator lista
    @staticmethod
    def get_lst_rcrsv_level( iterator, retorno=None, level=None):
        """ >>> Devuelve el nivel que se va encontrando en una estructura, leyendo los items de izquierda a derecha.
        Ejemplo: >>> lst_levels = get_lst_rcrsv_level( [1,[2,3], 4, [5,6,7]], level=None)
                >>> print(lst_levels) ==> [0,1,1,0,1,1,1]
        """
        # p r i m e r a   v u e l t a  
        if retorno == None and level == None : 
            level = 0        
            retorno = []

        # p r o c e s o  r e c u r s i v o
        if isinstance(iterator, list) or isinstance(iterator, tuple):
            level += 1
            for subList in iterator:
                SttS.get_lst_rcrsv_level(iterator=subList, retorno=retorno, level=level)
        else:
            retorno.append(level)
        # R e t o r n o 
        return retorno

    @staticmethod
    def to_str_rcrsv(iterator , lst_retorno=None):
        # if not isinstance(iterator, list): return None
        if lst_retorno == None: 
            lst_retorno = []

        if isinstance(iterator, list) or isinstance(iterator, tuple):
            for item in iterator:
                SttS.to_str_rcrsv(item, lst_retorno)            
        elif isinstance(iterator, dict):                            
            t_fila = [(key, item) for key, item in iterator.items()][0]          
            """ >>> Convierte el dicc en una list (key , valor en str)... con el primer elemento la key del diccionario 
            """
            fila_str = [str(item) for item in t_fila]
            """ >>> Convierte a string cada elemento de la item 
            """
            lst_retorno.append(fila_str)
            SttS.to_str_rcrsv(t_fila, lst_retorno)

        else:            
            lst_retorno.append(iterator)
        
        return lst_retorno
    
    # Entra una matriz o lista y la convierte recursivmente en una lista de elementos unicos. No contempla dict.
    @staticmethod
    def aplanar_matriz(matriz):
        """ >>> Funcion recursiva que aplana matrices(listas de listas) o listas o datos. 
        [data] es cualquier dato de entrada(menos diccionarios, que los añade como un valor.)
        Retorno: lst de una sola dimension.
        Ejemplo: SttS.aplanar_matriz( [3,4,[5,6,7],8,[9,10]] ) -> [3,4,5,6,7,8,9,10]
        """
        lista = []
        try:
            for elemento in matriz:
                if isinstance(elemento, list) or isinstance(elemento, tuple)  or isinstance(elemento, set) :
                    lista.extend(SttS.aplanar_matriz(matriz=elemento))
                else:
                    lista.append(elemento)
        except Exception as e:
            print(f'Error ::: aplanar_matriz ::: {e}')
            return None
        return lista

    # lo contrario de SttS.aplanar_matriz(). 
    @staticmethod
    def encuadrar_matriz(matriz:list):
        """ >>> Pasa los valores de una matriz a un rango creado a partir de una celda determinada del rango.
        la diferencia con __push_plana() es que __push_plana lo mete lineal, valor por valor. 
        push_matriz mete una matriz con su forma en el rango. Para ello tiene que ser menor que el rango.
        en caso de ser mayor se puede crear un rango para tener acceso a su lst_celdas y verificar si coinciden.

        entra [3, 2, [4, 6]] y devuelve => [ [3,''] , [2,''] , [4,6] ]      3 filas x 2 columnas.
        entra [[3, 2] , [4, 6]] y devuelve => [ [3,2] , [4,6] ]             2 filas x 2 columnas.
        entra [3, 2, 4, 6] y devuelve => [3,2,4,6]                          1 filas x 4 columnas ... o 1 columna x 4 filas ;)
        entra [3, [2], 4, 6] y devuelve => [3,2,4,6]                        1 filas x 4 columnas ... o 1 columna x 4 filas ;)


        """
        # Validaciones previas con la dimension... la vuelvo plana por si acaso
        matriz_plana = SttS.aplanar_matriz(matriz=matriz)
        if not matriz_plana: return None 

        b_valid = SttS.es_matriz( matriz = matriz )
        if not b_valid: return None
        """ 
        >>> Calculo la longitud de la dimension de la matriz maxima(por si no es simetrica.) """
        try:
            filas = len(matriz)
            lst_len_matriz = [len(item) for item in matriz]
            columnas = max(lst_len_matriz) if lst_len_matriz else 0
            
            dimension = f'{filas}X{columnas}'       # Saco la dimension
        except Exception as e:
            return None

        """ 
        >>> Creo la nueva matriz uniforme """
        try:        
            # Creo una fila de columnas para rellenar los huecos
            lst_max_columna = [i for i in range(columnas)]

            # hago la matriz de entrada uniforme y relleno los vacios con el valor Inicial fila x fila 
            for i  in range(len(matriz)):
                matriz[i] = SttS.igualar_listas(lista_keys = lst_max_columna, lista_to_relong = matriz[i], valor_relleno = Celda.VALOR_INICIAL)
        except Exception as e:
            return None
        
        # Retorno ....la matriz recuadrada a su columna maxima
        return matriz
    
    @staticmethod
    def dimensiones_by_matriz(dato):
        """ Entra un dato y devuelve sus filas , columnas y dimension
        ■ Si MATRIZ, devulve las filas = n , columnas = m y dimension ( nXm )
        ■ Si LISTA,  devuleve    filas = 1 , columnas = n y dimension ( 1Xcolumnas )
        ■ Si OTRO,   devuelve    filas = 1 , columnas = 1 , dimension = 1x1
        """
        try:
            if isinstance(dato, list):
                if SttS.es_matriz(matriz=dato):
                    """ ES MATRIZ """
                    matriz_cuadrada = SttS.encuadrar_matriz(matriz=dato)
                    filas = len(matriz_cuadrada)
                    columnas = len(matriz_cuadrada[0])
                    dimension = f'{filas}X{columnas}'
                else:
                    """ ES LISTA HORIZONTAL"""
                    filas = 1
                    columnas = len(dato)
                    dimension = f'{filas}X{columnas}'
            else:
                """ ES DATO """
                filas = 1
                columnas = 1
                dimension = f'{1}X{1}'
            
            return filas, columnas, dimension
        except Exception as e:
            return False

# ███████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████

                                        # -   C E L D A   -  

# ███████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████

# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
class Celda():
    """ >>> Clase que Define una Celda como el cruce entre una FILA y una COLUMNA.
    CONTIENE OPERACIONES ELEMENTALES SOBRE UNA CELDA: SUMAR FILAS, SUMAR COLUMNAS Y 
    PROPIEDADES COMO LETRA O VALOR. 
    """
    VALOR_INICIAL = ''
    
    def __init__(self, valor = None , **kwargs):
        """ >>> Crea una celda y le asigna un valor de inicio.
        [fila](int):  Fila de la celda.
        [columna](int/str): 
        [valor]:
        Retorno:            
        >>> ej: Celda(fila=3, columna=0, valor = 'Hola') => pone el valor 'Hola' sobre la celda A:2
        >>> ej: Celda(celda="A:2" , valor = 'Hola')      => pone el valor 'Hola' sobre la celda A:2
        >>> ej: Celda(celda='A:2') => Pone el valor '' sobre la celda A:2
        
        """     
        # ▄▄▄▄▄▄▄▄▄▄  Establece los dicc validos para columna: letra:numero y numero:letra
        SttS.inicializa_diccs_letra_numero()

        # ▄▄▄▄▄▄▄▄▄▄  RECOGE LOS VALORES DE FILA , COLUMNA  O CELDA.
        self.fila = kwargs.get('fila', None)
        self.columna = kwargs.get('columna', None)
        self.nombre_celda = kwargs.get('celda', None)
        self.letra = ''
        
        # ▄▄▄▄▄▄▄▄▄▄  EVALUA EL RESULTADO
        if self.nombre_celda == None and self.fila == None and self.columna == None: 
            return None
        
        elif self.nombre_celda != None:             # Si entra una celda, la descompone en fila y columna y lo Prioriza sobre fila y columna en caso de querer meter tb esos valores.
            try:
                self.fila, self.columna = SttS.fc_by_celda(celda=self.nombre_celda)   # devuelve los valores abs de fila y columna o None, None
                if self.fila == None or self.columna == None: 
                    return None
                self.letra = SttS._may_nl[self.columna]      # Paso a letra
            except Exception as e:
                print(f'Error __init__ Celda :::: {e}')
                return None
        elif self.fila != None and self.columna != None:        # Si entra fila y columna, calculo la celda
            try:
                self.fila = abs(self.fila)                
                """ 
                Trabajamos con la  c o l u m n a ... pq puede venir como letra o como numero. """
                if isinstance(self.columna, str):           # E n t r a   u n a   l e t r a 
                    if isdigit(self.columna):               # E n t r a   u n a   n u m e r o  e n   s t r i n g
                        self.columna = abs(self.columna)
                        self.letra = SttS._may_nl[self.columna]      # Paso a letra...y mayusculas
                    else:
                        self.columna = self.columna.upper()         # Paso a mayusculas
                        self.letra = self.columna                   # Paso a letra
                        self.columna = SttS._may_ln[self.letra]      # Paso a numero
                
                elif isinstance(self.columna, int):         # E n t r a   u n   n u m e r o
                    self.columna = abs(self.columna)        # Paso a natural
                    self.letra = SttS._may_nl[self.columna]      # Paso a letra
                
            except Exception as e:
                print(f'Error __init__ Celda :::: {e}')
                return None
        else:
            print(f'Error __init__ Celda :::: Entrada de datos erronea :::: {e}')
            return None

        # ▄▄▄▄▄▄▄▄▄▄  v a l o r    
        if valor is None:
            valor = self.__class__.VALOR_INICIAL        
        self.valor = valor
        # ▄▄▄▄▄▄▄▄▄▄  Celda en formato 'A:0' 
        self.nombre_celda = f"{self.letra}:{self.fila}"

    def __str__(self):
        return f"{self.nombre_celda} = {self.valor}"
        
    def get_fila(self):
        return self.fila if self.fila else 0
    def get_columna(self):
        return self.columna if self.columna else 0
    def get_letra(self):
        return self.letra if self.letra else ''
    def get_nombre_celda(self):
        return self.nombre_celda if self.nombre_celda else ''
    def get_valor(self):
        return self.valor 
    def set_valor(self, valor, b_iter_to_str:bool=True):
        """ >>> Establece el valor de la celda y lo guarda en el diccionario celda:valor.
        [valor]: El valor a establecer en la celda.
        [b_iter_to_str]: Si es True, convierte el valor a string antes de guardarlo... int, list, dict, objetos, ....
        >>> Si quieres guardar un objeto(por ejemplo) debes poner False(guardarlo exactamente).
        ej: celda.set_valor(10, b_iter_to_str=False) => Guarda el 10 como int y no como str.
        ej: celda.set_valor(10, b_iter_to_str=True)  => Guarda el 10 como str.
        ej: celda.set_valor(10) => Guarda el 10 como str ( '10' ).
        """
        # if isinstance(valor, iterator):
        if isinstance(valor, str) or isinstance(valor, list) or isinstance(valor, tuple) or isinstance(valor, set) or isinstance(valor, dict):
            if isinstance(valor, str):
                self.valor = valor
            else:
                if b_iter_to_str == True:
                    self.valor = str(valor)
                else:
                    self.valor = valor
        else:
            self.valor = valor
        return self.valor

    # SUMA UNA FILA A UNA CELDA y DEVUELVE LA CELDA RESULTANTE
    def sumar_filas(self, filas:int = 1, b_copy_value = False):
        """ >>> Suma/O resta una cantidad de filas a una celda y devuelve la celda resultante 
        >>> No Transforma la celda en la que está, sino que crea una nueva celda con la suma de filas.
        >>> Hace validacion de que la fila no se pase de los limites de las filas posibles. 
            Si te pasas por abajo, lo deja en Zero(0)
            Por arriba no hay límite de filas....de momento.
        """
        try:
            new_fila = self.fila + filas
            if new_fila < 0: new_fila = 0   # las filas o tienen límite por arriba
            
            new_celda = f"{self.letra}:{new_fila}"
            if b_copy_value == True:
                return Celda(celda=new_celda , valor=self.valor)
            else:
                return Celda(celda=new_celda, valor=Celda.VALOR_INICIAL)            
        except Exception as e:
            print(f'Error suma_filas :::: {e}')
            return None
    
    def sumar_columnas(self, columnas:int = 1, b_copy_value = False):
        """ >>> Suma(o resta) una cantidad de columnas a una celda y devuelve la celda resultante 
        >>> No Transforma la celda en la que está, sino que crea una nueva celda con la suma de columnas.
        >>> Hace validacion de que la columna no se pase de los limites de las columnas posibles. 
            Si te pasas por abajo, lo deja en Zero(0)
            Si te pasas por arriba, lo deja en el máximo de columnas posibles=>(702)=>(len(SttS._may_ln))
        """
        try:
            new_columna = self.columna + columnas
            if new_columna < 0: 
                new_columna = 0                                         # limite por abajo
            if new_columna >= len(SttS._may_ln): 
                new_columna = len(SttS._may_ln) - 1    # limite por arriba

            new_celda = f"{SttS._may_nl[new_columna]}:{self.fila}"
            if b_copy_value == True:
                return Celda(celda=new_celda , valor=self.valor)
            else:
                return Celda(celda=new_celda, valor=Celda.VALOR_INICIAL)            
        except Exception as e:
            print(f'Error suma_columnas :::: {e}')
            return None
    
    def sumar_fc(self, filas:int, columnas:int, b_copy_value:bool = False):
        celda_suma_fila = self.sumar_filas(filas = filas, b_copy_value = b_copy_value)
        if not celda_suma_fila: return None
        celda_resultado = celda_suma_fila.sumar_columnas(columnas = columnas, b_copy_value = b_copy_value)
        return celda_resultado if celda_resultado else None

    @staticmethod
    def numero_columna(columna):
        # ES UNA LETRA??
        numero_columna = SttS.letra_to_numcol(letra=columna)           
        if numero_columna == None:
            # NO ES UNA LETRA.... SERÁ UN NÚMERO??
            try:
                numero_columna = abs(int(columna))
                return numero_columna
            except Exception as e:
                # NO ES NI UNA LETRA VALIDA NI UN NUMERO.
                return None
        else:
            return numero_columna
        
# ███████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████
""" 
                                        -  R A N G O  -  
"""
# ███████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████
# ============================================================================================
# Rango no hereda ni usa tablero para establecerse. 
# Rango es una clase que se instancia en Tablero en una lista o en un diccionario .... ya veremos
# Tablero es quien gestiona Rango a través de su lista de rangos.
# ============================================================================================
# Rango es un concepto. una dimension con un inicio y un final y sobre todo ...UN NOMBRE
# Rango es un diccionario de informacion de una estructura cuadrada 2x2 o rectangular 3x2 o 2x3 .... CONTINUA
# Esa informacion del diccionario de Rango(data) es la que se usará en tablero para almacenar los rangos que se quieran crear en una lista o diccionario....veremos :)
# De esta manera tablero puede acceder a sus rangos guardados y usar la lógica para crear operaciones complejas con los rangos en terminal.
# ============================================================================================
""" 
Para expresarme regularmente """
import re

"""
Enumeracion Que define que tipos de rango puede haber: 
de celda, de fila, de columna , de cuadrado, de rectangulo"""
from enum import Enum as TypeRng
class Type_Rng(TypeRng):    
    CELDA = 0 
    FIL = 1
    COL = 2
    CUADR = 3
    RECTG = 4    

from enum import Enum as TYPEIMPR
class TYPE_PRINT(TYPEIMPR):
    LITERAL = 0
    MOSAICO = 10
    MAX_SSP = 20
    MAX_CSP = 30
    FIXED_SSP = 40
    FIXED_CSP = 50
    LIST_LITERAL = 60
    LIST_MOSAICO = 70
    LIST_FIXED_SSP = 80
    LIST_FIXED_CSP = 90
    LIST_MAX_SSP = 100    
    LIST_MAX_CSP = 110


# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# >>> Con la celda de inicio[C:2] y la dimension(3x4) ( o celda fin[H:8] ) tenemos todos los datos para crear un rango......
class Rango(Celda):
    """ Clase que crea un Rango. Que Qué es un rango? y tu lo pregutas...
    Un rango es una coleccion de datos. Equiparacion con celdas.... información. 
    Contiene como variables fundamentales la variable data, dicc, matriz, 
    b_ghost==True cambia el funcionamiento del rango y pasa de tener reflejo inmediato a ser un objeto virtual.    
    """
    def __init__(self, nombre_rango, celda_inicio:str = 'A:0', dimension:str = "1x1", valor_default='' ,  b_oculto = False, b_ghost=False):
        """
        Inicializa un rango con información sobre celdas de inicio y fin, dimensiones y más.
            nombre_rango (str): Nombre del rango.
            celda_inicio (str): Celda inicial en formato 'Letra:Fila' (e.g., 'A:0').
            dimension (str): Dimensiones en formato 'FilasxColumnas' o celda final (e.g., '1x1', 'C:3').
        Retorno:
            None: Configura las propiedades del rango, como 'data', 'dicc' y valores derivados.
        Ejemplo:
            >>> rango = Rango(nombre_rango="Ejemplo_1", celda_inicio="B:2", dimension="3x4")
            >>> rango = Rango(nombre_rango="Ejemplo_2", celda_inicio="B:2", dimension="D:5")
            >>> print(rango.data)
            {'nombre': 'Ejemplo', 'fila_inicio': 1, 'columna_inicio': 1, ...}

            
            
            >>> rango = Rango(nombre_rango='x',celda_inicio='A:0',dimension=None, valor_default='[[1,2][3,4][5,6]]'
        """  

        # VALIDACION INICIAL
        if not isinstance(dimension, str): return None
        fila, columna = SttS.fc_by_celda( celda = celda_inicio )        # valida que celda se introduce con el formato correcto.
        if fila == None or columna == None: return None

        super().__init__( celda = celda_inicio )
        """ >>> C e l d a   d e   i n i c i o  Rango se define como una celda de Inicio y a partir de ahora le sumamos cosas
        """         

        # >>> DIMENSION  Puede venir como una celda de fin(AX:9) o como una dimension(3x4)  
        self.total_filas, self.total_columnas = self.__desempaqueta_dimension(dimension=dimension)  
        if self.total_filas == None or self.total_columnas == None: 
            print(f"Error en dimension: {dimension}")
            return None        
        
        """ >>> CELDA FIN  ... (a partir de celda_inicio y dimension) ...Esto define un rango. ahora hay que capturar las celdas implicadas y los valores de cada celda""" 
        celda_fin = self.__get_str_celda_fin(total_filas = self.total_filas , total_columnas = self.total_columnas)        
        if not celda_fin: 
            print("Error en la creacion de la Celda Fin")
            return None

        # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ CREACION DE CELDA FIN DEL RANGO.
        self.celda_fin      = Celda(celda = celda_fin)
        
        # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ LISTA DE LAS CELDAS IMPLICADAS
        self.lst_celdas = self.__get_list_celdas()                       
        """ >>> LISTA DE OBJETOS CELDA  """

        # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ CREACION DE CELDA INICIO DEL RANGO A PARTIR DE LST_CELDAS (para no autoReferenciarme y crear una celda de inicio de la que soy heredera.)
        self.celda_inicio   = self.lst_celdas[0]      

        # ASIGNO LAS  P R O P I E D A D E S                
        self.nombre = nombre_rango                
        self.total_celdas   = self.total_filas * self.total_columnas        
        self.es_numerico = False
        self.flag = ''          
        self.family = ''  
        self.b_oculto = b_oculto    
        """ >>> Si no quieres que se vea en self.ver_rango con rango a None (ver Todos) 
            sirve para marcar el primer rango ('Tabero') como oculto... es todo el panel y son muchos valores que mostraar. así es mas agíl.
            con las filas pasa parecido.....en Brackets
        """                                    
        self.b_ghost = b_ghost      
        """ >>> True, no se copia de tablero directamente al crear el rango (es virtual, para operar) 
                False, se crea y se copian los valores de tablero.         """
        pass       
        self.b_print_cabecera = True
        """ >>> True(byDef) Indica que se tienen que imprimir las cabeceras en __str__  y False que se imprimen por fuera.
        """        

        # ESTABLECE LA MATRIZ:
        self.matriz = self.__get_matriz()
        if not self.matriz: return None
        
        # VALOR INICIO ... puede ser una lista, una matriz, un str, int, bool...
        self.valor_default = None
        if isinstance(valor_default , list) or isinstance(valor_default, tuple) or isinstance(valor_default, set):
            self.__push_plana(data_push = valor_default, relleno = valor_default)
            self.valor_default = Celda.VALOR_INICIAL
        else:
            self.iniciar(valor=valor_default)        
            self.valor_default = valor_default

        pass

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    # Info del Rango
    def __str__(self):
        """Devuelve una representación legible del diccionario de datos.
        """
        titulos = ["Rango", "Inicio", "Fin", "Total Celdas", "Filas", "Columnas", "Es Oculto", "Ghost"]
        
        # TAMAÑOS DE LAS COLUMNAS: cte. Sirve para dar la info por terminal.
        tamanos_columnas = [25, 10, 10, 15, 8, 10, 10, 10]
        
        # VALORES DE LAS COLUMNAS
        valores = [
            self.nombre ,
            self.celda_inicio.nombre_celda ,
            self.celda_fin.nombre_celda ,
            self.total_celdas ,
            self.total_filas ,
            self.total_columnas ,
            self.b_oculto ,
            self.b_ghost                
        ]
        # PREGUNTA SI SE TIENE QUE IMPRIMIR LA CABECERA O NO.
        if self.b_print_cabecera == True:            
            
            # FORMATEO DE NOMBRES DE COLUMNA, TAMAÑOS Y VALORES 
            cabeceras   = "".join([f"{titulo:<{ancho}}" for titulo, ancho in zip(titulos, tamanos_columnas)])
            datos       = "".join([f"{str(valor):<{ancho}}" for valor, ancho in zip(valores, tamanos_columnas)])
            
            # RESULTADO FINAL
            return f"{cabeceras}\n{'-' * sum(tamanos_columnas)}\n{datos}"
        else:
            datos = "".join([f"{str(valor):<{ancho}}" for valor, ancho in zip(valores, tamanos_columnas)])
            return f"{datos}"  
    
    # VISUALIZA LOS NOMBRES DE LAS CELDAS EN FORMATO MATRIZ.
    def ver_matriz(self):
        """ >>> Muy basico, sirve para ver el nombre de las celdas en su posicion matricial. """
        if not self.matriz: return None
        for fila in self.matriz:
            for celda in fila:
                print(celda.nombre_celda, end=' '*4)
            print()
        pass

    # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
    def iniciar(self, valor=Celda.VALOR_INICIAL):
        """ ■ INICIALIZA LOS VALORES DEL TABLERO CON UN VALOR DE ENTRADA O '-'  - over tablero -  
        """
        try:
            for celda in self.lst_celdas:
                celda.valor = valor
        except Exception as e:
            print(f'Error iniciar :::: {e}')
            return 
    
    # ██ DESDE UN DATO QUE PUEDE SER str, list, matriz, int, bool CREO UN RANGO
    # ██ ES LA BASE DE PUSH. PUSH CONVIERTE EL DATO EN RANGO Y EL RANGO LO METE EN EL TABLERO CRUZANDO CELDAS con (self.cross().
    def rangutan(self, data_push, celda_inicio, b_lineal:bool=False, eje:str='X', b_repetir:bool=False):
        """
        ■■■■■■■■■ DESDE UN DATO CREO UN RANGO ■■■■■■■■■ 
        CREA UN RANGO CON data_push EN CELDA_INICIO, LO FORMATEA SEGUN  b_lineal, eje y repetir. 
        
        [data_push](any, matriz): LOS DATOS PUEDEN SER TIPOS PYTHON, ITERADORES(LIST, TUPLE, SET), MATRICES.
        [celda_inicio](Objeto Celda) Celda de inicio del Rango donde se va a introducir data_push. 
                                     Entra como objeto para tener acceso a filas y columnas para formar las dimensiones para el Rango.
        ■■  'eje' = 'X' o 'Y'  ■ solo en caso de que data_push sea list.
        ■■  'b_repetir': True, False ■ solo en caso de que data_push sea str 
        ■■  b_lineal: True, si se hace el cruce lineal (como vengan las celdas en linea)(self.__push_plana)
                      False(byDef), Si el cruce Celda a Celda coincidente(self.cross())
                                        
                    En caso de que data_push sea un str, se puede introducir:
                    'H' para b_repetir data_push horizontalmente celda_inicio hasta fin linea
                    'V', para b_repetir data_push verticalmente  desde celda_inicio hasta fin columna.

        • LOS ARGUMENTOS ( excepto data_push ) VIENEN VALIDADOS DE self.push().
        • CREO UN OBJETO ■ Rango  CON ■ data_push CON ■ celda_inicio  COMO PRIMERA CELDA DEL RANGO.
        • EN EL RANGO SIEMPRE SE METEN LOS DATOS DE FORMA PLANA.
        ENTONCES LO QUE HAGO ES JUGAR CON LAS ■ DIMENSIONES  PARA CONTROLAR COMO ENTRAN LOS DATOS EN EL RANGO. 
        • PARA MATRICES, A VECES, HAY QUE HACER RELLENOS, QUE SE HACEN CON self.valor_default
        • HAY 10 TIPOS DE OBJETOS RANGOS DISTINTOS QUE SE PUEDEN FORMAR:
         █ 1-MATRIZ_LINEAL  █ 2-MATRIZ_CUADRADA     █ 3-RANGO-RANGO             █ 4-LISTA_VERTICAL      █ 5-LISTA_HORIZONTAL 
         █ 6-STR_CELDA      █ 7-STR_REPETIDO_FILA   █ 8-STR_REPETIDO_COLUMNA    █ 9-STR_TO_LISTAWORDS   █ 10-X_TO_CELDA (int, float, bool,...)
        """
        
        # ■■ PRIMERO BUSCAMOS SI ES UNA MATRIZ U OTRO TIPO DE DATO.
        es_matriz = SttS.es_matriz( matriz = data_push )
        
        # ■■ EVALUAMOS EL TIPO        
        if not es_matriz: 
            # NO ES MATRIZ...SEGUIMOS BUSCANDO ... puede ser iterador / str / Rango / int, bool, float...
            if isinstance(data_push, list) or isinstance(data_push, tuple) or isinstance(data_push, set):                
                # ITERADOR. Si es Iterador ENTRA PLANO SI O SI... sobre el eje X o el eje Y 
                if eje == 'X':
                    """ ■■■■ (By Def) PREPARA LA DIMENSION PARA LA ■ LISTA HORIZONTAL   """
                    dimension = f'1x{len(data_push)}'
                elif eje == 'Y':
                    """ ■■■■ PREPARA LA DIMENSION PARA LA ■ LISTA VERTICAL   """                    
                    dimension = f'{len(data_push)}X1'
                # SE CREA UN RANGO CON LA LISTA COMO VALOR INICIAL
                rango = Rango( nombre_rango = "rango_aux" , celda_inicio = celda_inicio.nombre_celda , dimension = dimension , valor_default = data_push )                

            elif isinstance(data_push, str):                
                """ ■■■■■ METE data_push COMO UNA CADENA(O CHAR). """                    
                data_push = str(data_push)
                if b_lineal == False:           
                    # ■■■ ES STR ....Repetir o sólo Insertar?
                    if b_repetir == False:        # (byDef)

                        # ███ (By Def) CADENA TO CELDA_INICIO
                        rango = Rango( nombre_rango = "rango_aux" , celda_inicio = celda_inicio.nombre_celda , dimension = f'1X1' , valor_default = data_push )                

                    elif b_repetir == True:       # ■■ repetir el str. preguntar por eje = ['X','Y'] para saber si Horizontal(Fila) o Vertical(Columna)                        
                        if eje != None:                            
                            if str(eje).upper() == 'X':                                
                                # ■ Repetir en el eje HORIZONTAL
                                dimension = f'1x{self.total_columnas - celda_inicio.columna}'  # PREPARA LA DIMENSION PARA b_repetir DESDE CELDA_INICIO EN HORIZONTAL.
                            elif str(eje).upper() == 'Y':
                                # ■ Repetir en el eje VERTICAL
                                dimension = f'{self.total_filas - celda_inicio.fila}X1'        # PREPARA LA DIMENSION PARA b_repetir DESDE CELDA_INICIO EN VERTICAL.
                            pass
                            rango = Rango( nombre_rango = "rango_aux" , celda_inicio = celda_inicio.nombre_celda , dimension = dimension , valor_default = data_push )                
                        else:   
                            """ ■■ SIN eje ==> Al no meter eje pero si Repetir toma el eje X por defecto """
                            dimension = f'1x{self.total_columnas - celda_ini.columna}'  # PREPARA LA DIMENSION PARA b_repetir DESDE CELDA_INICIO EN HORIZONTAL.
                            rango = Rango( nombre_rango = "rango_aux" , celda_inicio = celda_inicio.nombre_celda , dimension = dimension , valor_default = data_push )                
                
                elif b_lineal == True:   
                    """  ■■■■ METE LA CADENA COMO SI FUERA UNA LISTA A PARTIR DE LA CELDA DE INICIO CHAR A CHAR. """                    
                    lst_chars = [c for c in data_push]
                    if not lst_chars: return None
                    
                    # PREUNTO POR EL eje PARA COLOCAR LA LISTA HORIZONTAL(eje X) O VERTICAL(eje Y)                    
                    dimension = f'1x{len(lst_chars)}'        # PONGO HORIZONTAL POR DEFECTO
                    if eje == 'Y':
                        dimension = f'{len(lst_chars)}X1'    # Y SI LO TENGO QUE CAMBIAR A VERTICAL PUES LO CAMBIO.                        

                    rango = Rango( nombre_rango = "rango_aux" , celda_inicio = celda_inicio.nombre_celda , dimension = dimension , valor_default = lst_chars )                
            
            elif isinstance(data_push, Rango):
                """ ■■■■ ENTRA UN RANGO!! """                
                dimension       = data_push.get_dimension()
                valor_default   = data_push.get_valores()

                rango = Rango( nombre_rango = "aux_rango" , celda_inicio = celda_inicio.nombre_celda , dimension = dimension , valor_default = valor_default )
            else:
                """ ■■■■ EL RESTO: int, float, bool, objetos, date, time, .... """
                # ■■ SI HAY ALGUNA CELDA EN LA LISTA DE CELDAS QUE COINCIDA CON LA CELDA DE ENTRADA
                if any(celda_inicio.nombre_celda in celda_lst.nombre_celda for celda_lst in self.lst_celdas):
                    rango = Rango( nombre_rango = "aux_other" , celda_inicio = celda_inicio.nombre_celda , dimension = '1x1' , valor_default = data_push )                                    
        else:
            """ ■■■■ ES MATRIZ ■■■■
                ■■■■ Si datapush == MATRIZ::: NI ■ b_repetir NI ■ eje TIENEN EFECTO, solo ■ b_lineal  """
            if b_lineal == True:    
                # ■■ METE LOS DATOS EN LA MATRIZ DE FORMA PLANA(Uno detras de otro sin tener en cuenta la estrucutra, de izquierda a derecha)
                # ■ CREO UNA MATRIZ CUADRADA DEPENDIENDO DEL MAXIMO NUMERO DE COLUMNAS QUE TENGA LA MATRIZ ENTRANTE...xa sacar la columna mas grande.
                matriz_cuadrada = SttS.encuadrar_matriz(matriz = data_push)   
                if not matriz_cuadrada: return None
                
                # APLANO LA MATRIZ PARA OBTENER LA LISTA DE DATOS DE IZQUIERDA A DERECHA
                lst_plana = SttS.aplanar_matriz(matriz = data_push)   
                if not lst_plana: return None

                # ■ SACO LAS COLUMNAS COMO BASE PARA CALCULAR LAS FILAS                
                columnas = len(matriz_cuadrada[0])

                # ■ SACO LOS DATOS QUE NECESITO DE LA MATRIZ RE-CREADA PARA CREAR UN RANGO CUADRADO
                matriz_resultado = []  # Matriz vacía
                for seq, data_plana in enumerate(lst_plana):
                    fila = seq // columnas      # Calcular la fila
                    columna = seq % columnas    # Calcular la columna
                    # Si la fila no existe aún, la creamos
                    if fila >= len(matriz_resultado):
                        matriz_resultado.append([])
                    # Insertamos el valor en la fila correspondiente
                    matriz_resultado[fila].append(data_plana)

                if not matriz_resultado:
                    print(f'Error ::: rangutan ::: matriz resultado ')
                    return None
                
                # ■ DIMENSION
                dimension = f'{len(matriz_resultado)}X{len(matriz_resultado[0])}'

                # ■ CREO EL RANGO
                rango = Rango( nombre_rango = "rango_aux" , 
                                celda_inicio = celda_inicio.nombre_celda , 
                                dimension = dimension , 
                                valor_default = matriz_resultado )
                
                # ■ VALIDO LIMITES DEL RANGO
                retorno = self.es_rango_in(rango=rango)
                if not retorno: 
                    print("Error Logico ::: Limites ")
                    return None
            else:            
                """ ■■ QUIERO METER LOS DATOS CON LA ESTRUCTURA DE MATRIZ CON LA QUE VIENE. """
                # ■ CREO UNA MATRIZ CUADRADA DEPENDIENDO DEL MAXIMO NUMERO DE COLUMNAS QUE TENGA LA MATRIZ ENTRANTE
                matriz_cuadrada = SttS.encuadrar_matriz(matriz = data_push)        
                # ■ SACO LOS DATOS QUE NECESITO DE LA MATRIZ RE-CREADA PARA CREAR UN RANGO CUADRADO
                filas = len(matriz_cuadrada)
                columnas = len(matriz_cuadrada[0])
                dimension = f'{filas}X{columnas}'
                try:
                    # ■ CREO EL RANGO CUADRADO
                    rango = Rango( nombre_rango = 'rango_aux' , celda_inicio = celda_inicio.nombre_celda , dimension = dimension , valor_default = matriz_cuadrada )            
                    if not rango: 
                        return None

                    # ■ VALIDO LIMITES DEL RANGO
                    retorno = self.es_rango_in(rango=rango)
                    if not retorno: 
                        print("Error Logico ::: Limites ")
                        return None
                except Exception as e:
                    print(f'Error ::: Tablero ::: push ::: {e}')
                    return None

        # ■■ RETORNO ■■ 
        return rango if rango else None

    # ██ OBTIENE LA DIMENSION DE UN DATO DE ENTRADA QUE PUEDE SER STR, LIST, SET, TUPLE, MATRIZ, INT, BOOL...
    # ██ CUANDO OBTIENES LA DIMENSION, PUEDES CREAR EL TABLERO, UN RANGO, UN FRANKY.HEAD....
    def get_dimension_data_push(self, data_push, b_lineal:bool=False, eje:str='X', b_repetir:bool=False):
        """ Entra un dato en los tipos de dato: (str, int, boolean, list, set, tuple, matriz) y devuelve la DIMENSION  
        """
        # INICIALIZO EL RETORNO
        dimension:str = None        
        # ■■ PRIMERO BUSCAMOS SI ES UNA MATRIZ U OTRO TIPO DE DATO.
        es_matriz = SttS.es_matriz( matriz = data_push )        
        # ■■ EVALUAMOS EL TIPO        
        if not es_matriz:                                   # NO ES MATRIZ...SEGUIMOS BUSCANDO            
            if (isinstance(data_push, list) or              
                isinstance(data_push, tuple) or             # ■■ SI ES ITERADOR ENTRA PLANO SI O SI, PUEDE SER AL eje X O AL eje Y.
                isinstance(data_push, set)):                                
                
                if str(eje).upper() == 'X':      # ■■ (By Def) PREPARA LA DIMENSION PARA LA ■ LISTA HORIZONTAL                      
                    dimension = f'1x{len(data_push)}'
                elif str(eje).upper() == 'Y':    # ■■ PREPARA LA DIMENSION PARA LA ■ LISTA VERTICAL                                          
                    dimension = f'{len(data_push)}X1'
            
            elif isinstance(data_push, str):                # ■■ METE data_push COMO UNA CADENA(O CHAR).                                    
                if b_lineal == False:           

                    # ■■ ES TRATADO COMO UN STR NORMAL. Ahora veo si se debe b_repetir o si sólo se coloca en el tablero una vez.
                    if b_repetir == False:        # ■■ (By Def) CADENA TO CELDA_INICIO                        
                        dimension = f'1X1'

                    elif b_repetir == True:     # ■■ b_repetir LA CADENA O CARACTER. Ahora hay que preguntar por eje = ['X','Y'] para saber si Horizontal(Fila) o Vertical(Columna)
                        if eje != None:                            
                            if str(eje).upper() == 'X':         # ■■■■■ CON eje HORIZONTAL
                                dimension = f'1x{self.total_columnas - celda_inicio.columna}'  # PREPARA LA DIMENSION PARA b_repetir DESDE CELDA_INICIO EN HORIZONTAL.
                            
                            elif str(eje).upper() == 'Y':       # ■■■■■ CON eje VERTICAL
                                dimension = f'{self.total_filas - celda_inicio.fila}X1'        # PREPARA LA DIMENSION PARA b_repetir DESDE CELDA_INICIO EN VERTICAL.
                        else:       # ■■■■■ SIN eje ==> Al no meter eje pero si Repetir toma el eje X por defecto                            
                            dimension = f'1x{self.total_columnas - celda_ini.columna}'  # PREPARA LA DIMENSION PARA b_repetir DESDE CELDA_INICIO EN HORIZONTAL.
        else:
            """ ■■■■ ES MATRIZ ■■■■  """
            # QUIERO METER LOS DATOS A CAPÓN UNO DETRAS DE OTRO SIN ESTRUCTURA.
            # Si entra datapush COMO MATRIZ, no le afecta ni repetir ni eje, unicamente b_lineal.
            # b_lineal = True, se meten los datos planos, de uno en uno
            if b_lineal == True:    # ■■■■ METE LOS DATOS EN LA MATRIZ DE FORMA PLANA                
                # 
                matriz_cuadrada = SttS.encuadrar_matriz(matriz = data_push)   
                if not matriz_cuadrada: return None
                lst_plana = SttS.aplanar_matriz(matriz = data_push)   
                if not lst_plana: return None
                                
                # SACO LOS DATOS QUE NECESITO DE LA MATRIZ RE-CREADA PARA CREAR UN RANGO CUADRADO
                columnas = len(matriz_cuadrada[0])

                matriz_resultado = []       # Matriz vacía
                for seq, data_plana in enumerate(lst_plana):
                    fila = seq // columnas  # Calcular la fila
                    columna = seq % columnas  # Calcular la columna

                    # Si la fila no existe aún, la creamos
                    if fila >= len(matriz_resultado):
                        matriz_resultado.append([])

                    # Insertamos el valor en la fila correspondiente
                    matriz_resultado[fila].append(data_plana)

                dimension = f'{len(matriz_resultado)}X{len(matriz_resultado[0])}'

            else:    # ■■■■ QUIERO METER LOS DATOS EN LA FORMA DE MATRIZ TAL COMO VIENE                                
                # CREO UNA MATRIZ CUADRADA DEPENDIENDO DEL MAXIMO NUMERO DE COLUMNAS QUE TENGA LA MATRIZ ENTRANTE
                matriz_cuadrada = SttS.encuadrar_matriz(matriz = data_push)        
                if not matriz_cuadrada: return None
                # SACO LOS DATOS QUE NECESITO DE LA MATRIZ RE-CREADA PARA CREAR UN RANGO CUADRADO
                filas = len(matriz_cuadrada)
                columnas = len(matriz_cuadrada[0])
                dimension = f'{filas}X{columnas}'

        # ■■ RETORNO ■■ 
        return dimension if dimension else None

    # ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    #                                       GETTING
    # •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    # CREA Y DEVUELVE LA MATRIZ DE self.lst_celdas. FUNDAMENTAL PARA LA CREACION DE self.matriz
    def __get_matriz(self):
        """ >>> DEVUELVE UN RANGO EN FORMA DE LISTA DE LISTAS DONDE CADA ITEM ES UN OBJETO CELDA
        """
        if not self.lst_celdas: return None
        lst_matriz = [] 
        for i in range(self.total_filas):
            lst_fila = []            
            for j in range(self.total_columnas):
                nombre_celda = SttS.celda_by_fc( fila = self.fila + i, columna = self.columna + j )
                celda = self.buscar_celda( nombre_celda = nombre_celda )
                if not celda: return None
                lst_fila.append(celda)
            pass
            lst_matriz.append(lst_fila)
        pass
        return lst_matriz if lst_matriz else None
    
    # UNA FUNCION PARA REUNIRLAS A TODAS, UNA FUNCION UNICA DE PODER....
    def getting(self, fila:int=None, columna=None, celda:str='', b_valor:bool=False, **kwargs):
        """ ■■■■■■ LA FUNCION PARA OBTENER COSAS DEL RANGO ■■■■■■ 
        
        ■■ [kwargs](dict) 'fila_to'(int) , 'columna_to'(int)

        ■ LAS COSAS QUE SE PUEDEN OBTENER SON: celdas, filas, columnas, matriz, TANTO EN VALORES COMO EN CELDAS.
        
        ■ ejemplo: TABLERO.getting(fila=3, columna=2, b_valor=True)   => OBTIENE EL VALOR DE L FILA 3 , COLUMNA 2
        ■ ejemplo: TABLERO.getting(celda='C:3', b_valor=True)         => OBTIENE EL VALOR DE LA CELDA C:3
        ■ ejemplo: TABLERO.getting(fila=3, b_valor=True)              => OBTIENE EL VALOR DE LA FILA 3    EN FORMA DE LISTA
        ■ ejemplo: TABLERO.getting(columna=3, b_valor=True)           => OBTIENE EL VALOR DE LA COLUMNA 3 EN FORMA DE MATRIZ
        ■ ejemplo: TABLERO.getting(columna=3, columna_to=5,  b_valor=True)    => OBTIENE EL VALOR DE LA COLUMNA 3 A LA 5 EN FORMA DE MATRIZ.
        ■ ejemplo: TABLERO.getting(fila=3, fila_to=5,  b_valor=True)          => OBTIENE EL VALOR DE LA FILA 3 A LA 5 EN FORMA DE MATRIZ.

        """
        fila_to = kwargs.get('fila_to', None)
        columna_to = kwargs.get('columna_to', None)        
        pass
        if celda != '':
            """ ••• CELDA 
            """
            celda = self.get_celda(nombre_celda = celda, b_valor=False)
            if celda:
                if b_valor==True:
                    return celda.valor
                else:
                    return celda

        elif fila != None and columna != None:
            """ XXX CELDA ••• FILA ••• COLUMNA >>> CELDA 
            """
            celda = self.get_celda(fila=fila, columna=columna, b_valor=False) 
            if celda != None:
                if b_valor==True:
                    return celda.valor
                else:
                    return celda

        elif fila == None and columna != None:
            """ XXX CELDA XXX FILA  ••• COLUMNA 
            """
            if columna_to != None:
                # ESTO HACE QUE SE PUEDA INTRODUCIR LETRA O NUMERO. Y DEVUELVE NUMERO
                columna_to = Celda.numero_columna(columna=columna_to)                
                if isinstance(columna_to, int):
                    columna_to = abs(columna_to)
                    if columna > columna_to:
                        # ITERCAMBIO LOS VALORES
                        col_aux = columna
                        columna = columna_to
                        columna_to = col_aux

                else:
                    columna_to = columna

            matriz_columna = self.get_columnas(columna_from = columna, columna_to = columna_to , b_valor = b_valor)
            # RETORNO
            return matriz_columna if matriz_columna else None

        elif fila != None and columna == None:
            """ XXX CELDA ••• FILA XXX COLUMNA  
            """
            if fila_to:
                if isinstance(fila_to, int):
                    fila_to = abs(fila_to)
                    if fila > fila_to:
                        # ITERCAMBIO LOS VALORES
                        fila_aux = fila
                        fila = fila_to
                        fila_to = fila_aux
                else:
                    fila_to = fila
            else:
                fila_to = self.celda_fin.fila
            matriz_fila = self.get_filas(fila_from = fila, fila_to = fila_to , b_valor = b_valor)
            # RETORNO
            return matriz_fila if matriz_fila else None

        elif fila == None and columna == None:
            """ XXX CELDA XXX FILA XXX COLUMNA >>> MATRIZ 
            """
            if b_valor == True:
                return self.get_values()
            else:
                return self.matriz
            pass

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    def get_filas(self, fila_from:int, fila_to:int , b_valor:bool=False):
        """ OBTIENE LAS FILAS CONSECUTIVOS DE UN RANGO EN UNA LISTA """
        if not self.matriz: 
            return None
        if b_valor == False:
            """ ■■ DEVUELVE LAS FILAS DE CELDAS """
            return [ fila  for i, fila in enumerate(self.matriz) if (fila_from <= i <= fila_to) ]
        else:
            """ ■■ DEVUELVE LAS FILAS DE VALORES """
            matriz_valores = []
            for i, fila in enumerate(self.matriz):      # BUSCA EN CADA FILA
                b_match = False
                if fila_from <= i <= fila_to:           # CUANDO ENCUENTRA UNA COINCIDENCIA:
                    b_match = True
                    lst_valores_fila = []
                    for celda in fila:                  
                        lst_valores_fila.append(celda.valor)    # METE TODOS LOS VALORES DE LA FILA EN UNA LISTA...
                    
                if b_match == True:
                    matriz_valores.append(lst_valores_fila)        # Y LA FILA EN UNA LISTA...CON LO QUE SE CREA LA MATRIZ.
            
            # RETORNO
            return matriz_valores if matriz_valores else None
            pass

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    # OBTIENE LAS COLUMNAS FROM - TO DE self.matriz.
    def get_columnas(self, columna_from:int=None, columna_to:int=None, b_valor:bool=False):    
        """ DEVUELVE UNA MATRIZ DESDE LA COLUMNA 'columna_from' HASTA LA COLUMNA 'columna_to'
        [columna_from](int):Columna 'Desde'
        [columna_to](int):  Columna 'Hasta'
        [b_valor](bool): ■ True ► Devuleve el valor de la celda. ■ False ► Devuelve la celda.
        Retorno: matriz(lista de listas) de los datos pedidos(celdas o valores)
        """   
        if columna_from == None: columna_from = 0
        if columna_to   == None: columna_to = self.total_columnas
        try:
            columna_from    = abs(int(columna_from))
            columna_to      = abs(int(columna_to))
            
            matriz_valores = []
            for fila in self.matriz:
                lst_valores_columna = []
                for j, celda in enumerate(fila):
                    if columna_from <= j <= columna_to:
                        if b_valor==False:
                            lst_valores_columna.append(celda)           # DEVUELVE LA CELDA.
                        else:
                            lst_valores_columna.append(celda.valor)     # DEVUELVE EL VALOR.

                if lst_valores_columna:
                    matriz_valores.append(lst_valores_columna)

            # Transponer la matriz para devolver columnas
            return [list(col) for col in zip(*matriz_valores)] if matriz_valores else None

        except Exception as e:
            return None

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    # DEVUELVE UNA LISTA DE LOS VALORES EN FORMATO MATRIZ O IMPRIME VALORES BASIC
    def get_values(self, b_print=False):
        """ >>> DEVUELVE UNA LISTA EN FORMATO DE MATRIZ CON LOS VALORES DEL RANGO """
        lst_matriz = []
        for fila in self.matriz:
            lst_fila   = []
            for celda in fila: 
                lst_fila.append(celda.valor)            
            lst_matriz.append(lst_fila)
        
        if b_print == False:
            return lst_matriz
        else:
            # IMPRIME EN FORMATO MAX CSP = 3
            self.imprimir(sp_between=3)            
    
    # OBTIENE UN OBJETO CELDA O UN VALOR CELDA DE UNA CELDA DENTRO DEL RANGO. 
    # PUEDE ENTRAR TANTO NUMERO DE COLUMNA COMO NOMBRE DE COLUMNA. 
    def get_celda(self, b_valor=False , **kwargs):
        """ >>> DEVUELVE UN OBJETO CELDA(b_valor=False) O EL VALOR DEL OBJETO CELDA(b_valor=True) 

        [kwargs]: 'nombre_celda', 'fila' , 'columna'
        >>> ejemplo: get_celda(fila = 1, columna = 3 , b_valor=False)  => correcto , devuelve ■ la celda ■ de la fila 1 columna 3 (C:1)
        >>> ejemplo: get_celda(nombre_celda='C:2' , b_valor=False)      => correcto , devuelve ■ la celda ■ de la celda (C:2)
        >>> ejemplo: get_celda(nombre_celda='C:2' , b_valor=True)      => correcto , devuelve ■ el valor ■ de la celda (C:2)
        >>> ejemplo: get_celda(nombre_celda='C:2' , b_valor=True)      => correcto , devuelve ■ el valor ■ de la celda (C:2)
        Si no existe la celda, la fila o la columna dentro del rango devuelve None

        """
        if not self.lst_celdas: return None
        # RECOGE LOS DATOS         
        nombre_celda = kwargs.get('nombre_celda', None)
        fila         = kwargs.get('fila', None)
        columna      = kwargs.get('columna', None)

        # OPERAMOS
        try:
            if nombre_celda == None:
                if fila == None or columna == None: 
                    return None
                else:
                    fila    = abs(int(fila))
                    # ESTA FUNCION HACE QUE PUEDAS PASAR LA COLUMNA COMO UN NUMERO O COMO UNA LETRA
                    columna = Celda.numero_columna(columna=columna)
                    columna = abs(int(columna))
                    return self.__get_celda_by_fila_columna(fila=fila, columna=columna, b_valor=b_valor)
            else:
                celda = self.buscar_celda(nombre_celda = nombre_celda)
                if not celda:
                    return None
                else:
                    if b_valor == False:
                        return celda
                    else:
                        return celda.valor
        except Exception as e:            
            return None
  
    # DESDE UNA FILA Y COLUMA INT DEVUELVE UNA CELDA O UN VALOR-CELDA.... SIEMPRE QUE ESTÉN EN EL RANGO
    # FUNCION DEDICADA XA self.get_celda()
    def __get_celda_by_fila_columna(self, fila:int, columna:int, b_valor:bool=False):
        """ Entra una fila y columna y devuelve un objeto celda si se encuentra en el rango. 
        [fila](int):
        [columna](int)
        Retorno: None, si no encuentra la celda en el rango independientemente de que pueda crear la celda.
        ejemplo_1:
        """
        celda_aux = Celda(fila=fila, columna=columna)
        if celda_aux:
            # AHORA REPITO PERO EN EL RANGO
            celda = self.buscar_celda(nombre_celda=celda_aux.nombre_celda)
            if not celda:
                """ NO EXISTE EN EL RANGO """
                return None
            else:
                """ SI EXISTE EN EL RANGO """
                if b_valor == False:
                    return celda
                else:
                    return celda.valor
                # return celda
        return None
        pass
    
    # BUSCA UN OBJETO CELDA X SU NOMBRE EN LA LISTA DE CELDAS DEL RANGO
    # AQUI HUBIERA METIDO UN ANY , PERO POR VARIAR ;)
    def buscar_celda(self, nombre_celda:str):
        for celda in self.lst_celdas:
            if nombre_celda == celda.nombre_celda:
                return celda
        return False
        
    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    # G E T T E R ' S   A N D   S E T T E R ' S    
    def get_oculto(self):                               # oculto,   para ver. no para buscar.
        if isinstance(self.b_oculto, bool):
            return self.b_oculto
        else:
            self.b_oculto = False
            return self.b_oculto
    def set_oculto(self, valor:bool=True):
        self.b_oculto = valor
    def get_ghost(self):                                # Ghost
        return self.b_ghost
    def set_ghost(self, valor:bool):
        self.b_ghost = valor
    def get_flag(self):                                 # Flag
        return self.flag
    def set_flag(self, valor:str):
        self.flag = valor
    def get_family(self):                               # Family
        return self.family
    def set_family(self, valor:str):
        self.family = valor
    def get_dimension(self):
        return f'{self.total_filas}X{self.total_columnas}'
    def get_total_celdas(self):
        return len(self.lst_celdas)
    
    
    # DESEMPAQUETA DIMENSION y  devuelve fila y columna
    def __desempaqueta_dimension(self, dimension:str):
        """ 
        [dimension]  puede ser Celda o dimension
            Si celda: necesita fila_inicio y columna de inicio para calcular la dimension final. 
                >>> dimension_fila = fila_fin - fila_ini + 1 
                >>> dimension_columna = columna_fin - columna_ini + 1 
            Si dimension: Se extraen los valores de la cadena y se devuelve el resultado.
        """
        b_dimension_es_celda=True
        letra_columna = None
        columna = None
        total_columnas = None
        total_filas = None
        
        dimension = dimension.upper()                                               # Para poner la x minuscula.
        if ':' in dimension:
            bi_columna , bi_fila = SttS.desata_binomio(dimension, ':')
            """ dimension como CELDA_FINAL ( M:13 ) hay que transformar esto en una dimension
            """
            try:
                bi_fila:int = int(bi_fila)                                                  
                # Saca el numero de columna de la dimension, que es con lo que se va a calcular la dimension.
                columna:int = SttS.letra_to_numcol(letra = bi_columna)
                if columna == None: 
                    return None, None
                """ 
                Aplica la Formula  """    
                total_filas = int(bi_fila) - self.get_fila() + 1
                total_columnas = int(columna) - self.get_columna() + 1

                # Valida que la columna fin sea mayor que la columna inicio. y que la fila fin sea mayor que la fila inicio.
                if total_filas < 0 or total_columnas < 0:
                    return None, None
            except Exception:
                return None, None        
        else:
            if 'X' in dimension:
                try:
                    """ d i m e n s i o n   c o m o   d i me n s i o n ( 3x4 )"""
                    total_filas , total_columnas = SttS.desata_binomio(dimension, 'X')
                    if total_filas == None or total_columnas == None:
                        return None, None
                    total_filas     = int(total_filas)                                     # si no es bueno, casca
                    total_columnas  = int(total_columnas)                                  # si no es bueno, casca
                except Exception as e:
                    print(f'Error init Rango: {e}')
                    return None, None
            else:
                return None, None
        
        return total_filas, total_columnas

    def __get_str_celda_fin(self, total_filas:int, total_columnas:int):
        """ >>> Obtiene la cadena de la celda fin (pej. 'D:3' ), no el objeto Celdt 
        """
        try:            
            fila_fin    = self.fila     + total_filas    - 1         
            columna_fin = self.columna  + total_columnas - 1 

            letra_columna_fin = SttS._may_nl[columna_fin]
            celda_fin = f'{letra_columna_fin}:{fila_fin}'
        except Exception as e:
            print(f'Error __init__ Rango :::: {e}')
            return None

        return celda_fin
    
    def __get_list_celdas(self):
        """ >>> Genera una lista de celdas iterando a través del número total de filas y columnas.
        Retorno:
            list: Una lista de celdas obtenidas llamando al método 'sumar_fc' con los índices actuales de fila y columna.
                  Si ocurre una excepción, imprime un mensaje de error y retorna None.
        >>> lst_celdas=[]
        >>> for i in range(self.total_filas)):            
        >>>     for j in range(self.total_columnas):
        >>>         sig_celda = self.sumar_fc(filas = i, columnas = j,  b_copy_value=True)            
        >>>         lst_celdas.append(sig_celda)
        """
        try:
            return [
                self.sumar_fc(filas=i, columnas=j, b_copy_value=True)
                for i in range(self.total_filas )
                for j in range(self.total_columnas )                  
            ]

        except Exception as e:
            print(f'Error en __get_list_celdas :::: {e}')
            return None

    # ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    #  PUSH - DATOS HACIA SELF.
    # •••••••••••••••••••••••••••••••••••••••••••••••••••••
    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    def __push_plana(self, data_push, relleno:str = ''):
        """ >>> establece un dato en el rango .
        Aplana la lista dada, ajusta su longitud para que coincida con la lista interna 'self.lst_celdas' rellenando con un valor predeterminado,
        y establece los valores de las celdas en 'self.lst_celdas' a los valores correspondientes en la lista ajustada o no dependiendo de b_relleno.
        [data_push] : el dato a procesar. Puede ser matriz, lista, int, bool, str, o cualquier objeto.
        Returns:
            None

        Se llama desde __init__ , lo que provoca que se pueda crear un rango con las medidas de la matriz.
        """
        try:
            # APLANO EL DATO: ...Si es matriz lo convierte en lista , si es lista lo deja como lista y si es str , int, bool, lo deja como está.
            lista_plana = SttS.aplanar_matriz(matriz = data_push)
            
            # EVALUO SI TENGO QUE RELLENAR EL RESTO DEL RANGO CON DATOS DE INICIO O LO DEJO COMO ESTÁ
            if relleno == '':
                lista_plana = SttS.igualar_listas( lista_keys = self.lst_celdas , lista_to_relong = lista_plana , valor_relleno = self.valor_default )        
                """ >>> lst len(self.lst_celdas) == len(lista_plana). lista_plana se rellena con Celda.VALOR_INICIAL ( '' ) 
                """
            else:
                lista_plana = SttS.igualar_listas( lista_keys = self.lst_celdas , lista_to_relong = lista_plana , valor_relleno = relleno )        
                """ >>> lst len(self.lst_celdas) == len(lista_plana). lista_plana se rellena con cualquier valor 
                """
            # En caso de que b_relleno = False, se emparejan hasta el mas corto :)
            # El Rango (las celdas del rango) cambien de valor
            for celda, valor in zip(self.lst_celdas, lista_plana):
                celda.set_valor( valor = valor )  

            return True    
        except Exception as e:
            print(f'Error ::: Rango ::: __push_plana ::: {e}')
            return None

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    def push(self, data_push, celda_inicio:str='A:0', b_lineal:bool=False, **kwargs):
        """ ■■■■■■■■■■■■  INSERTA DATOS EN TABLERO  ■■■■■■■■■■■■
        CREA UN RANGO CON data_push EN CELDA_INICIO, LO FORMATEA SEGUN  b_lineal, eje Y b_repetir. 
        
        [data_push](any, matriz): LOS DATOS PUEDEN SER TIPOS PYTHON, ITERADORES(LIST, TUPLE, SET), MATRICES.
        [celda_inicio](str) celda de inicio del rango donde introducir data_push
        [b_lineal](bool)(str): True, si se hace el cruce lineal (como vengan las celdas en linea)(self.__push_plana)
                               False, Si el cruce Celda a Celda coincidente(self.cross())
                               
                               En caso de que data_push sea un str, se puede introducir:
                               'X' para b_repetir data_push horizontalmente desde celda_inicio hasta fin linea
                               'Y' para b_repetir data_push verticalmente   desde celda_inicio hasta fin columna.
        
        [**kwargs](dict): ■■  'eje' = 'X' o 'Y'  ■ solo en caso de que data_push sea list.
                          ■■  'b_repetir' = True, False ■ solo en caso de que data_push sea str 

        CREO UN RANGO CON LOS DATOS SEGÚN VIENEN EN LA CELDA_INICIO. 
        LUEGO LOS CRUZO CELDA A CELDA CON EL RANGO CON CROSS
        
        SI ES MATRIZ, SI B_LINEAL = TRUE, TB LOS CARGO SEGÚN VIENEN COMO EN LA TÉCNICA ANTERIOR.        
        SI B_LINEAL = FASE, ENCUADRO LA MATRIZ Y CREO EL RANGO. LUEGO LO CRUZO CON CROSS COMO TODAS LAS ANTERIORES.
        
        ■ Introduce la List en B:5 HORIZONTAL (si entra una lista siempre entra plana, uso 'eje' para definir la direccion)
        >>> ejemplo: TABLERO.push([3,2,1], celda_inicio='B:5', eje='X') 

        ■ Introduce la List en B:5 VERTICAL 
        >>> ejemplo: TABLERO.push([3,2,1], celda_inicio='B:5', eje='Y')  
        
        ■ Introduce la matriz en B:5
        >>> ejemplo: TABLERO.push([[3,2,1],[4, 5,6]], celda_inicio='B:5', b_lineal=False)   
        
        ■ Introduce el texto en B:5
        >>> ejemplo: TABLERO.push('Tres tristes tigres', celda_inicio='B:5', b_lineal=False)   
        """

        # ■■ CACHO LAS VARIABLES OPCIONALES
        lst_ejes_validos = ['X', 'Y', 'x', 'y']

        # ■■  KWARGS eje
        eje = kwargs.get('eje', 'X')            
        if not eje in lst_ejes_validos:
            eje = 'X'                           # Lo fuerzo al eje X en caso de que no entre un valor valido.
        else:
            eje = str(eje).upper()

        # ■■  KWARGS b_repetir
        repetir = kwargs.get('repetir', False)
        if not isinstance(repetir, bool):
            repetir = False

        # ■■ CACHO LA CELDA DE INICIO COMO CELDA
        if isinstance(celda_inicio, str): 
            celda_inicio = celda_inicio.upper()
            celda_ini = self.get_celda(nombre_celda=celda_inicio)        
            if not celda_ini:
                print(f'Celda Inicio No existe en el Tablero: {celda_inicio}')
                return None
        elif isinstance(celda_inicio, Celda):
            celda_ini = celda_inicio
        else:
            print(f'FORMATO DE celda_inicio ERRORNEO: {celda_inicio}')
            return None
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■  
        # ■■■■■■ OBTENGO UN RANGO SOBRE EL DATO PASADO ■■■■■■ 
        rango = self.rangutan(data_push=data_push, celda_inicio = celda_ini, b_lineal=b_lineal , eje = eje , b_repetir = repetir )
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■  
        # ■■■■■ CRUZO LOS DATOS ■■■■■ 
        if rango:
            return self.cross(rango = rango)
        else:
            return None
        
    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    # CRUZO UN RANGO CON SELF. CELDA A CELDA COINCIDENTE
    def cross(self, rango , to_rango:bool = False):
        """ Cruza Celda a Celda un Rango con otro y asigna su valor ....pej C:1 de self con C:1 de rango 
        [rango](class Rango): entra un rango y cruzo Celda a Celda(Las que coincidan) en self.
        [to_rango](bool): True ::: From Tablero To Rango    ■■ PULL
                          False::: From Rango   To Tablero  ■■ PUSH         (byDef)
        Retorno: None, si hay algún fallo.        
        True en caso de que todo haya ido bien.
        """
        if not rango: return None
        if not isinstance(rango, Rango):
            return False
        
        # ▄▄▄▄▄▄▄ VALIDACION DE TODO EL CONTENIDO.
        if not self.es_rango_in(rango = rango): return False
        
        # ▄▄▄▄▄▄▄ CRUZO CELDA A CELDA COMPARANDO SUS NOMBRES_CELDA.
        for celda in self.lst_celdas:
            for celda_rango in rango.lst_celdas:
                if celda.nombre_celda == celda_rango.nombre_celda:
                    if to_rango == False:                       # Desde el Rango de entrada  a éste Rango
                        celda.valor = celda_rango.valor
                    else:                                   # Desde éste Rango a el Rango de entrada.
                        celda_rango.valor = celda.valor
                    break
        return True
        
    # RANGO IN SELF?
    def es_rango_in(self, rango):
        """ VALIDA SI UN RANGO ESTÁ CONTENIDO EN EL RANGO SELF. 
        Compara el nombre de la celda de inicio y celda de fin en self.lst_celdas 

        [rango](Class Rango): representa un objeto Rango(esta misma Clase).
        Retorno: True, si el rango está contenido en el Rango self. 
        False, si el Rango no está contenido (está sobre-pasado).

        """
        # VALIDACION INICIAL
        if not self.lst_celdas or not self.matriz or not rango: 
            return False
        # COMPROBACION DE NOMBRES POR MEDIO DE ANY
        if not any (rango.celda_inicio.nombre_celda in celda.nombre_celda for celda in self.lst_celdas):
            return False

        if not any (rango.celda_fin.nombre_celda in celda.nombre_celda for celda in self.lst_celdas):
            return False
        
        return True            

    # ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    # BORRAR VALORES DEL RANGO
    # •••••••••••••••••••••••••••••••••••••••••••••••••••••
    def delete(self, **kwargs):
        """ ELIMINA(valor/Rango) DEL TABLERO. 
        
        SE PUEDEN ELIMINAR:
        ■ Valores en Objeto Celda
        ■ Valores en Columna
        ■ Valores en Fila
        ■ Valores en Rango, no borra el rango. Para borrar el rango está self.delete_rango()

        AL FINAL HAY QUE HACER UN PULL_ALL PARA QUE SE ACTUALIZEN TODOS LOS RANGOS DEL TABLERO.
        """
        # ■■ RECOGO LOS DATOS DE LA ENTRADA
        fila = kwargs.get('fila', None)         
        columna = kwargs.get('columna', None)   
        celda = kwargs.get('celda', None)       
        rango = kwargs.get('rango', None)       
        del_rango = kwargs.get('b_rango', False)  # Sólo para rango y es una opicion que si se pone a True elimina el rango de self.lst_rangos


        b_pull = True
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■ ANALIZO LOS DATOS DE ENTRADA Y LOS PONGO EN LA FORMA CORRECTA
        if fila == None and columna == None and celda == None and rango == None:
            return False
        elif rango != None:
            """ ■ 1º RANGO SOBRE TODO LO DEMAS. Si entra rango, ya no miro lo demas. """
            if isinstance(rango, str):
                if del_rango == True:
                    """ ■■ ELIMINA RANGO """
                    rango = self.buscar_rango(nombre_rango=rango)
                    self.delete_rango( rango = rango )
                    
                    b_pull = False
                else:
                    """ ■■ ELIMINA VALOR RANGO """
                    rango = self.buscar_rango(nombre_rango=rango)
                    rango.iniciar(valor=self.valor_default)
                pass
            elif isinstance(rango, Rango):
                if del_rango == True:
                    """ ■■ ELIMINA RANGO """
                    self.eliminar_rango( rango=rango )
                    
                    b_pull = False
                else:
                    """ ■■ ELIMINA VALOR RANGO """
                    rango = self.buscar_rango(nombre_rango=rango)
                    rango.iniciar(valor=self.valor_default)
                pass
            else:
                return False

        elif celda != None:
            """ ■ 2º CELDA. Si entra celda y no entra rango, ya no miro lo demás.  """
            if isinstance(celda, str):
                obj_celda = self.getting(celda=celda)
                if not obj_celda: return False
            elif isinstance(celda, Celda):
                obj_celda = self.getting(celda=celda.nombre_celda)
                if not obj_celda: return False
            else:
                return False

            obj_celda.valor = self.valor_default

        elif fila != None and columna != None:
            """ ■ 3º FILAS Y COLUMNAS. Configuran una Celda. Pasa por aquí cuando ni hay rango, ni celda.  """
            try:
                fila = abs(int(fila))
            except Exception as e:
                return False

            # PERMITE LETRA Y NUMERO PARA COLUMNA
            columna = Celda.numero_columna(columna=columna)
            if not columna: 
                return False

            # AHORA TENGO LA FILA Y LA COLUMNA COMO NUMEROS
            obj_celda = self.getting(fila=fila, columna= columna)
            if not obj_celda: return False

            obj_celda.valor = self.valor_default  
            
        elif fila != None and columna == None:
            """ ■ 4º FILAS . Configuracion fija de la celda_inicio.  """
            try:
                fila = abs(int(fila))
            except Exception as e:
                return False
            
            self.push(data_push=self.valor_default, celda_inicio=f'{self.celda_inicio.letra}:{fila}', b_lineal=False, repetir=True, eje='X')

        elif fila == None and columna != None:
            """ ■ 5º COLUMNAS  """
            # PERMITE LETRA Y NUMERO PARA COLUMNA
            columna = Celda.numero_columna(columna=columna)
            if not columna: return False
            # MONTO UNA CELDA SOBRE LA FILA 0 PARA RECUPERAR LA LETRA(COLUMNA) ;)
            fila = 0
            celda = Celda(fila=fila, columna=columna)
            if not celda: return False

            self.push(data_push=self.valor_default, celda_inicio=f'{celda.letra}:0', b_lineal=False, repetir=True, eje='Y')

        elif fila == None and columna == None:
            return False    # NO SE PUEDE DAR, PERO LO DEJO POR DEJAR TODAS LAS OPCIONES A LA VISTA
        else:
            return False    # NO SE PUEDE DAR, PERO LO DEJO POR DEJAR TODAS LAS OPCIONES A LA VISTA

        # ███ EL ULTIMO PASO NECESARIO ES LINKEAR LOS CAMBIOS CON LOS RANGOS PARA QUE SIEMPRE TENGAN LA INFO ACTUALIZADA.
        if b_pull == True:
            self.pull_all()
    

    # ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    #  IMPRIMIR
    # •••••••••••••••••••••••••••••••••••••••••••••••••••••
    
    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    def imprimir(self, sp_between:int = 0, ancho_columna:int = None, lista:list = None ):    
        """ 
        Imprime el Rango con configuracion. Es la base de impresion sobre todo. 
        [sp_between] (int): el espacio entre columnas
        [**kwargs] (dict):  "ancho_columna"(int)  = ancho de columna fixed or 
                            "lista"(list) = lista de anchos para cada columna. 
        
        >>> ejemplo: imprimir( ) => ajusta al maximo de cada columna(mode tabla)
        >>> ejemplo: imprimir( sp_between = 2 ) => maximo de cada columna (mode tabla)        
        >>> ejemplo: imprimir( ancho_columna = 0 , sp_between = 0 ) => L i t e r a l   P u r o ....XindeX
        >>> ejemplo: imprimir( ancho_columna = 1 , sp_between = 0 ) => L i t e r a l   con espacio entre columnaas
        >>> ejemplo: imprimir( ancho_columna = 15 , sp_between = 5 ) => columnas al 15 todas. no restrictivo. sp_between = 5 . espacio entre columnas de 5 char
        >>> ejemplo: imprimir( lista = [0,1,5,4,3,2] , sp_between = 5 ) => cada columna a su ajuste y 5 entre columnas
        >>> ejemplo: imprimir( ancho_columna = 15 , lista = [0,1,5,4,3,2] , sp_between = 3 ) => Prevalece la lista. y deja 3 entre columnas.
        """
        # CACHO  LOS DATOS DE ENTRADA
        # ancho_columna = kwargs.get('ancho_columna', None)  # Si no existe, usa 0
        # lista = kwargs.get('lista', None)  # Si no existe, usa 0
        
        # ANALIZA Y CREA LA CADENA DE FORMATO.
        str_formato = self.get_baseline_format(sp_between = sp_between , ancho_columna = ancho_columna , lista = lista )        
        if not str_formato:
            print("Error Imprimir::: Error al formar str_formato:::get_baseline_format() ")
            return None
        """ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
             I M P R I M E   V A L O R E S
        """
        try:    
            # Recorro las filas
            for i in range( len(self.matriz) ):                
                
                # OBTIENE UNA FILA EN FORMATO DE MATRIZ CON GET_FILAS. ADEMÁS DEVUELVE LAS CELDAS EN LA MATRIZ.
                matriz_fila = self.get_filas(fila_from = i, fila_to = i )   
                
                # OBTIENE LOS VALORES DE UNA FILA EN FORMA DE LISTA.
                lst_values_fila = [celda.valor for fila in matriz_fila for celda in fila ]

                # INTERCALA EL CARACTER CHAR ENTRE LOS VALORES DE LA LISTA: [1,2,3,4] => [1,'',2,'',3,'',4,''] => PARA CONTEMPLAR  sp_between.
                lst_valores_formato_print_x_fila = Rango.between_listas( lista = lst_values_fila, char = self.valor_default)
                                
                print(str_formato.format(*lst_valores_formato_print_x_fila)) 

        except Exception as e:
            print(f'{e}')
            return None
    
    # DEVUELVE LA CADENA DE FORMATO PARA IMPRIMIR. LOS PARAMETROS SON LOS MISMOS QUE self.imprimir()
    def get_family_impresion(self, sp_between, ancho_columna , lista ):
        """ DEVUELVE EL ENUM TYPE_PRINT SEGUN LOS ARGUMENTOS DE IMPRESION PASADOS.
        SIRVE PARA CALCULAR EL ESPACIO ESCRITO EN EL RANGO.
        
        [sp_between] (int): el espacio entre columnas
        [ancho_columna](int)  = ancho de columna fixed or 
        [lista](list) = lista de anchos para cada columna.  """

        if ancho_columna == None and lista == None and sp_between == 0:
            """ ■ MAX-COLUMNA SSP (PURO) """
            name_impresion = TYPE_PRINT.MAX_SSP
        
        elif ancho_columna == None and lista == None and sp_between != 0:
            """ ■ MAX-COLUMNA CSP"""
            name_impresion = TYPE_PRINT.MAX_CSP
        
        elif ancho_columna != None and lista == None and sp_between == 0:
            if ancho_columna == 0:
                """ ■ LITERAL SSP (PURO) """
                name_impresion = TYPE_PRINT.LITERAL
            else:
                """ ■ FIXED SSP"""
                name_impresion = TYPE_PRINT.FIXED_SSP
        
        elif ancho_columna != None and lista == None and sp_between != 0:
            if ancho_columna == 0:
                """ ■ LITERAL + CSP + ANCHO-ZERO """
                name_impresion = TYPE_PRINT.MOSAICO
            else:
                """ ■ FIXED CSP"""
                name_impresion = TYPE_PRINT.FIXED_CSP
        
        elif ancho_columna == None and lista != None and sp_between == 0:
            """ ■ LISTA PERSONAL + SSP + ANCHO-MAX(RESTO) """
            name_impresion = TYPE_PRINT.LIST_MAX_SSP

        elif ancho_columna == None and lista != None and sp_between != 0:
            """ ■ LISTA PERSONAL + CSP + ANCHO-MAX(RESTO) """
            name_impresion = TYPE_PRINT.LIST_MAX_CSP

        elif ancho_columna != None and lista != None and sp_between == 0:
            if ancho_columna == 0:
                """ ■ LISTA + SSP + ANCHO-ZERO"""
                name_impresion = TYPE_PRINT.LIST_LITERAL
            else:
                """ ■ LISTA + ANCHO FIXED + SSP """
                name_impresion = TYPE_PRINT.LIST_FIXED_SSP
        
        elif ancho_columna != None and lista != None and sp_between != 0:
            if ancho_columna == 0:
                """ ■ LISTA + CSP + ANCHO-ZERO"""
                name_impresion = TYPE_PRINT.LIST_MOSAICO
            else:
                """ ■ LISTA + ANCHO + CSP """
                name_impresion = TYPE_PRINT.LIST_FIXED_CSP
        else:
            # print(f'Error::: No se ha podido determinar el tipo de impresion.')
            return None
        # Una vez que sabemos el tipo por-menorizado de la impresión, Retornamos su Familia.
        if (name_impresion == TYPE_PRINT.LITERAL      or name_impresion == TYPE_PRINT.MOSAICO or 
            name_impresion == TYPE_PRINT.LIST_LITERAL or name_impresion == TYPE_PRINT.LIST_MOSAICO ):
            return 'MOSAICO'
        elif (name_impresion == TYPE_PRINT.FIXED_SSP      or name_impresion == TYPE_PRINT.FIXED_CSP or 
              name_impresion == TYPE_PRINT.LIST_FIXED_SSP or name_impresion == TYPE_PRINT.LIST_FIXED_CSP):
            return 'FIX'
        elif (name_impresion == TYPE_PRINT.MAX_SSP      or name_impresion == TYPE_PRINT.MAX_CSP or 
              name_impresion == TYPE_PRINT.LIST_MAX_SSP or name_impresion == TYPE_PRINT.LIST_MAX_CSP):                 
            return 'MAX'
        else:
            # print(f'Error::: No se ha podido determinar el tipo de impresion.')
            return None
    
    # RECOGE TODAS LAS OPCIONES DE IMPRESION CON: ANCHO_COLUMNA Y/O LISTA + ESPACIO_ENTRE_COLUMNAS
    def get_baseline_format(self, sp_between:int = 0, ancho_columna:int = 0, lista:list = None):
        """ CACHA TODAS LAS OPCIONES DE IMPRESION:
        [sp_between]:int: ESPACIO ENTRE LAS COLUMNAS DE CONTENIDO.
        [ancho_columna](int): ANCHO DE LA COLUMNA
        [lista](list)(INT): LISTA DE INT, QUE DEFINE LOS ANCHOS DE LAS COLUMNAS.
        Retorno:
            None: Si ocurre un error durante la creación del formato.
            str: Devuelve la cadena de formato para imprimir el rango.
            
            ■ LITERAL {:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}
            ■ MOSAICO {:<0}{:<3}{:<0}{:<3}{:<0}{:<3}{:<0}{:<3}{:<0}{:<3}{:<0}{:<3}{:<0}{:<3}{:<0}{:<3}{:<0}{:<3}{:<0}{:<3}
            
            ■ FIXED   {:<5}{:<3}{:<5}{:<3}{:<5}{:<3}{:<5}{:<3}{:<5}{:<3}{:<5}{:<3}{:<5}{:<3}{:<5}{:<3}{:<5}{:<3}{:<5}{:<3}            
            ■ FIXED   {:<5}{:<0}{:<5}{:<0}{:<5}{:<0}{:<5}{:<0}{:<5}{:<0}{:<5}{:<0}{:<5}{:<0}{:<5}{:<0}{:<5}{:<0}{:<5}{:<0}
            
            ■ MAX-COL {:<11}{:<0}{:<4}{:<0}{:<5}{:<0}{:<4}{:<0}{:<1}{:<0}{:<0}{:<0}{:<0}{:<0}{:<17}{:<0}{:<0}{:<0}{:<0}{:<0}
            ■ MAX-COL {:<11}{:<3}{:<4}{:<3}{:<5}{:<3}{:<4}{:<3}{:<1}{:<3}{:<0}{:<3}{:<0}{:<3}{:<17}{:<3}{:<0}{:<3}{:<0}{:<3}

        """
        str_formato:str = ''
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # MAXIMO_COLUMNA - SSP  - SIN LISTA - HASTA  LAST_COLUMNA_USED
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        if ancho_columna == None and lista == None and sp_between == 0:
            """ ■ MAX-COLUMNA SSP (PURO) """
            try:
                str_formato = self.__formato_max_columnas( sp_between = 0  )
            except Exception as e:
                print(f'{e}')
                return None

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # MAXIMO_COLUMNA CSP - SIN LISTA - HASTA  LAST_COLUMNA_USED
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        elif ancho_columna == None and lista == None and sp_between != 0:
            """ ■ MAX-COLUMNA CSP"""
            try:
                str_formato = self.__formato_max_columnas(  sp_between = sp_between  )
            except Exception as e:
                print(f'{e}')
                return None

        elif ancho_columna != None and lista == None and sp_between == 0:
            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            # LITERAL - SIN LISTA
            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            if ancho_columna == 0:
                """ ■ LITERAL SSP (PURO) """
                try:
                    str_formato = self.__formato_imprimir_fixed(  len_columnas = 0, sp_between = 0 )
                except Exception as e:
                    print(f'{e}')
                    return None

            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            # FIXED - CSP  - SIN LISTA
            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            else:
                """ ■ FIXED SSP"""
                try:
                    str_formato = self.__formato_imprimir_fixed( len_columnas = ancho_columna, sp_between = 0)
                except Exception as e:
                    print(f'{e}')
                    return None

        elif ancho_columna != None and lista == None and sp_between != 0:

            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            # LITERAL - CSP - SIN LISTA - MOSAICO
            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            if ancho_columna == 0:
                """ ■ LITERAL + CSP + + ANCHO-ZERO """
                try:
                    str_formato = self.__formato_imprimir_fixed(  len_columnas = 0, sp_between = sp_between)
                except Exception as e:
                    print(f'{e}')
                    return None
            else:
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                # FIXED - CSP - SIN LISTA
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                """ ■ FIXED CSP"""
                try:
                    str_formato = self.__formato_imprimir_fixed( len_columnas = ancho_columna, sp_between = sp_between)
                except Exception as e:
                    print(f'{e}')
                    return None

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # █ CON LISTAS - RESTO MAX_COLUMNA - SSP 
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        elif ancho_columna == None and lista != None and sp_between == 0:
            """ ■ LISTA PERSONAL + SSP + ANCHO-MAX(RESTO) """
            if isinstance(lista, list):
                try:
                    # SON INT O PETA
                    lst_lens = [int(item) for item in lista]
                    str_formato = self.__formato_imprimir_list( lista=lst_lens , sp_between = 0 , ancho_columna = None )
                except Exception as e:
                    print(f'{e}')
                    return None
            else:
                return None

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # █ CON LISTAS - RESTO MAX_COLUMNA - CSP 
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        elif ancho_columna == None and lista != None and sp_between != 0:
            """ ■ LISTA PERSONAL + CSP + ANCHO-MAX(RESTO) """
            try:
                lst_lens = [int(item) for item in lista]
                str_formato = self.__formato_imprimir_list( lista=lst_lens , sp_between = sp_between , ancho_columna = None )
            except Exception as e:
                print(f'{e}')
                return None

        elif ancho_columna != None and lista != None and sp_between == 0:

            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            # █ CON LISTAS - RESTO ZERO (LITERAL)- SSP 
            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            if ancho_columna == 0:
                """ ■ LISTA + SSP + ANCHO-ZERO"""
                try:
                    lst_lens = [int(item) for item in lista]
                    str_formato = self.__formato_imprimir_list( lista=lst_lens , sp_between = 0 , ancho_columna = 0 )
                except Exception as e:
                    print(f'{e}')
                    return None
            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            # █ CON LISTAS - RESTO FIXED - SSP 
            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            else:
                """ ■ LISTA + ANCHO FIXED + SSP """
                try:
                    lst_lens = [int(item) for item in lista]
                    str_formato = self.__formato_imprimir_list(lista = lst_lens , sp_between = 0 , ancho_columna = ancho_columna )
                except Exception as e:
                    print(f'{e}')                    
                    return None

        elif ancho_columna != None and lista != None and sp_between != 0:
            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            # █ CON LISTAS - RESTO ZERO (LITERAL) - CSP 
            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            if ancho_columna == 0:
                """ ■ LISTA + CSP + ANCHO-ZERO"""
                try:
                    lst_lens = [int(item) for item in lista]
                    str_formato = self.__formato_imprimir_list(lista = lst_lens , sp_between = sp_between , ancho_columna = 0 )
                except Exception as e:
                    print(f'{e}')
                    return None

            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            # █ CON LISTAS - RESTO FIXED (LITERAL) - CSP 
            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            else:
                """ ■ LISTA + ANCHO + CSP """
                try:
                    # SON INT O PETA
                    lst_lens = [int(item) for item in lista]
                    # CREA EL FORMATO
                    str_formato = self.__formato_imprimir_list(lista = lst_lens , sp_between = sp_between , ancho_columna = ancho_columna )
                except Exception as e:
                    print(f'{e}')
                    return None
        pass
        return str_formato

    #  BORRAR..... SUSTITUIDA POR self.get_filas()
    def __get_fila_rango_prango(self,  fila_a_buscar:int):
        if SttS.b_fila_valida( fila = fila_a_buscar , from_incl=0, to_incl = self.total_filas ) == False: 
            return None
        for f, fila in enumerate(self.matriz):
            if  f == fila_a_buscar:
                return fila

    # FORMATO IMPR _____________________________
    def __formato_max_columnas(self,  sp_between:int = 0 ):        
        """ >>> Pone cada columna a su maximo 
        strformato += "{:<" + str(num_espacios_columna) + "}"  pejem: {:<"+str(15)+"}" 
        [sp_between](int): cuanndo b_ajustado = True -> es el espacio que tiene que haber entre el final de una columna y la siguiente.
        """  
        totalLen    = 0
        strformato  = ''
        try:
            sp_between = abs(sp_between)
        except Exception as e:
            print(f'Error __formato_max_columnas ::: {e}')

        for i in range (self.total_columnas): 
            maximo = self.max_len_columna( columna = i )
            strformato += "{:<" + str(maximo) + "}" + "{:<" + str(sp_between) + '}'
        # RETORNO EL FORMATO DE DE IMPRESION UNA FILA 
        return strformato
    
    def get_lst_max_columnas(self):
        """ DEVUELVE UNA LISTA CON LA LONGITUD MAXIMA DE CADA COLUMNA 
        """
        # lst_max_columna = []
        # for i in range(self.total_columnas):
        #     maximo = self.max_len_columna(columna = i)
        #     lst_max_columna.append(maximo)
        # return lst_max_columna
        lst_max_columna = [self.max_len_columna(columna = i) for i in range(self.total_columnas)]
        return lst_max_columna
    
    # FORMATO IMPR _____________________________
    def __formato_imprimir_fixed(self,  len_columnas = 0, sp_between=0):        
        """ >>> Imprime un Rango sin ajuste de ventanas.
        [len_columnas](int) : Longitud de la columna fijo... cuando b_ajustado = False
        [sp_between](int): cuanndo b_ajustado = True -> es el espacio que tiene que haber entre el final de una columna y el siguiente.
        """  
        totalLen = 0
        strformato = ''
        """ >>> strformato +=  pejem: {:<"+str(15)+"}" {:<"+str(2)+"}"  """                

        for i in range (self.total_columnas):
            # strformato += "{:<" + str(len_columnas + sp_between) + "}" 
            strformato += "{:<" + str(len_columnas) + "}" + "{:<" + str(sp_between) + '}'
        return strformato
    
    # FORMATO IMPR _____________________________
    def __formato_imprimir_list( self, lista , ancho_columna:int , sp_between:int=0 ):        
        """ >>> ESTABLECE EL FORMATO DE UNA FILA DE LA MATRIZ . 
        introduce una columna de mas between  item a imprimir(sp_between). 

        [lista](list) : Lista con las Longitudes de la columna fijo... cuando b_ajustado = False
        [sp_between](int): cuanndo b_ajustado = True -> es el espacio que tiene que haber entre el final de una columna y el siguiente.
        """  
        strformato = ''
        """ >>> strformato += "{:<" + str(len(item)) + "}"  pejem: {:<"+str(15)+"}"  """                
        if not self.matriz: return None

        len_lista = len(lista)

        # Una opción mas directa  de coger una fila(para su tamaño) pero que me gusta menos.
        lista_fila = self.matriz[0]       
        len_lista_fila = len(lista_fila)
        
        # CALCULO LA DIFERENCIA ENTRE LA LONGITUD DE LA PRIMERA FILA DE LA MATRIZ Y LA LISTA
        diferencia_filas = len_lista_fila - len_lista

        if diferencia_filas != 0:
            # ASEGURA QUE SE GESTIONA diferencia_filas POSITIVO.
            if diferencia_filas < 0:        # ENTRA UNA LISTA MAYOR QUE LA MATRIZ.
                lista = SttS.igualar_listas( lista_keys = lista_fila , lista_to_relong = lista )
            else:
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                # ■■■ EMPIEZA EL ANALISIS Y PROCESO ■■■
                if ancho_columna == None:
                    """ ■ RESTO MAX """
                    for i in range(diferencia_filas):
                        lista = lista + [ self.max_len_columna(columna = len_lista + i ) ]                    
                elif ancho_columna == 0:
                    if ancho_columna == 0:                
                        """ ■ RESTO ZERO """
                        lista = SttS.igualar_listas( lista_keys = lista_fila , lista_to_relong = lista , valor_relleno = 0 )
                elif ancho_columna != 0:
                    """ ■ RESTO FIXED """
                    for i in range(diferencia_filas):
                        lista = lista + [ancho_columna]
        pass
        if not lista: 
            return None

        # ■■■ CON LA LISTA REMODELADA SE CREA EL FORMATO DE IMPRESION DE LISTAS ■■■
        for item in lista:
            # strformato += "{:<" + str(len_columnas + sp_between) + "}" 
            strformato += "{:<" + str(item) + "}" + "{:<" + str(sp_between) + "}"
        return strformato

    # ◘◘◘◘◘◘◘ LONGITUD MAXIMA DEL CONTENIDO DE UNA COLUMNA DEL RANGO.
    def max_len_columna(self, columna , b_limpio:bool = True):
        """ ■ OBTIENE LA MATRIZ DE LAS LONGITUDES DE UNA COLUMNA.
        [columna](int)(str): puede ser el número o la letra de la columna.
        [b_limpio](bool): ■ True ► Devuelve el valor sin caracteres ANSI de colorama. ■ False ► Devuelve el valor tal cual.
        """
        matriz_columnas = self.get_columnas(columna_from = columna , columna_to= columna)
        if not matriz_columnas: return None

        lst_longitudes=[]
        for lst_columna in matriz_columnas:
            for celda in lst_columna:
                if b_limpio == True:
                    lst_longitudes.append( Rango.len_limpio(texto = str(celda.valor)) )
                else:
                    lst_longitudes.append(len(str(celda.valor)))
                
        return max(lst_longitudes) if lst_longitudes else 0
    
    # LISTA CON LAS LONGITUDES MAXIMAS DE TODAS LAS COLUMNAS
    def get_list_maxlen_columna(self, b_limpio:bool = True):
        """ DEVUELVE UNA LISTA CON LA LONGITUD MAXIMA DE CADA COLUMNA """
        lst_max_columna = []
        for i in range(self.total_columnas):
            maximo = self.max_len_columna(columna = i, b_limpio = True)
            lst_max_columna.append(maximo)
        return lst_max_columna

    # DEVUELVE UNA LIST CON LA ULTIMA COLUMNA USADA EN CADA FILA
    def get_lst_last_columna_used_xfila(self):
        """Def: Lista con la última columna usada en cada fila de la matriz.        
        """ 
        lst_last_columna_used = []
        for fila in self.matriz:
            last_columna_used = 0                # Valor por defecto si no se encuentro otra columna
            for celda in reversed(fila):
                if celda.valor != self.valor_default:                    
                    last_columna_used = celda.columna
                    break
            lst_last_columna_used.append(last_columna_used)
        
        # RETORNO
        return lst_last_columna_used if lst_last_columna_used else None

    # LONGITUD MAXIMA DE TODAS LAS FILAS    
    def max_len_filas(self, b_limpio:bool = True):
        """ >>> Devuelve el valor maximo de todas las filas 
        [b_limpio](bool): si es True cuenta los caracteres ANSI.
        [resta_fija](int): opcional. Sirve para no contar con caracteres... Si lo introduces es pq hay caracteres que no quieres contar(bordes y marcos en impresion Literal). 
        """
        lst_fila    = []
        for fila in self.matriz:
            longitud_fila=0
            for celda in fila:
                if b_limpio == True:
                    longitud_fila += Rango.len_limpio(texto = str(celda.valor))
                else:
                    longitud_fila += len(str(celda.valor))
            pass
            lst_fila.append(longitud_fila)    
        pass 
        return max(lst_fila) if lst_fila else 0
    
    # LISTA CON EL SUMATORIO DE LONGITUD DE CADA FILA
    def get_lstlen_valores_xfila(self, b_limpio:bool = True):
        """ LISTA CON LA LONGITUD DE CADA FILA
        [b_limpio](bool): si es True cuenta los caracteres ANSI.
        """
        lst_len_x_row = []
        for fila in self.matriz:
            longitud_total_fila=0
            for celda in fila:
                if b_limpio == True:
                    longitud_total_fila += Rango.len_limpio(texto = str(celda.valor))
                else:
                    longitud_total_fila += len(str(celda.valor)) 
            pass            
            lst_len_x_row.append(longitud_total_fila)    
        pass                
        return lst_len_x_row if lst_len_x_row else None

    
    # ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    #  MISCELANEA
    # •••••••••••••••••••••••••••••••••••••••••••••••••••••
    
    # ULTIMA FILA CON USO DE UN TABLERO
    def last_fila_used(self):
        """ ■■ DEVUELVE EL INDICE DE LA ÚLTIMA FILA USADA ....que contiene algún valor distinto de 'valor_default'. """    
        if not self.matriz:
            return None    

        for i, fila in enumerate(reversed(self.matriz)):
            if any(celda.valor != self.valor_default for celda in fila):  
                return len(self.matriz) - 1 - i  # Convertir índice de reversed al original

        return None

    # def get_last_columna_used(self, tablero = None):
    def get_last_columna_used( self ):
        """ ■■ DEVUELVE EL ÍNDICE DE LA ÚLTIMA COLUMNA USADA EN LA MATRIZ DE CELDAS.  """
        # if tablero is None: 
        #     tablero = self

        if not self.matriz:
            return None    
        
        # OBTENGO UNA MATRIZ CON LAS COLUMNAS DESDE LA PRIMERA A LA ÚLTIMA(MATRIZ TRANSPUESTA)
        try:
            matriz_columnas = self.get_columnas( columna_from = self.celda_inicio.columna , columna_to = self.celda_fin.columna )
            # RECORRO LA MATRIZ TRANSPUESTA EMPEZANDO POR LA ÚLTIMA COLUMNA Y PREGUNTO SI HAY ALGÚN VALOR DISTINTO DEL VALOR_INCIIAL ('')
            for i, columna in enumerate(reversed(matriz_columnas)):
                if any(celda.valor != self.valor_default  for celda in columna):
                    return len(matriz_columnas) - i - 1
            pass
            return -1  # Si no se encuentra ninguna columna usada
        except Exception as e:
            print(f'Error en get_last_columna_used: {e}')
            return None

    @staticmethod
    def between_listas(lista:list , char:str=Celda.VALOR_INICIAL):
        """ Intercala el valor inicial entre los elementos de una lista duplicando su len  
        [lista](list): lista de elementos.
        [char](str): caracter a implementar entre elemento y elemento.
        Retorno: Devuelve la lista con los elementos intercalados duplicando su longitud.
        ■ Ejemplo: lst_retorno = SttS.between_listas(lista=[1,2,3,4], ' ') => [1, '', 2, '', 3, '', 4, ''] 
        """
        
        return [elem for item in lista for elem in (item, char)]
    
    @staticmethod
    def len_limpio(texto: str) -> int:
        """ Calcula la longitud real del texto sin códigos ANSI """
        ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return len(ANSI_ESCAPE.sub('', texto))

# ███████████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████
""" 
                        T A B L E R O  : ... somos cuadrados (Berto y BuenaFuente) 
"""
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████████████████████████████████████

import copy             # Para realizar copia profunda de self.tablero

# ■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■
class Tablero(Rango):
    """ >>> Crea un MARCO para Imprimir """
    # ______________________________________________________________________
    # C O N S T A N T E S   D E   C L A S E ....(Tablero.SP  ó Tablero.TAB)
    SP  = ' '
    TAB = f'{SP*4}'
    BASE_RANGO_TABLERO = 'rango_tablero'
    BASE_RANGO_FILA = 'rango_fila_'
    BASE_RANGO_COLUMNA = 'rango_columna_'

    pass
    def __init__(self, total_columnas_tablero:int, total_filas_tablero:int = 10 , valor_default = Celda.VALOR_INICIAL):       
        """ >>> Crea un Tablero(Rango), que empieza en A:0 y tiene la dimension establecida por total_filas_tablero y total_columnas_tablero 
        Se puede poner un valor inicial '-' distinto del que tiene Celda.VALOR_INICIAL = ''.
        Se tienen que crear y almacenar los rangos característicos del tablero como son: rango_filas y rango_columnas.
        Hay que incluir las características oculto, ghost, numerico, 
        crear_rango() |  rango_to_tablero() | tablero_to_rango() | buscar_rango() | ver_rangos() 

        >>> pej: tablero = Tablero(total_filas_tablero = 30 y total_columnas_tablero = 20 , valor_default='')
        """
        self.valor_default = valor_default
        try:
            total_columnas_tablero  = abs(int(total_columnas_tablero))
            total_filas_tablero     = abs(int(total_filas_tablero))
        except Exception as e:
            print(f'{e}')
            return None
        
        # Creamos la  d i m e n s i o n  para llamar al padre(Rango).
        self.dimension = f'{total_filas_tablero}X{total_columnas_tablero}'
        """ 
        >>> Después de esto, self es un Rango. CRUD. Mantiene una lista de rangos creados sobre el Rango Tablero. 
        """
        super().__init__(nombre_rango = 'main_tablero' , 
                        celda_inicio = 'A:0' , 
                        dimension = self.dimension ,
                        valor_default = self.valor_default , 
                        b_oculto = False , 
                        b_ghost = False)
        
        # •••••••••••••••••••••••••••••••••
        # MONTO LA ESTRUCTURA DE COLUMNAS..... (sobre la que voy a trabajar)       
        SttS.inicializa_diccs_letra_numero()

        # ••••••••••••••••••••••••••••••••••••••••••••
        # VALIDACION INICIAL DE LOS DATOS DE ENTRADA
        if total_columnas_tablero >= len( SttS._may_ln ):                   
            total_columnas_tablero = len( SttS._may_ln.keys() )-1
        pass        
        self.iniciar(valor=self.valor_default)
        pass
        # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        # LISTA DE RANGOS DEL TABLERO
        self.lst_rangos=[]           

        # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        # CREA UN RANGO X FILA
        lst_valores = self.get_values()
        if lst_valores:
            for i, fila in enumerate(lst_valores):
                nombre_new_fila = self.__new_nombre_secuencial(cadena=Tablero.BASE_RANGO_FILA)
                # CREA UN RANGO DE NOMBRE SECUENCIAL.
                celda_inicio = self.sumar_filas( i + self.celda_inicio.fila , b_copy_value = True)
                rango = self.crear_rango(nombre=nombre_new_fila, celda_inicio=celda_inicio.nombre_celda, dimension=f'1X{self.total_columnas}', valor_default = fila)
                if rango:
                    # INTRODUCE EL RANGO EN self.lst_rangos
                    rango.flag = 'ROW_SYS'
                    # self.lst_rangos.append(rango)

        # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        # CREA UN RANGO X COLUMNA
        lst_valores_columnas = self.get_columnas(columna_from=self.celda_inicio.columna, columna_to=self.celda_fin.columna, b_valor=True)
        if lst_valores_columnas:
            for j, columna in enumerate(lst_valores_columnas):
                # CREA UN RANGO DE NOMBRE SECUENCIAL.
                nombre_secuencial = self.__new_nombre_secuencial(cadena=self.BASE_RANGO_COLUMNA)
                # CELDA DE INICIO
                celda_inicio = self.celda_inicio.sumar_columnas(columnas=j, b_copy_value = True)
                rango = self.crear_rango(nombre = nombre_secuencial , celda_inicio=celda_inicio.nombre_celda, dimension=f'{self.total_filas}X1', valor_default = columna)
                if rango:
                    # INTRODUCE EL RANGO EN self.lst_rangos
                    rango.flag = 'COL_SYS'
                    # self.lst_rangos.append(rango)
        
    # _________________________________str__
    def __str__(self):
        """Devuelve una representación legible del diccionario de datos.
        """
        # Validacion
        if self.b_print_cabecera == True:
            # NOMBRES DE LAS COLUMNAS
            titulos = ["Rango", "Inicio", "Fin", "Total Celdas", "Filas", "Columnas", "Es Oculto", "Ghost", "Num de Rangos"]
            
            # TAMAÑOS DE LAS COLUMNAS
            tamanos_columnas = [25, 10, 10, 15, 8, 10, 10, 10, 15]
            
            # VALORES DE LAS COLUMNAS
            valores = [
                self.nombre ,
                self.celda_inicio.get_nombre_celda() ,
                self.celda_fin.get_nombre_celda() ,
                self.total_celdas ,
                self.total_filas ,
                self.total_columnas ,
                self.b_oculto ,
                self.b_ghost  , 
                len(self.lst_rangos)
            ]
            
            # FORMATEO DE NOMBRES DE COLUMNA, TAMAÑOS Y VALORES 
            cabeceras = "".join([f"{titulo:<{ancho}}" for titulo, ancho in zip(titulos, tamanos_columnas)])
            datos = "".join([f"{str(valor):<{ancho}}" for valor, ancho in zip(valores, tamanos_columnas)])
            
            # RESULTADO FINAL
            return f"{cabeceras}\n{'-' * sum(tamanos_columnas)}\n{datos}"
        else:
            return f"\nDatos del Rango( {valores[0]} ): [ {valores[1]} ]  To [ {valores[2]} ] Total Celdas: {valores[3]} => {valores[4]} Filas y {valores[5]} Columnas .......es Oculto?: {valores[6]} ..... Ghost?: {valores[7]}, Rangos Internos: {valores[8]} "  

        pass
    
    def get_valor_inicial(self):
        return self.valor_default
    
    def set_valor_inicial(self, valor:str):
        self.valor_default = valor

    def get_lst_rangos(self):
        return self.lst_rangos if self.lst_rangos else None
    
    # ╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦
    # BUSCAR RANGO .... POR NOMBRE O POR INDICE
    def buscar_rango(self, nombre_rango:str=None, b_index:bool=False, like_name:str='', flag:str=''):
        """ Busca un rango en lst_rangos. 
        [nombre_rango](str) = None, busca todos los ragos.
        [b_index](bool) = False , devuelve el rango. | True, devuelve el indice en lst_rangos. Si nnombre_a_buscar == None, b_index no tiene efecto.
        """
        # Validacion
        if not self.lst_rangos: 
            return None        
        # SI NO METE NOMBRE DE RANGO TIENES LA POSIBILIDAD DE OBTENER RANGOS POR LIKE Y POR FLAG
        if nombre_rango == None:
            if   like_name == '' and flag == '':
                """ DEVUELVE TODOS LOS RANGOS """
                return self.lst_rangos
            
            elif like_name == '' and flag != '':
                """ DEVULEVE TODOS LOS FLAGS """
                return [rango for rango in self.lst_rangos if flag == rango.flag] 
            
            elif like_name != '' and flag == '':
                """ DEVULEVE TODOS NOMBRES """
                return [rango for rango in self.lst_rangos if like_name in rango.nombre] 
            
            elif like_name != '' and flag != '':
                """ DEVULEVE POR NOMBRE Y POR FLAG  """
                return [rango for rango in self.lst_rangos if like_name in rango.nombre or flag == rango.flag] 
        else:
            # BUSCA POR EL NOMBRE. PUEDE DEVOLVER EL RANGO O EL INDICE DEL RANGO(UTIL PARA BORRAR RANGOS)
            for i, rango in enumerate(self.lst_rangos):
                if rango.nombre == nombre_rango:
                    if b_index == False:
                        return rango
                    else:
                        return i
        return None

    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    def pull(self, rango:str = None):
        """ >>> TIRA LOS DATOS DEL TABLERO HACIA UN RANGO PASADO COMO ARGUMENTO(to_rango=False). CRUZA CELDA A CELDA(self.cross de Rangos)
        [rango](str)(Rango): el nombre del rango que se quiere llenar de valores o el objeto Rango directamente al que le quiero pasar los valores.        


        """
        if not self.lst_rangos: return None
        
        if isinstance(rango, str):
            rango = self.buscar_rango(nombre_rango = rango)        
        elif isinstance(rango, Rango):
            pass
        else:
            return None
            
        if not rango: return None

        # ENVIO LOS VALORES AL RANGO CRUZANDO LAS CELDAS(cross)
        self.cross(rango, to_rango=True)

    # ■■■■■■■■■■■■■■■■■■■ PULL
    def pull_all(self, filtro:str=''):
        """ pasa todos los datos desde el tablero hacia los rangos de fila 
        y los carga en la matriz y dicc de Rango"""
        lst_rangos_to_pull = []
        try:
            # ■■■ CON O SIN FILTRO
            if filtro != '':
                lst_rangos_to_pull = [rango for rango in self.lst_rangos if filtro in rango.nombre and rango.b_ghost == False]
            else:
                lst_rangos_to_pull = [rango for rango in self.lst_rangos if rango.b_ghost == False]

            if not lst_rangos_to_pull:
                return None
            # ■■■ OPERACION
            for rango in lst_rangos_to_pull:
                self.cross(rango = rango, to_rango=True)            
                pass

        except Exception as e:
            print(f'{e}')
            return None
        finally:
            return True

    # ███████████████████████████████████████████████████████████████████████████████████
    # - C R E A R   R A N G O  - 
    def crear_rango(self, nombre:str, 
                    celda_inicio:str    = 'A:0', 
                    dimension:str       = '1x1', 
                    b_ghost:bool        = False, 
                    valor_default       = Celda.VALOR_INICIAL, 
                    go_to_lst_rangos:bool = True ):
        """
        Crea un nuevo rango si no existe un rango con el mismo nombre o propiedades.
            [nombre] (str): Nombre único para identificar el rango.
            [celda_inicio] (str): Celda inicial del rango (e.g., 'A:0').
            [dimension] (str): Dimensión del rango en formato 'FilasxColumnas' (e.g., '3x2').
            [b_ghost](bool):True (by Def), crea un rango y se carga desde tablero. 
                            False, para que un rango sea cargado desde tablero.
            [go_to_lst_rangos](bool): True(byDef) indica uqe se tiene que hacer append a lst_rangos. 
                                    False, indica que se devuelve el rango pero no se introduce en lst_rangos.
        Retorno:
            Rango: El rango creado si es válido y único.
            None: Si el rango ya existe o hay un error.
        Ejemplo:
            >>> tablero.crear_rango("MiRango", "A:0", "3x2")
            >>> tablero.crear_rango("MiRango", "A:0", "B:2")
        """

        if not self.matriz: return None     
        # EN CASO DE QUE NO META VALOR INICIAL Y SI EL VALOR INICIAL ES DISTINTO AL DE LA CELDA, PONGO EL ESTABLECIDO POR EL USUARIO
        if self.valor_default != Celda.VALOR_INICIAL and valor_default == Celda.VALOR_INICIAL:
            valor_default = self.valor_default

        rango = None
        try:
            rango = Rango(nombre_rango = nombre, celda_inicio = celda_inicio, dimension = dimension, valor_default=valor_default, b_ghost=b_ghost)
            """ ■■■ VALIDACIONES ■■■ """
            if rango:
                # NO ADMITO RANGOS OUT TABLERO.
                if self.celda_inicio.fila <= rango.celda_inicio.fila <= rango.celda_fin.fila <= self.celda_fin.fila:
                    if self.celda_inicio.columna <= rango.celda_inicio.columna <= rango.celda_fin.columna <= self.celda_fin.columna:
                        pass # :) OPCION CORRECTA. LO HAGO ASÍ POR COMPRENSION LECTORA.
                    else:
                        return None
                else:
                    return None

                # NO ADMITO NOMBRES REPETIDOS.
                if self.b_existe_nombre_rango(nombre_rango = rango.nombre) == True:  
                    print(f'Rango {rango.nombre} YA EXISTE :(')
                    return None

                # LOS FANTASMAS NO SE CARGAN DE TABLERO. SE CARGAN DE VALOR_INICIAL
                if rango.b_ghost == True:
                    rango.init_values(valor=self.valor_default)
                else:
                    self.cross(rango, to_rango=True)
                
                # VEO SI ES UN RANGO NUMERICO
                rango.es_numerico = self.es_rango_numerico(rango = rango )
                
                # LO METO EN LA SACA Y LO RETORNO
                if go_to_lst_rangos == True:
                    self.lst_rangos.append(rango)
                
                return rango
        except Exception as e:
            print(e)
            return None

    # VALIDA SI EXISTE UN NOMBRE DE UN RANGO EN LA LISTA DE RANGOS.
    def b_existe_nombre_rango(self, nombre_rango:str):
        if any(rango.nombre == nombre_rango for rango in self.lst_rangos):
            return True
        return False
    
    # ELIMINA RANGO DE LA LISTA
    def delete_rango(self, rango):
        """ Elimina un rango de la lista de Tablero self.lst_rangos """
        i_rango = None

        # ME PERMITE PODER PASAR O UN OBJETO RANGO O UN NOMBRE DE RANGO
        if isinstance(rango, str):
            i_rango = self.buscar_rango(nombre_rango = rango, b_index=True)        
        elif isinstance(rango, Rango):             
            i_rango = self.buscar_rango(nombre_rango = rango.nombre, b_index=True)        
        else:
            return False            
        # i_rango = self.buscar_rango(nombre_rango=nombre_rango, b_index=True)        
        if i_rango != None:
            try:
                rango = self.lst_rangos.pop(i_rango)
                return rango
            except Exception as e:
                print(f'Error Elimina Rango: :::: {e}')
                return Falso
        else:
            print(f'ESE RANGO: {nombre_rango}, NO ESTA REGISTRADO :( ')
            return False
    
    # ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    #                             -  MISCELANEA  -  
    # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄    
    
    # sssssssssssssssssssssssssssssssssssssssssssssssssss
    # C r e a   u n   n o m b r e   s e c u e n c i a l 
    def __new_nombre_secuencial(self, cadena:str, separador:str='_'):
        """ Crea un nuevo nombre en lst.rangos a partir de una cadena de head. """
        lst_nombres = [rango.nombre for rango in self.lst_rangos]
        lst_match = [nombre for nombre in lst_nombres if cadena in nombre]
        
        if lst_match:
            # Extraer el número secuencial al final de cada nombre
            lst_num = []
            for match in lst_match:
                partes = match.split(separador)
                if partes[-1].isdigit():
                    lst_num.append(int(partes[-1]))
            # Generar el nuevo nombre con el siguiente número
            nuevo_numero = max(lst_num) + 1 if lst_num else 0
            return f'{cadena}{nuevo_numero}'
        else:
            # Si no hay coincidencias, se usa el primer número
            return f'{cadena}0'

    # VALIDA SI LOS VALORES DE UN RANGO SON TODO NÚMEROS.
    def es_rango_numerico(self, rango):
        if not any ( rango.nombre == rango_reg.nombre for rango_reg in self.lst_rangos ):
            return False
        try:
            # INTENTO CONVERTIR A ENTERO. NO SIGNIFICA QUE HAYA NÚMEROS, SINO QUE LOS PUEDO CONVERTIR.
            for celda in rango.lst_celdas:
                valor = int(celda.valor)
            return True
        except Exception as e:
            return False    

    # ■■■■■■■■■■■■■■■■■■■ IMPRIMIR
    def ver_rangos(self, nombre_rango:str = '' , like_name:str='', flag:str = ''):
        """ Imprime por consola los rangos (tanto valores como datos) de los rangos que no estan marcados b_oculto. 
        [nombre_rango](str) =>None, imprime todo | =>str imprime el rango elegido si no es b_oculto.
        [b_valores](bool): =>False, imprime los datos del rango =>True, imprime los datos de los rangos
        >>> Ejemplo_1: tablero_ej.ver_rango(nombre_rango='r1', b_valores=False) => ver las propiedades de 'r1' por terminal.
        >>> Ejemplo_2: tablero_ej.ver_rango(nombre_rango='r1', b_valores=True) => ver los valores de 'r1' por terminal.
        >>> Ejemplo_3: tablero_ej.ver_rango(nombre_rango=None, b_valores=True) => ver los valores de todos los rangos por terminal.
        >>> Ejemplo_4: tablero_ej.ver_rango(nombre_rango=None, b_valores=False) => ver las propiedades de todos los rangos por terminal.
        """
        if not self.lst_rangos:        
            return
        
        if nombre_rango == '':
            # TODOS            
            for i, rango in enumerate(self.lst_rangos):                
                rango.b_print_cabecera = True
                if i != 0: 
                    rango.b_print_cabecera = False             
                # SI INTRODUCE LOS FILTROS like_name ó flag SE SOLO IMPRIME LOS FILTROS.
                if (like_name != '' and like_name in rango.nombre) or (flag!='' and flag == rango.flag) :
                    # IMPRIME EL __str__ DE LA CLASE RANGO
                    print(rango)
                elif like_name == '' and flag == '':
                    print(rango)
                else:
                    continue
        elif nombre_rango != '':
            # X NOMBRE
            for rango in self.lst_rangos:
                if rango.nombre == nombre_rango:                    
                    rango.b_print_cabecera = True                        
                    print(rango) 
                    break                                   
        
        # Y PROCURO DEJAR TODO COMO ESTABA
        self.b_print_cabecera = True
    
    # MISCELANEA. NO USADO. DEFINE EL TIPO DE RANGO QUE SE PASA.
    def get_rango_type(self, nombre_rango:str):
        """ >>> un rango puede ser: de celda, de fila, de columna , de cuadrado, de rectangulo """
        rango = self.buscar_rango(nombre_rango = nombre_rango)    
        if self.valida_limites_rango(rango=rango) == False: return None
        if not rango: return None        
        if rango.total_filas == 1 and rango.total_columnas == 1:
            typo = Type_Rng(CELDA)        
        elif rango.total_filas == 1:
            typo = Type_Rng(COL)
        elif rango.total_columnas == 1:
            typo = Type_Rng(FIL)
        if rango.total_filas == rango.total_columnas :
            typo = Type_Rng(CUADR)
        else:
            typo = Type_Rng(RECTG)
        return typo

# ████████████████████████████████████████████████████████████████████████████████████████████████████████████
# ████████████████████████████████████████████████████████████████████████████████████████████████████████████
 
#                                           -   F R A N K Y   -  

# ████████████████████████████████████████████████████████████████████████████████████████████████████████████
# ████████████████████████████████████████████████████████████████████████████████████████████████████████████

# Usa la clase Tablero para Crear un Menu con 3 tableros distintos: Head, Body(self), Pie 
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

# •••••••••••••••••••••••••••••••••
# VARIABLES GLOBALES Y CONSTANTES 
import pyfiglet                                     # Letras compuestas de diferentes tamaños
from colorama import init , Fore, Back, Style       # Colores
init(autoreset=True)                                # Colores Para windows

# ■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■
class F_r_a_n_k_y(Tablero):
    """ ■■■■  DEFINE LAS PARTES ESENCIALES DE UN MENU CREANDO Y MANTENIEDO UNA LISTA DE TABLEROS ( Head + Cuerpo + Pie )
    
    >>> Linaje ::: Celda ► Rango ► Tablero ► F_r_a_n_k_y   

    Definicion de Franky(por linea): 
    char_head  => margen + char_marco * total
    Head    => margen + char_marco + x_pad +DATA_ENTRADA) + pad_x + char_marco
    char_up_body  => margen + char_marco * total

    Cuerpo(x Fila)  => :  margen + marco_v + X_pad + DATA + pad_x + marco

    char_down_body   => margen + marco_h_fin_datos * total
    Pie     => margen + char_marco +  DATA_SALIDA + char_marco
    char_pie   => margen + char_marco * total

    >>> DATA_ENTRADA:  Datos de entrada(HEAD) del menu. Puede ser un str o una lista de str o matriz de str
    >>> DATA:          Datos del cuerpo del menu. Puede ser un str o una lista de str o matriz de str
    >>> DATA_SALIDA:   Datos de salida(PIE) del menu. Puede ser un str o una lista de str o matriz de str
    """
    RESET_ALL = f'{Style.RESET_ALL}'            # ► cte colorama para quitar todos los formatos ANSI establecidos.
    lista_family = ['MOSAICO', 'FIX', 'MAX']    
    FRANKY_STYLE = {'char_head' : '▄',        # ► Char de arriba del HEAD ■ 
                    'char_up_body'  : '▄' ,   # Char bajo el HEAD / sobre el BODY
                    'char_down_body': '▀' ,   # Char de arriba el PIE / bajo el BODY
                    'char_pie'   : '▀'  ,     # Char del abajo del PIE.
                    'char_marco' : '█'  ,     # Char Horizontal del BODY
                    'x_pad' : 0   ,           # Espacio entre el char_marco izquierdo y el Tablero.
                    'pad_x' : 5               # Espacio entre el último caracter mayor de (HEAD/BODY/PIE) y el char_marco derecho.
                    }            
    
    ESTILOS_FRANKY = {
        "default": {              # clasic
            "char_head":    "+" , 
            "up_body":      "-" ,
            "down_body":    "-" ,
            "char_pie":     "+" ,
            'char_marco' :  '|' ,
            'x_pad' :       2   ,
            'pad_x' :       5   ,
            'margen':       0
        },
        "unicode": {                # algo mas moderno que el clasic
            "char_head":    "═" ,
            "up_body":      "─" ,
            "down_body":    "─" ,
            "char_pie":     "═" ,         
            'char_marco' :  '┼' ,
            'x_pad' :       2   ,
            'pad_x' :       5   ,
            'margen':       0
        },
        "doble": {                  # doble
            "char_head":    "═" ,
            "up_body":      "═" ,
            "down_body":    "═" ,
            "char_pie":     "═" ,                      
            'char_marco' :  '║' ,
            'x_pad' :       2   ,
            'pad_x' :       7   ,
            'margen':       0
        },
        "vacio": {                  # sin nada, compacto
            "char_head":    '' ,
            "up_body":      '' ,
            "down_body":    '' ,
            "char_pie":     '' ,
            'char_marco' :  '' ,
            'x_pad' :       1  ,
            'pad_x' :       3  ,
            'margen':       0
        },         
        "moderno": {               # compacto y con color
            "char_head":    f'{Fore.CYAN}•{Style.RESET_ALL}' ,
            "up_body":      f'{Fore.CYAN}•{Style.RESET_ALL}' , 
            "down_body":    f'{Fore.CYAN}─{Style.RESET_ALL}' ,
            "char_pie":     f'{Fore.CYAN}─{Style.RESET_ALL}' ,
            'char_marco':   f'{Fore.CYAN}█{Style.RESET_ALL}' ,
            'x_pad' :       1  ,
            'pad_x' :       3  ,
            'margen':       10          # flotante
        }, 
        "elegante": {
            "char_head":   "▀"  ,       # primer marco arriba del head.
            "up_body":     "▄"  ,       # char marco de arriba del body.
            "down_body":   "▀"  ,       # char marco de abajo del body.
            "char_pie":   "▄"   ,       # char marco de abajo del pie.
            'char_marco':   '▓' ,       # char marco de los laterales.
            'x_pad' :      3    ,       # pad izquierdo.
            'pad_x' :      10   ,       # pad derecho.
            'margen':      0            # flotante.
        },
        "franky": {                 # (byDef)
            "char_head":    "▄" ,       
            "up_body":      "▄" ,       
            "down_body":    "▀" ,       
            "char_pie":     "▀" ,        
            'char_marco' :  '█' ,        
            'x_pad' :       3   ,       
            'pad_x' :       10  ,
            'margen':       0
        }
    }
    COLOR_MAP = {
        # Colores básicos
        'black': Fore.BLACK,
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'purple': Fore.MAGENTA,        # púrpura ≈ magenta en terminales
        'cyan': Fore.CYAN,
        'white': Fore.WHITE,
        
        # Colores claros (light)
        'lblack': Fore.LIGHTBLACK_EX,   # gris
        'lred': Fore.LIGHTRED_EX,
        'lgreen': Fore.LIGHTGREEN_EX,
        'lyellow': Fore.LIGHTYELLOW_EX,
        'lblue': Fore.LIGHTBLUE_EX,
        'lmagenta': Fore.LIGHTMAGENTA_EX,
        'lcyan': Fore.LIGHTCYAN_EX,
        'lwhite': Fore.LIGHTWHITE_EX,  # blanco brillante
        
        # Alias y variantes
        'grey': Fore.LIGHTBLACK_EX,    # alias para lblack
        'gray': Fore.LIGHTBLACK_EX,    # ortografía alternativa
        'lgrey': Fore.LIGHTWHITE_EX,
        'dgrey': Fore.LIGHTBLACK_EX,
        
        # Especiales
        'default': Fore.RESET,
        'reset': Fore.RESET,
        'none': Fore.RESET,
        
        # Puedes añadir más combinaciones si lo deseas
        'pink': Fore.LIGHTMAGENTA_EX,  # alias para lmagenta
        'lime': Fore.LIGHTGREEN_EX,    # alias para lgreen
        'aqua': Fore.LIGHTCYAN_EX,     # alias para lcyan
    }

    def __init__( self, dimension:str= "20x30" , 
                        head_datapush = None , 
                        pie_datapush = None , 
                        margen:int = 0 ,  
                        pad_x:int = 20 , 
                        x_pad:int = 2 ):        
        """ ■■■■ Inicializa el Menu con los valores de la cabecera y el pie.
        [dimension](str): Dimension del Menu
        [head_datapush](str)(list): Frase del Head
        [pie_datapush]:(str)(list): Frase del Pie
        [x_pad]:                    Espacio interior entre el marco y el contenido
        [pad_x](int):               Espacio interior desde el último caracter de la linea y el margen
        [margen](int):              Espacio entre el inicio del Screen y el principio del Brackets.
        """        
        
        self.NUM_CHAR = 40                        
        self.ESPACIO  = ' ' 
        if not isinstance(dimension, str):
            print(f'ERROR::: {dimension} :(')
            return None

        # ■■■■■ CACHA LAS FILAS Y LAS COLUMNAS POR LA DIMENSION .... Lo necesito para llamar a super()
        num_filas, num_columnas = SttS.filas_columnas_from_dimension(dimension=dimension)
        if not num_filas   or  not num_columnas: return None

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        # ■■■■■ CREA EL TABLERO BODY ■■■■■ SOY EL RANGO CUERPO PRINCIPAL ■■■■■■■■■■
        super().__init__(total_columnas_tablero = num_columnas, 
                        total_filas_tablero = num_filas , 
                        valor_default = '' )
        
        if not self.lst_rangos or not self.matriz: 
            print('\n\nNO SE HA PODIDO CREAR EL TABLERO.!!!!!!\n\n')
            return None
        
        # ■■■■■■ Diccionario de tipos de impresion byDef de Head Body y Pie. 
        self.dicc_print = {'head': {'lista': None, 'ancho_columna': None, 'sp_between': 1},    # ■ ■ ■ 'MAX'
                            'body': {'lista': None, 'ancho_columna': None, 'sp_between': 1},    # ■ ■ ■ 'MAX'
                            'pie':  {'lista': None, 'ancho_columna': None, 'sp_between': 1}     # ■ ■ ■ 'MAX'
                        }
         
        # ■■■■■ DEFINICION DE LOS ESPACIOS HORIZONTALES
        self.margen:int = margen    # ESPACIO entre el inicio y el char_marco izq
        self.x_pad:int  = x_pad     # ESPACIO entre el char_marco y la columna 'A' (inicio de contenido)
        self.pad_x:int  = pad_x     # ESPACIO entre el final del contenido y el char_marco derecho

        # ■■■■■ CARACTERES VERTICALES PARA EL MARCO DEL TABLERO PPAL (CUERPO) 
        self.char_marco:str     = self.FRANKY_STYLE.get('char_marco', '█')          # caracter de la linea de inicio y cierre de: Head / Body / Pie
        # ■■■■■ CHARS HORIZONTALES PARA EL MARCO DE LA CABECERA Y EL PIE
        self.char_head:str      = self.FRANKY_STYLE.get('char_head', '▄')           # up caracter de la primera linea de cabecera.
        self.char_up_body:str   = self.FRANKY_STYLE.get('char_up_body', '▄')        # down - caracter de la linea de cierre del Head
        self.char_down_body:str = self.FRANKY_STYLE.get('char_down_body', '▄')      # caracter de la linea de cierre               
        self.char_pie:str       = self.FRANKY_STYLE.get('char_pie', '■')            # down - caracter de la ultima linea de cierre del Pie
        
        # ■■■■■ DATOS DE HEAD Y PIE
        self.head_datapush = head_datapush      # Data Que se pone en el Head del Menu: (frase, rango, matriz, lista)                
        self.pie_datapush = pie_datapush        # informacion del pie(Salida Help Repeat)

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■       
        # ■■■■■ CREAR TABLERO:  HEAD ■■■■■■     
        self.head = None          
        if self.head_datapush:                  # Puede venir en formato string, list o matriz(list de list de str).
            if isinstance(self.head_datapush, str):
                """ ■■■ CADENA  """
                self.head  = Tablero( total_columnas_tablero = num_columnas, total_filas_tablero = 1 )
            elif isinstance(self.head_datapush, list):
                if SttS.es_matriz(matriz = self.head_datapush):
                    """ ■■■ MATRIZ """
                    filas = len(self.head_datapush)                                    
                    self.head  = Tablero( total_columnas_tablero = num_columnas, total_filas_tablero = filas )
                else:
                    """ ■■■ LISTA """
                    self.head  = Tablero( total_columnas_tablero = num_columnas, total_filas_tablero = 1 )
                pass
            # Empuja los datos al Tablero recien creado
            self.head.push( data_push = self.head_datapush , celda_inicio = 'A:0' )
        

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        #  ■■■■■ CREAR TABLERO:  PIE ■■■■■
        self.pie = None
        if self.pie_datapush:            
            # EL MENSAJE DE PIE PUEDE VENIR COMO STR , LIST, MATRIZ(LIST d LIST)
            if isinstance(self.pie_datapush, str):
                """ ■■■ CADENA """
                self.pie  = Tablero( total_columnas_tablero = num_columnas, total_filas_tablero = 1 )

            elif isinstance(self.pie_datapush, list):
                if SttS.es_matriz(matriz = self.pie_datapush):
                    """ ■■■ MATRIZ """
                    filas = len(self.pie_datapush)
                    self.pie  = Tablero( total_columnas_tablero = num_columnas, total_filas_tablero = filas ) 
                else:
                    """ ■■■ LISTA """
                    # VALIDAR SI LEN(LISTA) > NUM_COLUMNAS                    
                    self.pie  = Tablero( total_columnas_tablero = num_columnas, total_filas_tablero = 1 )

            # data_push = self.magen*self.ESPACIO + self.char_marco + self.x_pad + self.pie_datapush + diferencia + self.pad_x + self.char_marco
            self.pie.push( data_push=self.pie_datapush, celda_inicio = 'A:0' )

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■■■ ESTILO 
        self.estilo = "franky"      # pongo el estilo por defecto. self.style() tiene que recogerlo ahora y asignarlo.

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■■■ IMPRESION ■■■■■■■■■■■■■■■■■■
        
        self.sp_between: int = 0            # Espacio entre celdas
        self.ancho_columna: int = None      # Ancho de las columnas del tablero. Si es None, se calcula el len del valor mas largo de la columna
        self.lista: list = None             # Lista de datos a imprimir en el tablero.  [ 7,7,8,5 ] pej.
        self.matriz_V_bruto:  list = None     # matriz de valores de celdas a imprimir en bruto(con codigos de color colorama).
        self.matriz_L_limpio: list = None     # matriz de valores de celdas a imprimir sin codigos de color colorama.

        self.matriz_F: list = None          # matriz de Formato de celdas a imprimir 
        self.matriz_V: list = None          # matriz de Valores de celdas a imprimir


        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■■■■ CREAR TABLERO:  HEAD EXCEL ■■■■■■               A B C D E F ......
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■               #   ► IF b_excel == True   ►  Es un ayudante ► Tablero Excel (filas numericas y columnas Letras)        
        
        self.head_excel = None                  # Tablero Excel (filas numericas y columnas Letras). Es fijo y se define por el número de columnas. 
        self.b_excel:bool = False               # Imprime las Columnas en la cabecera y los numeros en las filas..... ayuda para colocar datos.
        self.color_excel = f'{Fore.MAGENTA}'    # color alterno de head_excel. para filas y para columnas.
        
        self.head_excel  = Tablero( total_columnas_tablero = num_columnas, total_filas_tablero = 1 )    # ■ Creo el Tablero head_excel
        # Creo una lista de datos que es lo que vamos a insertar en el Tablero head_excel. El Color va en las posiciones pares.
        data_head_excel = [f'{Style.RESET_ALL}{self.color_excel}{SttS._may_nl[j]}' if j % 2 == 0 else f'{Style.RESET_ALL}{SttS._may_nl[j]}' for j in range(num_columnas) ]
        ret_push = self.head_excel.push( data_push = data_head_excel , celda_inicio = 'A:0', eje='X' )  # ■ Introduce los datos del head_excel en su tablero. Siempre en A:0 y como lista horizontal(eje='X')


        """ 
        •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
        UNA VEZ CREADOS LOS TABLEROS, SE PUEDE HACER: PUSH , IMPRIMIR , GETTING, PULL , CREAR RANGOS SOBRE SELF( F_r_a_n_k_y )
        ...Y TODO LO REFERNTE A LOS CARACTERES Y LOS MENSAJES HEAD Y PIE EN:  ■■ self.style()
        ••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• 
        """

    """ ■254  █219  ▄220  ▀223  ••••• LE PONEMOS LOS BRACKETS A FRANKY •••••• """
    # IMPRIMIR LA CLASE POR NOMBRE: IMPRIMIR FRANKY ENTERO
    def __str__(self):                
        return f('Tablero Franky:\n■ Dimension head: {self.head.dimension if self.head else "SIN HEAD"} \n■ Dimension Body: {self.dimension} \n■ Dimension Pie:  {self.head.dimension if self.pie else "SIN PIE"}')
    
    # GETTER HEAD:  
    def get_head(self):
        """ GETTER HEAD:  Devuelve El Tablero HEAD or None ....Puede servir para validar en caso de que devuelva None """
        return self.head if self.head else None
    
    # SETTER HEAD: CREA UN NUEVO HEAD Y DESTRUYE EL ANTERIOR... SI QUIERO MODIFICAR EL HEAD ANTERIOR: self.head.push()
    def set_head(self, data_push ):
        """ ■■■ ESTABLECE EL HEAD A Través de su Valor ....Hay Que Tener En Cuenta Que Head Puede Existir or Not.
        [data_push](str, list, matriz): Dato que se quiere poner en el Head. Es un Tablero, así que se usa push para poner datos.
        Pone a None el Head anterior y crea uno nuevo, no añade al head anterior ...Si quiero añadir al head anterior Tienes self.head.push()
        ► CALLED: None
        """
        # ANALIZO EL DATO DATA_PUSH: b_lineal = False, meto los datos de forma matricial, eje = 'X', siempre sobre el eje X, estamos en head!! b_repetir = False, en head no se repite nada. solo info.
        dimension_data_push = self.get_dimension_data_push(data_push=data_push, b_lineal=False, eje='X', b_repetir=False)
        if self.head: self.head = None
        
        filas, columnas =  SttS.filas_columnas_from_dimension(dimension=dimension_data_push)
        if not filas or not columnas: 
            print(f"Error::: de dimension{dimension_data_push}")
            return None

        # ███ Creo el tablero Head::: No varío las columnas del Head, sólo las filas.
        self.head  = Tablero( total_columnas_tablero = self.total_columnas, total_filas_tablero = filas )
        if not self.head: 
            print(f'Error::: Creacion del Head')
            return None
        
        # METO LOS DATOS EN EL TABLERO CREADO
        self.head.push( data_push = data_push , celda_inicio = 'A:0' )        
        
        self.head_datapush = data_push                                  # Actualizo el head_datapush con el nuevo valor de data_push
        
        # RETORNO EL HEAD 
        return self.head

    # ■■■■■■■■ SET STYLE PRINT TABLERO: Establece el estilo de impresión para HeadOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    def set_family_head(self, lista:list=None, ancho_columna:int=None, sp_between:int=0):
        """ ■■ Establece el estilo de impresión para el Tablero Head.
        [lista] (list, opcional): Lista de datos a imprimir en el tablero.
        [ancho] (int, opcional): Ancho del tablero.
        [sp_between] (int, opcional): Espacio entre los elementos impresos.
        ► CALLED: None
        ■ EJEMPLO: VER set_family_pie()
        """        
        lista, ancho, sp_between, fila_from , fila_to = self.__ok_data(tablero = self.head, lista = lista , ancho_columna = ancho_columna , sp_between = sp_between )
        if sp_between == None and fila_from == None and fila_to == None: 
            print(f'Error de Entrada de datos, se mantienen los valores anteriores validos para Head: ■ lista: {lista} ■ ancho: {ancho_columna} ■ sp_between: {sp_between}')
            return None

        self.dicc_print['head']['lista'] = lista
        self.dicc_print['head']['ancho_columna'] = ancho
        self.dicc_print['head']['sp_between'] = sp_between
        return True
    
    def get_pie(self):
        """ ■ getter del Tablero self.pie:  Devuelve el Tablero Pie .... Puede servir para validar en caso de que devuelva None 
        """
        return self.pie if self.pie else None
    
    # SETTER PIE: CREA UN NUEVO PIE Y DESTRUYE EL ANTERIOR... SI QUIERO MODIFICAR EL PIE EXISTENTE: self.pie.push()
    def set_pie(self, data_push):
        """ ■■■ ESTABLECE EL PIE or EL VALOR EN EL PIE ....Hay Que Tener En Cuenta Que PIE Puede Existir or Not.
        [data_push](str, list, matriz): Dato que se quiere poner en el Head. Es un Tablero, así que se usa push para poner datos.
        ► CALLED: None
        """
        # ANALIZO EL DATO DATA_PUSH: b_lineal = False, meto los datos de forma matricial, eje = 'X', siempre sobre el eje X, estamos en head!! b_repetir = False, en head no se repite nada. solo info.
        dimension_data_push = self.get_dimension_data_push(data_push=data_push, b_lineal=False, eje='X', b_repetir=False)
        if self.pie: self.pie = None
        
        filas, columnas =  SttS.filas_columnas_from_dimension(dimension=dimension_data_push)
        if not filas or not columnas: 
            print(f"Error::: de dimension{dimension_data_push}")
            return None
        # ███ Creo el tablero Head::: No varío las columnas del Head, sólo las filas.
        self.pie  = Tablero( total_columnas_tablero = self.total_columnas, total_filas_tablero = filas )
        if not self.pie: 
            print(f'Error::: Creacion del Pie')
            return None
        
        # METO LOS DATOS EN EL TABLERO CREADO
        self.pie.push( data_push = data_push , celda_inicio = 'A:0' )        
        
        # RETORNO EL HEAD 
        return self.pie

    # ■■■■■■■■ SET STYLE PRINT TABLERO: Establece el estilo de impresión para Headooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    def set_family_pie(self, lista:list=None, ancho_columna:int=None, sp_between:int=0):
        """ ■■ Permite Establecer el estilo de impresión  para el Tablero Pie.
        [lista] (list, opcional): Lista de datos a imprimir en el tablero.
        [ancho] (int, opcional): Ancho del tablero.
        [sp_between] (int, opcional): Espacio entre los elementos impresos.
        ► CALLED: None
        ■ EJEMPLO:
            set_family_pie(lista=None, ancho_columna=0, sp_between=0)           ► LITERAL    
            set_family_pie(lista=None, ancho_columna=0, sp_between=2)           ► MOSAICO
            set_family_pie(lista=None, ancho_columna=None, sp_between=0)        ► MAX
            set_family_pie(lista=None, ancho_columna=None, sp_between = 2)      ► MAX
            set_family_pie(lista=None, ancho_columna = 5, sp_between = 2)       ► FIX
            set_family_pie(lista=[7,7], ancho_columna = 5, sp_between = 2)      ► LISTA-FIX
            set_family_pie(lista=[7,7], ancho_columna = None, sp_between = 2)   ► LISTA-MAX
            set_family_pie(lista=[7,7], ancho_columna = 0, sp_between = 2)      ► LISTA-MOSAICO
        """        
        lista, ancho, sp_between, fila_from , fila_to = self.__ok_data(tablero = self.pie, lista = lista , ancho_columna = ancho_columna , sp_between = sp_between )
        if sp_between == None and fila_from == None and fila_to == None: 
            print(f'Error de Entrada de datos, se mantienen los valores anteriores validos para el Pie: ■ lista: {self.dicc_print['pie']['lista']} ■ ancho: {self.dicc_print['pie']['ancho_columna']} ■ sp_between: {self.dicc_print['pie']['sp_between']}')
            return None

        self.dicc_print['pie']['lista'] = lista
        self.dicc_print['pie']['ancho_columna'] = ancho
        self.dicc_print['pie']['sp_between'] = sp_between
        return True

    def set_excel(self, b_excel:bool = False):
        """ ■■ Establece el modo Excel para el Tablero Franky. Sustituye el head por el nombre de las columnas (A, B, C....) y el número de filas(1, 2, 3, ... )
        [b_excel](bool): Si es True, se activa el modo Excel, que imprime las columnas en la cabecera y los números en las filas.
        ► CALLED: None
        """
        self.b_excel = b_excel
        return self.b_excel
    
    def set_color_excel(self, color:str=Fore.MAGENTA):
        """ ■ Pone un color en las letras Excel de Cabecera(Tablero self.head_excel) ► A, B, C, D....AZ y los números de fila (1, 2, 3.. n)
        Realmente, cambia el color y cambia la cabecera.
        ► CALLED: None
        ■ EJEMPLOs:
            ■ self.set_color_excel(color=Fore.YELLOW)     ► 'YELLOW'
            ■ self.set_color_excel()                      ► 'MAGENTA'
        """
        
        colores_validos = [
            Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.RESET,
            Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE, Back.RESET
        ]
        
        if color not in colores_validos:
            self.color_excel = f'{Fore.MAGENTA}'
        else:
            self.color_excel = color
        
        # Y CAMBIO LA CABECERA PARA QUE CACHE EL NUEVO COLOR        
        data_head_excel = [f'{Style.RESET_ALL}{self.color_excel}{SttS._may_nl[j]}' if j % 2 == 0 else f'{Style.RESET_ALL}{SttS._may_nl[j]}' for j in range(self.total_columnas) ]
        # INTRODUCE LOS DATOS DE HEAD-EXCEL EN SU TABLERO
        ret_push = self.head_excel.push( data_push = data_head_excel , celda_inicio = 'A:0', eje='X' )
        if ret_push == None: 
            return False
        return True
        

    # ████████████████████████████████████████████████████████████████████
    # CAMBIA EL ESTILO(CARACTERES DE CABECERA, PIE, PRE-NUM , POST-NUM )
    """ ■254  ▄220  ▀223  █219  ••••• LE PONEMOS LOS BRACKETS A FRANKY •••••• """    
    def style(self, estilo:str=None, **kwargs):
        """ 
        Modifica el estilo del Tablero  Franky.
        
        ■ Si 'estilo' es un string válido en 'ESTILOS_FRANKY', se aplican esos valores primero.
        ■ Luego, cualquier 'kwargs' proporcionado sobrescribe los valores del estilo.
        ■ Si no se proporciona 'estilo' ni 'kwargs', se usa el estilo '"franky"' por defecto.
        
        Argumentos en 'kwargs' (todos opcionales):
            ■ [char_head](str): Caracter de arriba del HEAD.
            ■ [up_body](str): Caracter bajo el HEAD / sobre el BODY.
            ■ [down_body](str): Caracter de arriba del PIE / bajo el BODY.
            ■ [char_marco](str): Caracter de los bordes verticales.
            ■ [char_pie](str): Caracter de la parte inferior.
            ■ [pad_x](int): Espacio entre el último caracter y el borde derecho.
            ■ [x_pad](int): Espacio entre el borde izquierdo y el inicio del contenido.
        ► CALLED: None
        ■ EJEMPLOS:
            ■ obj.style(estilo="ascii")                         ► Carga el estilo "ascii" y lo aplica a self
            ■ obj.style(estilo="doble", char_pie="*", pad_x=15) ► Carga "doble" y cambia char_pie a "*" y pad_x a 15
            ■ obj.style(char_head="@", char_pie="#")            ► Solo se aplican los valores de kwargs, sin cargar un estilo.
            ■ obj.style()                                       ► Carga el estilo "franky" automáticamente.
        """
        if estilo != None:
            if estilo in self.ESTILOS_FRANKY.keys():            # entra estilo AND está en keys.... se asigna
                self.char_head      = self.ESTILOS_FRANKY[estilo]["char_head"]
                self.char_up_body   = self.ESTILOS_FRANKY[estilo]["up_body"]
                self.char_down_body = self.ESTILOS_FRANKY[estilo]["down_body"]
                self.char_pie       = self.ESTILOS_FRANKY[estilo]["char_pie"]
                self.char_marco     = self.ESTILOS_FRANKY[estilo]["char_marco"]
                self.x_pad          = int(self.ESTILOS_FRANKY[estilo]["x_pad"])
                self.pad_x          = int(self.ESTILOS_FRANKY[estilo]["pad_x"])       
                self.margen          = int(self.ESTILOS_FRANKY[estilo]["margen"])   

        elif estilo is None and len(kwargs) == 0:       # llamada sin parametros: style()
                self.char_head      = self.ESTILOS_FRANKY['franky']["char_head"]
                self.char_up_body   = self.ESTILOS_FRANKY['franky']["up_body"]
                self.char_down_body = self.ESTILOS_FRANKY['franky']["down_body"]
                self.char_pie       = self.ESTILOS_FRANKY['franky']["char_pie"]
                self.char_marco     = self.ESTILOS_FRANKY['franky']["char_marco"]
                self.x_pad          = self.ESTILOS_FRANKY['franky']["x_pad"]
                self.pad_x          = self.ESTILOS_FRANKY['franky']["pad_x"]
                self.margen          = int(self.ESTILOS_FRANKY['franky']["margen"])      
                # RETORNA PQ YA ESTÁ TODO EL PESCADO VENDIDO :) 
                return True
        
        # # Aplicar valores de kwargs si fueron proporcionados, si no, pone el mismo caracter que tenía.
        self.char_head      = kwargs.get("char_head", self.char_head)
        self.char_up_body   = kwargs.get("up_body", self.char_up_body)
        self.char_down_body = kwargs.get("down_body", self.char_down_body)
        self.char_pie       = kwargs.get("char_pie", self.char_pie)
        self.char_marco     = kwargs.get("char_marco", self.char_marco)
        self.x_pad          = int(kwargs.get("x_pad", self.x_pad))
        self.pad_x          = int(kwargs.get("pad_x", self.pad_x))
        self.margen         = int(kwargs.get("margen", self.margen))

    # ◘◘◘◘◘◘◘ Pone un Formato Cuadrado sobre la última columna usada. entre sp_between y ancho_columna
    def __get_lst_formato_cuadrado(self, baseline_format:str, sp_between:int = 0, tablero = None):
        """ ■■■ GENERA LA LISTA DE FORMATOS DE LA MAXIMA LONGITUD X COLUMNA.
        ■ [baseline_format](str): linea Base del formato.
             ► '{:<0}{:<2}{:<0}{:<2}{:<0}{:<2}{:<0}{:<2}{:<0}{:<2}{:<0}{:<2}'
        ■ [sp_between](int)=0: espacio entre columnas.
        ■ [tablero](Tablero): Instancia de un Objeto Tablero.
        ■ CALLED::: ► __get_matrices_formato() ► __ruta_natural() ► __ruta_cuadrado()
        ■ EJEMPLO:
            matriz_LIST_F_cuadrado = self.__get_lst_formato_cuadrado(baseline_format = baseline_format, sp_between = 2 , tablero = self/None/self.head/self.pie/self.head_excel )
        ■ SALIDA:
           ['{:<35}{:<2}{:<4}{:<2}{:<9}{:<2}{:<6}{:<0}{:<0}{:<0}{:<0}{:<0}', 
           '{:<35}{:<2}{:<4}{:<2}{:<9}{:<2}{:<6}{:<0}{:<0}{:<0}{:<0}{:<0}', 
           '{:<35}{:<2}{:<4}{:<2}{:<9}{:<2}{:<6}{:<0}{:<0}{:<0}{:<0}{:<0}', 
           '{:<35}{:<2}{:<4}{:<2}{:<9}{:<2}{:<6}{:<0}{:<0}{:<0}{:<0}{:<0}']
        """
        if tablero is None:
            tablero = self

        if  not tablero.matriz:
            print('Error::: __get_lst_formato_cuadrado() ::: No hay matriz')
            return None
        numero_de_filas = len(tablero.matriz)
        
        # ████ Re-convierte el baseline_format a una Matriz X su Numero de Filas.
        lst_cad_formato_body = [ baseline_format for i in range (numero_de_filas) ]
        
        # ULTIMA COLUMNA USADA
        last_columna_used = tablero.get_last_columna_used()  # ■■ Devuelve la última columna usada en el tablero.
        if last_columna_used is None:
            last_columna_used = 0

        ANCHO = 0   # cte del ancho del formato del binomio.
        BETWEEN = 1 # cte del sp_between del formato del binomio.
        new_lst_formato = []
        for i, cadena_formato_fila in enumerate(lst_cad_formato_body):
            lst_binomios = re.findall(r'({:[<>^]\d+})({:[<>^]\d+})', cadena_formato_fila)
            if not lst_binomios: 
                return None
            
            new_lst_formato_fila = []
            for b , binomio in enumerate(lst_binomios):
                if b < last_columna_used:                                        
                    new_lst_formato_fila.append(binomio[ANCHO])
                    new_lst_formato_fila.append(binomio[BETWEEN])
                elif b == last_columna_used:    # ■ En La Ultima Columna Used No Incluyo El Sp_Between en el formato...lo pongo a {:<0} (Zero)
                        new_lst_formato_fila.append(binomio[ANCHO])
                        new_lst_formato_fila.append('{:<0}')
                else:                           # ■ A partir de La Ultima Columna Used todo el formato a Zero.
                    new_lst_formato_fila.append('{:<0}')
                    new_lst_formato_fila.append('{:<0}')
            pass
            # new_lst_formato.append(new_lst_formato_fila))
            new_lst_formato.append(''.join(new_lst_formato_fila))
        pass
        return new_lst_formato
    
    # ◘◘◘◘◘◘◘ 
    def __get_lst_formato_natural(self, baseline_format: str, sp_between:int = 0, tablero = None):
        """ ■■■■■ Genera una lista de formatos ajustados a la última columna utilizada en cada fila y ajustando todas las filas 
        a la última columna utilizada en la fila más larga.
        ■ [baseline_format](str) ► '{:<0}{:<2}{:<0}{:<2}{:<0}{:<2}{:<0}{:<2}{:<0}{:<2}{:<0}{:<2}'
        ■ [b_between] (bool): Indica si se usa lst_formato_between (True) o lst_formato_ancho_columna (False).
        ■ [tablero](Tablero): Instancia de un objeto Tablero. (self, self.head, self.pie, self.head_excel)
        ► CALLED:   ► self.__get_matrices_formato() ► self.__ruta_natural()
        ■ EJEMPLO:
            matriz_LIST_F_natural  = self.__get_lst_formato_natural( baseline_format = baseline_format, sp_between = sp_between , tablero = tablero)
        ■ SALIDA:   
            ['{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}', 
            '{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}', 
            '{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}', 
            '{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}']
        """
        if tablero is None:
            tablero = self
        # ■■ Lista De Int Con La Ultima Columna Usada Por Fila. Zero No Implica Que No Haya Datos En La Columna 0(A:0, B:0, ...)
        lst_last_columna_used:list = tablero.get_lst_last_columna_used_xfila()         
        last_columna_matriz:int = max(lst_last_columna_used)        # ■■ INT , ULTIMA COLUMNA USADA DE TODAS LAS FILAS
        lst_len_organico_xfila = self.__get_lst_len_natural(sp_between = sp_between, tablero = tablero)  # ■■ LISTA DE LONGITUDES ■ ORGANICA ■ 

        """ ■■■■ Divido el baseline_format en dos partes: ancho_columna y between """
        lst_formato_ancho_columna   = F_r_a_n_k_y.__desempaqueta_str_formato(str_formato = baseline_format, b_between=False)
        lst_formato_between         = F_r_a_n_k_y.__desempaqueta_str_formato(str_formato = baseline_format, b_between=True)

        """ ■■■■ Creo la Lista/matriz del Formato del Body a partir de las dos partes anteriores y 
        la lista de la ultima columna usada por fila. """
        lista_formato_final = []    
        for i, last_columna_used in enumerate(lst_last_columna_used):            
            # ■■ Creo el Formato Ajustado A la Ultima COLUMNA usada para el ancho_columna Y Pen-ultima para sp_between 
            lst_ancho_new_xfila   = [ formato_ancho if (j <= last_columna_used) and (lst_len_organico_xfila[i] != 0) 
                                                    else '{:<0}' 
                                                    for j , formato_ancho  in enumerate(lst_formato_ancho_columna) ]

            lst_between_new_xfila = [ formato_between   if (j < last_columna_used ) and (lst_len_organico_xfila[i] != 0 ) 
                                                        else '{:<0}' 
                                                        for j , formato_between in enumerate(lst_formato_between) ]            
            # ■■ Generar la cadena de formato intercalando ancho y between
            formato_final_xfila = ''.join(a + b for a, b in zip(lst_ancho_new_xfila, lst_between_new_xfila))            
            
            # ■■ Agrega la cadena anterior a la lista de formatos y vamos a por la siguiente fila...
            lista_formato_final.append(formato_final_xfila)
        pass
        # ■■ RETORNO
        return lista_formato_final if lista_formato_final else None

    # LISTA CON LA LONGITUD ORGANNICA DE LOS VALORES DE CADA FILA ► [ 7,0,5,3,0,0,0,0,0 ] pej.
    def __get_lst_len_natural(self, tablero = None , sp_between:int = 0 ):        
        """ Obtiene una Lista con las longitudes de los valores de cada fila + los espacios between hasta la última columna usada - 1
        En caso de que haya valores en la fila, en caso contrario pone 0 en la fila(no cuenta los espacios between).
        [sp_between] (int): Espacio entre columnas. 0 byDef
        [tablero] (Tablero): Tablero del que se quiere obtener la lista de longitudes. Por defecto es el mismo objeto. Body
        ► CALLED: __get_lst_formato_natural()
        ■ EJEMPLO: 
            lst_len_organico_xfila = self.__get_lst_len_natural(sp_between = 2, tablero = self)  
        ► SALIDA:  [57, 12, 15, 0, 5, 0] con una dimension 4x6 porejemplo.
        """
        if tablero is None:
            tablero = self
        # ██ LISTA-INT CON LA LONGITUD DE LOS 'VALORES' Sin contar con el color
        lst_longitud_filas = tablero.get_lstlen_valores_xfila(b_limpio=True)                            

        # ■■■■■ LISTA-INT CON LA ULTIMA COLUMNA USADA DE CADA FILA ■ ... para calcular los sp_between
        lst_last_columna_used = tablero.get_lst_last_columna_used_xfila()     

        # ██ LISTA DE ESPACIOS USADOS HASTA LA PENULTIMA COLUMNA USADA [last_columna_used - 1] 
        # pero hay que sumar 1 pq la columna 'A' empieza en 0 y si no se suma se perdería con lo que queda last_columna_used
        lst_sp_between_x_fila = [ (last_columna_used * sp_between)  if (last_columna_used > 0 and lst_longitud_filas[i] > 0)
                                                                    else 0 if ( last_columna_used == 0 and lst_longitud_filas[i] > 0 )
                                                                    else 0 if ( last_columna_used == 0 and lst_longitud_filas[i] == 0 )
                                                                    else 0
                                                                    for i, last_columna_used in enumerate(lst_last_columna_used) ]
        # ■■■■■■■■■ SUMA LAS 2 LONGITUDES X FILA ::: VALORES + ESPACIOS BETWEEN
        lst_lentotal_x_fila = [ len_fila + sp_between_x_fila 
                                    for len_fila , sp_between_x_fila in zip(lst_longitud_filas, lst_sp_between_x_fila) ]
        # RETORNO
        return lst_lentotal_x_fila
        
    # Separa LA CADENA DE FORMATO EN POSICIONES PARES(ANCHO_COLUMNAS) O IMPARES(SP_BETWEEN)... trabaja con __get_parte_entera_monomio_formato para transformar una linea de formato en una lista.
    @staticmethod
    def __desempaqueta_str_formato( str_formato:str, b_between:bool=False):
        """ ■ DEVUELVE UNA LISTA CON EL MONOMIO( {:<x} ) DE LA CADENA DE FORMATO COMPLETO, LAS POSICIONES PARES O IMPARES.
        [str_formato](str): baseline_format, ► '{:<55}{:<1}{:<0}{:<1}{:<0}{:<1}{:<0}{:<1}{:<0}{:<1}{:<0}{:<1}{:<0}{:<1}{:<0}{:<1}{:<0}{:<1}'
            Cadena de formato.{:<ANCHO}{:<BETWEEN}     ► Hay dos monomios que forman un binomio, que representa donde se situará una celda en la tabla. 
        [b_between](bool): ► True, si quieres los pares( sp_between )  ► False, 
        ■ EJEMPLO: 
            lst_formato_ancho_columna = F_r_a_n_k_y.__desempaqueta_str_formato( str_formato = formato, b_between=False ) ► ['{:<55}','{:<0}', '{:<0}', '{:<0}', '{:<0}', '{:<0}', '{:<0}', '{:<0}', '{:<0}']
            lst_formato_between       = F_r_a_n_k_y.__desempaqueta_str_formato( str_formato = formato, b_between=True )  ► ['{:<1}', '{:<1}', '{:<1}', '{:<1}', '{:<1}', '{:<1}', '{:<1}', '{:<1}', '{:<1}']
        """
        # Expresión regular para capturar toda la estructura {:<X}, {:<X}, {:^X}
        patrones = re.findall(r'{:[<>^]\d+}', str_formato)        
        
        if b_between == True:
            return patrones[1::2]   # ► Elementos en posiciones impares - sp_between
        else:
            return patrones[::2]    # ► Elementos en posiciones pares  - ancho columna

    # DE UN MONOMIO DE FORMATO OBTIENE SU NUMERO    {:<4} ► 4 
    @staticmethod
    def __get_parte_entera_monomio_formato(monomio_formato: str):       
        """ Devuelve la parte entera(ancho) de una cadena de formato. 
        [monomio_formato](str): cadena de formato.... '{:<x}'
        ■ EJEMPO: 
            self.__get_parte_entera_monomio_formato(monomio_formato = '{:<7}')  ►  7
        ■ RETORNO: (int) Ancho del monomio.
        """
        match = re.search(r'{:[<>^](\d+)}', monomio_formato)
        
        # RETORNO ... devuelve el grupo 1 de la expresión regular(el primer parentesis de la expresión regular)        
        return int(match.group(1)) if match else 0  # Devuelve 0 si no hay coincidencias

    def __linea_horizontal( self, char:str, maximo_franky:int, color:str=None ):
        """ ■ Imprime una línea horizontal con el caracter y color especificados CON LA longitud especificada en maximo_franky.
        [char] (str): Caracter a usar para la línea.
        [color] (str): Color a usar para la línea.

        Sustitye
        # print(f'{self.ESPACIO * self.margen}{self.char_up_body * ( largo_total_marco )}')   
        # print(f'{self.ESPACIO * self.margen}{self.char_up_body * ( maximo_franky + len_marco_limpio + self.x_pad + self.pad_x + len_marco_limpio )}')        

        ■ EJEMPLO:
            ► print(self.__linea_horizontal(char=self.char_head, maximo_franky = 95))
        """
        # TAMAÑO DEL CHAR MARCO(SE PUEDEN ELEGIR MAS DE UN CARACTER PARA EL MARCO) 
        len_marco_limpio = Rango.len_limpio(texto = self.char_marco) if self.char_marco else 0
        
        # CALCULA LA LONGITUD TOTAL DE LA LINEA
        longitud_linea = maximo_franky + len_marco_limpio + self.x_pad + self.pad_x + len_marco_limpio
        
        if color is None:
            # devuelve la línea horizontal con el caracter especificado y sin color(o arrastrando el color que tenga el marco)
            return f'{self.ESPACIO * self.margen}{char * longitud_linea}'
        else:
            # devuelve la línea horizontal con el color y el caracter especificados
            return f'{self.ESPACIO * self.margen}{color}{char * longitud_linea}{Style.RESET_ALL}'
    
    @staticmethod
    def __from_formato_to_matriz( lst_formato:list, b_ancho_columna:bool=True, b_sp_between:bool=False ):
        """ ■ Def: Convierte una lista de formatos en una matriz de enteros.
        [lst_formato] (list): Lista de formatos a convertir.
        [b_ancho_columna] (bool): Si True, devuelve la lista de anchos de columna.
        [b_sp_between] (bool): Si True, devuelve la lista de espacios entre columnas.
        ■ Retorno: Una lista de enteros con los valores del formato.
        ■ Ejemplo ■
            {:<4}{:<2} {:<0}{:<2} {:<0}{:<2}       4 - 2 - 0 - 2 - 0 - 2
            {:<0}{:<2} {:<0}{:<2} {:<0}{:<2}   ►   0 - 2 - 0 - 2 - 0 - 2
            {:<0}{:<2} {:<0}{:<2} {:<0}{:<2}       0 - 2 - 0 - 2 - 0 - 2
        """        
        lst_matriz_formato = []
        # ■■ LISTA DE ENTEROS DE LOS VALORES DEL FORMATO
        lst_int_ancho_columna = []
        lst_int_sp_between = []
        for formato in lst_formato:                    

            lst_formato_ancho_columna = F_r_a_n_k_y.__desempaqueta_str_formato( str_formato = formato, b_between=False )
            lst_formato_between       = F_r_a_n_k_y.__desempaqueta_str_formato( str_formato = formato, b_between=True )

            # LISTA DE ENTEROS DE LOS VALORES DEL FORMATO
            lst_int_ancho_columna.append([F_r_a_n_k_y.__get_parte_entera_monomio_formato(monomio_formato) for monomio_formato in lst_formato_ancho_columna])
            lst_int_sp_between.append(   [F_r_a_n_k_y.__get_parte_entera_monomio_formato(monomio_formato) for monomio_formato in lst_formato_between])                        
        pass
        lst_matriz_formato = [ [a + b for a, b in zip(sublista_ancho, sublista_between)] 
                                      for sublista_ancho, sublista_between in zip(lst_int_ancho_columna, lst_int_sp_between)
        ]

        if b_ancho_columna == True and b_sp_between == False:
            return lst_int_ancho_columna if lst_int_ancho_columna else None
        if b_ancho_columna == False and b_sp_between == True:
            return lst_int_sp_between if lst_int_sp_between else None
        if b_ancho_columna == True and b_sp_between == True:
            return lst_matriz_formato if lst_matriz_formato else None
        if b_ancho_columna == False and b_sp_between == False:
            return lst_matriz_formato if lst_matriz_formato else None

    @staticmethod
    def obtener_columna( matriz:list, indice_col: int ) ->list[int]:
        """ ■ Extrae una columna de una matriz de enteros por su índice.
        ■ [matriz] (list[list[int]]): Matriz representada como lista de listas.
        ■ [indice_col] (int): Índice de la columna a extraer (base 0).
        De momento sin uso, pero BASE para conseguir columnas del mismo color 
        """
        return [fila[indice_col] for fila in matriz]

    # ████████████████████████████████████████████████████████████████████████████████████████████
    # ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘ METODOS PARA COLOR
    # ████████████████████████████████████████████████████████████████████████████████████████████
    
    # ■ Función principal para cambiar el color del marco
    def color_marco(self, color=Fore.WHITE):
        """ ■ Cambia el color  del marco.        
        [color] (str o código Colorama): Color a aplicar::: Fore.RED, Fore.YELLOW 
        ► CALLED: None
        ■ EJEMPLO: 
            self.color_marco(color=Fore.CYAN)
        """
        color_procesado = self.from_nombre_to_color(color = color)
        if color_procesado is None:
            print(f"Color no válido: {color}... pongo Negro por defecto.")
            color_procesado = Fore.BLACK
        # Diccionario con los componentes del marco a colorear
        componentes = {
            'char_marco': self.char_marco,
            'char_head': self.char_head,
            'char_pie': self.char_pie,
            'char_down_body': self.char_down_body,
            'char_up_body': self.char_up_body
        }
        # ■ Aplicar nuevo color a cada componente
        for nombre, valor in componentes.items():
            caracter_visible = F_r_a_n_k_y.__texto_limpio(texto = valor)
            setattr(self, nombre, f'{color_procesado}{caracter_visible}{Style.RESET_ALL}')

        print(f'Color {color_procesado} cambiado correctamente {Style.RESET_ALL}')
    
    # Función para procesar el color (convertir string a código Colorama)
    # @staticmethod
    def from_nombre_to_color(self, color:str):
        """ ■ Convierte un string de color a su código Colorama correspondiente.        
        [color]  (str o código Colorama): Color a procesar     
        ► CALLED: self.color_marco()       
        RETURN: 1• Código Colorama  2• None si no es válido
        """
        if isinstance(color, str):
            if color in self.COLOR_MAP.items():
                return color
            elif color.lower() in self.COLOR_MAP.keys():            
                return self.COLOR_MAP.get(color.lower(), None)
            else:                
                return None
        
    # ◘◘◘◘ FORMA SEGURA DE RETORNAR UN TEXTO SIN EL COLOR DE COLORAMA
    @staticmethod
    def __texto_limpio( texto:str, b_get_txt:bool = True):
        """ Convierte cualquier entrada en str SIN CODIGOS ANSI. y devuelve:
            ► Lista de rangos visibles (inicio, fin)
            ► O el texto visible reconstruido (si b_get_txt=True)
        CALLED: ► self.__get_valor_diferencia()  ► __get_head_excel() ► __get_maximo_head()  ► __imprimir_matricial() ► __get_lista_L_SUM() ► __ruta_natural() ► __ruta_cuadrado()
        EJEMPLO:
            valor_limpio:str = F_r_a_n_k_y.__texto_limpio(texto='\x1b[32mLoren \x1b[0mIpsum ', b_get_txt = True)  ► 'Loren Ipsum'
            valor_limpio:str = F_r_a_n_k_y.__texto_limpio(texto='\x1b[32mLoren \x1b[0mIpsum ', b_get_txt = False) ► [(4,8), (13,17)] ► SIN USO 
        """
        if not isinstance(texto, str):
            try:
                texto = str(texto)
            except Exception:
                texto = ''

        # Patrón mejorado para capturar más secuencias ANSI
        ansi_pattern = re.compile(r'\x1b\[[0-9;]*[a-zA-Z]')
        lst_cadena = []
        pos_actual = 0

        for match in ansi_pattern.finditer(texto):
            start, end = match.span()
            if pos_actual < start:
                lst_cadena.append((pos_actual, start))
            pos_actual = end

        if pos_actual < len(texto):
            lst_cadena.append((pos_actual, len(texto)))
        
        # ■ RETORNO
        if b_get_txt:
            texto_visible = ''.join(texto[inicio:fin] for inicio, fin in lst_cadena)
            return texto_visible
        else:
            return lst_cadena
    
    # ◘◘◘◘ Devuelve siempre Un texto por un indice saltandose colorama.
    @staticmethod
    def __truncate_colored_string(valor:str, max_width:int) -> str:
        """ ■ Trunca una cadena con códigos ANSI a un ancho máximo, manteniendo los códigos intactos.    
        ■ USADO SOLO PARA MODO DE IMPRESION 'FIX' Y 'LISTA-FIX'      
            ► 1- Extraer los códigos ANSI (Colorama) y separarlos del texto visible.
            ► 2- Cortar el texto visible según el ancho especificado.
            ► 3- Reconstruir la cadena con los códigos ANSI y el texto visible cortado
        ► CALLED: ► self.__get_valor_diferencia() 
        [valor] (str): Cadena con códigos ANSI.
        [max_width] (int): Ancho máximo permitido.        
        ■ EJEMPLO:
            valor_to_append = F_r_a_n_k_y.__truncate_colored_string(valor='\x1b[32mLoren \x1b[0mIpsum ', max_width = 8 ) ► '\x1b[32mLoren \x1b[0mIp'
            valor_to_append = F_r_a_n_k_y.__truncate_colored_string(valor='\x1b[32mLoren \x1b[0mIpsum ', max_width = 5 ) ► '\x1b[32mLoren'
        """
        # ■■■■■■■■■■■■Expresión regular para encontrar códigos ANSI (Colorama)
        # ansi_escape = re.compile(r'(\033\[[0-9;]*m)')
        # ansi_escape = re.compile(r'\x1b\[[0-9;]*[a-zA-Z]')
        ansi_escape = re.compile(r'(\x1b\[[0-9;]*m)')
        
        len_valor_limpio = Rango.len_limpio(texto = valor)
        len_valor_bruto = len(valor)
        
        # ■■■■■■■■■■■■ Si no hay color Asignado, recorto al max_width
        if len_valor_limpio == len_valor_bruto:  
            return valor[:max_width] if len_valor_bruto > max_width else valor             

        # Dividir la cadena en partes: códigos ANSI y texto normal
        parts = []
        current_pos = 0
        for match in ansi_escape.finditer(valor):
            start, end = match.span()
            if current_pos < start:
                parts.append(('text', valor[current_pos:start]))
            parts.append(('ansi', match.group()))
            current_pos = end
        if current_pos < len(valor):
            parts.append(('text', valor[current_pos:]))
        
        # Reconstruir el texto visible y los códigos ANSI
        visible_length = 0
        truncated_parts = []
        for part_type, part_content in parts:
            if part_type == 'text':
                allowed_length = max(0, max_width - visible_length)
                truncated_text = part_content[:allowed_length]
                truncated_parts.append(truncated_text)
                visible_length += len(truncated_text)
                if visible_length >= max_width:
                    break
            else:
                truncated_parts.append(part_content)
        
        return ''.join(truncated_parts)

    @staticmethod
    def __eliminar_ansi_final(texto):
        """ ■ Elimina solo los códigos ANSI al FINAL del texto, preservando los internos.
        En base a esta diferenciacion (valor en bruto - valor sin ansi final) se calculan las longitudes para el marco derecho.
        ► CALLED: F_r_a_n_k_y.__get_valor_diferencia()
        ■ EJEMPLO:
            valor_reset:str  = F_r_a_n_k_y.__eliminar_ansi_final(texto='\x1b[32mLoren Ipsum \x1b[0m')   ► '\x1b[32mLoren Ipsum'   
            valor_reset:str  = F_r_a_n_k_y.__eliminar_ansi_final(texto='\x1b[32mLoren \x1b[0mIpsum')    ► '\x1b[32mLoren \x1b[0mIpsum'   
        """
        return re.sub(r'(\x1b\[[0-9;]*m)+$', '', texto)

    # ████████████████████████████████████████████████████████████████████████████████████████████
    # ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘ METODOS PARA IMPRIMIR
    # ████████████████████████████████████████████████████████████████████████████████████████████

    # ◘◘◘◘◘◘◘
    def imprimir(self, sp_between:int = 0, ancho_columna:int = None, lista:list = None , fila_from:int=0, fila_to:int=None):    
        """ ■■■ SOBRE-ESCRIBE EL METODO IMPRIMIR DE TABLERO:
        ■ IMPRIME UN OBJETO F_R_A_N_K_Y EN LA TERMINAL SEGUN LA CONFIGURACION ESTABLECIDA.
        ► CALLED: None
        ■ [sp_between] (int): el espacio entre columnas.... 0 byDef
                                    Un sp_between = 0, significa que NO va a haber espacio entre columnas.
                                    Un sp_between = valor entero positivo, significa que va a haber un espacio entre columnas.
        ■ [ancho_columna](int)  = ancho_columna de columna. Puede ser None, 0 o valor entero positivo... 0 byDef
                                    Un ancho columna == None, significa que vamos a coger el valor MAXIMO para la columna.
                                    Un ancho de columna = 0, significa que NO se va a tener en cuenta el ancho de la columna(LITERAL / MOSAICO)
                                    Un ancho de columna = valor entero positivo, significa que va a ser ancho FIXED
        ■ [lista](list) = lista de anchos para cada columna.  Puede tener cualquier longitud.... None byDef
                                    Si lista == None, No se tiene en cuenta la lista y se trabaja con sp_between y ancho_columna.
                                    Si lista != None, se trabaja con la lista como ancho FIXED y el resto(si falta alguna) se tiene en cuenta sp_between y ancho_columna como en los casos anteriores.
        ■ [fila_from](int): fila desde la que se empieza a imprimir. 0 byDef
        ■ [fila_to](int): fila hasta la que se imprime. None byDef, imprime hasta el final del tablero.
        ■ RETORNO:  None, imprime los tableros franky (head, body , pie)
        ■ EJEMPLOS:
            ► F_RANK_Y.imprimir(  lista = None , sp_between = 2,  ancho_columna = None , fila_from=2, fila_to=10 )   ►   'MAX'
            ► F_RANK_Y.imprimir(  lista = None , sp_between = 2,  ancho_columna = 9 , fila_from=2, fila_to=10 )      ►   'FIX'
            ► F_RANK_Y.imprimir(  lista = None , sp_between = 2,  ancho_columna = 0 , fila_from=2, fila_to=10 )      ►   'MOSAICO'
            ► F_RANK_Y.imprimir(  lista = None , sp_between = 0,  ancho_columna = 0 , fila_from=2, fila_to=10 )      ►   'MOSAICO-LITERAL' 
            ► F_RANK_Y.imprimir(  lista = [7,7] , sp_between = 0, ancho_columna = 0 , fila_from=2, fila_to=10 )      ►   'LISTA-MOSAICO-LITERAL' 
            ► F_RANK_Y.imprimir(  lista = [7,7] , sp_between = 2, ancho_columna = 0 , fila_from=2, fila_to=10 )      ►   'LISTA-MOSAICO' 
            ► F_RANK_Y.imprimir(  lista = [7,7] , sp_between = 2, ancho_columna = None , fila_from=2, fila_to=10 )   ►   'LISTA-MAX' 
            ► F_RANK_Y.imprimir(  lista = [7,7] , sp_between = 2, ancho_columna = 9 , fila_from=2, fila_to=10 )      ►   'LISTA-FIX' 
        """        
        # ■ Valida la entrada
        lista, ancho_columna, sp_between, fila_from, fila_to = self.__ok_data(tablero = self, 
                                                                            lista = lista , ancho_columna = ancho_columna , sp_between = sp_between , 
                                                                            fila_from = fila_from , fila_to = fila_to )        
        if sp_between == None and fila_from == None and fila_to == None:
            print(f'Error::: Imprimir Franky ::: No se han pasado los parametros necesarios para imprimir el tablero')
            return None
        
        # ■ Cacha los datos para el body 
        self.dicc_print['body']['lista']         = lista
        self.dicc_print['body']['ancho_columna'] = ancho_columna
        self.dicc_print['body']['sp_between']    = sp_between

        family_impresion = self.get_family_impresion(lista = lista, ancho_columna = ancho_columna , sp_between = sp_between  )
        if family_impresion is None or str(family_impresion).upper() not in self.lista_family : return None

        # ■ Cacha el maximo_franky para imprimir el tablero.
        maximo_franky = self.__get_maximo_franky()
        if maximo_franky is None:
            print(f'Error::: Imprimir Franky ::: No se ha podido calcular el maximo_franky')
            return None        

        # ■ HEAD
        if self.b_excel == True:
            head_excel_F , head_excel_V = self.__get_head_excel( family_impresion = family_impresion, maximo_franky=maximo_franky )          # ■■ HEAD-Excel
            
            print(self.__linea_horizontal(char=self.char_head, maximo_franky=maximo_franky))
            print( head_excel_F.format(*head_excel_V) )

        else:
            if self.head:
                self.__imprimir_franky(tablero=self.head, maximo_franky=maximo_franky , up_line = True , down_line = False)                             # ■■ HEAD
        pass
        # ■ BODY        
        self.__imprimir_franky(tablero=self, maximo_franky=maximo_franky , up_line = True , down_line = True , fila_from=fila_from, fila_to=fila_to)    # ■■ BODY
        pass
        # ■ PIE
        if self.pie:
            self.__imprimir_franky(tablero=self.pie, maximo_franky=maximo_franky , up_line = False, down_line = True )                                  # ■■ PIE
        
        
        # ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘ imprime en una sóla funcion. SinUSO, pero es la BASE.
        # self.__imprimir_matricial(tablero = self, sp_between = sp_between , ancho_columna = ancho_columna , lista = lista , fila_from = fila_from, fila_to = fila_to )
        # ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘ 
        pass    

    @staticmethod
    def __get_valor_diferencia(valor_bruto, width_formato:int, family_impresion:str='MAX', b_lista:bool=False):
        """ Por cada valor bruto que entra devuelve el nuevo texto y la diferencia con el original.
        Necesareo para tener el valor final a imprimir dependiendo del tipo de impresion.
        [valor_bruto]:str, valor en bruto, Con caracteres ANSII
        [width_formato]:int, ancho que debe llevar el formato.
        [family_impresion]:str, 'MOSAICO', 'FIX', 'MAX'
        [b_lista]:bool, si hay lista en la configuración.
        ► CALLED: self.__ruta_natural(), self.__ruta_cuadrado()
        ■ EJEMPLO:
            valor_OK , diferencia = F_r_a_n_k_y.__get_valor_diferencia(valor_bruto="Loren Ipsum", width_formato=8, family_impresion='FIX', b_lista=False)
        ■ RETORNO:
            el Texto impreso dependiendo de la configuracion y la diferencia de tamaño ► "Loren ip" , 15 xejemplo
        """
        valor_limpio:str = F_r_a_n_k_y.__texto_limpio(texto = valor_bruto)
        valor_reset:str  = F_r_a_n_k_y.__eliminar_ansi_final(texto=valor_bruto)
        
        len_bruto:int = len(valor_bruto)
        len_limpio:int = len(valor_limpio)
        len_reset:int = len(valor_reset)
        diferencia:int = 0              # 
        
        # ■■■■■■■■ En caso de que sea lista OBLIGA a FIX
        if b_lista == True:
            family_impresion = 'FIX'

        """ ■■ Analiza las longitudes del Valor.  """
        # ■ texto ► Tal Cual
        if (len_bruto == len_reset) and (len_reset == len_limpio):  
            valor_to_append =  valor_bruto
            if family_impresion == 'FIX' and len(valor_bruto) > width_formato:
                valor_to_append = F_r_a_n_k_y.__truncate_colored_string(valor=valor_bruto, max_width=width_formato)

        # ■ansi■texto | ■texto■ansi■texto ►  Se mete tal cual 
        elif (len_bruto == len_reset) and (len_reset != len_limpio):    
            if family_impresion == 'MOSAICO':
                valor_to_append = valor_bruto
                pass
            elif family_impresion == 'FIX':
                if len(valor_reset) > width_formato:
                    valor_to_append = F_r_a_n_k_y.__truncate_colored_string(valor=valor_reset, max_width=width_formato)
                else:
                    valor_to_append = valor_reset
            elif family_impresion == 'MAX':
                valor_to_append = valor_reset
                pass
        
        # ■ansi■texto■ansi | ■ansi■texto■ansi■texto■ansi... ►
        elif (len_bruto != len_reset)  and (len_reset != len_limpio):   
            if family_impresion == 'MOSAICO':
                valor_to_append = valor_reset
                pass
            elif family_impresion == 'FIX':
                if len(valor_reset) > width_formato:
                    valor_to_append = F_r_a_n_k_y.__truncate_colored_string(valor=valor_reset, max_width=width_formato)
                else:
                    valor_to_append = valor_reset
            elif family_impresion == 'MAX':
                valor_to_append = valor_reset   # puede tener longitud mayor que el max pero no imprimible.
                pass
        
        # ■texto■ansi ► Raro. Limpiar
        elif (len_bruto != len_reset)  and (len_reset == len_limpio):   
            if family_impresion == 'MOSAICO':
                valor_to_append =  valor_reset
                pass
            elif family_impresion == 'FIX':
                if len(valor_reset) > width_formato:
                    if width_formato == 0:
                        valor_to_append = valor_reset                        
                    else:
                        valor_to_append = F_r_a_n_k_y.__truncate_colored_string(valor=valor_reset, max_width=width_formato)
                else:
                    valor_to_append = valor_reset
                pass
            elif family_impresion == 'MAX':
                valor_to_append =  valor_reset
                pass
        pass 
        # ■ Establece la diferencia por colorama. Se compara la longitud sin ansi-final(len_reset) con el ancho que debe tener        
        if len(valor_reset) <= width_formato:                           # ■ Contenido Menor que Formato.
            diferencia = len(valor_reset) - len(valor_limpio)           # ■■■ Negativo
        else:                          # ■ Contenido Mayor que Formato 
            diferencia = width_formato - len(valor_limpio)              # ■■■ Positivo
        # ■ Retorno
        return f'{valor_to_append}' , diferencia

    # IMPRIME UN HEAD EN FORMATO EXCEL, Que es con los nombres de las columnas
    def __get_head_excel(self, family_impresion,  maximo_franky:int):
        """ ■ Imprime el Head en formato Excel. No rompe el anterior. Este es otro Tablero distinto que se crea en el __init__ con el total de las columnasç de la matriz.
        ■ Desarrollo: Desarmamos baseline y la transf en matriz(de int) opero con las matrices ancho y between para sacar el 'formato deseado' y vuelvo a montar.
        ■ Hay que tener en cuenta que si el ancho = 0 y sp = 2 y no hay nada escrito en esa columna. la letra del formato va a ocupar un espacio y luego le seguirán 2 en blanco(sp_between)
        Esto es un error IF family_impresion == 'MAX', y hay que controlarlo con self.get_list_maxlen_columna().
        [family_impresion](str): familia de Impresion: 'MOSAICO', 'FIX' , 'MAX'       
        [maximo_franky](int): el maximo entre el Head_Excel / Self(Body) / Pie
        ■ RETORNO:   
            ■ head_excel_F:
                '{:<0}{:<1}{:<2}{:<8}{:<2}{:<8}{:<2}{:<8}{:<2}{:<8}{:<0}{:<0}{:<0}{:<0}{:<0}{:<21}{:<5}{:<1}'
            ■ head_excel_V
                ['', '█', '  ', '\x1b[0m\x1b[35mA       ', '  ', '\x1b[0mB       ', '  ', '\x1b[0m\x1b[35mC       ', '  ', '\x1b[0mD       ', ' ', '\x1b[0m\x1b[35mE', '', '\x1b[0mF', '\x1b[0m', '', '     ', '█']
        ■ EJEMPLO:
                >>> if self.b_excel == True:
                >>>     head_excel_F , head_excel_V = self.__get_head_excel( family_impresion = 'MAX', maximo_franky = 95 )
        """
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■■■■■■■■■■■ CACHO DATOS PRA TRABAJAR 
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        lista = self.dicc_print['body']['lista']         
        ancho_columna = self.dicc_print['body']['ancho_columna'] 
        sp_between = self.dicc_print['body']['sp_between']
        # ■ ULTIMA COLUMNA Usada... del Body
        lista_ultima_columna_used = self.get_lst_last_columna_used_xfila()                              # Lista con la última columna usada xfila  - [Rango]
        ultima_columna_used = max(lista_ultima_columna_used) if lista_ultima_columna_used else 0        # ultima columna usada en la matriz.
        columnas_to_FIN = self.total_columnas - ultima_columna_used - 1                                      
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■■■■■■■■■■■ A PARTIR DE LA BASELINE, Transformo baseline en dos matrices de enteros para trabajar con números.
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # BASELINE FORMATO - Del Body   
        baseline_format = self.get_baseline_format(sp_between = sp_between , ancho_columna = ancho_columna , lista = lista)
        if not baseline_format: return None, None
        # LISTA De Monomios FORMATO
        lst_paquete_ancho = F_r_a_n_k_y.__desempaqueta_str_formato( str_formato=baseline_format, b_between=False)
        lst_paquete_between = F_r_a_n_k_y.__desempaqueta_str_formato( str_formato=baseline_format, b_between=True )
        # LISTA DE ENTEROS DE LOS VALORES DEL FORMATO. No se Incluye la última columna para que desde la última hasta el final queden ajustadas.
        lst_F_ancho_columna = [F_r_a_n_k_y.__get_parte_entera_monomio_formato(m) if j <= ultima_columna_used else 0 for j , m in enumerate(lst_paquete_ancho)]
        lst_F_sp_between =    [F_r_a_n_k_y.__get_parte_entera_monomio_formato(m) if j < ultima_columna_used else 0 for j , m in enumerate(lst_paquete_between)]
                
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■■■■■■■■■■■ DESARME Y TRANSF MATRICIAL... Las Head Excel no se rigen por los mismos pararametros del body. 
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

        # ■■■■■■■■■■■■ Diferencia entre un tablero normal y un head_excel.
        if family_impresion == 'MOSAICO':
            lst_F_ancho_final = [F_r_a_n_k_y.__get_parte_entera_monomio_formato(m) if j < ultima_columna_used else 0 for j , m in enumerate(lst_paquete_ancho)]
            lst_F_betwn_final = [F_r_a_n_k_y.__get_parte_entera_monomio_formato(m) if j < ultima_columna_used else 0 for j , m in enumerate(lst_paquete_between)]
        
        elif family_impresion == 'FIX':
            lst_F_ancho_final = [F_r_a_n_k_y.__get_parte_entera_monomio_formato(m) if j <= ultima_columna_used else 0 for j , m in enumerate(lst_paquete_ancho)]
            lst_F_betwn_final = [F_r_a_n_k_y.__get_parte_entera_monomio_formato(m) if j < ultima_columna_used else 0 for j , m in enumerate(lst_paquete_between)]
        
        elif family_impresion == 'MAX':
            lista_MAX_COL =  self.get_list_maxlen_columna()   # Tiene que ser self y no self.head_excel pq estamos tratando de sacar la regla del body para la disposición de las letras.
            
            lst_F_ancho_final = [ 0 if (max_col == 0 or j > ultima_columna_used ) else lst_F_ancho_columna[j] for j , max_col in enumerate(lista_MAX_COL) ]
            lst_F_betwn_final = [ 0 if (max_col == 0 or j > ultima_columna_used ) else lst_F_sp_between[j]    for j , max_col in enumerate(lista_MAX_COL) ]
        else:
            return None, None
        
        # print(f'{Fore.RED}lst_F_ancho_final: \t{Fore.BLUE}{lst_F_ancho_final}')
        # print(f'{Fore.LIGHTRED_EX}lst_F_betwn_final: \t{Fore.CYAN}{lst_F_betwn_final}')
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■■■■■■■■■■■ FORMATO
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        if family_impresion == 'MOSAICO':
            fila_F = ''.join( [ '{:<' + str(a) + '}' + '{:<' + str(1) + '}'  if j < ultima_columna_used 
                                                                             else '{:<' + str(a) + '}' + '{:<' + str(0) + '}'
                                                                             for j, a in  enumerate(lst_F_ancho_final)] )
        elif family_impresion == 'FIX' or family_impresion == 'MAX':
            fila_F = ''.join( [ '{:<' + str(a) + '}' + '{:<' + str(b) + '}'  
                                            for a, b in zip( lst_F_ancho_final, lst_F_betwn_final )] )

 
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■■■■■■■■■■■■ VALORES
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        lista_excel_V = []    # lista  de Valores del Head.
        for j, celda in enumerate(self.head_excel.matriz[0]):
            LETRA_HEAD = f'{celda.valor}'
            len_limpio = len(F_r_a_n_k_y.__texto_limpio( texto = LETRA_HEAD))     #
            # ■■■■■■■■■■■■■■■■■■ 
            if j < ultima_columna_used:         # ■■■■■ ► 0 <= j < Ultima Columna Usada 
                if family_impresion == 'MAX':
                    if lst_F_ancho_final[j] == 0:   # ■■■■■ ► Columna VACIA
                        lista_excel_V.append(f'')                                                            # ■ ancho
                        lista_excel_V.append(f'{LETRA_HEAD}{self.ESPACIO*(sp_between-len_limpio)}')          # ■ between: letra en el sp y de resto(sp_between-L_letra) relleno con espacios.                                               
                    else:                           # ■■■■■ ► Columna CON DATOS
                        lista_excel_V.append( f'{LETRA_HEAD}{self.ESPACIO * (lst_F_ancho_final[j]-len_limpio)}') # ■ ancho
                        lista_excel_V.append(f'{lst_F_betwn_final[j]*self.ESPACIO}')                             # ■ between

                elif family_impresion == 'FIX':
                    lista_excel_V.append(f'{LETRA_HEAD}{self.ESPACIO * (lst_F_ancho_final[j] - len_limpio)}')    # ■ ancho
                    lista_excel_V.append(f'{lst_F_betwn_final[j]*self.ESPACIO}')                                 # ■ between

                elif family_impresion == 'MOSAICO':
                    lista_excel_V.append(f'{LETRA_HEAD}')                                                        # ■ ancho
                    lista_excel_V.append(f'•')                                                                   # ■ between(Alt+7)

            elif j == ultima_columna_used:
                lista_excel_V.append(f'{LETRA_HEAD}{self.ESPACIO * (lst_F_ancho_final[j] - len_limpio)}')        # ■ ancho
                lista_excel_V.append(f'{self.ESPACIO}')                                                          # ■ between

            else:
                if j != self.total_columnas - 1 :   # ► La columna Es mayor que la ultima usada pero no es la ultima columna

                    # ► Desde la ultima columna usada + 1. Sólo puede haber 4 letras como maximo(1 letra puede ser AX, 2 digitos.).
                    b_letra = self.__cuatro_letras(columnas_to_FIN=columnas_to_FIN, actual_col=j, ultima_columna_used=ultima_columna_used)
                    if b_letra == True:
                        lista_excel_V.append(f'{LETRA_HEAD}')                                                    # ■ ancho
                    elif b_letra == False:
                        lista_excel_V.append(f'.')                                                               # ■ ...o ancho
                    elif b_letra == None:
                        lista_excel_V.append(f'')                                                                # ■ ...o ancho

                    lista_excel_V.append(f'')                                                                    # ■ between           
                else:
                    lista_excel_V.append(f'{LETRA_HEAD}')                                                    # ■ ancho
                    lista_excel_V.append(f'{Style.RESET_ALL}')                                                    # ■ ancho

        pass
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■ MAXIMO HEAD, Para todos los formatos(max, fix, mosaico).
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        maximo_head_excel = sum( [ len(F_r_a_n_k_y.__texto_limpio( texto = a ) ) for  a in lista_excel_V ]  )

        resto_to_max = maximo_franky - maximo_head_excel         

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■ ENVUELVE EL FORMATO Y LOS VALORES.
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        head_excel_F = self.__envuelve_fila_F( fila_F = fila_F , resto_to_max = resto_to_max)
        head_excel_V = self.__envuelve_fila_V( lista_V = lista_excel_V )

        # ■ RETORNO
        return head_excel_F , head_excel_V
        
    def __cuatro_letras(self, columnas_to_FIN:int, actual_col:int, ultima_columna_used:int):
        """ ■ Devuelve un booleano o None para saber si se tiene que imprimir la letra, el punto o nada en el head-excel.
        ■ Llamada desde __get_maximo_head(), __get_head_excel()
        [columnas_to_FIN]:int, cuantas columnas quedan desde la última columna(no incluida) hasta el fin de la matriz.
        [actual_col]:int, cual es la columna actual. Estamos recorriendo head_excel.
        [ultima_columna_used]:int, cual es la última columna usada en la matriz.
        ► CALLED: self.__get_maximo_head() ■ self.__get_head_excel()
        ■ EJEMPLO:
            b_letra = self.__cuatro_letras(columnas_to_FIN=columnas_to_FIN, actual_col=j, ultima_columna_used=ultima_columna_used)
            if b_letra == True:
                lista_excel_V.append(f'{LETRA_HEAD}')                                                    # ■ ancho
            elif b_letra == False:
                lista_excel_V.append(f'.')                                                               # ■ ...o ancho
            elif b_letra == None:
                lista_excel_V.append(f'')                                                                # ■ ...o ancho
        ■ RETORNO:
            ► True(Letra) ► False[ punto('.') ] ► None(Imprime vacío),  dependiendo del lugar que ocupe la columna actual...                     
        """
        if columnas_to_FIN < 4:
            return True
        else:                   # A partir de 4 (incluido)
            if actual_col == self.total_columnas - 1:   # FIN MATRIZ..... IF 'Z'
                return True
            elif actual_col == ultima_columna_used + 1: # (ultima_columna_used + 1) es La 1ª Letra después de la última usada ► PRIMERA LETRA.
                return True
            else:
                if self.total_columnas - actual_col <= 3:
                    return False
                else:
                    return None

    def __envuelve_fila_V(self, lista_V: list, resto:int=0) -> list:
        """ ■ llamada desde __get_head_excel()
        [lista_V]:list, ['\x1b[0m\x1b[35mA                                  ', '  ', '\x1b[0mB   ', '  ', '\x1b[0m\x1b[35mC        ', '  ', '\x1b[0mD     ', ' ', '\x1b[0m\x1b[35mE', '', '\x1b[0mF', '\x1b[0m']
        [resto]:int=0, 
        ► CALLED: self.__get_head_excel()
        ■ EJEMPLO:
            head_excel_V = self.__envuelve_fila_V( lista_V = lista_excel_V )
        ■ RETORNO:
            ['', '█', '  ', '\x1b[0m\x1b[35mA                                  ', '  ', '\x1b[0mB   ', '  ', '\x1b[0m\x1b[35mC        ', '  ', '\x1b[0mD     ', ' ', '\x1b[0m\x1b[35mE', '', '\x1b[0mF', '\x1b[0m', '', '     ', '█']
        """
        # Envoltorio izquierdo (primeros 3 elementos)
        envoltorio_izquierdo = [
            f'{self.margen*self.ESPACIO}',  # margen
            f'{self.char_marco}',            # marco
            f'{self.x_pad*self.ESPACIO}'     # x_pad
        ]
        
        # El centro es la lista_V que se pasa como parámetro
        
        # Envoltorio derecho (últimos 3 elementos)
        envoltorio_derecho = [
            f'{resto * self.ESPACIO}',          # RESTO (para el body)
            f'{self.pad_x*self.ESPACIO}',       # pad_x
            f'{self.char_marco}'                # marco
        ]
        
        # Combinar los tres envoltorios en una sola lista
        lista_resultado = envoltorio_izquierdo + lista_V + envoltorio_derecho
        
        return lista_resultado

    def __get_maximo_head(self):
        """ ■ Devuelve el int del LEN de los valores de toda la fila del HEAD-excel. Llamada desde __get_maximo_franky().
        ■ Los datos de configuracion: lista, ancho_columna y sp_between, se cojen del body ya que el head es el reflejo del body en formato columnas excel ( A, B, C, ..., AZ )
        Hay que crear la impresión con los datos de configuracion.
        ■ EJEMPLO:
            max_lista_L_head = self.__get_maximo_head()          # ■■ HEAD-Excel
        ■ SALIDA:
            int: 95 xejem, Que representa el valor maximo del head con el formato de impresion(family_impresion) de self('MOSAICO', 'FIX', 'MAX').
        """
        lista = self.dicc_print['body']['lista']         
        ancho_columna = self.dicc_print['body']['ancho_columna'] 
        sp_between = self.dicc_print['body']['sp_between']
        
        # BASELINE FORMATO - Del Body   
        baseline_format = self.get_baseline_format(sp_between = sp_between , ancho_columna = ancho_columna , lista = lista)
        if not baseline_format: return None, None
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        # TIPO DE IMPRESION - [Rango]        
        family_impresion = self.get_family_impresion(sp_between = sp_between , ancho_columna = ancho_columna , lista = lista)
        if family_impresion is None or str(family_impresion).upper() not in self.lista_family : return None
        
        # ■ ULTIMA COLUMNA Usada... del Body
        lista_ultima_columna_used = self.get_lst_last_columna_used_xfila()                              # Lista con la última columna usada xfila  - [Rango]
        ultima_columna_used = max(lista_ultima_columna_used) if lista_ultima_columna_used else 0        # ultima columna usada en la matriz.
        columnas_to_FIN = self.total_columnas - ultima_columna_used - 1                                      
        # RESTO = 0                                                                                       # resto que tiene que haber en la linea de manera formal. aquí va a Zero

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■■■■■■■■■■■■ DESARME Y TRANSF MATRIZ ■■■■■■■■■■■■ 
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # LISTA De Monomios FORMATO
        lst_paquete_ancho = F_r_a_n_k_y.__desempaqueta_str_formato( str_formato=baseline_format, b_between=False)
        lst_paquete_between = F_r_a_n_k_y.__desempaqueta_str_formato( str_formato=baseline_format, b_between=True )
        # LISTA DE ENTEROS DE LOS VALORES DEL FORMATO. No se Incluye la última columna para que desde la última hasta el final queden ajustadas.
        lst_F_ancho_columna = [F_r_a_n_k_y.__get_parte_entera_monomio_formato(m) if j <= ultima_columna_used else 0 for j , m in enumerate(lst_paquete_ancho)]
        lst_F_sp_between =    [F_r_a_n_k_y.__get_parte_entera_monomio_formato(m) if j < ultima_columna_used else 0 for j , m in enumerate(lst_paquete_between)]

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # Diferencia entre un tablero normal y un head_excel.
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        if family_impresion == 'MOSAICO':
            lst_F_ancho_final = [F_r_a_n_k_y.__get_parte_entera_monomio_formato(m) if j < ultima_columna_used else 0 for j , m in enumerate(lst_paquete_ancho)]
            lst_F_betwn_final = [F_r_a_n_k_y.__get_parte_entera_monomio_formato(m) if j < ultima_columna_used else 0 for j , m in enumerate(lst_paquete_between)]
        elif family_impresion == 'FIX':
            lst_F_ancho_final = [F_r_a_n_k_y.__get_parte_entera_monomio_formato(m) if j <= ultima_columna_used else 0 for j , m in enumerate(lst_paquete_ancho)]
            lst_F_betwn_final = [F_r_a_n_k_y.__get_parte_entera_monomio_formato(m) if j < ultima_columna_used else 0 for j , m in enumerate(lst_paquete_between)]
        elif family_impresion == 'MAX':
            # Lista de las Longitudes maxima de cada columna        
            lista_MAX_COL =  self.get_list_maxlen_columna()     # Tiene que ser self y no self.head_excel pq estamos tratando de sacar la regla del body para la disposición de las letras.
            lst_F_ancho_final = [ 0 if (max_col == 0 or j > ultima_columna_used ) else lst_F_ancho_columna[j] for j , max_col in enumerate(lista_MAX_COL) ]
            lst_F_betwn_final = [ 0 if (max_col == 0 or j > ultima_columna_used ) else lst_F_sp_between[j]    for j , max_col in enumerate(lista_MAX_COL) ]

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■ VALORES
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        lista_excel_V = []                                       # lista  de Valores del Head.
        for j, celda in enumerate(self.head_excel.matriz[0]):
            LETRA_HEAD = f'{celda.valor}'
            len_limpio = len(F_r_a_n_k_y.__texto_limpio( texto = LETRA_HEAD ))     #
            # ■■■■■■■■■■■■■■■■■■ 
            if j < ultima_columna_used:         # ■■■■■ ► 0 <= j < Ultima Columna Usada 
                if family_impresion == 'MAX':
                    if lst_F_ancho_final[j] == 0:   # ■■■■■ ► Columna VACIA
                        lista_excel_V.append(f'')                                                            # ■ ancho
                        lista_excel_V.append(f'{LETRA_HEAD}{self.ESPACIO*(sp_between-len_limpio)}')          # ■ between: letra en el sp y de resto(sp_between-L_letra) relleno con espacios.                                               
                    else:                           # ■■■■■ ► Columna CON DATOS
                        lista_excel_V.append( f'{LETRA_HEAD}{self.ESPACIO * (lst_F_ancho_final[j]-len_limpio)}') # ■ ancho
                        lista_excel_V.append(f'{lst_F_betwn_final[j]*self.ESPACIO}')                             # ■ between

                elif family_impresion == 'FIX':
                    lista_excel_V.append(f'{LETRA_HEAD}{self.ESPACIO * (lst_F_ancho_final[j] - len_limpio)}')    # ■ ancho
                    lista_excel_V.append(f'{lst_F_betwn_final[j]*self.ESPACIO}')                                 # ■ between

                elif family_impresion == 'MOSAICO':
                    lista_excel_V.append(f'{LETRA_HEAD}')                                                        # ■ ancho
                    lista_excel_V.append(f'•')                                                                   # ■ between(Alt+7)

            elif j == ultima_columna_used:
                lista_excel_V.append(f'{LETRA_HEAD}{self.ESPACIO * (lst_F_ancho_final[j] - len_limpio)}')        # ■ ancho
                lista_excel_V.append(f'{self.ESPACIO}')                                                          # ■ between

            else:
                # ► Desde la ultima columna usada + 1. Sólo puede haber 4 letras como maximo(1 letra puede ser AX, 2 digitos.).
                b_letra = self.__cuatro_letras(columnas_to_FIN=columnas_to_FIN, actual_col=j, ultima_columna_used=ultima_columna_used)
                if b_letra == True:
                    lista_excel_V.append(f'{LETRA_HEAD}')                                                    # ■ ancho
                elif b_letra == False:
                    lista_excel_V.append(f'.')                                                               # ■ ...o ancho
                elif b_letra == None:
                    lista_excel_V.append(f'')                                                                # ■ ...o ancho

                lista_excel_V.append(f'')                                                                    # ■ between           

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # ■ MAXIMO HEAD, Para todos los formatos(max, fix, mosaico).
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        maximo_head_excel = sum( [ len(F_r_a_n_k_y.__texto_limpio( texto = a ) ) for  a in lista_excel_V ]  )

        # ■ RETORNO
        return maximo_head_excel

    # ◘◘◘◘◘◘◘ Para imprimir un Tablero Head, Pie o Body
    def __imprimir_franky(self, tablero, maximo_franky:int , up_line:bool=False, down_line:bool=False, fila_from:int=0, fila_to:int=None):
        """ ■ Imprime Un tablero pasado como parámetro. Puede imprimir una linea superior y una linea inferior que dependen de maximo_franky.
        [tablero] (Tablero): Tablero a imprimir. Puede ser self.head, self.pie o self.
        [maximo_franky] (int): Ancho máximo de la impresión.
        [up_line] (bool): Si True, imprime una línea horizontal arriba del tablero.
        [down_line] (bool): Si True, imprime una línea horizontal abajo del tablero.
        [fila_from] (int): Fila desde la que se empieza a imprimir. 0 byDef
        [fila_to] (int): Fila hasta la que se imprime. None byDef, imprime hasta el final del tablero.
        ► CALLED: self.imprimir()
        ■ EJEMPLO:
            >>> ► self.__imprimir_franky(tablero=self.head, maximo_franky=95 , up_line = True )                               # ■■ HEAD   
            >>> ► self.__imprimir_franky(tablero=self, maximo_franky=95 , up_line = True , down_line = True , fila_from=1, fila_to=5)    # ■■ BODY
        ■ SALIDA: None, realiza una impresion en pantalla.
        """        
        if not tablero or not isinstance(tablero, Tablero): return

        # ■■■ DE MOMENTO FUERZO EL HEAD Y EL PIE DESDE LA FILA 0 HASTA LA ÚLTIMA FILA DEL TABLERO.
        if tablero == self.head or tablero == self.pie or tablero == self.head_excel:
            fila_from = 0
            fila_to   = tablero.celda_fin.fila

        # ■■■ CACHO LOS DATOS DEL TABLERO QUE TIENEN QUE VER CON EL TIPO DE IMPRESION:
        if tablero == self.head:
            lista           = self.dicc_print['head']['lista'] 
            ancho_columna   = self.dicc_print['head']['ancho_columna'] 
            sp_between      = self.dicc_print['head']['sp_between']
        
        elif tablero == self.pie:
            lista           = self.dicc_print['pie']['lista']
            ancho_columna   = self.dicc_print['pie']['ancho_columna']
            sp_between      = self.dicc_print['pie']['sp_between']
        
        elif tablero == self:            
            lista           = self.dicc_print['body']['lista']
            ancho_columna   = self.dicc_print['body']['ancho_columna']
            sp_between      = self.dicc_print['body']['sp_between']
        
        else:
            print(f'Error: El tablero  no es ni Head ni Pie.')
            return None            
        pass
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        # TIPO DE IMPRESION - [Rango]        
        family_impresion = tablero.get_family_impresion(sp_between = sp_between , ancho_columna = ancho_columna , lista = lista)
        if family_impresion is None or str(family_impresion).upper() not in self.lista_family : return None
        
        if family_impresion == 'MOSAICO':
            
            matriz_F, matriz_V = self.__ruta_natural( tablero = tablero, family_impresion = family_impresion, maximo_franky = maximo_franky, 
                                                      lista = lista, ancho_columna = ancho_columna, sp_between = sp_between )
        
        elif family_impresion == 'FIX' or family_impresion == 'MAX':
            
            matriz_F, matriz_V = self.__ruta_cuadrado( tablero = tablero, family_impresion = family_impresion, maximo_franky = maximo_franky, 
                                                       lista = lista, ancho_columna = ancho_columna, sp_between = sp_between )

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        # IMPRIMIR -
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                
        # LINEA SUPERIOR
        if up_line == True: print(self.__linea_horizontal(char=self.char_head, maximo_franky=maximo_franky))         
        
        for i, lista_V in enumerate(matriz_V):                                    
            if fila_from <= i <= fila_to:
                # ► CON CABECERA EXCEL.
                if tablero == self and self.b_excel == True:   
                    if i % 2 == 0:  # ► SI PAR ► COLOR
                        print( matriz_F[i].format(*lista_V) + f'{self.ESPACIO}{self.color_excel}{i}{Style.RESET_ALL}' ) 
                    else:            # ► SI IMPAR ► NO COLOR
                        print( matriz_F[i].format(*lista_V) + f'{self.ESPACIO}{i}' ) 
                else:
                    print( matriz_F[i].format(*lista_V) ) 
        
        # LINEA INFERIOR
        if down_line == True: print(self.__linea_horizontal(char=self.char_pie, maximo_franky=maximo_franky))        
        pass
        
    # ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘
    # ◘◘◘◘◘◘◘ BASE-SIN USO ◘◘◘◘◘◘◘
    def __imprimir_matricial(self, sp_between:int=0, 
                                 ancho_columna:int = None, 
                                 lista:list = None, 
                                 fila_from:int=0, 
                                 fila_to:int=None , 
                                 tablero = None):
        """ ■ Imprime los Tableros Head / Body y Pie de forma matricial. 
        Permite formato y colores en la matriz 
        NO LA USO, ES LA BASE DE LA IMPRESION MODULAR DE LA CLASE, DE AQUÍ PARTE TODO. 

        [sp_between] (int): Espacio entre columnas.
        [ancho_columna] (int): Ancho de las columnas.
        [lista] (list): Lista de columnas a imprimir. Si es None, imprime todas las columnas.
        [fila_from] (int): Fila desde la que empezar a imprimir.
        [fila_to] (int): Fila hasta la que imprimir. Si es None, imprime hasta el final.
        [tablero] (Tablero): Instancia de Tablero. Si es None, usa self(body).
        ■ SALIDA:
            imprime por pantalla la el tablero pasado con la configuracion pasada(lista, ancho_columna, sp_between).
        ■ EJEMPLO:
            self.__imprimir_matricial(tablero = self, sp_between = 2 , ancho_columna = None , lista = None , fila_from = 0, fila_to = None )
        """
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        # VALIDACION Parametros de entrada
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
       
        # ■■ Valida el tablero
        if tablero is None: tablero = self
        
        # ■■ Valida que exista matriz.
        if  not tablero.matriz: return None

        # ■ Valida fila_from
        if not isinstance(fila_from, int): return None
        fila_from = abs(fila_from)
        
        # Valida fila_to
        if fila_to == None:
            fila_to = tablero.celda_fin.fila        
        else:
            try:
                fila_to=abs(int(fila_to))
                # VALIDA LOS LIMITES DE LAS FILAS PASADAS
                if not tablero.celda_inicio.fila <= fila_from <= fila_to <= tablero.celda_fin.fila:
                    print(f'fila_from( {fila_from} ) ► fila_to( {fila_to} ) fuera de rango')
                    return None                
            except Exception as e:
                print(f'{e}')
                return None
        if fila_from > fila_to:
            print(f'fila_from( {fila_from} ) > fila_to( {fila_to} ) fuera de rango')
            return None
        
        # Valida lista
        if lista is not None:
            if not isinstance(lista, list): return None # Valida que sea typo list.
            if not lista: return None               # Valida que la lista no esté vacía
            try:                                    # Valida que sea una lista de enteros positivos
                lista = [int(i) for i in lista]
                lista = [abs(i) for i in lista]     # Valida que sean enteros positivos
            except Exception as e:
                print(f'{e}')
                return None            
        
        # Valida ancho_columna
        if ancho_columna is not None:    # Si es None, es un valor admitido así que No lo trato.
            try:                                   
                ancho_columna = int(ancho_columna)
                ancho_columna = abs(ancho_columna)
            except Exception as e:
                print(f'{e}')
                return None

        # ■■■■■■ Elimina los caracteres vacios por la derecha antes de nada(para evitar confusiones luego ;) UPDT: CUANDO SE CREA LA MATRIZ. 
        try:
            for fila in tablero.matriz:
                for celda in fila:
                    if celda.valor != '' and isinstance(celda.valor, str):
                        celda.valor = str(celda.valor).rstrip()
                pass
        except Exception as e:
            print(f'{e}')
            return None
        
        """ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        DATOS GENERALES 
        ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ """
        ultima_columna_used = tablero.get_last_columna_used()      # Ultima columna usada en self.matriz    - [Rango]
        lista_ultima_columna_used = tablero.get_lst_last_columna_used_xfila()  # Lista con la última columna usada xfila  - [Rango]

        # ■■ Matriz, con el valor en bruto ■■ ...con chars ansii colorama(si lo hay) ... ( celda.valor )
        matriz_V_bruto = [  [str(celda.valor) for celda in fila ] for fila in tablero.matriz ]             # matriz que se va a recorrer.

        # ■■ Matriz de longitud de celda.valor de los caracteres imprimibles 
        # ■■ Longitud del texto sin ANSI
        matriz_L_limpio = [ [ len(F_r_a_n_k_y.__texto_limpio( texto = str(celda.valor) ))  
                                for celda in fila ] for fila in tablero.matriz ]
                                
        """ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        BASELINE FORMATO - [Rango]
        ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ """
        # ■ Baseline-Format ■ {:<41}{:<2}{:<0}{:<2}{:<0}{:<2}{:<0}{:<2}{:<0}{:<2}{:<0}{:<2}{:<0}{:<2}{:<0}{:<2}{:<0}{:<2}
        # ■ Es la linea base del formato que marca el ancho de columna y el espacio entre columnas. - [Rango]
        # ■ ■ ■ Lo siguiete será transformar esta linea en una matriz de formato que se pueda imprimir.
        baseline_format = tablero.get_baseline_format(sp_between = sp_between , ancho_columna = ancho_columna , lista = lista)
        if not baseline_format: return None        
        
        """ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        TIPO DE IMPRESION - [Rango]
        ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ """
        # lista_family = ['MOSAICO', 'FIX', 'MAX']
        family_impresion = tablero.get_family_impresion(sp_between = sp_between , ancho_columna = ancho_columna , lista = lista)
        if family_impresion is None or family_impresion not in self.lista_family : return None


        """ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        MATRIZ BASE TYPE FORMATO IMPRESION ... Para sacar las matriz_(F) Formato - [Franky]
        ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ """
        matriz_LIST_F_natural  = self.__get_lst_formato_natural( baseline_format = baseline_format, sp_between = sp_between , tablero = tablero)
        matriz_LIST_F_cuadrado = self.__get_lst_formato_cuadrado(baseline_format = baseline_format, sp_between = sp_between , tablero = tablero )
        
        """ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        MATRICES FORMATO - [Franky]
         ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ """
        matriz_F_ancho_natural     = F_r_a_n_k_y.__from_formato_to_matriz(lst_formato=matriz_LIST_F_natural, b_ancho_columna=True, b_sp_between=False)
        matriz_F_between_natural   = F_r_a_n_k_y.__from_formato_to_matriz(lst_formato=matriz_LIST_F_natural, b_ancho_columna=False, b_sp_between=True)

        matriz_F_ancho_cuadrado    = F_r_a_n_k_y.__from_formato_to_matriz(lst_formato=matriz_LIST_F_cuadrado, b_ancho_columna=True, b_sp_between=False)
        matriz_F_between_cuadrado  = F_r_a_n_k_y.__from_formato_to_matriz(lst_formato=matriz_LIST_F_cuadrado, b_ancho_columna=False, b_sp_between=True)
            
        """ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        MATRICES  - [Franky]
        ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ """
        if family_impresion == 'MOSAICO':
            # ■■■■■■■■ 
            # ■ Suma Ancho + sp_between, celda a celda, en formato natural (hasta la ultima columna)
            matriz_L_SUM_natural = [[a + b 
                                for a, b in zip(fila_len_sin_ansi, fila_between_nat)]
                                for fila_len_sin_ansi , fila_between_nat in zip(matriz_L_limpio, matriz_F_between_natural) ]
            # ■ ■ ■  Listas de longitudes totales de cada fila ... ■ Necesareos para maximo_franky
            lista_L_SUM_natural  = [sum(fila) for fila in matriz_L_SUM_natural]         # ■mosaico 
            pass
            
            # ■■■■■■■■ 
            # IF Lista + Mosaico
            if lista is not None:
                # ■ Mezcla dos Matrices a través de la longitud de lista. ■ Por si hace impresión 'FIX-MOSAICO'.
                matriz_mezcla_natural =  [ [ fila_A[col] if col < len(lista) 
                                                        else fila_B[col] 
                                                for col in range(len(fila_A))]
                                                for fila_A, fila_B in zip(matriz_F_ancho_natural , matriz_L_limpio) ]                                            
                # ■ Matriz de la Suma de Ancho + sp_between. 
                matriz_L_SUM_FIX_natural = [ [a + b 
                                                for a, b in zip(fila_a, fila_b)]
                                                for fila_a , fila_b in zip(matriz_mezcla_natural, matriz_F_between_natural) ]

                # ■ ■ ■ Listas de longitudes totales de cada fila ... ■ Necesareos para maximo_franky
                lista_L_SUM_FIX_natural  = [sum(fila) for fila in matriz_L_SUM_FIX_natural]

        elif (family_impresion == 'FIX') or (family_impresion == 'MAX'):                   
            # ■■■■■■■■ 
            # ■ Suma Ancho + sp_between, celda a celda, en formato cuadrado (hasta la ultima columna)
            matriz_L_SUM_cuadrado = [ [a + b 
                                for a, b in zip(fila_a, fila_b)]
                                for fila_a, fila_b in zip(matriz_F_ancho_cuadrado, matriz_F_between_cuadrado) ]
            # ■ ■ ■ Listas de longitudes totales de cada fila ... ■ Necesareos para maximo_franky
            lista_L_SUM_cuadrado = [sum(fila) for fila in matriz_L_SUM_cuadrado]        # ■fix ■max ■fix-fix ■fix-max
            pass

        """ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        SUMA DE LONGITUDES TOTAL(BIN) DE CADA FILA ... para calcular el ■maximo_franky y el ■resto_to_maxfranky.
        ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ """
        if family_impresion == 'MOSAICO':
            if lista is None:
                lista_L_SUM = lista_L_SUM_natural         # ■ sin Lista.
            else:
                lista_L_SUM = lista_L_SUM_FIX_natural     # ■ con Lista

        elif (family_impresion == 'FIX') or (family_impresion == 'MAX'):                   
            lista_L_SUM = lista_L_SUM_cuadrado            # ■ con Lista ■ sin Lista
        else:
            return None

        """ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        FORMATO SP-BETWEEN - MATRIZ F_BTWN ... Para calcular la matriz_valores_impresion
        ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ """
        if family_impresion == 'MOSAICO':
            matriz_F_BTWN = matriz_F_between_natural            # ■■ Formato_BTWN
        elif family_impresion == 'FIX' or family_impresion == 'MAX':
            matriz_F_BTWN = matriz_F_between_cuadrado           # ■ Formato_BTWN

        """ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        MAXIMO FRANKY ( Max entre Head / Body / Pie ) 
        ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ """
        maximo_franky = self.__get_maximo_franky()

        lst_resto_to_maxfranky = [ maximo_franky - L for L in lista_L_SUM ]         # ■ Lista de enteros con el resto a añadir a cada fila para que llegue al maximo_franky.   

        """ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        ENVOLTORIO DEL BODY / MATRIZ LIST FORMATO_FINAL 
        ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ """ 
        if family_impresion == 'MOSAICO':
            matriz_lst_formato_impresion = self.__get_matriz_F( lista_formato_contenido = matriz_LIST_F_natural, 
                                                                              lista_enteros_resto     = lst_resto_to_maxfranky )
        elif family_impresion == 'FIX' or family_impresion == 'MAX':
            matriz_lst_formato_impresion = self.__get_matriz_F(lista_formato_contenido = matriz_LIST_F_cuadrado, 
                                                                             lista_enteros_resto     = lst_resto_to_maxfranky )
        # ■ Validation
        if matriz_lst_formato_impresion is None: 
            print(f'Error::: No se ha podido determinar el formato de impresión.')
            return None
        
        """ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        APPEND VALORES TO MATRIZ-IMPRESION 
        ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ """        
        matriz_valores_impresion:list = []              # Matriz REsultante del añadir los valores y between
        
        for i, fila in enumerate(matriz_V_bruto):

            lista_print_xfila=[]                        # ...cada append es una columna del formato_final de impresion.
            """ ■■■ Envoltorio Izquierdo """
            lista_print_xfila.append(self.ESPACIO * self.margen)
            lista_print_xfila.append(self.char_marco)                
            lista_print_xfila.append(self.ESPACIO * self.x_pad)

            """ 
            ███ FILA-ROW APPEND VALORES (Dependiendo del tipo de impresión) ███ 
                ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ """
            for j, valor_celda in enumerate(fila):      
                
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                # ■ Preparo el BETWEEN de la CELDA 
                # ■ Style.RESET_ALL + sp_between ■ Despues de cada celda un RESET_ALL antes del espacio between.
                RESET_between:str = f''
                if family_impresion == 'MOSAICO':
                    RESET_between  = f'{Style.RESET_ALL}' + ( self.valor_default if (matriz_F_BTWN[i][j] == 0) or (j >= lista_ultima_columna_used[i]) 
                                                                                else self.ESPACIO * matriz_F_BTWN[i][j] )
                elif family_impresion == 'FIX' or family_impresion == 'MAX': 
                    RESET_between  = f'{Style.RESET_ALL}' + ( self.valor_default if (matriz_F_BTWN[i][j] == 0) or (j >= ultima_columna_used) 
                                                                                else self.ESPACIO * matriz_F_BTWN[i][j] )
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
                # ■ Final de la Ultima Columna Usada?
                # ■ ... no tiene porque ser el final de la matriz.                
                if j > ultima_columna_used:                                 # ■ FROM la última columna Total es mas general
                    lista_print_xfila.append( self.valor_default )
                    lista_print_xfila.append( self.valor_default )
                    continue
                pass

                # ■ ■ ■ ■ ■ ■ ■ ■ A partir de Aquí, ESTOY en el RANGO DE USO:
                
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
                # ■ Celda Viene Vacía? 
                if(valor_celda == self.valor_default):     
                    lista_print_xfila.append( self.valor_default )
                    lista_print_xfila.append(RESET_between)
                    continue
                pass                  

                # ■ Preparo un booleano(b_lista) para pasarlo a la funcion self.__get_valor_diferencia(). 
                # ■ Sirve para saber si width_formato será tratado como fixed(si b_lista == True) o como family_impresion (si b_lista == False)
                b_lista = True if lista and 0 <= j < len(lista) else False
                
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
                # VALOR y la DIFERENCIA 
                # ■ ■ ■ ■ Valor de la celda y diferencia de tamaños por colorama 
                valor_OK , diferencia = F_r_a_n_k_y.__get_valor_diferencia(valor_bruto=valor_celda, 
                                                                     width_formato=matriz_F_ancho_cuadrado[i][j], 
                                                                     family_impresion=family_impresion, 
                                                                     b_lista=b_lista)

                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
                # LISTA-FIX 
                # ■■ Esta es al opcion de lista personalizada(lista == [7,7,5] xEj) 
                # ■■ Se trata siempre como Fixed
                if (lista is not None) and  (0 <= j < len(lista)):  
                    # ■■■ APPEND VALOR LISTA-FIX ■■■ 
                    if (matriz_L_limpio[i][j] > lista[j]) and (lista[j] != 0):                          # ■■ IF hay que CORTAR:
                        valor_RED = f'{valor_OK[:-1]}{Fore.RED}{valor_OK[-1]}{Style.RESET_ALL}'   # ■■ Termina en caracter rojo.
                        lista_print_xfila.append( valor_RED )    
                    else:                                                                               # ■■ IF Not hay que CORTAR:
                        lista_print_xfila.append( valor_OK )                                         # ■■ 
                    
                    # ■■■ APPEND SP_BETWEEN LISTA-FIX ■■■ 
                    diferencia_RESET_between = self.ESPACIO * diferencia + RESET_between
                    lista_print_xfila.append(diferencia_RESET_between)
                    continue
                pass    

                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
                # APPEND DATOS 
                if family_impresion == 'MOSAICO':  
                    lista_print_xfila.append(valor_OK)        # ■ Literal / Mosaico add tal cual 
                
                elif family_impresion == 'FIX':    
                    if (matriz_L_limpio[i][j] > matriz_F_ancho_cuadrado[i][j]) and (matriz_F_ancho_cuadrado[i][j] != 0):       # ■■ SI CORTAR:
                        valor_RED = f'{valor_OK[:-1]}{Fore.RED}{valor_OK[-1]}{Style.RESET_ALL}'                   # Termina en caracter rojo.
                        lista_print_xfila.append( valor_RED )    
                    else:                                          # ■■ NO CORTAR(menor o igual)
                        lista_print_xfila.append( valor_OK )    
                
                elif family_impresion == 'MAX':                    
                    if diferencia < 0:
                        lista_print_xfila.append( f'{valor_OK}{self.ESPACIO * diferencia.abs()}')
                    else:
                        lista_print_xfila.append( f'{valor_OK}')
                pass
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
                # APPEND SP_BETWEEN
                diferencia_RESET_between = self.ESPACIO * diferencia + RESET_between
                lista_print_xfila.append(diferencia_RESET_between)
            pass
            """ ■■■ Envoltorio Derecho """
            lista_print_xfila.append(self.ESPACIO * lst_resto_to_maxfranky[i] )  # AÑADE EL RESTO EN ESPACIOS
            lista_print_xfila.append( self.ESPACIO * self.pad_x )           # AÑADE PAD_X EN ESPACIOS      
            lista_print_xfila.append( Style.RESET_ALL + self.char_marco )                     # AÑADE EL MARCO HORIZONTAL █

            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            # ■■■■■■ Añade la Fila Completa a la Matriz de Impresión ■■■■■■
            matriz_valores_impresion.append(lista_print_xfila)  
        pass
        # ■ ■ ■ ■ de aqui se sale con la matriz de valores de impresión completa.

        """ ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘ 
        IMPRESION 
        ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘ """
        
        if self.head is not None:                                                                 
            self.__imprimir_franky(tablero=self.head, maximo_franky=maximo_franky , up_line = True )                # ■■ HEAD 

        print(self.__linea_horizontal(char=self.char_up_body, maximo_franky=maximo_franky))                         # ■■ Marco Superior 
        for i, fila_impresion in enumerate(matriz_valores_impresion):                                                                           
            if fila_from <= i <= fila_to:                                                                           # ■■ BODY
                print(matriz_lst_formato_impresion[i].format(*fila_impresion)) 
        print(self.__linea_horizontal(char=self.char_down_body, maximo_franky=maximo_franky))                       # ■■ Marco Inferior 
        
        if self.pie is not None:                                                                 
            self.__imprimir_franky(tablero = self.pie, maximo_franky = maximo_franky , down_line = True  )          # ■■ PIE  
        # ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘
        
        return      # ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥

    def __get_matrices_formato(self, tablero, sp_between:int=0, baseline_format:str=None, b_cuadrado:bool=True):
        """ ■■ Obtiene las matrices de formato para el tablero especificado separadas en ancho y between y en formato-de-impresión ó cuadrado ó natural
        El resultado es desde el formato hacia matrices de enteros para operar a través de baseline_format.
        [tablero] (Tablero): Instancia de Tablero.
        [sp_between] (int): Espacio entre columnas.
        [b_cuadrado] (bool): Si es True, devuelve la matriz en formato cuadrado. Si es False, devuelve en formato natural.

        [baseline_format] (str): Formato base para la matriz.  ►  '{:<35}{:<2}{:<4}{:<2}{:<9}{:<2}{:<6}{:<2}{:<0}{:<2}{:<0}{:<2}'
        ► CALLED: self.__get_lista_L_SUM()
        ■ EJEMPLO:
            ► matriz_F_ANCH_Q , matriz_F_BTWN_Q = self.__get_matrices_formato( tablero=self, sp_between=2, baseline_format=baseline_format, b_cuadrado=True)
            ► matriz_F_ANCH_N , matriz_F_BTWN_N = self.__get_matrices_formato( tablero=self, sp_between=2, baseline_format=baseline_format, b_cuadrado=False)
            
        ■ SALIDA:
            Matrices de formato ancho y between o bien en formato cuadrado(fix, max) o bien en formato natural(mosaico)
            ► return matriz_F_ancho_cuadrado, matriz_F_between_cuadrado 
                matriz_F_ANCH_Q ► [[35, 4, 9, 6, 0, 0], [35, 4, 9, 6, 0, 0], [35, 4, 9, 6, 0, 0], [35, 4, 9, 6, 0, 0]]
                matriz_F_BTWN_Q ► [[2, 2, 2, 0, 0, 0], [2, 2, 2, 0, 0, 0], [2, 2, 2, 0, 0, 0], [2, 2, 2, 0, 0, 0]]
        
            ► return matriz_F_ancho_natural, matriz_F_between_natural
                matriz_F_ANCH_N ► [[35, 0, 0, 0, 0, 0], [35, 4, 9, 0, 0, 0], [35, 4, 9, 6, 0, 0], [35, 4, 9, 0, 0, 0]]
                matriz_F_BTWN_N ► [[0, 0, 0, 0, 0, 0], [2, 2, 0, 0, 0, 0], [2, 2, 2, 0, 0, 0], [2, 2, 0, 0, 0, 0]]

        """
        if not tablero or not isinstance(tablero, Tablero): return
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # MATRIZ BASE TYPE FORMATO IMPRESION ... Para sacar las matriz_(F) Formato - [Franky]
        matriz_LIST_F_natural  = self.__get_lst_formato_natural( baseline_format = baseline_format, sp_between = sp_between , tablero = tablero)
        matriz_LIST_F_cuadrado = self.__get_lst_formato_cuadrado(baseline_format = baseline_format, sp_between = sp_between , tablero = tablero )
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # MATRICES FORMATO - [Franky]
        matriz_F_ancho_natural     = F_r_a_n_k_y.__from_formato_to_matriz(lst_formato=matriz_LIST_F_natural, b_ancho_columna=True, b_sp_between=False)
        matriz_F_between_natural   = F_r_a_n_k_y.__from_formato_to_matriz(lst_formato=matriz_LIST_F_natural, b_ancho_columna=False, b_sp_between=True)

        matriz_F_ancho_cuadrado    = F_r_a_n_k_y.__from_formato_to_matriz(lst_formato=matriz_LIST_F_cuadrado, b_ancho_columna=True, b_sp_between=False)
        matriz_F_between_cuadrado  = F_r_a_n_k_y.__from_formato_to_matriz(lst_formato=matriz_LIST_F_cuadrado, b_ancho_columna=False, b_sp_between=True)

        # ■■ Retorno
        if b_cuadrado==True:
            return matriz_F_ancho_cuadrado, matriz_F_between_cuadrado
        else:
            return matriz_F_ancho_natural, matriz_F_between_natural
    
    # ◘◘◘◘◘◘◘ Genera la matriz de Formato de impresion
    def __get_matriz_F(self, lista_formato_contenido:list, lista_enteros_resto:list):
        """ ■ Genera una lista de string_formato con el FORMATO Imprimible de cada Fila:
        Lo que hace es crear el envoltorio de FORMATO para la matriz. añade el RESTO por fila.
        ■ {:<'margen'}{:<'marco'}{:<'x_pad'} {:<'cont_1'}{:<'sp_between'}...{:<'cont_n'}{:<'sp_between'} {:<'resto'}{:<'pad_x'}{:<'marco'}
        ■ {:<'0'}     {:<'█'}    {:<'3'}     {:<'7'}     {:<'1'}...         {:<'5'}     {:<'1'}          {:<'10'}   {:<'15'}   {:<'█'}

        Llamada desde self.__ruta_natural() y desde self.__ruta_cuadrada()

        [lista_formato_contenido]: lista de str_formatos de cada fila - ejemplo dimension 4x6
            ['{:<35}{:<2}{:<4}{:<2}{:<9}{:<2}{:<6}{:<0}{:<0}{:<0}{:<0}{:<0}', 
            '{:<35}{:<2}{:<4}{:<2}{:<9}{:<2}{:<6}{:<0}{:<0}{:<0}{:<0}{:<0}', 
            '{:<35}{:<2}{:<4}{:<2}{:<9}{:<2}{:<6}{:<0}{:<0}{:<0}{:<0}{:<0}', 
            '{:<35}{:<2}{:<4}{:<2}{:<9}{:<2}{:<6}{:<0}{:<0}{:<0}{:<0}{:<0}']

        [lista_enteros_resto]: lista de enteros con el resto a añadir a cada fila ► [2, 2, 2, 2]
        ■ EJEMPLO:
            if family_impresion == 'MOSAICO': 
                matriz_lst_formato_impresion = self.__get_matriz_F( lista_formato_contenido = matriz_LIST_F_natural, lista_enteros_resto = lst_resto_to_maxfranky )
            elif family_impresion == 'FIX' or family_impresion == 'MAX':
                matriz_lst_formato_impresion = self.__get_matriz_F(lista_formato_contenido = matriz_LIST_F_cuadrado, lista_enteros_resto = lst_resto_to_maxfranky )
        
        ■ SALIDA: una lista de str_formatos para cada fila.
            ['{:<0}{:<1}{:<2}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<27}{:<5}{:<1}', 
            '{:<0}{:<1}{:<2}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<50}{:<5}{:<1}', 
            '{:<0}{:<1}{:<2}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<51}{:<5}{:<1}', 
            '{:<0}{:<1}{:<2}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<48}{:<5}{:<1}']
        """
        try:
            # TAMAÑO DEL CHAR MARCO(SE PUEDEN ELEGIR MAS DE UN CARACTER PARA EL MARCO) 
            len_marco_limpio = Rango.len_limpio(texto = self.char_marco) if self.char_marco else 0

            lst_FINAL_FORMAT = [ 
                "{:<" + str(self.margen)+"}"                +
                "{:<" + str(len_marco_limpio) + "}"         +
                "{:<" + str(self.x_pad)+"}"                 + 
                formato_contenido                           + 
                "{:<" + str( resto )+"}"                    +
                "{:<" + str(self.pad_x)+"}"                 +
                "{:<" + str(len_marco_limpio)+"}"

                    for formato_contenido, resto in zip(lista_formato_contenido, lista_enteros_resto)
                ]

            return lst_FINAL_FORMAT if lst_FINAL_FORMAT else None
        except Exception as e:
            print(f'{e}')
            return None

    def __envuelve_fila_F(self, fila_F:str, resto_to_max:int=0):
        """  ■ Entra una fila en formato str {:<'7'}{:<'1'}{:<'5'}{:<'1'}
        y le pone el envoltorio: margen, char_marco, x_pad ► izquierda  y  resto_to_max, pad_x, char_marco ► derecha.
        ■ margen, char_marco, x_pad , pad_x Están configurados en set_style()
        ► CALLED: self.__get_head_excel()
        ■ EJEMPLO:
            head_excel_F = self.__envuelve_fila_F( fila_F = '{:<'7'}{:<'1'}{:<'5'}{:<'1'}' , resto_to_max = 66)
        ■ SALIDA:
            {:<'0'}{:<'1'}{:<'3'}  ►  {:<'7'}{:<'1'}{:<'5'}{:<'1'}  ◄  {:<'66'}{:<'15'}{:<'1'}            
        """
        try:
            # TAMAÑO DEL CHAR MARCO(SE PUEDEN ELEGIR MAS DE UN CARACTER PARA EL MARCO) 
            len_marco_limpio = Rango.len_limpio(texto = self.char_marco) if self.char_marco else 0
            fila_envuelta = (
                "{:<" + str(self.margen)+"}" + "{:<" + str(len_marco_limpio) + "}" + "{:<" + str(self.x_pad)+"}" + 
                fila_F                           + 
                "{:<" + str( resto_to_max )+"}" + "{:<" + str(self.pad_x)+"}" + "{:<" + str(len_marco_limpio)+"}"
                )
            # RETORNO            
            return fila_envuelta
        except Exception as e:
            print(f'{e}')
            return None
    
    # ◘◘◘◘◘◘◘
    def __get_maximo_franky(self):
        """ ■■ Obtiene el máximo de la matriz del tablero entre Head, body , pie.
        ■ SALIDA:
            int, Máximo de la matriz del tablero.
            0 si no tiene head, body, pie
        ■ EJEMPLO:
            maximo_franky = self.__get_maximo_franky()
        """
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        # PIE
        if self.pie:
            max_lista_L_pie = max(self.__get_lista_L_SUM(tablero = self.pie))
            if max_lista_L_pie is None:  max_lista_L_pie = 0
        else:
            max_lista_L_pie = 0
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        # BODY
        max_lista_L_body = max(self.__get_lista_L_SUM(tablero = self))
        if max_lista_L_body is None: 
            max_lista_L_body = 0
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        max_lista_L_head = 0
        if self.b_excel == True:                            # ► HEAD DE EXCEL
            max_lista_L_head = self.__get_maximo_head()          # ■■ HEAD-Excel
        
        else:                                                    # ► HEAD DE USUARIO.
            if self.head: 
                max_lista_L_head = max(self.__get_lista_L_SUM(tablero = self.head))
                if max_lista_L_head is None:  max_lista_L_head = 0
            else:
                max_lista_L_head = 0

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        return max(max_lista_L_head, max_lista_L_body, max_lista_L_pie)

    def __ok_data(self, tablero, fila_from:int=0, fila_to:int=None , **kwargs):
        """ ■■ Valida y devuelve los datos "buenos" de configuración.
        [tablero] (Tablero): Instancia de Tablero.
        [fila_from]:int=0,  fila desde a imprimir.
        [fila_to]:int=None, fila hasta a imprimir.
        [kwargs]
            ► [lista] (list): Lista de columnas a imprimir. Si es None, imprime todas las columnas.
            ► [ancho] (int): Ancho de las columnas. Si es None, usa el ancho por defecto.
            ► [between] (int): Espacio entre columnas. Por defecto es 0.
        ■ SALIDA: (sobre una dimension =  "4x6")
            lista, ancho_columna, sp_between, fila_from, fila_to ►  [8,8] , None, 2 , 0, 3
                                                                 ►  None, None, None, None, None
        ■ EJEMPLO:
            lista, ancho, sp_between, fila_from , fila_to = self.__ok_data(tablero = self.head, lista=None, ancho_columna=None, sp_between=2 )
        """
        # ■■ Valida el tablero
        if tablero is None: tablero = self
        if not isinstance(tablero, Tablero): return None, None, None, None, None


        # ■■ Valida que exista matriz.
        if  not tablero.matriz: return None, None, None, None, None

        # ■ Se asignan Los valores de impresión según el tablero:
        if tablero == self.head:
            lista           = self.dicc_print['head']['lista'] 
            ancho_columna   = self.dicc_print['head']['ancho_columna'] 
            sp_between      = self.dicc_print['head']['sp_between']
        elif tablero == self.pie:
            lista           = self.dicc_print['pie']['lista']
            ancho_columna   = self.dicc_print['pie']['ancho_columna']
            sp_between      = self.dicc_print['pie']['sp_between']
        elif tablero == self:            
            lista = kwargs.get('lista', None)
            ancho_columna = kwargs.get('ancho_columna', None)
            sp_between = kwargs.get('sp_between', 0)
        else:
            print(f'Error::: El tablero debe ser  head o body o pie.')
            return None, None, None, None, None

        # ■ Valida fila_from
        try:                                   
            fila_from = int(fila_from)
            fila_from = abs(fila_from)
        except Exception as e:
            print(f'{e}')
            return None, None, None, None, None
        
        # Valida fila_to
        if fila_to is None:
            fila_to = tablero.celda_fin.fila        
        else:
            try:
                fila_to=abs(int(fila_to))
                # VALIDA LOS LIMITES DE LAS FILAS PASADAS
                if not tablero.celda_inicio.fila <= fila_from <= fila_to <= tablero.celda_fin.fila:
                    print(f'fila_from( {fila_from} ) ► fila_to( {fila_to} ) fuera de rango')
                    return None, None, None, None, None
            except Exception as e:
                print(f'{e}')
                return None, None, None, None, None

        # Asegura que fila_from <= fila_to
        if fila_from > fila_to:
            fila_from, fila_to = fila_to, fila_from  
        
        # Valida lista
        if lista is not None:
            if not isinstance(lista, list): return None, None, None, None, None     # Valida que sea typo list.
            if not lista: return None, None, None, None, None                       # Valida que la lista no esté vacía
            try:                                    # Valida que sea una lista de enteros positivos
                lista = [int(i) for i in lista]
                lista = [abs(i) for i in lista]     # Valida que sean enteros positivos
            except Exception as e:
                print(f'{e}')
                return None, None, None, None, None            
        
        # Valida ancho_columna
        if ancho_columna is not None:    # Si es None, es un valor admitido así que No lo trato.
            try:                                   
                ancho_columna = int(ancho_columna)
                ancho_columna = abs(ancho_columna)
            except Exception as e:
                print(f'{e}')
                return None, None, None, None, None
        
        # Valida sp_between
        try:                                   
            sp_between = int(sp_between)
            sp_between = abs(sp_between)
        except Exception as e:
            print(f'{e}')
            return None, None, None, None, None
        
        # ■■■■■■ Elimina los caracteres vacios por la derecha antes de nada(para evitar confusiones luego ;) UPDT: CUANDO SE CREA LA MATRIZ. 
        try:
            for fila in tablero.matriz:
                for celda in fila:
                    if celda.valor != '' and isinstance(celda.valor, str):
                        celda.valor = str(celda.valor).rstrip()
                pass
        except Exception as e:
            print(f'{e}')
            return None, None, None, None, None
        
        return lista, ancho_columna, sp_between, fila_from, fila_to

    def __get_lista_L_SUM(self, tablero):
        """ ■ Obtiene la lista de longitudes de las celdas en la fila de impresión.
        [tablero] (Tablero): Instancia de Tablero.
        ■ EJEMPLO:
            ► max_lista_L_body = max(self.__get_lista_L_SUM(tablero = self))
              if max_lista_L_body is None: max_lista_L_body = 0
            ► max_lista_L_pie = max(self.__get_lista_L_SUM(tablero = self.pie))
        ■ SALIDA: (dimension =  "4x6")
            [60, 60, 60, 60]    ► 'FIX' , 'MAX'
            [57, 15, 18, 6]     ► 'MOSAICO'
        """        
        if not tablero or not isinstance(tablero, Tablero): return

        if tablero == self.head:
            lista           = self.dicc_print['head']['lista'] 
            ancho_columna   = self.dicc_print['head']['ancho_columna'] 
            sp_between      = self.dicc_print['head']['sp_between']
        elif tablero == self.pie:
            lista           = self.dicc_print['pie']['lista']
            ancho_columna   = self.dicc_print['pie']['ancho_columna']
            sp_between      = self.dicc_print['pie']['sp_between']
        elif ( tablero == self or 
               tablero == self.head_excel ):            
            lista           = self.dicc_print['body']['lista']
            ancho_columna   = self.dicc_print['body']['ancho_columna']
            sp_between      = self.dicc_print['body']['sp_between']
        else:
            return None            
        pass

        # ■■ Matriz de longitud de celda.valor de los caracteres imprimibles 
        # ■■ Longitud del texto sin ANSI
        matriz_L_limpio = [ [ len(F_r_a_n_k_y.__texto_limpio(texto = str(celda.valor)))  
                                for celda in fila ] for fila in tablero.matriz ]
                                
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        # BASELINE FORMATO - [Rango]       
        baseline_format = tablero.get_baseline_format(sp_between = sp_between , ancho_columna = ancho_columna , lista = lista)
        if not baseline_format: return None        
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        # TIPO DE IMPRESION - [Rango]
        # lista_family = ['MOSAICO', 'FIX', 'MAX']
        family_impresion = tablero.get_family_impresion(sp_between = sp_between , ancho_columna = ancho_columna , lista = lista)
        if family_impresion is None or family_impresion not in self.lista_family : return None
        
        # GET_MATRICES_FORMATO          ► matriz_F_cuadrado, matriz_F_natural
        matriz_F_ANCH_Q , matriz_F_BTWN_Q = self.__get_matrices_formato( tablero=tablero, sp_between=sp_between, baseline_format=baseline_format, b_cuadrado=True)
        matriz_F_ANCH_N , matriz_F_BTWN_N = self.__get_matrices_formato( tablero=tablero, sp_between=sp_between, baseline_format=baseline_format, b_cuadrado=False)

        # GET_LISTA_SUM_L               ► maximo_franky ► lst_resto_to_franky
        if family_impresion == 'MOSAICO':
            lista_L_SUM = self.__get_lista_L_SUM_natural(lista=lista, matriz_L_limpio=matriz_L_limpio, matriz_F_ancho_natural=matriz_F_ANCH_N, matriz_F_between_natural=matriz_F_BTWN_N)
        elif family_impresion == 'FIX' or family_impresion == 'MAX':
            lista_L_SUM = self.__get_lista_L_SUM_cuadrado(matriz_F_ancho_cuadrado=matriz_F_ANCH_Q, matriz_F_between_cuadrado=matriz_F_BTWN_Q)

        return lista_L_SUM if lista_L_SUM  else None

    def __get_lista_L_SUM_natural(self, lista:list, matriz_L_limpio, matriz_F_ancho_natural , matriz_F_between_natural):
        """ ■■ Obtiene el máximo de la matriz del tablero. Se usa en Formato de Impresión 'MOSAICO'. cuenta los valores y los espacios hasta
        la última columna usada. 
        [tablero] (Tablero): Instancia de Tablero.        
        [len_lista_fix] (int): Longitud de la lista fija.
        [matriz_L_limpio] (list): Matriz de longitudes(int) limpias de ANSII(color).
        [matriz_F_ancho_natural] (list): Matriz de int de ancho en formato natural.
        [matriz_F_between_natural] (list): Matriz de int de sp_between en formato natural.
        ■ SALIDA:
            ► [32, 60, 18, 15, 0 , 2] , para una matriz de 6 filas. 
        ■ EJEMPLO:
            lista_L_SUM = self.__get_lista_L_SUM_natural(lista=lista, matriz_L_limpio=matriz_L_limpio, matriz_F_ancho_natural=matriz_F_ANCH_N, matriz_F_between_natural=matriz_F_BTWN_N)
        """        
        # ■■■■■■■■ 
        # ■ Suma Ancho + sp_between, celda a celda, en formato natural (hasta la ultima columna)
        matriz_L_SUM_natural = [[a + b 
                            for a, b in zip(fila_len_sin_ansi, fila_between_nat)]
                            for fila_len_sin_ansi , fila_between_nat in zip(matriz_L_limpio, matriz_F_between_natural) ]
        # ■ ■ ■  Listas de longitudes totales de cada fila ... ■ Necesareos para maximo_franky
        lista_L_SUM_natural  = [sum(fila) for fila in matriz_L_SUM_natural]         # ■mosaico 
        pass
        
        # ■■■■■■■■ 
        # IF Lista + Mosaico
        if lista is not None:
            # ■ Mezcla dos Matrices a través de la longitud de lista. ■ Por si hace impresión 'FIX-MOSAICO'.
            matriz_mezcla_natural =  [ [ fila_A[col] if col < len(lista) 
                                                    else fila_B[col] 
                                            for col in range(len(fila_A))]
                                            for fila_A, fila_B in zip(matriz_F_ancho_natural , matriz_L_limpio) ]                                            
            # ■ Matriz de la Suma de Ancho + sp_between. 
            matriz_L_SUM_FIX_natural = [ [a + b 
                                            for a, b in zip(fila_a, fila_b)]
                                            for fila_a , fila_b in zip(matriz_mezcla_natural, matriz_F_between_natural) ]

            # ■ ■ ■ Listas de longitudes totales de cada fila ... ■ Necesareos para maximo_franky
            lista_L_SUM_FIX_natural  = [sum(fila) for fila in matriz_L_SUM_FIX_natural]

        # ■■ Retorno:        
        if lista is None:
            return lista_L_SUM_natural         # ■ sin Lista.
        else:
            return lista_L_SUM_FIX_natural     # ■ con Lista

    def __get_lista_L_SUM_cuadrado(self, matriz_F_ancho_cuadrado, matriz_F_between_cuadrado):
        """ ■ Devuelve la lista de longitudes de los valores de una fila en formato cuadrado.
         ■ LLamada desde __get_lista_L_SUM() 
        [matriz_F_ancho_cuadrado]:list, Lista de enteros que representan el formato (F) del ancho del valor del Tablero. 
        [matriz_F_between_cuadrado]:list, Lista de enteros que representan el formato (F) del espacios entre celda y celda del Tablero.
        ■ SALIDA:
            ► [62], xejem, en caso de head o pie.
            ► [40, 40, 40, 40, 40, 40] devuelve la longitud de sp + sp_between de cada fila. para una matriz de 6 filas xejemp.
        ■ EJEMPLO:
            lista_L_SUM = self.__get_lista_L_SUM_cuadrado(matriz_F_ancho_cuadrado = matriz_F_ANCH_Q , matriz_F_between_cuadrado = matriz_F_BTWN_Q )
        """
        # ■■■■■■■■ 
        # ■ Suma Ancho + sp_between, celda a celda, en formato cuadrado (hasta la ultima columna)
        matriz_L_SUM_cuadrado = [ [a + b 
                            for a, b in zip(fila_a, fila_b)]
                            for fila_a, fila_b in zip(matriz_F_ancho_cuadrado, matriz_F_between_cuadrado) ]
        # ■ ■ ■ Listas de longitudes totales de cada fila ... ■ Necesareos para maximo_franky
        lista_L_SUM_cuadrado = [sum(fila) for fila in matriz_L_SUM_cuadrado]        # ■fix ■max ■fix-fix ■fix-max
        # ■■■■■■■■ RETORNO
        return lista_L_SUM_cuadrado
        
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # ██████████████████████████████████████████████████
    def __ruta_natural(self, tablero, family_impresion:str, maximo_franky:int, lista:list=None, ancho_columna:int=None, sp_between:int=0):
        """ ■ Realiza todo el camino de impresion NATURAL (MOSAICO) y devuelve dos matrices (matriz_lst_formato_impresion, matriz_valores_impresion), con los datos de impresión.
        [tablero], El objeto tablero que se quiere imprimir.
        [family_impresion]:str, ('MOSAICO', 'FIX', 'MAX')
        [maximo_franky]:int, El maximo del body de Head( ó Head-Excel ) , Body , Pie
        [lista]:list de int, enteros de la lista personalizada de impresion. print_config
        [ancho_columna]:int, Anchos de columna fijos.                        print_config
        [sp_between]:int, Espacio entre columnas.                            print_config

        SALIDA:  (matriz de dimension "4x6")
            ■ matriz_lst_formato_impresion: Lista de str
                ['{:<0}{:<1}{:<2}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<27}{:<5}{:<1}', 
                '{:<0}{:<1}{:<2}{:<0}{:<2}{:<0}{:<2}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<46}{:<5}{:<1}', 
                '{:<0}{:<1}{:<2}{:<0}{:<2}{:<0}{:<2}{:<0}{:<2}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<45}{:<5}{:<1}', 
                '{:<0}{:<1}{:<2}{:<0}{:<2}{:<0}{:<2}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<0}{:<44}{:<5}{:<1}']
            
            ■ matriz_valores_impresion: list de list 
                [['', '█', '  ', '\x1b[32mLoren\x1b[0m Ipsum que estas en los cielos', '\x1b[0m', '', '\x1b[0m', '', '\x1b[0m', '', '\x1b[0m', '', '', '', '', '                           ', '     ', '\x1b[0m█'], 
                 ['', '█', '  ', 'False', '\x1b[0m  ', 'None', '\x1b[0m  ', 'Kun', '\x1b[0m', '', '\x1b[0m', '', '', '', '', '                                              ', '     ', '\x1b[0m█'],
                 ['', '█', '  ', '\x1b[35m4', '\x1b[0m  ', '5.5', '\x1b[0m  ', '6', '\x1b[0m  ', '\x1b[36mEy\x1b[0m You', '\x1b[0m', '', '', '', '', '                                             ', '     ', '\x1b[0m█'], 
                 ['', '█', '  ', '\x1b[34mTrue', '\x1b[0m  ', '1', '\x1b[0m  ', 'Vygostsky', '\x1b[0m', '', '\x1b[0m', '', '', '', '', '                                            ', '     ', '\x1b[0m█']
                ]
        EJEMPLO:
            matriz_F, matriz_V = self.__ruta_natural( tablero = self, family_impresion = 'MAX', maximo_franky = 95, lista = None, ancho_columna = None, sp_between = 2 )
        """
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        # DATOS GENERALES     
        # ► ultima_columna_used, lista_last_columna_used, matriz_V_bruto, matriz_L_limpio, base_line, family_format
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        
        # BASELINE FORMATO - [Rango]       
        baseline_format = tablero.get_baseline_format(sp_between = sp_between , ancho_columna = ancho_columna , lista = lista)
        if not baseline_format: return None, None
        
        lista_ultima_columna_used = tablero.get_lst_last_columna_used_xfila()   # Lista con la última columna usada xfila  - [Rango]
        ultima_columna_used = max(lista_ultima_columna_used) if lista_ultima_columna_used else 0  # 
        
        # ■■ Matriz, con el valor en bruto ■■ ...con chars ansii colorama(si lo hay) ... ( celda.valor )
        matriz_V_bruto = [  [str(celda.valor) for celda in fila ] for fila in tablero.matriz ]             # matriz que se va a recorrer.

        # ■■ Matriz de longitud de celda.■■ Longitud del texto sin ANSI 
        matriz_L_limpio = [ [ len(F_r_a_n_k_y.__texto_limpio(texto = str(celda.valor)))  
                                for celda in fila ] for fila in tablero.matriz ]
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # MATRIZ BASE TYPE FORMATO IMPRESION ... Para sacar las matriz_(F) Formato - [Franky]
        matriz_LIST_F_natural  = self.__get_lst_formato_natural( baseline_format = baseline_format, sp_between = sp_between , tablero = tablero)
        matriz_LIST_F_cuadrado = self.__get_lst_formato_cuadrado(baseline_format = baseline_format, sp_between = sp_between , tablero = tablero )

        # """ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # MATRICES FORMATO - [Franky]"""

        matriz_F_ancho_natural     = F_r_a_n_k_y.__from_formato_to_matriz(lst_formato=matriz_LIST_F_natural, b_ancho_columna=True , b_sp_between=False)
        matriz_F_between_natural   = F_r_a_n_k_y.__from_formato_to_matriz(lst_formato=matriz_LIST_F_natural, b_ancho_columna=False, b_sp_between=True )
        matriz_F_ancho_cuadrado    = F_r_a_n_k_y.__from_formato_to_matriz(lst_formato=matriz_LIST_F_cuadrado,b_ancho_columna=True,  b_sp_between=False)

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        # MATRICES  - [Franky]       ■ Suma Ancho + sp_between, celda a celda, en formato natural (hasta la ultima columna)
        matriz_L_SUM_natural = [[a + b 
                            for a, b in zip(fila_len_sin_ansi, fila_between_nat)]
                            for fila_len_sin_ansi , fila_between_nat in zip(matriz_L_limpio, matriz_F_between_natural) ]
        
        # ■ ■ ■  Listas de longitudes totales de cada fila ... ■ Necesareos para maximo_franky
        lista_L_SUM_natural  = [sum(fila) for fila in matriz_L_SUM_natural]         # ■mosaico 

        # ■■■■■■■■ 
        # IF Lista + Mosaico
        if lista is not None:
            # ■ Mezcla dos Matrices a través de la longitud de lista. ■ Por si hace impresión 'FIX-MOSAICO'.
            matriz_mezcla_natural =  [ [ fila_A[col] if col < len(lista) 
                                                    else fila_B[col] 
                                            for col in range(len(fila_A))]
                                            for fila_A, fila_B in zip(matriz_F_ancho_natural , matriz_L_limpio) ]    

            # ■ Matriz de la Suma de Ancho + sp_between. 
            matriz_L_SUM_FIX_natural = [ [a + b 
                                            for a, b in zip(fila_a, fila_b)]
                                            for fila_a , fila_b in zip(matriz_mezcla_natural, matriz_F_between_natural) ]

            # ■ ■ ■ Listas de longitudes totales de cada fila ... ■ Necesareos para maximo_franky
            lista_L_SUM_FIX_natural  = [sum(fila) for fila in matriz_L_SUM_FIX_natural]

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        # SUMA DE LONGITUDES TOTAL(BIN) DE CADA FILA ... para calcular el ■maximo_franky y el ■resto_to_maxfranky.
        if lista is None:
            lista_L_SUM = lista_L_SUM_natural         # ■ sin Lista.
        else:
            lista_L_SUM = lista_L_SUM_FIX_natural     # ■ con Lista

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        # FORMATO SP-BETWEEN - MATRIZ F_BTWN ... Para calcular la matriz_valores_impresion
        matriz_F_BTWN = matriz_F_between_natural            # ■■ Formato_BTWN

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        # MAXIMO FRANKY ( Max entre Head / Body / Pie ) 
        maximo_franky = self.__get_maximo_franky()
        lst_resto_to_maxfranky = [ maximo_franky - L for L in lista_L_SUM ]         # ■ Lista de enteros con el resto a añadir a cada fila para que llegue al maximo_franky.   

        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        # ENVOLTORIO DEL BODY / MATRIZ LIST FORMATO_FINAL 
        matriz_lst_formato_impresion = self.__get_matriz_F( lista_formato_contenido = matriz_LIST_F_natural, lista_enteros_resto = lst_resto_to_maxfranky )

        # ■ Validation
        if matriz_lst_formato_impresion is None: 
            print(f'Error::: No se ha podido determinar el formato de impresión.')
            return None, None
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        # APPEND VALORES TO MATRIZ-IMPRESION 
        matriz_valores_impresion:list = []              # Matriz REsultante del añadir los valores y between
        for i, fila in enumerate(matriz_V_bruto):

            lista_print_xfila=[]                        # ...cada append es una columna del formato_final de impresion.
            """ ■■■ Envoltorio Izquierdo """
            lista_print_xfila.append(self.ESPACIO * self.margen)
            lista_print_xfila.append(self.char_marco)                
            lista_print_xfila.append(self.ESPACIO * self.x_pad)

            """ 
            ███ FILA-ROW APPEND VALORES (Dependiendo del tipo de impresión) ███ 
                ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ """
            for j, valor_celda in enumerate(fila):      
                
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                # ■ Preparo el BETWEEN de la CELDA 
                # ■ Style.RESET_ALL + sp_between ■ Despues de cada celda un RESET_ALL antes del espacio between.
                RESET_between  = f'{Style.RESET_ALL}' + ( self.valor_default if (matriz_F_BTWN[i][j] == 0) or (j >= lista_ultima_columna_used[i]) 
                                                                             else self.ESPACIO * matriz_F_BTWN[i][j] )
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
                # ■ Final de la Ultima Columna Usada?
                # ■ ... no tiene porque ser el final de la matriz.                
                if j > ultima_columna_used:                                 # ■ FROM la última columna Total es mas general
                    lista_print_xfila.append( self.valor_default )
                    lista_print_xfila.append( self.valor_default )
                    continue
                pass

                # ■ ■ ■ ■ ■ ■ ■ ■ A partir de Aquí, ESTOY en el RANGO DE USO:
                
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
                # ■ Celda Viene Vacía? 
                if(valor_celda == self.valor_default):     
                    lista_print_xfila.append( self.valor_default )
                    lista_print_xfila.append(RESET_between)
                    continue
                pass                  

                # ■ Preparo un booleano(b_lista) para pasarlo a la funcion self.__get_valor_diferencia(). 
                # ■ Sirve para saber si width_formato será tratado como fixed o como family_impresion (si b_lista == False)
                b_lista = True if lista and 0 <= j < len(lista) else False
                
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
                # VALOR y la DIFERENCIA 
                # ■ ■ ■ ■ Valor de la celda y diferencia de tamaños por colorama 
                valor_OK , diferencia = F_r_a_n_k_y.__get_valor_diferencia(valor_bruto=valor_celda, 
                                                                     width_formato=matriz_F_ancho_cuadrado[i][j], 
                                                                     family_impresion=family_impresion, 
                                                                     b_lista=b_lista)
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
                # LISTA-FIX 
                # ■■ Esta es al opcion de lista personalizada(lista == [7,7,5] xEj) 
                # ■■ Se trata siempre como Fixed
                if (lista is not None) and  (0 <= j < len(lista)):  
                    # ■■■ APPEND VALOR LISTA-FIX ■■■ 
                    if (matriz_L_limpio[i][j] > lista[j]) and (lista[j] != 0):                          # ■■ IF hay que CORTAR:
                        valor_RED = f'{valor_OK[:-1]}{Fore.RED}{valor_OK[-1]}{Style.RESET_ALL}'   # ■■ Termina en caracter rojo.
                        lista_print_xfila.append( valor_RED )    
                    else:                                                                               # ■■ IF Not hay que CORTAR:
                        lista_print_xfila.append( valor_OK )                                         # ■■ 

                    # ■■■ APPEND SP_BETWEEN LISTA-FIX ■■■ 
                    lista_print_xfila.append(self.ESPACIO * diferencia + RESET_between)
                    continue
                pass    

                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
                # APPEND CELDA
                lista_print_xfila.append(valor_OK)        # ■ Literal / Mosaico add tal cual 
                
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
                # APPEND SP_BETWEEN
                lista_print_xfila.append(self.ESPACIO * diferencia + RESET_between)
            pass
            """ ■■■ Envoltorio Derecho """
            lista_print_xfila.append(self.ESPACIO * lst_resto_to_maxfranky[i] )  # AÑADE EL RESTO EN ESPACIOS
            lista_print_xfila.append( self.ESPACIO * self.pad_x )           # AÑADE PAD_X EN ESPACIOS      
            lista_print_xfila.append( Style.RESET_ALL + self.char_marco )                     # AÑADE EL MARCO HORIZONTAL █

            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            # ■■■■■■ Añade la Fila Completa a la Matriz de Impresión ■■■■■■
            matriz_valores_impresion.append(lista_print_xfila)  
        pass
        # ■ ■ ■ ■ de aqui se sale con la matriz de valores de impresión completa.
        return matriz_lst_formato_impresion, matriz_valores_impresion

    # ██████████████████████████████████████████████████
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    def __ruta_cuadrado(self, tablero, family_impresion:str, maximo_franky:int, lista:list=None, ancho_columna:int=None, sp_between:int=0):
        """ ■ Realiza todo el camino de impresion cuadrada (FIX y MAX) y devuelve dos matrices (matriz_lst_formato_impresion, matriz_valores_impresion), con los datos de impresión.
        [tablero], 
        [family_impresion]:str, ('MOSAICO', 'FIX', 'MAX')
        [maximo_franky]:int, El maximo del body de Head( ó Head-Excel ) , Body , Pie
        [lista]:list de int, enteros de la lista personalizada de impresion. print_config
        [ancho_columna]:int, Anchos de columna fijos.                        print_config
        [sp_between]:int, Espacio entre columnas.                            print_config

        SALIDA: matriz de dimension "4x6"
            ■ matriz_lst_formato_impresion: Le llamo matriz pq representa una matriz, pero en realidad es una lista de str. 
                [
                '{:<0}{:<1}{:<2}{:<35}{:<2}{:<4}{:<2}{:<9}{:<2}{:<6}{:<0}{:<0}{:<0}{:<0}{:<0}{:<2}{:<5}{:<1}', 
                '{:<0}{:<1}{:<2}{:<35}{:<2}{:<4}{:<2}{:<9}{:<2}{:<6}{:<0}{:<0}{:<0}{:<0}{:<0}{:<2}{:<5}{:<1}', 
                '{:<0}{:<1}{:<2}{:<35}{:<2}{:<4}{:<2}{:<9}{:<2}{:<6}{:<0}{:<0}{:<0}{:<0}{:<0}{:<2}{:<5}{:<1}', 
                '{:<0}{:<1}{:<2}{:<35}{:<2}{:<4}{:<2}{:<9}{:<2}{:<6}{:<0}{:<0}{:<0}{:<0}{:<0}{:<2}{:<5}{:<1}'
                ]
            ■ matriz_valores_impresion: Lista de listas de valores.
                [
                ['', '█', '  ', '\x1b[32mLoren\x1b[0m Ipsum que estas en los cielos', '\x1b[0m  ', '', '\x1b[0m  ', '', '\x1b[0m  ', '', '\x1b[0m', '', '', '', '', '  ', '     ', '\x1b[0m█'], 
                ['', '█', '  ', 'False', '\x1b[0m  ', 'None', '\x1b[0m  ', 'Kun', '\x1b[0m  ', '', '\x1b[0m', '', '', '', '', '  ', '     ', '\x1b[0m█'], 
                ['', '█', '  ', '\x1b[35m4', '     \x1b[0m  ', '5.5', '\x1b[0m  ', '6', '\x1b[0m  ', '\x1b[36mEy\x1b[0m You', '\x1b[0m', '', '', '', '', '  ', '     ', '\x1b[0m█'], 
                ['', '█', '  ', '\x1b[34mTrue', '     \x1b[0m  ', '1', '\x1b[0m  ', 'Vygostsky', '\x1b[0m  ', '', '\x1b[0m', '', '', '', '', '  ', '     ', '\x1b[0m█']
                ]
        EJEMPLO:
            matriz_F, matriz_V = self.__ruta_cuadrado( tablero = self.head, family_impresion = 'FIX', maximo_franky = 95, lista = [5,5,7], ancho_columna = 8, sp_between = 1 )
        """
        # BASELINE FORMATO - [Rango]       
        baseline_format = tablero.get_baseline_format(sp_between = sp_between , ancho_columna = ancho_columna , lista = lista)
        if not baseline_format: return None
        
        lista_ultima_columna_used = tablero.get_lst_last_columna_used_xfila()   # Lista con la última columna usada xfila  - [Rango]
        ultima_columna_used = max(lista_ultima_columna_used) if lista_ultima_columna_used else 0  # 

        # ■■ Matriz, con el valor en bruto ■■ ...con chars ansii colorama(si lo hay) ... ( celda.valor )
        matriz_V_bruto = [  [str(celda.valor) for celda in fila ] for fila in tablero.matriz ]             # matriz que se va a recorrer.

        # ■■ Matriz de longitud de celda.■■ Longitud del texto sin ANSI 
        matriz_L_limpio = [ [ len(F_r_a_n_k_y.__texto_limpio(texto = str(celda.valor) ))  
                                for celda in fila ] for fila in tablero.matriz ]
        
        # MATRIZ BASE TYPE FORMATO IMPRESION ... Para sacar las matriz_(F) Formato - [Franky]
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        matriz_LIST_F_cuadrado = self.__get_lst_formato_cuadrado(baseline_format = baseline_format, sp_between = sp_between , tablero = tablero )
        
        # MATRICES FORMATO - [Franky]
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        matriz_F_ancho_cuadrado    = F_r_a_n_k_y.__from_formato_to_matriz(lst_formato=matriz_LIST_F_cuadrado, b_ancho_columna=True, b_sp_between=False)
        matriz_F_between_cuadrado  = F_r_a_n_k_y.__from_formato_to_matriz(lst_formato=matriz_LIST_F_cuadrado, b_ancho_columna=False, b_sp_between=True)
            
        # MATRICES  - [Franky]  ■■■■■■■■ Suma Ancho + sp_between, celda a celda, en formato cuadrado (hasta la ultima columna)
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        matriz_L_SUM_cuadrado = [ [a + b 
                            for a, b in zip(fila_a, fila_b)]
                            for fila_a, fila_b in zip(matriz_F_ancho_cuadrado, matriz_F_between_cuadrado) ]
        # ■ ■ ■ Listas de longitudes totales de cada fila ... ■ Necesareos para maximo_franky
        lista_L_SUM_cuadrado = [sum(fila) for fila in matriz_L_SUM_cuadrado]        # ■fix ■max ■fix-fix ■fix-max

        # SUMA DE LONGITUDES TOTAL(BIN) DE CADA FILA ... para calcular el ■maximo_franky y el ■resto_to_maxfranky.
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        lista_L_SUM = lista_L_SUM_cuadrado            # ■ con Lista ■ sin Lista

        # FORMATO SP-BETWEEN - MATRIZ F_BTWN ... Para calcular la matriz_valores_impresion
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        matriz_F_BTWN = matriz_F_between_cuadrado           # ■ Formato_BTWN

        # MAXIMO FRANKY ( Max entre Head / Body / Pie ) 
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        maximo_franky = self.__get_maximo_franky()
        lst_resto_to_maxfranky = [ maximo_franky - L for L in lista_L_SUM ]         # ■ Lista de enteros con el resto a añadir a cada fila para que llegue al maximo_franky.   

        # ENVOLTORIO DEL BODY / MATRIZ LIST FORMATO_FINAL  
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        matriz_lst_formato_impresion = self.__get_matriz_F(lista_formato_contenido = matriz_LIST_F_cuadrado, 
                                                            lista_enteros_resto     = lst_resto_to_maxfranky )
        # ■ Validation
        if matriz_lst_formato_impresion is None: 
            print(f'Error::: No se ha podido determinar el formato de impresión.')
            return None, None
        
        # APPEND VALORES TO MATRIZ-IMPRESION 
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
        matriz_valores_impresion:list = []              # Matriz REsultante del añadir los valores y between
        for i, fila in enumerate(matriz_V_bruto):
            lista_print_xfila=[]                        # ...cada append es una columna del formato_final de impresion.
            """ 
            ■■■ Envoltorio Izquierdo """
            lista_print_xfila.append(self.ESPACIO * self.margen)
            lista_print_xfila.append(self.char_marco)                
            lista_print_xfila.append(self.ESPACIO * self.x_pad)
            
            """ 
            ■■■ CUERPO / Celda a Celda / Columna a Columna / Hasta completar una FILA """
            for j, valor_celda in enumerate(fila):                      
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                # ■ Preparo el BETWEEN de la CELDA ■ Style.RESET_ALL + sp_between ■ Despues de cada celda un RESET_ALL antes del espacio between.
                RESET_between  = f'{Style.RESET_ALL}' + ( self.valor_default if (matriz_F_BTWN[i][j] == 0) or (j >= ultima_columna_used) 
                                                                                else self.ESPACIO * matriz_F_BTWN[i][j] )
                # ■ Final de la Ultima Columna Usada?    ■ ... no tiene porque ser el final de la matriz.                
                if j > ultima_columna_used:                                 
                    lista_print_xfila.append( self.valor_default )
                    lista_print_xfila.append( self.valor_default )
                    continue
                pass
                # ■ ■ ■ ■ ■ ■ ■ ■ A partir de Aquí, ESTOY en el RANGO DE USO:                
                # ■ Celda Viene Vacía? 
                if(valor_celda == self.valor_default):     
                    lista_print_xfila.append( self.valor_default )
                    lista_print_xfila.append(RESET_between)
                    continue
                pass                  

                # ■ Preparo un booleano(b_lista) para pasarlo a la funcion self.__get_valor_diferencia(). 
                # ■ Sirve para saber si width_formato será tratado como fixed(si b_lista == True) o como family_impresion (si b_lista == False)
                b_lista = True if lista and 0 <= j < len(lista) else False
                
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
                # VALOR y la DIFERENCIA 
                # ■ ■ ■ ■ Valor de la celda y diferencia de tamaños por colorama 
                valor_OK , diferencia = F_r_a_n_k_y.__get_valor_diferencia(valor_bruto=valor_celda, 
                                                                     width_formato=matriz_F_ancho_cuadrado[i][j], 
                                                                     family_impresion=family_impresion, 
                                                                     b_lista=b_lista)
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
                # LISTA-FIX 
                # ■ ■ ■ ■ Esta es al opcion de lista personalizada(lista == [7,7,5] xEj) 
                if (lista is not None) and  (0 <= j < len(lista)):  
                    # ■■■ APPEND VALOR LISTA-FIX ■■■ 
                    if (matriz_L_limpio[i][j] > lista[j]) and (lista[j] != 0):                          # ► IF hay que CORTAR:
                        valor_RED = f'{valor_OK[:-1]}{Fore.RED}{valor_OK[-1]}{Style.RESET_ALL}'         # ■■ Termina en caracter rojo.
                        lista_print_xfila.append( valor_RED )    
                    else:                                                                               # ► IF Not hay que CORTAR:
                        lista_print_xfila.append( valor_OK )                                            # ■■ Tal cual.
                    
                    # ■■■ APPEND SP_BETWEEN LISTA-FIX ■■■ 
                    diferencia_RESET_between = self.ESPACIO * diferencia + RESET_between
                    lista_print_xfila.append(diferencia_RESET_between)
                    continue
                pass    

                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
                # APPEND DATOS 
                if family_impresion == 'FIX':    
                    if (matriz_L_limpio[i][j] > matriz_F_ancho_cuadrado[i][j]) and (matriz_F_ancho_cuadrado[i][j] != 0):        # ► SI CORTAR:
                        valor_RED = f'{valor_OK[:-1]}{Fore.RED}{valor_OK[-1]}{Style.RESET_ALL}'                                 # Termina en caracter rojo.
                        lista_print_xfila.append( valor_RED )    
                    else:                                                                                                       # ► NO CORTAR(menor o igual)
                        lista_print_xfila.append( valor_OK )    
                
                elif family_impresion == 'MAX':                    
                    if diferencia < 0:
                        lista_print_xfila.append( f'{valor_OK}{self.ESPACIO * diferencia.abs()}')
                    else:
                        lista_print_xfila.append( f'{valor_OK}')
                pass
                # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 
                # APPEND SP_BETWEEN
                diferencia_RESET_between = self.ESPACIO * diferencia + RESET_between
                lista_print_xfila.append(diferencia_RESET_between)
            pass
            """ 
            ■■■ Envoltorio Derecho """
            lista_print_xfila.append(self.ESPACIO * lst_resto_to_maxfranky[i] )     # AÑADE EL RESTO EN ESPACIOS
            lista_print_xfila.append( self.ESPACIO * self.pad_x )                   # AÑADE PAD_X EN ESPACIOS      
            lista_print_xfila.append( Style.RESET_ALL + self.char_marco )           # AÑADE EL MARCO HORIZONTAL █

            # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
            # ■■■■■■ Añade la Fila Completa a la Matriz de Impresión ■■■■■■
            matriz_valores_impresion.append(lista_print_xfila)
        pass        
        # ■ ■ ■ ■ de aqui se sale con la matriz de valores de impresión completa.
        
        # ■ Validation
        if matriz_lst_formato_impresion is None: 
            print(f'Error::: No se ha podido determinar el formato de impresión.')
            return None, None
        
        # ► RETORNO
        return matriz_lst_formato_impresion, matriz_valores_impresion


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    # •••••••••  By David Quesada Heredia davidquesadaheredia@gmail.com ••••••••••
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■