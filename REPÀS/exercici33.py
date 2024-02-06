def calcular_compra(lista_compra, iva):
    total_con_descuento = sum((precio - (precio * descuento / 100)) for precio, descuento in lista_compra.items())
    total_con_iva = total_con_descuento + (total_con_descuento * iva / 100)

    print("Resumen de la compra:")
    for i, (precio, descuento) in enumerate(lista_compra.items(), start=1):
        precio_con_descuento = precio - (precio * descuento / 100)
        print(f"Producto {i}: Precio con descuento: {precio_con_descuento}, Precio con IVA: {precio_con_descuento + (precio_con_descuento * iva / 100)}")

    print(f"\nTotal con descuento: {total_con_descuento}")
    print(f"Total con IVA: {total_con_iva}")


