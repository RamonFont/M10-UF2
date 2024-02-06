from exercici33 import calcular_compra

def main():
    lista_compra = {100: 10, 250: 5, 1500: 30}
    
    iva = float(input("Introduce el porcentaje de IVA a aplicar: "))

    calcular_compra(lista_compra, iva)

if __name__ == "__main__":
    main()
