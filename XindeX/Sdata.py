
import re       # patrones
from datetime import date, datetime     # fecha
from datetime import time               # hora
import shutil   # para obtener el tamaño de la terminal
import pyfiglet                               # ■ LETRAS GRANDES.
from colorama import Fore, Back, Style, init  # ■ COLORAMA PARA COLORES EN TERMINAL....por si se quiere usar colores para 'ayudas'


class Sdata():
    """ >>> CLASE ESTÁTICA ENTRA UNA KEY STR Y DEVUELVE UN DICCIONARIO CON VALUE LA ENTRADA X TECLADO 
    CON EL TIPO CORRECTO O VALOR POR DEFECTO O NULO (DEPENDIENDO DE LA CONFIGURACION).

    LOS TIPOS DE DATOS PUEDEN SER: str, int, float, bool, date, time, 'IP', 'DNI', 'EMAIL', 'BETWEEN', list, set, tuple.

    EL DICCIONARIO SE PUEDE IR AUTO-INCREMETANDO... INTRODUCIENDO DICC COMO PARAMETRO OPCIONAL DE UN DICCIONARIO QUE EXISTA.

    Ejemplo:
    >>> dict_result = Sdata.get_data( key_dict='l', tipo=list , msg_entrada='INTRODUCE LISTA SEPARANDO POR COMAS (1,2,3,...)', permite_nulo=True)
    >>> dict_result = Sdata.get_data( dicc=dict_result , key_dict='pos', tipo='BETWEEN' , msg_entrada=['VERTICAL', 'HORIZONTAL'], permite_nulo=False)    
    >>> dict_result = Sdata.get_data( dicc=dict_result , key_dict='dat', tipo = date , msg_entrada='INTRODUCE FECHA (dd/mm/yyyy)')    
    >>> print(f'lista: {dict_result['l']} - fecha: {dict_result['dat']} - hora: {dict_result['pos']} ')
    
    """
    
    # ■■■ Es un diccionario cuyo valor es una función lambda(func de una linea) que llama a una funciónn de la clase estática StringTo.
    #   ■ ■ Ejemplo de uso:   
    #       1• dato_tipado = Sdata.TIPOS_VALIDOS[<class int>](5)    ► Devuelve el int 5
    #       2• dato_tipado = Sdata.TIPOS_VALIDOS[<class int>]('A')  ► Devuelve None 
    #       3• dato_tipado = Sdata.TIPOS_VALIDOS[<class int>]('')   ► Devuelve None 

    TIPOS_VALIDOS = {
        int: lambda v: StringTo.esInt(v) if StringTo.esInt(v) is not False else None,
        float: lambda v: StringTo.esFloat(v) if StringTo.esFloat(v) != False else None,
        str: lambda v: v  ,
        bool: lambda v: v ,  # SOLO DEVUELVE VALOR, VALIDACION FUERA
        list: lambda v: v ,  # SOLO DEVUELVE VALOR, VALIDACION FUERA
        set: lambda v: v  ,  # SOLO DEVUELVE VALOR, VALIDACION FUERA
        tuple: lambda v: v ,  # SOLO DEVUELVE VALOR, VALIDACION FUERA
        date: lambda v: datetime.strptime(v, "%d/%m/%Y").date() if StringTo.esDate(v) else None,
        time: lambda v: datetime.strptime(v, "%H:%M").time() if re.match(r"^(2[0-3]|[01]?\d):([0-5]\d)$", v) else None,
        "DNI": lambda v: v if StringTo.esDNI(v) else None,
        "Email": lambda v: v if StringTo.esMail(v) else None,
        "IP": lambda v: v if StringTo.esIPValida(v) else None,
        "BETWEEN": lambda v: v  # SOLO DEVUELVE VALOR, VALIDACION FUERA
    }
    VALORES_POR_DEFECTO = {
        int: 0,
        float: 0.0,
        str: '',
        bool: False,
        list: None,
        set: None,
        tuple: None,
        date: date(1900, 1, 1),
        time: time(0, 0),
        "DNI": "00000000X",
        "Email": "unknown@mail.com",
        "IP": "0.0.0.0",
        "BETWEEN": None 
    }
    LISTA_VERDADEROS = ['v', 'verdad' , 'verdadero', 't' , 'true','y', 'yes', 'si', 's' ]
    LISTA_FALSOS = ['f' , 'false', 'no' , 'n' , 'falso']

    def __init__(self):
        pass

    def __str__(self):
        pass
   
    @staticmethod
    def get_valor_bydef(tipo):
        """ ■ Devuelve el valor por defecto de un tipo.
        ■ EJEMPLO:  Sdata.get_valor_bydef(tipo=int)
        ■ SALIDA:   el valor asignado al tipo del diccionario VALORES_POR_DEFECTO o None si no encuentra el tipo.
        """
        return Sdata.VALORES_POR_DEFECTO.get(tipo, None)

    @staticmethod
    def set_valor_bydef(tipo, valor):
        """ ■ Modifica o agrega un nuevo tipo al diccionario VALORES_POR_DEFECTO
        ■ EJEMPLO:  Sdata.set_valor_bydef(tipo=int, valor=None)
        ■ SALIDA:   None si Error y True si OK.
        """
        try:
            Sdata.VALORES_POR_DEFECTO[tipo] = valor
        except Exception as e:
            print(e)
            return None
        finally:
            return True

    @staticmethod
    def reset_valores_bydef():
        """ ■ Restaura los valores por defecto a sus valores iniciales.
        ■ EJEMPLO:  Sdata.reset_valores_bydef()
        """
        Sdata.VALORES_POR_DEFECTO = {
            int: 0,
            float: 0.0,
            str: "",
            bool: False,
            list: None,
            set: None,
            tuple: None,
            date: date(1900, 1, 1),
            time: time(0, 0),
            "DNI": "00000000X",
            "EMAIL": "unknown@mail.com",
            "IP": "0.0.0.0",
            "BETWEEN": None
        }

    # *******************************************
    # OBLIGA A INTRODUCIR EL DATO CORRECTO.
    # CON ( permite_nulo = True ) SI INTRODUCE ''(INTRO) SE BUSCA EL VALOR POR DEFECTO.
    # Funcion Que hace Tipado del diccionario JUSTO DESPUÉS DE INTRODUCIR LOS DATOS.
    # *******************************************
    @staticmethod
    def get_data(key_dict:str, dicc:dict = None, tipo = str, msg_entrada:str='Intro... ', permite_nulo:bool=False , valores_between:list=None ):
        """ 
        ■ Convierte una key de entrada en un diccionario (key): Intro by Teclado

            ■ ■ ■ entrada == ENTRADA_NULL and permite_nulo == True:   => obtiene el valor por defecto.
            ■ ■ ■ entrada == ENTRADA_NULL and permite_nulo == False:  => Repite entrada
            ■ ■ ■ entrada != ENTRADA_NULL                             => si valor valido => entrada
                                                                          => si valor no valido => Repite entrada
        
        [key_dict](str): la clave el dict resultante. INTRODUCIDA POR EL USUARIO
        [dicc](dict): si se introduce, y es un diccionario que existe, se añade la key a las keys del diccionario.
        [tipo](type, iterators,  'IP', 'MAIL', 'DNI', 'BETWEEN'): HACE TIPADO DE LA ENTRADA y VALIDACION.
        [permite_nulo](bool):   ► True, puedes meter un valor nulo con lo que se devuelve el valor por defecto.
                                ► False, Obliga: Tienes que meter un valor valido.
        [msg_entrada](str, list):   str: Son los mensajes que se muestran para cada pedida de datos al usuario.
                                    list: Son las opciones cuando el tipo es 'BETWEEN'... aunque tambien podría ser str separado por comas.

        ■ EJEMPLO:       
            1•  lista = Sdata.get_data( key_dict='l', tipo=list , msg_entrada='INTRODUCE LISTA SEPARANDO POR COMAS (1,2,3,...)', permite_nulo=True)
                lista = Sdata.get_data( dicc=lista , key_dict='pos', tipo='BETWEEN' , msg_entrada=['VERTICAL', 'HORIZONTAL'], permite_nulo=False)    
                lista = Sdata.get_data( dicc=lista , key_dict='dat', tipo = date , msg_entrada='INTRODUCE FECHA (dd/mm/yyyy)')    
                print(f'lista: {lista['l']} - fecha: {lista['dat']} - hora: {lista['pos']} ')
        ■ SALIDA:
               {'A': 9, 'B': 2} ► Salida de un diccionario creado con las key 'A' y 'B' y valores respectivos 9(tipo int) y 2(tipo int)
        """        
        # VALIDA QUE EL TIPO ESTÉ REGISTRADO
        if not tipo in Sdata.TIPOS_VALIDOS: 
            if isinstance(tipo, str):
                if not tipo.upper() in Sdata.TIPOS_VALIDOS:
                    return None
            else:
                return None                   
        
        # Diccionario de parametros         
        options = { 'msg_entrada':msg_entrada , 'permite_nulo': permite_nulo  } 

        # DICCIONARIO QUE SE CREA CON LOS PARAMETROS PASADOS. LUEGO TIENE QUE PASAR POR DICC PARA EL RETORNO FINAL        
        dictRetorno = {
            key_dict:Sdata.__introByTcld(key_dict = key_dict, tipo = tipo , options = options, valores_between = valores_between )
        }

        # ADD LA CLAVE AL DICCIONARIO PASADO COMO ARGUMENTO.
        if dictRetorno and dicc and key_dict not in dicc.keys() :
            dicc[key_dict] = dictRetorno.get(key_dict, None)
            return dicc
        else:
            return dictRetorno if dictRetorno else None

    # ********************
    # ********************
    @staticmethod
    def __introByTcld(key_dict, tipo, options=None, valores_between:list=None):
        """ 
        ■ From lista de str To Dict(k)valorLista1 (v)Intro Teclado. Permite elegir Nulo/noNulo y crecer
        K[ F ] - INTRODUCE FILA FROM   - ( INT - NULL )..... 1 ►  •key 'F' •tipo (int) •Permite Nulo(NULL) 
        
        [key_dict](str): key del dicc creado por el USER     ► 'C'
        [tipo](list)                                         ► <class 'str'>
        [options](dict) ► {'msg_entrada': 'INTRODUCE CELDA ( pejem: M:8 ) Xa Posicionar la MATRIZ', 'permite_nulo': True}
        [valores_between](list)

        ► CALLED: self.get_data(): 
        ■ EJEMPLO:
            dictRetorno = { key_dict:Sdata.__introByTcld(key_dict = key_dict, tipo = tipo , options = options, valores_between = valores_between ) }

        ■ SALIDA:   Depende de las condiciones(permite Nulo) tiene una salida u otra. Ejemplos de salidas...
                    Lo que Hace esta funcion 
            1• 'B:4' ►(str)  
            2• 9 ►(int)  
            3• True ►(bool)  
            4• None ►(byDef)  
            5• 7.44 ►(float)
            •••• 
        """
        ENTRADA_NULL = ''
        # EL DICT OPTIONS SE TIENE QUE DEFINIR ASÍ: Si tiene datos, se asignan , si no tiene datos se asigna diccionario vacio {}
        options = options or {}
        
        # RECOGE LOS DATOS DEL DICCIONARIO DE ENTRADA OPTIONS
        permite_nulo = options.get('permite_nulo', False)  
        msg_entrada  = options.get('msg_entrada', False)  
        
        # KEY DEL DICCIONARIO A CREAR ... INFO DEL MENSAJE INPUT
        
        pass
        
        # .... INFORMACION DEL TIPO EN STR
        if isinstance(tipo, type): 
            str_tipo = tipo.__name__.upper()
        elif isinstance(tipo, str):
            str_tipo = tipo
        elif isinstance(tipo, date): 
            str_tipo = 'DATE'
        elif isinstance(tipo, time):
            str_tipo = 'TIME'
        else:  # Si es una instancia de otro tipo, devolvemos su tipo
            str_tipo = type(tipo).__name__.upper()
        
        # EL TIPO CONDICIONA msg_entrada EN CASO DE SER BETWEEN
        if tipo == 'BETWEEN' :
            str_entrada = f'Elige Entre: [ {msg_entrada} ]'
        else:
            str_entrada = msg_entrada

        # .... INFO PERMITE NULL EN STR
        if permite_nulo == True:
            msg_nulo = 'NULL'
        else:
            msg_nulo = 'NOT NULL'
        pass
        
        # ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        # PIDO DATOS POR TECLADO
        while True:
            entrada = input(f'K[ {key_dict} ] - {str_entrada}  - ( {str_tipo} - {msg_nulo} )..... ')

            entrada = entrada.strip()
            try:
                if entrada == ENTRADA_NULL and permite_nulo == True:
                    """ ■ RETORNA ESTE VALOR PARA QUE SE TRATE EL ■■■ VALOR POR DEFECTO 
                    """
                    entrada = Sdata.get_valor_bydef(tipo=tipo)
                    break
                
                elif entrada == ENTRADA_NULL and not permite_nulo:
                    """ ■ REPITE, NO ADMITE NULO 
                    """
                    continue

                elif entrada != ENTRADA_NULL:                
                    """ ■ ENTRA DATO ... Se hace CASTING al tipo recogido 
                    """
                    try:
                        if tipo is bool:
                            """ ■ BOOL PUEDE SER MUCHAS COSAS... 
                            """
                            entrada = Sdata.__tratarBoolano(entrada)
                            if entrada == None:
                                continue

                        elif tipo is list or tipo is tuple or tipo is set:
                            """ ■ ENTRA UNA CADENA Y TIENE QUE SALIR UNA LISTA. 
                            """
                            entrada = StringTo.cadena_to_lista(cadena=entrada)
                            if not entrada: 
                                continue
                            else:
                                entrada = tipo(entrada)

                        elif str(tipo).upper() == 'BETWEEN':
                            """ ■ ENTRA BETWEEN. HAY VARIAS POSIBILIDADES.
                            [valores_between](list, str): una lista de valores o un string que son una lista de valores separados por comas.
                                No es obligatorio. Si no entra, Buscamos la lista de valores en msg_entrada
                            """
                            if valores_between:
                                if isinstance(valores_between, str):
                                    """ >>> ENTRA COMO UNA CADENA ... vemos si tiene items separados por comas Y LO DEJAMOS COMO UNA LISTA
                                    """
                                    lst_between = StringTo.cadena_to_lista(cadena=valores_between if valores_between else msg_entrada)

                                    # CONVIERTE LOS ELEMENTOS A STRING
                                    lst_between = [str(item_between) for item_between in lst_between]
                                    
                                    # COMPARA:
                                    if not entrada in lst_between:
                                        continue

                                elif isinstance(valores_between, list):
                                    """ >>> ENTRA COMO UNA LISTA .... LO IDEAL
                                    """
                                    may_entrada = entrada.upper()
                                    msg_between = [str(item).upper() for item in valores_between]
                                    if not may_entrada in msg_between:
                                        continue
                                    else: 
                                        # COMPARO LOS VALORES EN MAYUSCULAS CON EL ITEM DE ENTRADA EN MAYUSCULAS Y PASO EL VALOR BETWEEN(TYPO)
                                        for valor in valores_between:    
                                            if str(valor).upper() == may_entrada:
                                                entrada = valor
                                                break

                            elif not valores_between and msg_entrada:
                                """ >>> NO TIENES VALOR_BETWEEN, VAMOS A PROBAR CON MSG_ENTRADA, PERO NO DEBERÍA SER ASÍ. """
                                if isinstance(msg_entrada, str):
                                    lst_between = StringTo.cadena_to_lista(cadena=msg_entrada)                                    
                                    # CONVIERTE LOS ELEMENTOS A STRING
                                    lst_between = [str(item_between) for item_between in lst_between]
                                    # COMPARA:
                                    if not entrada in lst_between:
                                        continue

                                elif isinstance(msg_entrada, list):
                                    # ENTRA COMO UNA LISTA
                                    may_entrada = entrada.upper()
                                    msg_entrada = [str(item).upper() for item in msg_entrada]
                                    if not may_entrada in msg_entrada:
                                        continue
                                    else: 
                                        for item in msg_entrada:
                                            if item == may_entrada:
                                                entrada = item
                                                break
                            else:
                                continue
                        else:
                            """ ■ DATE, TIME, IP, DNI, EMAIL, ... 
                            """
                            entrada = Sdata.TIPOS_VALIDOS[tipo](entrada)    # FORMA DE LLAMAR A LA FUNCION DEL DICCIONARIO DE CLASE.
                            if entrada == None and permite_nulo == False:
                                continue
                            elif entrada == None and permite_nulo == True:
                                entrada = Sdata.get_valor_bydef(tipo=tipo)
                            pass  
                    except Exception as e:
                        print(f'{e}')
                        continue
                    else:
                        break
            except Exception as e:
                print(f'ERROR: {e}')
                return None
        return entrada

    @staticmethod
    def __tratarBoolano(entrada_bool:str):
        """ 
        ■ ADMITE Varias FORMAS DE BOOLEANO.('v', 'verdad', 'falso', 'f' ... )
        ► CALLED: self.__introByTcld()

        ■ EJEMPLO:  entrada = Sdata.__tratarBoolano(entrada)
        ■ SALIDA: 1• True ► si el usuario introduce un forma-verdadero , 2• False ► si el usuario introduce un forma-falso , 3• None ► No es una forma-bool.
        """
        entrada_bool=str(entrada_bool).strip().lower()
        if entrada_bool in Sdata.LISTA_VERDADEROS:
            return True
        elif entrada_bool in Sdata.LISTA_FALSOS:
            return False
        else:
            return None

    @staticmethod
    def big_text(texto: str, color: str = Fore.WHITE):
        """ 
        ■ Pone un texto en letra grande pyfiglet con un color. siempre con la fuente small... de momento 
        ■ EJEMPLO:
            print(big_text(texto='Hola', color=Fore.YELLOW))
        """
        try:            
            ancho_terminal = Sdata.__obtener_ancho_ajustado()
            big = pyfiglet.figlet_format(f'{texto}', font="small", width=ancho_terminal)  # Ajusta el font y width aquí.
            big_color = f'{color}{big}{Fore.RESET}' if color else big
        except Exception as e:
            return ''
        finally:
            return big_color

    @staticmethod
    def obtener_tamaño_terminal():
        """ ■ IA. 
        A traves de la librería shutil obtenemos las filas y columnas del terminal.
        """ 
        columnas, filas = shutil.get_terminal_size()
        return columnas, filas
    
    @staticmethod
    def __obtener_ancho_ajustado(margen=10):
        """Obtiene el ancho de la terminal con un margen de seguridad."""
        columnas, _ = shutil.get_terminal_size()
        return max(20, columnas - margen)  # Evita valores muy pequeños

    # NO USADA
    @staticmethod
    def imprimir_con_pausa(texto, lineas_por_pausa=None):
        """
        Imprime texto en la terminal y pausa si el contenido es más grande que la terminal.... IA
        [texto] (str): Texto a imprimir.
        [lineas_por_pausa] (int, opcional): Número de líneas a imprimir antes de pausar. Si es None, se usa el tamaño de la terminal.
        EJEMPLO:
            OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        """
        _ , filas_terminal = shutil.get_terminal_size()
        lineas = texto.split('\n')  # Divide el texto en líneas
        
        if lineas_por_pausa is None:
            lineas_por_pausa = filas_terminal - 1  # Deja espacio para el mensaje "Presiona una tecla..."

        for i, linea in enumerate(lineas, 1):
            print(linea)
            
            # Pausa si se alcanza el límite de líneas o si el texto es más grande que la terminal
            if i % lineas_por_pausa == 0 or len(lineas) > filas_terminal:
                input("\n--- Presiona Enter para continuar ---\n")

