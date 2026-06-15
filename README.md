<div align="center">
  <h1>🌌 XindeX</h1>
  <p>
    <strong>Un potente y elegante gestor de menús interactivos, genéticos y jerárquicos para la terminal en Python.</strong>
  </p>
  <p>
    <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python Version">
    <img src="https://img.shields.io/badge/Terminal-CLI-orange.svg" alt="CLI">
    <img src="https://img.shields.io/badge/Dependencies-Colorama-brightgreen.svg" alt="Dependencies">
  </p>
</div>

---

## 📌 ¿Qué es XindeX?

**XindeX** es una librería diseñada para facilitar la creación de interfaces de línea de comandos (CLI) avanzadas. Su filosofía principal es la **genética de menús**: permite anidar infinitos menús y submenús estableciendo relaciones *Padre-Hijo*, vinculando visualmente opciones de texto con funciones ejecutables en Python de manera intuitiva y sin colapsar la terminal.

## ✨ Características Destacadas

* 🌳 **Jerarquía Genética Infinita**: Crea estructuras anidadas (Nivel 1, Nivel 2, Nivel 3...) estableciendo relaciones lógicas de forma sencilla.
* 🔢 **Índices Flexibles**: Soporta numeración tradicional (`1, 2, 3`), alfabética (`a, b, c` / `A, B, C`) o mixta.
* ⚙️ **Ejecución Directa**: Vincula cada opción a una función de Python (`callable`) o úsala como puente hacia un submenú.
* 🛡️ **Validación Segura**: Incorpora módulos para pedir datos por teclado de forma segura, evitando que un *input* erróneo del usuario rompa el programa (módulos *Sdata* y *Franky*).
* 🎨 **Estilos Personalizables**: Personaliza colores (mediante `colorama`), espaciado, títulos, pies de página y el diseño del marco del menú.
* 🔁 **Modos Dinámicos**: Controla si el menú debe estar en bucle (`b_loop`) y si el usuario puede elegir cualquier opción o solo los nodos finales (`b_mode_all`).

---

## 🚀 Instalación y Despliegue

Sigue estos pasos para clonar el repositorio, instalar las dependencias y ejecutar la aplicación en tu máquina local.

**1. Clonar el repositorio**
```bash
git clone https://github.com/deividqh/XindeX.git
cd XindeX
```
**2. Crear un entorno virtual (Recomendado)**
```bash
python -m venv venv
```
# En Windows:
```bash
venv\Scripts\activate
```
# En Linux/Mac:
```bash
source venv/bin/activate
```

**3. Instalar dependencias**
El proyecto incluye un archivo de requisitos. Principalmente requiere colorama para la gestión de colores en terminal.
```bash
pip install -r requirements.txt
```

**4. Ejecutar el ejemplo principal**
Puedes probar el entorno interactivo ejecutando el archivo principal:
```bash
python over_main.py
```

## 🏗️ Arquitectura Interna

El sistema está construido sobre una arquitectura modular orientada a objetos:

* **`MenuDvd`**: Clase base que representa un menú bidimensional estático. Gestiona los ítems visuales y empareja cada opción con su respectiva función ejecutable.
* **`classXindeX` / `Over_Main`**: El corazón del sistema. Hereda de `MenuDvd` y actúa como el gestor genético. Almacena la jerarquía de todos los menús, dibuja dinámicamente la matriz de impresión y evalúa las entradas del usuario.
* **`Sdata.py` y `Franky.py`**: Módulos de soporte encargados de validar que los inputs del teclado sean correctos (evitando crashes por `TypeErrors` o `ValueErrors`) y de embellecer la salida ASCII en consola.
