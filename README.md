# XindeX - Sistema de Menús Interactivos por Terminal (Rama `with_st`)

XindeX es una librería en Python diseñada para generar, gestionar y ejecutar menús interactivos y jerárquicos directamente desde la terminal. En esta rama (`with_st`), XindeX integra un configurador visual usando **Streamlit**, lo que permite diseñar la estructura de los menús (hijos, padres e ítems) y asignar sus funciones correspondientes desde una interfaz web intuitiva, para luego ser ejecutados en la consola mediante la clase maestra `Over_Main`.

... Y para que sirve? Yo lo uso para documentación de clases que genero en python.
Aunque también cuando hago algún curso y quiero organizar mis ejercicios.
Simplemente te permite ejecutar cosas desde un índice así que puede valer para lo que se te ocurra:
por ejemplo cuando quise programar un cliente y servidor... desde XindeX fué genial, 
o cuando quería probar ventanas de Tkinter y no ceder el control del XindeX las lanzaba como demonios y listo.
También lancé un servidor e hice modificaciones a una base de datos que estaban trabajando clientes web en caliente todo como pruebas de unas clases con lo que todo queda super bien organizado. son unas Memorias Vivas.
---

## 🚀 Guía de Inicio Rápido

Sigue estos pasos para clonar la rama correcta, preparar tu entorno y ejecutar el proyecto por primera vez.

### 1. Clonar el repositorio

Asegúrate de clonar específicamente la rama `with_st` donde se encuentra la integración con Streamlit:

```bash
git clone -b with_st https://github.com/deividqh/xindex.git
cd xindex
```

### 2. Crear el entorno virtual

Es una buena práctica aislar las dependencias del proyecto creando un entorno virtual (recomendado usar Python 3.8 o superior).

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

Con el entorno activado, instala los requerimientos necesarios para el proyecto:

```bash
pip install -r requirements.txt
```

### 4. Primera ejecución

El punto de entrada principal del programa es el archivo `over_main.py`. Este archivo gestiona tanto el menú de consola como la llamada al configurador web.

**Para lanzar el configurador visual web (Modo Configuración Streamlit):**

Invocando el modo configuración pasando el flag `--config`, el sistema se encargará de levantar automáticamente la interfaz en tu navegador para que puedas crear tu menú.

```bash
python over_main.py --config
```

**Para lanzar el menú por consola (Modo Ejecución):**

Una vez configurado, lanza el menú interactivo en tu terminal con:

```bash
python over_main.py
```

---

## 🛠️ Uso y Advertencia Importante: `DICC_FUNCIONES`

La magia de XindeX radica en cómo separa el diseño visual del menú de la lógica del código. Para que los botones del menú (creados en la interfaz de Streamlit) sepan qué código deben ejecutar, XindeX utiliza un mapa de ejecución llamado `DICC_FUNCIONES`.

> ⚠️ **¡ATENCIÓN DESARROLLADOR!** Es tu responsabilidad mantener actualizado el `DICC_FUNCIONES` dentro del archivo `over_main.py` (o donde instancies la clase `Over_Main`). Si configuras un botón en la interfaz web para que llame a una acción (ej. `mi_funcion_magica`), debes obligatoriamente mapear ese nombre exacto (como string) a tu función real en este diccionario. Si no lo haces, la opción del menú no ejecutará nada o lanzará un error.

### Ejemplo sencillo de configuración

Supongamos que tienes un archivo llamado `mis_funciones.py` con las lógicas de tu programa:

```python
# mis_funciones.py
def saludar_usuario():
    print("¡Hola! Bienvenido a XindeX.")

def borrar_datos():
    print("Borrando datos del sistema...")
```

Tu archivo principal (`over_main.py`) debe enlazar las referencias de texto (que pondrás en la web de Streamlit) con estas funciones reales de la siguiente manera:

```python
# over_main.py
import multiprocessing
import os
import mis_funciones as cmd
from XindeX.classXindeX import Over_Main

# ■ EL MAPA DE EJECUCIÓN (¡Crucial!)
DICC_FUNCIONES = {
    "accion_saludar": cmd.saludar_usuario,
    "accion_borrar": cmd.borrar_datos
}

if __name__ == "__main__":
    multiprocessing.freeze_support()
    os.system('cls' if os.name == 'nt' else 'clear')

    # Inyectamos DICC_FUNCIONES en Over_Main al instanciar
    menu_xindex = Over_Main(
        dicc_funciones=DICC_FUNCIONES, 
        tipo_index='a', 
        b_mode_all=True, 
        b_loop=True
    )

    # Lanzar el menú principal
    menu_xindex.mystyca(titulo='MAIN_MENU')
```

---

## 📋 Resumen del flujo de trabajo

1. Crea tus funciones (ej. `cmd.saludar_usuario`).
2. Regístralas en el `DICC_FUNCIONES` de `over_main.py` asignándoles una clave de texto (ej. `"accion_saludar"`).
3. Abre el configurador web (`python over_main.py --config`), diseña tu menú y asigna al botón la clave exacta `"accion_saludar"`.
4. Ejecuta el menú (`python over_main.py`) y comprueba que todo funciona en la terminal.

## ... a partir de aquí entramos en las cosas que podemos hacer con el XindeX:
1. Parámetros Ayuda:
    * '??'      Muestra la ayuda de parametros que se pueden usar en XindeX.
    * 'help'    Muestra una ayuda de como configurar XindeX para copiar / pegar.
2. Parámetros Sobre el Menú:
    * '<<<' Salir de XindeX
    * '<'   Repite el menu limpiando la pantalla. (muy usado)
    * '--config'    Abre Streamlit con el menú de config_menu.json(menu actual) para editarlo y retornar a la terminal.
    * '?'   Muestra la funcion que se ejecuta en cada linea del XindeX. (muy usado)
            También muestra en la Cabecera si se ejecuta en modo Directorio o Se ejecuta Todo.
3. Parámetros Sobre la Visualizacion del Contenido:
    * '=b'  Muestra el directorio b si existe. No persiste, es solo visual. 
    * '**b'  Muestra sólo el directorio b pero es un menu independiente y se sale con '<<<'.
    * '1-5'  Muestra de la linea 1 a la 5 del XindeX ambas incluidas.
    * "par"  Muestra todas las lineas del XindeX que contengan el string 'par'
4. Parámetros Sobre el Estyle:
    * '@'   Cambia el estilo del marco. da una lista para elegir... vacío.
    * '#'   Cambia el modo de Directorio a Ejecutar Todo y viceversa.
    * '$'   Cambia el color del marco. Da una lista para elegir color.
5. Parámetros Sobre la Ejecución:
    * '[b1]'    Lanza un proceso en background
    * '=>b1'    Lanza un proceso demonio
    * 'list/listar'    Lista los procesos lanzados como demonio o background
    * 'kill/stop 1783'    Termina el proceso 1783 si existe.
    * 'kill/stop'    Termina todos los procesos lanzados(pregunta confirmación).



