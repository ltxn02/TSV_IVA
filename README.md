# Entorno de trabajo — TSV_IVA

Guía rápida para preparar Python en los ordenadores del laboratorio antes de las prácticas o del examen.

## Requisitos

El material del curso utiliza **Python 3.12.0**. Comprueba la versión instalada abriendo un terminal y ejecutando:

```powershell
python -V
```

La salida esperada es:

```text
Python 3.12.0
```

> No se garantiza la compatibilidad con versiones anteriores o posteriores de Python.

## Opción rápida: activar el entorno del laboratorio

En los ordenadores del laboratorio ya debería existir el entorno `practicasTSV_env` con las dependencias del curso.

### Desde PowerShell

```powershell
& "C:\Users\eps\practicasTSV\practicasTSV_env\Scripts\Activate.ps1"
```

### Desde el símbolo del sistema (cmd)

```bat
C:\Users\eps\practicasTSV\practicasTSV_env\Scripts\activate.bat
```

Si se ha activado correctamente, el prompt del terminal comenzará por:

```text
(practicasTSV_env)
```

Puedes comprobar qué Python se está utilizando con:

```powershell
python -V
where python
```

Para salir del entorno virtual:

```powershell
deactivate
```

## Si el entorno del laboratorio no funciona: crear uno nuevo

Esta es la receta de recuperación. Ejecútala desde la carpeta del repositorio, donde se encuentra `requirements.txt`.

### 1. Crear el directorio del entorno

En PowerShell:

```powershell
mkdir "$env:USERPROFILE\practicasTSV" -Force
```

También puedes crear la carpeta con el explorador de archivos en:

```text
C:\Users\TU_USUARIO\practicasTSV
```

### 2. Crear el entorno virtual con Python 3.12

```powershell
python -m venv "$env:USERPROFILE\practicasTSV\practicasTSV_env"
```

Si tienes varias versiones de Python instaladas, utiliza el lanzador de Windows:

```powershell
py -3.12 -m venv "$env:USERPROFILE\practicasTSV\practicasTSV_env"
```

### 3. Activarlo

```powershell
& "$env:USERPROFILE\practicasTSV\practicasTSV_env\Scripts\Activate.ps1"
```

En `cmd.exe`, el comando equivalente es:

```bat
%USERPROFILE%\practicasTSV\practicasTSV_env\Scripts\activate.bat
```

### 4. Instalar o actualizar las dependencias

Con el entorno activo, el prompt debe comenzar por `(practicasTSV_env)`. Después ejecuta:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Usar `python -m pip` ayuda a garantizar que los paquetes se instalan en el entorno activo y no en otra instalación de Python.

## Solución rápida para errores habituales

### `python` no se reconoce como comando

Prueba:

```powershell
py -3.12 -V
```

Si también falla, Python no está disponible en el `PATH` del equipo. En ese caso, utiliza el entorno del laboratorio ya preparado o solicita asistencia.

### PowerShell bloquea `Activate.ps1`

Si aparece un error relacionado con la política de ejecución, puedes activar el entorno desde `cmd.exe` usando:

```bat
%USERPROFILE%\practicasTSV\practicasTSV_env\Scripts\activate.bat
```

Como alternativa, en PowerShell puedes permitir scripts únicamente para la sesión actual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
& "$env:USERPROFILE\practicasTSV\practicasTSV_env\Scripts\Activate.ps1"
```

### El terminal muestra `(practicasTSV_env)`, pero VSCode utiliza otro Python

En VSCode:

1. Abre la carpeta raíz del repositorio.
2. Pulsa `Ctrl + Shift + P`.
3. Selecciona **Python: Select Interpreter**.
4. Elige el intérprete dentro de:
   `C:\Users\TU_USUARIO\practicasTSV\practicasTSV_env\Scripts\python.exe`
5. Abre un terminal nuevo en VSCode y comprueba que aparece `(practicasTSV_env)`.

## Comprobación final antes del examen

Ejecuta estos comandos desde la carpeta del repositorio:

```powershell
python -V
python -c "import sys; print(sys.executable)"
python -m pip list
```

Comprueba que:

- La versión es `Python 3.12.0`.
- `sys.executable` apunta a `practicasTSV_env\Scripts\python.exe`.
- El terminal muestra `(practicasTSV_env)`.
- La instalación de `requirements.txt` terminó sin errores.

## Comandos esenciales — resumen

```powershell
# Activar el entorno ya preparado del laboratorio
& "C:\Users\eps\practicasTSV\practicasTSV_env\Scripts\Activate.ps1"

# Crear un entorno nuevo si el anterior falla
py -3.12 -m venv "$env:USERPROFILE\practicasTSV\practicasTSV_env"
& "$env:USERPROFILE\practicasTSV\practicasTSV_env\Scripts\Activate.ps1"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Desactivar
 deactivate
```

> En la última línea escribe `deactivate` sin el espacio inicial; se muestra así únicamente para separar visualmente el comando del comentario anterior.

## Referencias

- [Documentación de `venv` para Python 3.12](https://docs.python.org/3.12/tutorial/venv.html)
- [Entornos Python en VSCode](https://code.visualstudio.com/docs/python/environments)
- [Descargas de Python](https://www.python.org/downloads)
