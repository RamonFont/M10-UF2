import psycopg2

def create_connection():
    try:
        conn =  psycopg2.connect(
            database = "postgres",
            user = "user_postgres",
            password = "pass_postgres",
            host = "localhost",
            port = "5432"
        )

        connection = conn.cursor()
        print(connection)

        sql = '''CREATE TABLE USERS(
                        user_id SERIAL PRIMARY KEY,
                        user_name VARCHAR(255) NOT NULL,
                        user_surname VARCHAR(255) NOT NULL,
                        user_age BIGINT NOT NULL,
                        user_email VARCHAR(255) NOT NULL
        )'''

        #connection.execute(sql)
        conn.commit()
    except(Exception, psycopg2.Error) as error:
        print("Error", error)
