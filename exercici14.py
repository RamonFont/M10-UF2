num= input("Escriu 10 numeros separats per espais ")

numInt = num.split()

tupla =[int(numero) for numero in numInt]

tupla_ordenada = tuple(sorted(tupla, reverse=True))

print(tupla_ordenada)
