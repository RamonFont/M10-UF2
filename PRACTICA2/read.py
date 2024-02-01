from connection import conn
from connection import connection

sql_read = '''SELECT user_id, user_name, user_surname, user_age, user_email
                FROM public.users'''

connection.execute(sql_read)
result = connection.fetchall()

for i in result:
    print("user_id ", i[0],)
    print("user_name ", i[1],)
    print("user_surname ", i[2],)
    print("user_age ", i[3],)
    print("user_email ", i[4], "\n")

conn.close()