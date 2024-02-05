import psycopg2

def create_connection():
    try:
        conn = psycopg2.connect(
            database="postgres",
            user="user_postgres",
            password="pass_postgres",
            host="localhost",
            port="5432"
        )
        return conn

    except (Exception, psycopg2.Error) as error:
        print("Error:", error)
        return None

def close_connection(conn):
    if conn:
        conn.close()
        print("Connection closed.")