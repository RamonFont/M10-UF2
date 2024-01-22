tupla = []

frase = input("Escriu una frase: ")

frase = "".join(dict.fromkeys(frase))

tupla.append(frase.replace(' ', ''))

print(tupla)