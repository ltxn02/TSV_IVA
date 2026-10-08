# Entorno virtual en Windows (CMD)

Python compatible: **3.12.0**.

## Activar el entorno del laboratorio

Abre **CMD** y ejecuta:

```bat
C:\Users\eps\practicasTSV\practicasTSV_env\Scripts\activate.bat
```

Si funciona, aparecerá `(practicasTSV_env)` al principio de la línea.

Comprobar Python:

```bat
python -V
```

Salir del entorno:

```bat
deactivate
```

## Crear un entorno nuevo si el anterior falla

Ejecuta estos comandos desde la carpeta del repositorio, donde está `requirements.txt`:

```bat
mkdir "%USERPROFILE%\practicasTSV"
py -3.12 -m venv "%USERPROFILE%\practicasTSV\practicasTSV_env"
"%USERPROFILE%\practicasTSV\practicasTSV_env\Scripts\activate.bat"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Cuando aparezca `(practicasTSV_env)`, el entorno está activo.

## Comprobación rápida

```bat
python -V
where python
```

`where python` debe mostrar una ruta que termine en:

```text
practicasTSV_env\Scripts\python.exe
```
