import threading
from classXindeX import XindeX

class Over_Main(XindeX):
    def __init__(self):
        super().__init__()
        self.hilos_activos = {}

    def Xavier_get_USUARIO(self, menu_dvd, lst_Valid, max_length, execAll, mystica_skin_str):
        """ Valida entradas con > y >> """
        while True:
            opcion = input(f"{menu_dvd.introData} ").strip()

            # Manejo de prefijos especiales
            if opcion.startswith((">", ">>")):
                prefijo = opcion[:2] if opcion.startswith(">>") else opcion[:1]
                opcion_real = opcion.lstrip(">").strip()

                if opcion_real in lst_Valid:
                    return prefijo + opcion_real
                else:
                    print(f"Opción '{opcion_real}' no válida.")
            elif opcion in lst_Valid:
                return opcion
            elif opcion == "<<<":
                print("Saliendo del menú...")
                return None
            else:
                print("Entrada no válida. Intente de nuevo.")
                
    def Terminator(self, titulo_menu, item, respuesta, execFunc=True):
        match item:
            case "?":
                self.get_mystyca_informacion(
                    titulo_menu=titulo_menu, 
                    lst_padres=self.Mystyca_lst_padres(self.get_menudvd(titulo_menu)), 
                    lst_hijos=self.get_lst_dict_hijosX(titulo_menu), 
                    execAll=True, 
                    max_length=self.total_length
                )
            case "<":
                print("Volviendo al menú anterior...")
            case "<<<":
                print("Saliendo del menú...")
                return False
            case _ if item.startswith((">", ">>")):
                es_interactivo = item.startswith(">>")
                nombre_opcion = item.lstrip(">").strip()

                hilo = threading.Thread(
                    target=self.ejecutar_funcion, 
                    args=(titulo_menu, nombre_opcion, es_interactivo)
                )
                hilo.daemon = not es_interactivo
                hilo.start()

                self.hilos_activos[nombre_opcion] = hilo
                print(f"Hilo '{nombre_opcion}' iniciado como {'interactivo' if es_interactivo else 'no interactivo'}.")
            case _:
                print(f"Opción '{item}' no reconocida.")

    def ejecutar_funcion(self, titulo_menu, nombre_opcion, es_interactivo):
        funcion = self.get_menudvd(titulo_menu).dicc_menu.get(nombre_opcion)
        if funcion:
            funcion()
        else:
            print(f"Función '{nombre_opcion}' no encontrada.")

    def ver_estado_hilos(self):
        for nombre, hilo in self.hilos_activos.items():
            estado = "Activo" if hilo.is_alive() else "Finalizado"
            print(f"Hilo '{nombre}': {estado}")

    def detener_hilo(self, nombre_opcion):
        hilo = self.hilos_activos.get(nombre_opcion)
        if hilo and hilo.is_alive():
            print(f"No es posible detener el hilo '{nombre_opcion}' directamente.")
        else:
            print(f"Hilo '{nombre_opcion}' no está activo.")
