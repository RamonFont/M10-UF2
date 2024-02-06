import json

def crear_json():
    # Crear datos de libros
    datos_libros = [
        {"title": "Los Juegos del Hambre", "cover": "juegos_hambre.jpg", "year": 2008, "pages": 374},
        {"title": "Crepusculo", "cover": "crepusculo.jpg", "year": 2005, "pages": 498},
        {"title": "Divergente", "cover": "divergente.jpg", "year": 2011, "pages": 487},
        {"title": "Las Cronicas de Narnia", "cover": "narnia.jpg", "year": 1950, "pages": 767}
    ]

    # Crear diccionario 
    json_data = {"book": datos_libros * 4}

    # Mostrar el JSON por consola
    print("JSON:")
    print(json.dumps(json_data, indent=2))

    # Guardar el JSON 
    with open("libros.json", "w") as archivo:
        json.dump(json_data, archivo, indent=2)

# Llamar funcion
crear_json()
