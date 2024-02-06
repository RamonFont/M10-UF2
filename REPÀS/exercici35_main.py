from exercici35 import comptar_paraules

def main():
    frase_usuari = input("Introduce una frase: ")

    resultat = comptar_paraules(frase_usuari)

    print("Diccionario:", resultat)


if __name__ == "__main__":
    main()
