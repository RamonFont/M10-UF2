import psycopg2

def delete_users(connection):
    try:
        sql = '''DELETE FROM public.users WHERE user_id = 1'''

        connection.execute(sql)
        connection.connection.commit()
        print("All users deleted successfully.")

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)

