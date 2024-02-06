import xml.etree.ElementTree as ET

def crear_xml():
    # Crear raiz
    root = ET.Element("students")

    # Crear cinco  hijos (student)
    for i in range(1, 6):
        student = ET.SubElement(root, "student")

        # Añadir atributo a student
        student.set("id", str(i))

        # Crear cuatro subelementos en cada elemento student
        name = ET.SubElement(student, "name")
        surname = ET.SubElement(student, "surname")
        email = ET.SubElement(student, "email")
        dni = ET.SubElement(student, "dni")

        # Asignar valores a las etiquetas
        name.text = "Juan"
        surname.text = "Lopez"
        email.text = "juan.lopez@gmail.com"
        dni.text = "12345678A"

    # Crear el arbol XML
    tree = ET.ElementTree(root)

    # Guardar en un archivo .xml
    tree.write("students.xml")

    # Imprimir el arbol 
    ET.dump(root)

# Llamar a la funcion 
crear_xml()
