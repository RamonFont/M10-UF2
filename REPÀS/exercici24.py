import json

def leer_json():
    # Abrir el archivo JSON
    with open("libros.json", "r") as archivo:
        # Leer contenido 
        contenido_json = json.load(archivo)

    # Mostrar lo en JSON
    print(json.dumps(contenido_json, indent=2))

# Llamar función 
leer_json()
