import psycopg2

#Legir els usuaris de la base de dades amb un layout personalitzat
def read_users(connection):
    try:
        sql = '''SELECT * FROM public.users'''
        connection.execute(sql)
        result = connection.fetchall()
        
        for i in result:
            print("user_id ", i[0],)
            print("user_name ", i[1],)
            print("user_surname ", i[2],)
            print("user_age ", i[3],)
            print("user_email ", i[4], "\n")

        

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)
