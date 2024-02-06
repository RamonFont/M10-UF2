import psycopg2

#Funció de crear usuari
def create_user(connection):
    try:
        sql = '''INSERT INTO USERS (user_id, user_name, user_surname, user_age, user_email)
                 VALUES ('1', 'roger', 'sobrino', 30, 'sisis@gmail.com')'''

        connection.execute(sql)
        connection.connection.commit()
        
    except (Exception, psycopg2.Error) as error:
        print("Error:", error)



