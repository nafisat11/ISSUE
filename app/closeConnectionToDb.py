#All necessary imports
import psycopg2

def closeConnectionToDb(cursor, connection):
    #Close connection to db
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
