import psycopg2

def create_table(connection):
    try:

        sql = '''CREATE TABLE IF NOT EXISTS USERS (
                    user_id SERIAL PRIMARY KEY,
                    user_name VARCHAR(255) NOT NULL,
                    user_surname VARCHAR(255) NOT NULL,
                    user_age BIGINT NOT NULL,
                    user_email VARCHAR(255) NOT NULL
                )'''

        connection.execute(sql)
        connection.connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)
