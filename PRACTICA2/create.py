from psycopg2 import connection
from psycopg2 import connect


sql_insert = '''INSERT INTO public.users(user_id, user_name, user_surname, user_age, user_email)
                            VALUES ('1', 'Roger', 'Sobrino', 40, 'roger@sobrino.com')'''

connection.execute(sql_insert)
connect.commit()