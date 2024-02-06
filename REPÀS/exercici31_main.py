from exercici31 import calcular_factura

def main():
    try:
        cantidad_sin_iva = float(input("Introduce la cantidad sin IVA: "))
        iva = int(input("Introduce el porcentaje de IVA (4%, 10% o 21%): "))

        calcular_factura(cantidad_sin_iva, iva)

    except ValueError:
        print("Error.")

if __name__ == "__main__":
    main()
