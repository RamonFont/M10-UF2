def comptar_paraules(frase):
    paraules = frase.split()
    diccionari_paraules = {paraula: len(paraula) for paraula in paraules}
    return diccionari_paraules
