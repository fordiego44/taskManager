# TaskManager

TaskManager es un gestor de tareas en línea de comandos desarrollado en Python que permite crear, listar, completar y eliminar tareas de forma sencilla. Además, incluye una función opcional de inteligencia artificial para descomponer tareas complejas en subtareas más simples.

## Descripción del proyecto

Esta aplicación está pensada para practicar conceptos básicos de programación orientada a objetos, persistencia de datos en archivos JSON, manejo de entradas por consola y consumo de una API externa (OpenAI) para enriquecer la experiencia del usuario.

## Funcionalidades

- Añadir tareas simples.
- Añadir tareas complejas y convertirlas en subtareas mediante IA.
- Listar todas las tareas actuales.
- Marcar tareas como completadas.
- Eliminar tareas.
- Guardar el estado de las tareas en un archivo JSON para conservar la información entre ejecuciones.

## Requisitos

- Python 3.10 o superior
- Dependencias listadas en requirements.txt

## Instalación

1. Clona este repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd TaskManager
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Crea un archivo `.env` en la raíz del proyecto con tu clave de OpenAI:
   ```env
   OPENAI_API_KEY=tu_clave_aqui
   ```

> Si no configuras la clave de OpenAI, la opción de generar subtareas con IA mostrará un mensaje de error en lugar de funcionar.

## Ejecución

Para iniciar la aplicación ejecuta:

```bash
python main.py
```

Al arrancar, aparecerá un menú con estas opciones:

1. Añadir tarea
2. Añadir tarea compleja (con IA)
3. Listar tareas
4. Completar tarea
5. Eliminar tarea
6. Salir

## Estructura del proyecto

```text
TaskManager/
├── ai_service.py         # Lógica para generar subtareas con OpenAI
├── main.py               # Menú principal de la aplicación
├── task_manager.py       # Gestión de tareas y persistencia en JSON
├── tasks.json            # Archivo donde se almacenan las tareas
├── requirements.txt      # Dependencias del proyecto
└── tests/                # Pruebas unitarias del gestor de tareas
```

## Pruebas

El proyecto incluye pruebas unitarias para verificar el comportamiento del gestor de tareas. Puedes ejecutarlas con:

```bash
python -m unittest discover -s tests -v
```

## Notas importantes

- Las tareas se guardan automáticamente en el archivo `tasks.json`.
- El estado de cada tarea incluye su identificador, descripción y si está completada o no.
- El módulo `ai_service.py` utiliza la API de OpenAI para descomponer tareas complejas en acciones más simples.

## Autor

Proyecto desarrollado como práctica de fundamentos de desarrollo de software.
