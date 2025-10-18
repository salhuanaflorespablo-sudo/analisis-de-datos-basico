"""
Calculadora Simple - Versión Orientada a Objetos
Refactorización del código original manteniendo la funcionalidad
"""

class CalculadoraSimple:
    def __init__(self):
        """Inicializa la calculadora"""
        self.nombre = "Calculadora Simple"
    
    def mostrar_menu(self):
        """Muestra el menú de opciones"""
        print("---Calculadora Simple---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")
        print("--------------------------------")
    
    def obtener_numeros(self):
        """Obtiene dos números del usuario"""
        try:
            numero1 = float(input("Introduce el primer numero: "))
            numero2 = float(input("Introduce el segundo numero: "))
            return numero1, numero2
        except ValueError:
            raise ValueError("Debes introducir números válidos")
    
    def sumar(self, numero1, numero2):
        """Realiza la operación de suma"""
        return numero1 + numero2
    
    def restar(self, numero1, numero2):
        """Realiza la operación de resta"""
        return numero1 - numero2
    
    def multiplicar(self, numero1, numero2):
        """Realiza la operación de multiplicación"""
        return numero1 * numero2
    
    def dividir(self, numero1, numero2):
        """Realiza la operación de división"""
        if numero2 == 0:
            raise ValueError("No se puede dividir por cero")
        return numero1 / numero2
    
    def ejecutar_operacion(self, operacion):
        """Ejecuta la operación seleccionada"""
        if operacion == "1":
            numero1, numero2 = self.obtener_numeros()
            resultado = self.sumar(numero1, numero2)
            print(f"El resultado de la suma es: {resultado}")
            
        elif operacion == "2":
            numero1, numero2 = self.obtener_numeros()
            resultado = self.restar(numero1, numero2)
            print(f"El resultado de la resta es: {resultado}")
            
        elif operacion == "3":
            numero1, numero2 = self.obtener_numeros()
            resultado = self.multiplicar(numero1, numero2)
            print(f"El resultado de la multiplicacion es: {resultado}")
            
        elif operacion == "4":
            numero1, numero2 = self.obtener_numeros()
            resultado = self.dividir(numero1, numero2)
            print(f"El resultado de la division es: {resultado}")
            
        elif operacion == "5":
            print("Salir")
            return False
        else:
            print("Operacion no valida")
        
        return True
    
    def ejecutar(self):
        """Función principal que ejecuta la calculadora"""
        while True:
            try:
                self.mostrar_menu()
                operacion = input("Introduce la operacion: ")
                
                if not self.ejecutar_operacion(operacion):
                    break
                    
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")
                break
        
        print("Fin del programa")

# Función principal
def main():
    """Función principal del programa"""
    calculadora = CalculadoraSimple()
    calculadora.ejecutar()

if __name__ == "__main__":
    main()
