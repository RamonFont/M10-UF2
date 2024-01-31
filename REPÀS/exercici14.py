cadenaImput= input("Escriu 10 numeros separats per espais: ")

cadenaInt = cadenaImput.split()

tupla =[int(num) for num in cadenaInt]

tupla_ordenada = tuple(sorted(tupla, reverse=True))

print(tupla_ordenada)