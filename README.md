# TableroMensajes
Proyecto para gestionar mensajes utilizando Django. Tiene las funciones de crear mensajes, eliminar mensajes y listar los mensajes enviados o recibidos según el usuario seleccionado de las 3 opciones disponibles.

## Instalación

1. Clonar el repositorio.
git clone https://github.com/Axell505/TP2.git

2. Crear y activar el entorno virtual.
 Linux: python -m venv entorno source entorno/bin/activate
 En Windows: entorno\Scripts\activate

3. Instalar las dependencias.
   pip install -r requirements.txt

4. Aplicar las migraciones de la base de datos.
python manage.py migrate

5. Correr el servidor.
python manage.py runserver

## Uso
Accede a la aplicación desde el navegador usando: http://localhost:8000/ o http://127.0.0.1:8000/
Al seleccionar el remitente debe escribir el usuario tal cual está escrito, pues distingue entre mayúsculas. Ejemplo: Usuario1, Usuario2, Usuario3.

## Requisitos
Python 3.12.5 Django 4.2 y SQLlite (u otra base de datos compatible)
