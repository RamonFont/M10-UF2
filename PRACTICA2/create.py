from connection import conn
from connection import connection


def crear_user(connection, user_name, user_surname, user_age, user_email):
    sql_insert = '''INSERT INTO public.users(user_id, user_name, user_surname, user_age, user_email)
                            VALUES ('1', 'Roger', 'Sobrino', 40, 'roger@sobrino.com')'''

    connection.execute(sql_insert)
    conn.commit()