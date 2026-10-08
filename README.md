ENTORNO VIRTUAL EN WINDOWS (CMD + VS CODE)

Este entorno se creará en:
C:\Users\eps\Downloads\venv

1. Abrir CMD.

2. Crear el entorno virtual:

cd /d C:\Users\eps\Downloads
py -3.12 -m venv venv

3. Activar el entorno:

C:\Users\eps\Downloads\venv\Scripts\activate.bat

Si se ha activado correctamente, CMD mostrará (venv) al principio de la línea.

4. Comprobar Python:

python -V
where python

Debe aparecer Python 3.12.0 y una ruta que termine en:
C:\Users\eps\Downloads\venv\Scripts\python.exe

5. Instalar las dependencias del proyecto.

Si requirements.txt está en C:\Users\eps\Downloads, ejecutar:

python -m pip install --upgrade pip
python -m pip install -r C:\Users\eps\Downloads\requirements.txt

6. Seleccionar el entorno en VS Code.

Abrir en VS Code la carpeta del proyecto.

Pulsar Ctrl + Shift + P.

Buscar y seleccionar:
Python: Select Interpreter

Elegir este intérprete:
C:\Users\eps\Downloads\venv\Scripts\python.exe

7. Ejecutar o depurar.

Abrir el archivo .py en VS Code.

Para ejecutar:
Pulsar el botón ▶ de la esquina superior derecha.

Para depurar:
Pulsar F5 o seleccionar Run and Debug.

8. Salir del entorno en CMD:

deactivate
