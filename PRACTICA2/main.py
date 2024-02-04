import psycopg2
from connection import crear_connection
from create import crear_user

if __name__ == "__main__":
    conn = crear_connection()

    if conn:
        try:
            connection = conn.cursor()

            # Aquí puedes llamar a la función create_user con los datos del nuevo usuario
            crear_user(connection, "John", "Doe", 30, "john.doe@example.com")

        except (Exception, psycopg2.Error) as error:
            print("Error:", error)