class StringTo():
    """ 
    Clase Estática que usa expresiones regulares para validar patrones:
    Tb es convertidor de tipo int, float, str, date(aun no).
    Tb tiene funciones utiles con listas y diccionarios.

    partirDNI()       => r"^(\d{8})[-.\s]?([a-zA-Z])$"
    esMail()          => r'^(\w+)@(\w+)$'
    esIPValida()      => r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'
    partirIP()        => r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$'
    estaEnLista()     => Valida si un elemento está en una lista pasada como argumento.
    esInt()           => r'^-?\d+$'
    esFrase()         => r'^[da-zA-Z]+$'
    esFloat()         => r"^[+-]?(\d*\.\d+|\d+\.\d*|\d+)$"
    copyDict() copyList() => lo dejo pq ya está hecho, pero se sustituye por: 
        dicc2=dicc1.copy() 
        dicc2=dict(dicc1)
    copyList() => lo dejo pq ya está hecho, pero se sustituye por: 
        list2=list(list1)
    """
    def __init__(self):
        """ 
        Constructor: 
        """
        pass
    def __str__(self):
        pass    
            
    @staticmethod
    def partirDNI(dni):
        """
        Def: Valida un dni con expresiones regulares [8 numeros + ['.','-',' ']letra]
        Retorno: El numero de dni , la letra del dni
        None si no es formato valido.
        """
        pattern = r"^(\d{8})[-.\s]?([a-zA-Z])$"
        
        match = re.match(pattern, dni)
        if match:
            number = match.group(1)
            letter = match.group(2)
            return number, letter
        else:
            return None, None
    
    @staticmethod
    def esDNI(dni):
        """ Devuelve True o False si se introduce un DNI valido o Invalido. """
        numero, letra = StringTo.partirDNI(dni) 
        if numero == None or letra == None: 
            return False
        else:
            return True

    @staticmethod
    def partirIP(ip):
        """ 
        Def: Entra una ip y la descompongo en los 4 grupos que tiene.
        Args: [ip]: Una ip
        Return: return grupo_1, grupo_2, grupo_3, grupo_4 
        """
        try:
            regIp = r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$'
            if infoSocket.esIPValida():
                match = re.match(regIp, ip)
                if match:
                    grupo_1 = match.group(1)
                    grupo_2 = match.group(2)
                    grupo_3 = match.group(3)
                    grupo_4 = match.group(4)            
                    return grupo_1,grupo_2, grupo_3, grupo_4
                else:
                    return None
        except Exception as e:
            return None

    @staticmethod
    def esIPValida(ip='127.0.0.1'):
        """  
        Def: Comprueba que la ip es desde 0.0.0.0 hasta 255.255.255.255
        Retorno: True si ip buena
        False si ip mala.
        """
        try:
            regIp = r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'
            if re.search(regIp, ip):
                return True
            else:
                return False
        except Exception as e:
            return None
    @staticmethod
    def esMail(cad):
        """  
        Valida mail. Puede haber otras expresiones regulares mas adecuadas pero esta vale.
        cadena de caracteres @ cadena de caracteres
        """
        try:
            cad=cad.strip()
            patron = r'^(\w+)@(\w+)$'    
            palabra=re.match(patron, cad)
        
            return palabra.group(1), palabra.group(2)
        except Exception as e:
            return None

    @staticmethod
    def esDate(cadena, formato_entrada="%d/%m/%Y", formato_salida="%d/%m/%Y"):
        """ Valida si una cadena se puede convertir a una fecha con cualquier formato dado y devuelve la fecha en el formato deseado.
        [cadena] (str): La cadena que contiene la fecha.
        [formato_entrada] (str): El formato en que se espera recibir la fecha (e.g., "%d%m%Y", "%Ymd").
        [formato_salida] (str): El formato en que se quiere retornar la fecha. Por defecto es "%d/%m/%Y".
        Returns:
            str | None: La fecha en el formato deseado si es válida, o None si no es válida. 
        """   
        try:
            fecha = datetime.strptime(cadena, formato_entrada)
            return fecha.strftime(formato_salida)
        except ValueError:
            return False
    
    @staticmethod
    def esHora(cadena, formato_entrada="%H:%M:%S", formato_salida="%H:%M:%S"):
        """ Valida si una cadena se puede convertir a una hora con cualquier formato dado y devuelve la hora en el formato deseado.
        [cadena] (str): La cadena que contiene la hora.
        [formato_entrada] (str): El formato en que se espera recibir la hora (e.g., "%H:%M", "%I:%M %p").
        [formato_salida] (str): El formato en que se quiere retornar la hora. Por defecto es "%H:%M:%S".
        Returns:
            str | None: La hora en el formato deseado si es válida, o None si no es válida. 
        """   
        try:
            hora = datetime.strptime(cadena, formato_entrada)
            return hora.strftime(formato_salida)
        except ValueError:
            return False

    @staticmethod
    def esInt(strNum):
        """ 
        Def: Valida si el codeDigit pasado como argumento es un número entero.
                No incluye _ , . (decimal)
                si entra en el patron True / si no entra, False 
        """
        # .... Se lee: en toda la cadena [ From Ini(^); to Fin ($) ]
        #              Buscamos:  guion(-) opcional(?) y/o  0-9(\d)   ,  n veces(+)(solo el digito) 
        patronInt=r'^-?\d+$'
        num = re.match(patronInt, str(strNum))        
        if num:
            return int(strNum) 
        else:
            return False

        # return (int(num) if num else False)
    # _______________________________
    @staticmethod
    def esFrase(texto):        
        """     
        Def:    Valida la Entrada segun expresion la Regular: r'^[da-zA-Z]+$' 
                Si [texto] no se ajusta al patron => ha introducido un char no valido($ pej)

                ^          => Inicio de la cadena
                [da-zA-Z]  => [char] | d=>un digito | a-z => From a To z | A-Z => from A to Z
                + =>  cualquier numero de veces. Si no se pone sólo valdría para un sólo char
                $          => Fin de la cadena
        Args:   [texto] = str() no Validado.
        
        Return: (True/False)
                None, si texto==''
        """                
        if not isinstance(texto, str):  return False
        texto=texto.strip()
        if texto=='': return None
        # patron=r'^[\da-zA-Z_.\s]+$'
        patron=r'^[a-zA-Z0-9\s._-]+$'
        if re.search(patron, texto):
            return True
        else:
            return False
    
    @staticmethod
    def es_char(sting):
        """>>> Valida un solo caracter imprimible 
        [sting] (str): El caracter a validar.
        """
        patron = r'^[\w!@#$%^&*()\-_=+{}\[\]:;"\'<>,.?/|\\~`\s]$'
        return True if re.search(patron, sting) else False

    @staticmethod
    def es_n_char(sting):
        """ >>> Valida si toda la cadena contiene solo caracteres alfanuméricos, caracteres especiales permitidos y espacios.
        [sting] (str): La cadena a validar.
        Retorno:
            bool: True si es válida, False en caso contrario.
        """
        patron = r'^[\w!@#$%^&*()\-_=+{}\[\]:;"\'<>,.?/|\\~`\s]+$'
        return bool(re.fullmatch(patron, sting))

    @staticmethod
    def es_palabra(sting):
        """ 
        Letras may y min digitos _ 
        """
        patron= r'^\w$'
        return True if re.search(patron, sting) else False
    
    @staticmethod
    def esFloat(cadena):
        """ 
        Def: valida si se pasa un float
        ^[+-]?: Opcionalmente permite un signo + o - al inicio.
        \d*\.\d+: Opcionalmente dígitos antes del punto, pero al menos uno después del punto (ej. .5 o 0.123)
        \d+\.\d*: Al menos un dígito antes del punto y opcionalmente dígitos después (ej. 5.)
        \d+: Solo dígitos, por si deseas considerar números enteros como válidos (ej. 3)

        Ejemplo: 
            peso = StringTo.esFloat(peso)
            if StringTo.estaEnLista(sexo, ['H', 'M']): pass

                
        """
        patron = r"^[+-]?(\d*\.\d+|\d+\.\d*|\d+)$"
        num = re.match(patron, cadena)
        return float(cadena) if num else False
    
    # Entra una cadena separada por un caracter (coma) y devuelve una l i s t a   c o n   c a d a   i t e m 
    @staticmethod
    def cadena_to_lista(cadena:str, char:str=','):  
        """ >>> Entra Una cadena separada por comaas, retorna una list de coma en coma 
        Entra: 'cadena, de , ejemplo' |   Sale: ['cadena', 'de', 'ejemplo'] """      
        try:            
            if not isinstance(cadena, str): return None
            cadena = cadena.strip()
            # if not StringTo.esFrase(cadena): return None            

            # ELIMINAR LAS COMAS AL INICIO Y AL FINAL 
            if cadena.startswith(char) or cadena.endswith(char):
                cadena = cadena.strip(char)
            # CONVIERTE LA CADENA EN UNA LISTA
            lst_str = cadena.split(sep=char)
            if not lst_str: 
                return None

            # QUITA LOS ESPACIOS DELANTE Y DETRAS DE CADA ITEM
            lst_retorno = [str(item).strip() for item in lst_str]

            return lst_retorno
        except Exception as e:
            return None

   

