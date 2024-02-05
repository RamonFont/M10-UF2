import psycopg2

from connection import create_connection, close_connection
from create import create_user
from delete import delete_users
from read import read_users
from update import update_user
from create_table import create_table

if __name__ == "__main__":
    conn = create_connection()

    #Si ens connectem a la base de dades, truquem a tots els metodes, quan acabem tanquem la connexió
    if conn:
        try:

            with conn.cursor() as connection:
                create_table(connection)

            with conn.cursor() as connection:
                create_user(connection)

            with conn.cursor() as connection:
                read_users(connection)

            with conn.cursor() as connection:
                update_user(connection)

            with conn.cursor() as connection:
                read_users(connection)

            with conn.cursor() as connection:
                delete_users(connection)

            with conn.cursor() as connection:
                read_users(connection)

        except (Exception, psycopg2.Error) as error:
            print("Error:", error)

        finally:
            close_connection(conn)
