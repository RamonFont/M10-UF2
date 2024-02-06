def calcular_factura(cantidad_sin_iva, iva):
    try:
        # Verificar IVA
        if iva not in (4, 10, 21):
            # Aplicar el 21% si el valor es incorrecto
            iva = 21 

        # Calcular el total con IVA
        total = cantidad_sin_iva + (cantidad_sin_iva * iva / 100)

        # Mostrar resultados
        print(f"Valor sin IVA: {cantidad_sin_iva}")
        print(f"IVA ({iva}%): {cantidad_sin_iva * iva / 100}")
        print(f"Total con IVA: {total}")

    except ValueError:
        print("Error.")
