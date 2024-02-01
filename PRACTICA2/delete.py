from connection import conn
from connection import connection


sql_delete = """DELETE FROM public.users WHERE user_id=1
"""

connection.execute(sql_delete)
conn.commit()