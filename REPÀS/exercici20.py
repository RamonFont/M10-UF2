myDict = {}
nom = ""
edat = 0
afegir = "a"
while afegir == "a":
    nom = input("Escriu un nom: ")
    edat = input("Escriu una edat: ")
    afegir = input("Vols seguir afegint? a:si, b:no ")
    myDict[nom] = edat
    
print(myDict)