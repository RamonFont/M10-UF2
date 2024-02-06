from exercici27 import sumar_numeros

def main():
    try:
        # Solicitar dos numeros
        num1 = float(input("Introduce el primer numero: "))
        num2 = float(input("Introduce el segundo numero: "))

        # Mostrar resultado
        resultado = sumar_numeros(num1, num2)
        print(f"La suma de {num1} y {num2} es: {resultado}")

    except ValueError:
        print("Error.")

if __name__ == "__main__":
    main()
