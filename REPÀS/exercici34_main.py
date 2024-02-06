from exercici34 import calcular_quadrat, calcular_quadrats_llista

def main():
    try:
        # Definir lista 
        llista_numeros = [1, 2, 3, 4, 5]

        # Mostrar lista
        print("Lista original:", llista_numeros)

        # Calcular cuadrado
        llista_quadrats = calcular_quadrats_llista(llista_numeros)

        # Mostrar nueva lista
        print("Lista cuadrados:", llista_quadrats)

    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
