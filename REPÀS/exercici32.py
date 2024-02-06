def calcular_quadrats(lista_numeros):
    try:
        # Verificar que sean 10 numeros
        if len(lista_numeros) != 10:
            raise ValueError("La lista debe contener exactamente 10 numeros.")

        # Calcular cuadrados 
        lista_quadrats = [numero ** 2 for numero in lista_numeros]

        return lista_quadrats

    except ValueError as error:
        print(f"Error: {error}")

