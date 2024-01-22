nums_cadena = input("Introdueix 10 números separats per espais: ")
nums_separats = [int(num) for num in nums_cadena.split()]

print("Números de l'usuari: ", nums_separats)

suma_nums = sum(nums_separats)
print("Suma total: ", suma_nums)


mitjana = suma_nums / len(nums_cadena)
print("Mitjana: ", mitjana)

nums_separats.append(suma_nums)
nums_separats.append(mitjana)

print("Llista final:", nums_separats)