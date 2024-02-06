from exercici32 import calcular_quadrats

def main():
    try:
        # Solicitar numeros 
        entrada = input("Introduce 10 numeros separados por espacios: ")

        # Convertir en lista de numeros
        lista_numeros = list(map(int, entrada.split()))

        # Llamar funcion
        resultado = calcular_quadrats(lista_numeros)

        # Imprimir el resultado
        if resultado:
            print(f"Lista original: {lista_numeros}")
            print(f"Lista de cuadrados: {resultado}")

    except ValueError:
        print("Error: Ingresa 10 numeros separados por espacios.")

if __name__ == "__main__":
    main()
