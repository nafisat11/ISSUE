#All necessary imports
import psycopg2

def executeQuery(cursor, query):
    #Execute query    
    cursor.execute(query)
    print("Selecting rows from rooms table using cursor.fetchall")
    queryResults = cursor.fetchall() 
