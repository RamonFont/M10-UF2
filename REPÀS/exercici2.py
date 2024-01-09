valor = input("Escriu un valor en €")
iva = input("Escriu el iva que vols aplicar")
resultat = int(valor) * ((int(iva) / 100) + 1)

print(valor)
print(iva)
print(resultat)