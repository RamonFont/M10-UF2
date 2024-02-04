from connection import conn
from connection import connection

def user_update(connection):
    sql_update = """UPDATE public.user SET user_email='rogers@info.com' WHERE user_id=1
    """

    connection.execute(sql_update)
    conn.commit()
    result = connection.rowcount
    print("id modificada: ", result, "Actualització efectuada sense errors")