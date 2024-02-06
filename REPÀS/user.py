import json

class Usuario:
    def __init__(self, nombre_usuario, correo, telefono, edad, genero, pais):
        self.nombre_usuario = nombre_usuario
        self.correo = correo
        self.telefono = telefono
        self.edad = edad
        self.genero = genero
        self.pais = pais

    # Getters
    def obtener_nombre_usuario(self):
        return self.nombre_usuario

    def obtener_correo(self):
        return self.correo

    def obtener_telefono(self):
        return self.telefono

    def obtener_edad(self):
        return self.edad

    def obtener_genero(self):
        return self.genero

    def obtener_pais(self):
        return self.pais

    # Setters
    def establecer_nombre_usuario(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario

    def establecer_correo(self, correo):
        self.correo = correo

    def establecer_telefono(self, telefono):
        self.telefono = telefono

    def establecer_edad(self, edad):
        self.edad = edad

    def establecer_genero(self, genero):
        self.genero = genero

    def establecer_pais(self, pais):
        self.pais = pais

    # Mostrar el saludo del usuario
    def saludo(self):
        print(f"Hola, {self.nombre_usuario}! Aquí están tus detalles:")
        print(f"Correo: {self.correo}")
        print(f"Teléfono: {self.telefono}")
        print(f"Edad: {self.edad}")
        print(f"Género: {self.genero}")
        print(f"País: {self.pais}")

    #Convertir en diccionario
    def a_diccionario(self):
        return {
            "nombre_usuario": self.nombre_usuario,
            "correo": self.correo,
            "telefono": self.telefono,
            "edad": self.edad,
            "genero": self.genero,
            "pais": self.pais
        }

if __name__ == "__main__":
    # Crear  objeto 
    mi_usuario = Usuario("juan_lopez", "juan.lopez@gmail.com", "12345678A", 30, "Masculino", "España")

    # Mostrar el saludo del usuario
    mi_usuario.saludo()

    # Convertir en diccionario y mostrarlo en formato JSON
    usuario_dict = mi_usuario.a_diccionario()
    print("Usuario como JSON:")
    print(json.dumps(usuario_dict, indent=2))
