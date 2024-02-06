# main.py
from exercici28 import generar_numero_aleatorio

def main():
    try:
        # Solicitar dos numeros
        num1 = int(input("Introduce el primer numero: "))
        num2 = int(input("Introduce el segundo numero (debe ser mayor que el primero): "))

        # Verificar que el primer numero no sea mayor que el segundo
        if num1 > num2:
            num1, num2 = num2, num1

        resultado = generar_numero_aleatorio(num1, num2)
        print(f"El numero aleatorio entre {num1} y {num2} es: {resultado}")

    except ValueError:
        print("Error")

if __name__ == "__main__":
    main()
