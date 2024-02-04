from connection import conn
from connection import crear_connection

def delete_user(connection):
    sql_delete = """DELETE FROM public.users WHERE user_id=1
    """

    connection.execute(sql_delete)
    conn.commit()