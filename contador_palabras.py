#programa para contar palabras en un texto
#1. pedir al usuario ingresar la ruta del archivo
#2.leer el archivo
#3.separar en palabras
#4.contar las palabras
#5.mostrar el resultado
#6.mostrar las 10 palabras mas repetidas

import re
archivo = input("Introduce la ruta del archivo de texto: ")

try:

    with open(archivo, "r", encoding="utf-8") as f:
        texto = f.read()
except FileNotFoundError:

    print("El archivo especificado no existe.")

    exit(1)
# Separar el contenido en palabras

import re

palabras = re.findall(r"\w+", texto.lower())

total_palabras = len(palabras)

print(f"Total palabras: {total_palabras}")


