# Tabla Periodica y Enlaces Quimicos

Aplicacion educativa construida con Python y Flet para consultar los 118 elementos de la tabla periodica y clasificar, de forma introductoria, el enlace entre dos elementos seleccionados.

- Aplicacion web: https://wdaann.github.io/tabla-periodica-enlaces/
- Repositorio: https://github.com/wDaann/tabla-periodica-enlaces

## Contenido

- [Descripcion](#descripcion)
- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Instalacion](#instalacion)
- [Ejecutar localmente](#ejecutar-localmente)
- [Uso de la aplicacion](#uso-de-la-aplicacion)
- [Clasificacion utilizada](#clasificacion-utilizada)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Compilar para la web](#compilar-para-la-web)
- [Autores](#autores)

## Descripcion

La interfaz permite explorar la tabla periodica, buscar elementos y consultar su numero atomico, simbolo, nombre, masa atomica, categoria y descripcion. Para estudiar un enlace, el usuario confirma dos elementos y presiona **Clasificar enlace**.

El clasificador es una herramienta didactica basada en categorias generales. No sustituye los metodos avanzados de quimica ni determina formulas, geometria molecular, polaridad o estabilidad real de compuestos.

## Funcionalidades

- Tabla periodica completa organizada por periodos y grupos.
- Busqueda por numero atomico, simbolo, nombre o masa atomica aproximada.
- Seleccion de un elemento directamente desde la tabla.
- Panel con la informacion detallada del elemento seleccionado.
- Confirmacion independiente de dos elementos.
- Clasificacion del enlace como ionico, covalente, metalico o no estable.
- Calculo de la masa atomica combinada de los dos elementos.
- Explicacion textual del resultado.
- Clasificacion de materiales covalentes como intrinsecos, extrinsecos tipo P o extrinsecos tipo N.
- Interfaz adaptable a ventanas verticales y horizontales.

## Requisitos

- Windows 10 o posterior.
- Python 3.14 recomendado para el entorno actual.
- Visual Studio Code, opcional.
- Git, opcional, para administrar el repositorio.

## Instalacion

1. Abre PowerShell dentro de la carpeta del proyecto.

2. Crea un entorno virtual:

```powershell
python -m venv .venv
```

3. Instala las dependencias registradas:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

4. En Visual Studio Code, ejecuta **Python: Select Interpreter** y selecciona:

```text
.venv\Scripts\python.exe
```

## Ejecutar localmente

### Aplicacion de escritorio

```powershell
.venv\Scripts\python.exe main.py
```

### Vista web local

```powershell
.venv\Scripts\flet.exe run --web main.py
```

## Uso de la aplicacion

1. Selecciona un elemento haciendo clic sobre su casilla.
2. Pulsa **Confirmar Elem 1**.
3. Selecciona el segundo elemento.
4. Pulsa **Confirmar Elem 2**.
5. Presiona **Clasificar enlace**.

Tambien puedes escribir una consulta en el buscador:

- Numero atomico: `8`
- Simbolo: `O`
- Nombre sin importar acentos: `oxigeno`
- Masa aproximada: `15.999`

El boton **Limpiar** elimina las dos selecciones confirmadas y restablece el resultado.

## Clasificacion utilizada

Las reglas principales se encuentran en `clasificar_enlace` dentro de `enlaces.py`.

| Combinacion | Clasificacion |
|---|---|
| Metal + metal | Metalico |
| Metal + no metal | Ionico |
| No metal o metaloide + no metal o metaloide | Covalente |
| Metal + metaloide | Covalente |
| Uno de los elementos es gas noble | No es posible hacer un enlace estable en este modelo escolar |

Los materiales covalentes se clasifican adicionalmente como:

- **Extrinseco tipo P:** combinacion entre un elemento del Grupo III y uno del Grupo IV.
- **Extrinseco tipo N:** combinacion entre un elemento del Grupo V y uno del Grupo IV.
- **Intrinseco:** las demas combinaciones covalentes.

La masa combinada se calcula sumando las masas atomicas registradas y redondeando a cuatro decimales.

## Estructura del proyecto

```text
appT/
|-- main.py          Interfaz, eventos y construccion de la aplicacion Flet
|-- enlaces.py       Datos de los elementos y reglas de clasificacion
|-- requirements.txt Dependencias reproducibles del proyecto
|-- README.md        Documentacion del proyecto
|-- dist/            Build web local generado por Flet
|-- docs/            Build web publicado por GitHub Pages
```

## Compilar para la web

Para regenerar la aplicacion web:

```powershell
.venv\Scripts\flet.exe publish main.py --distpath dist --base-url /tabla-periodica-enlaces/
```

GitHub Pages utiliza la carpeta `docs/`. Antes de publicar cambios web, copia el contenido generado a esa carpeta:

```powershell
Copy-Item -Path dist\* -Destination docs -Recurse -Force
git add docs
git commit -m "Actualizar aplicacion web"
git push origin master
```

## Autores

- Angel Daniel Hernandez Arteag
- Fernando Cruz Calderon
