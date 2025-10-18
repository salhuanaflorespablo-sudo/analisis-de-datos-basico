#Crear una lista con los cuadredados de los 4 primeros numeros enteros
"""
def cuadrados_4_primeros_numeros():
    cuadrados = []
    for i in range(1, 5):
        cuadrados.append(i**2)
    return cuadrados

cuadrados = cuadrados_4_primeros_numeros()
print(cuadrados)
"""
#determinar si es un numero primo dentro de un rango de 40 numeros
# Explicacion del código:
# La función es_primo(numero) determina si un número es primo o no.
# Primero, verifica si el número es menor que 2, ya que los primos son mayores o iguales a 2.
# Luego, recorre desde 2 hasta el número-1 para ver si el número es divisible por algún valor.
# Si encuentra un divisor exacto, retorna False (no es primo).
# Si no encuentra ningún divisor, retorna True (es un número primo).
# Luego, en el ciclo for, se itera sobre los números del 0 al 39.
# Por cada número, se usa la función es_primo para comprobar si es primo o no
# y se imprime en pantalla si el número es o no es primo.

def es_primo(numero):
    if numero < 2:
        return False  # Los números menores que 2 no son primos
    for i in range(2, numero):
        if numero % i == 0:
            return False  # Si encuentra un divisor, no es primo
    return True  # Si no encuentra divisores, es primo

for i in range(40):
    if es_primo(i):
        print(f"{i} es un numero primo")
    else:
        print(f"{i} no es un numero primo")
