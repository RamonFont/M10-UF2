tupla = []

num = 1

while True:
    num = input("Ingrese un número (ingrese 0 para finalizar): ")

    if num == '0':
        break

    numInt = int(num)
    tupla.append(numInt)

tupla_ordenada = tuple(sorted(tupla, reverse=True))

print("Tupla ordenada de mayor a menor:", tupla_ordenada)