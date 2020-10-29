#All necessary imports
import psycopg2

def connectToDb(userName, password, hostName, portNum, databaseName):
    #Establish connection to db
    connection = psycopg2.connect(user = userName,
                                    password = password,
                                    host = hostName,
                                    port = portNum,
                                    database = databaseName)
    cursor = connection.cursor()
    return connection, cursor
