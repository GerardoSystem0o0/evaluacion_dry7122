# leer_token.py

import json
import time

# Paso 1: Llamar a archivo específico dentro de una variable
nombre_archivo = "datos_token.json"

# Paso 2: Cargar archivo JSON como string y luego convertirlo en objeto
with open(nombre_archivo, "r") as archivo:
    contenido_json = archivo.read()  # Cargar como string
    datos = json.loads(contenido_json)  # Convertir a diccionario

# Paso 3: Imprimir el token y el tiempo restante antes que expire
token = datos.get("token")
expira_en = datos.get("expira_en")  # tiempo en segundos

print(f"Token: {token}")
print(f"Tiempo restante antes de caducar: {expira_en} segundos")
