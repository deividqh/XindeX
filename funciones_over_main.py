from XindeX.Sdata import Sdata                 # ■ AYUDA PARA EL OVER-MAIN PARA PEDIR DATOS SEGUROS AL USUARIO
# Declaramos la variable global para este módulo (se llenará automáticamente desde over_main.py)
The_X_Men = None


def  version_web():
    # global The_X_Men    
    print(f'Accion version Web WIP')
    The_X_Men.get_web_lsts_lens_linea( titulo='Menu1',  tipo_index=0, b_mode_all=True, b_loop=True, pad_x=15)

def lanza_flask():
    print('LANZA FLASK')
    # from proyecto_final_v1 import funciones_tablas
    # from proyecto_final_v1.main import app as servidor_flask
    # servidor_flask.run()

def set_style():
    # global The_X_Men
    if The_X_Men.get_b_mode_all() == True:
        b_mode_all = False
    else:
        b_mode_all = True
    The_X_Men.set_style(b_mode_all = b_mode_all)
    print(f'::: MODO {f'Directorio Switch  To ► Exec-All' if b_mode_all == True else f'Exec-All  Switch To ► Directorio'}  ::: ')
    

def from_to():
    # global The_X_Men    
    sdata = Sdata.get_data(key_dict='FD', tipo=int, msg_entrada='INTRO FILA-DESDE: ', permite_nulo=False)
    sdata = Sdata.get_data(key_dict='FH', dicc=sdata, tipo=int, msg_entrada='INTRO FILA-HASTA: ', permite_nulo=False)
    print(f'FROM {sdata["FD"]} TO {sdata["FH"]}')
        
    The_X_Men.F_RANK_Y.imprimir(sp_between = 2, ancho_columna = None, fila_from=sdata['FD'], fila_to=sdata['FH'] )

def listar_procesos():
    # global The_X_Men    
    print(f'{The_X_Men.listar_procesos()}')

def subprocess_os():
    import subprocess
    
    # sdata = Sdata.get_data(key_dict='P', tipo=str, msg_entrada='Intro Filtro: ', permite_nulo=True)
    # resultado = subprocess.run(f'tasklist | findstr {sdata['P']}', shell=True, capture_output=True, text=True)
    resultado = subprocess.run(f'tasklist | findstr "python"', shell=True, capture_output=True, text=True)
    print(resultado.stdout)

# PROCESO LARGO DE EJEMPLO... PRUEBAS PAR BACKGROUND Y DEMONIO
import time
def proceso_largo(**kwargs):
    minutos = kwargs.get('minutos') if kwargs else None
    if minutos is not None:
        tiempo_hasta = minutos * 60
    else:
        tiempo_hasta = 60

    print(f"⏳ Proceso iniciado (duración: {tiempo_hasta} segundos)")
    inicio = time.time()

    while True:
        elapsed = time.time() - inicio
        # print(f"⌛ {int(elapsed)}s transcurridos...", end="\r")
        time.sleep(1)

        if elapsed >= tiempo_hasta:
            break

    print("\n✅ Proceso finalizado.")

def lanzar_proceso():
    # global The_X_Men    
    sdata = Sdata.get_data(key_dict='B', tipo='BETWEEN', msg_entrada='Elige Entre (D)emonio o (B)ackground', permite_nulo=False, valores_between=['D','B'])
    sdata = Sdata.get_data(key_dict='M', tipo=int, msg_entrada='Intro Minutos', permite_nulo=False, dicc=sdata)
    if sdata['B'] == 'D':
        The_X_Men.lanzar_proceso(nombre = proceso_largo.__name__ , proceso=proceso_largo, minutos=sdata['M'],  demonio=True)        
    elif sdata['B'] == 'B':
        The_X_Men.lanzar_proceso(nombre = proceso_largo.__name__ , proceso=proceso_largo, minutos=sdata['M'],  demonio=False)        
    
def cambiar_estilo_marco():
    # global The_X_Men    
    sdata = Sdata.get_data(key_dict='S', tipo=str, msg_entrada='Nombre Estilo(franky/default/unicode/doble/vacio/moderno/elegante)', permite_nulo=False)
    The_X_Men.F_RANK_Y.style(estilo=sdata['S'])
    The_X_Men.F_RANK_Y_DEF.style(estilo=sdata['S'])
    print(f'::: Estilo Marco cambiado a {sdata["S"]} ::: ')
