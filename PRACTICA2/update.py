import psycopg2

#Modificar parametre de un usuari
def update_user(connection):
    try:
        sql = '''UPDATE public.users
                 SET user_email = 'rogers@info.com'
                 WHERE user_id = 1'''

        connection.execute(sql)
        connection.connection.commit()
        

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)
