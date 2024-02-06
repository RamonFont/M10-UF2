def mostrar_numeros_entre_dos(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1

    print(f"Numeros enteros entre {num1} y {num2}:")
    suma = 0
    for numero in range(num1 + 1, num2 ):
        print(numero)
        suma += numero

        print(f"La suma de los numeros enteros es: {suma}")

