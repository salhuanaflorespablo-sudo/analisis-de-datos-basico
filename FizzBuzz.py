#fizzbuzz
#Vamos a recorrer de el 1 hasta el 51(bueno 50)
#si el numeero es divisible por 3, se debe imprimir Fizz
#si el numero es divisible por 5, se debe imprimir Buzz
#si el numero es divisible por 3 y por 5, se debe imprimir FizzBuzz

def main():
    for number in range(1, 51):
     if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
     elif number % 3 == 0:
        print("Fizz")
     elif number % 5 == 0:
        print("Buzz")
     else:
        print(number)
#print("Fin del programa")

if __name__ == "__main__":
    main()

