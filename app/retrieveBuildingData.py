#All necessary imports
import psycopg2

#queryType == 0 buildings list
#queryType == 1 list of floors from building name
#queryType == 2 room list from floor number and building name
#queryType == 3 max occupancy from floor  and room number
#queryType == 4 blueprint from building id and room number

#Function to handle all data
def getBuildingData(queryType, *info):
    result = []

    #DEFINE Database Info
    userName = "standard"
    password = "CapstoneGroup3"
    hostName = "localhost"
    portNum = ""
    databaseName = "CapstoneDB"

    #Function to retrieve data from db
    def retrieveBuildingData(queryForDB):
        try:
            #Establish connection to db
            connection, cursor = connectToDb(userName, password, hostName, portNum, databaseName)
                
            #Execute query
            queryResults = executeQuery(cursor, queryForDB)
        
            #Close connection to db
            if(connection):
                closeConnectionToDb(cursor, connection)
                
            return queryResults
        
        #Exception handling   
        except (Exception, psycopg2.Error) as error :
            print ("Error while fetching data from PostgreSQL", error)

    #Function to connect to db        
    def connectToDb(userName, password, hostName, portNum, databaseName):
        #Establish connection to db
        connection = psycopg2.connect(user = userName,
                                        password = password,
                                        host = hostName,
                                        port = portNum,
                                        database = databaseName)
        cursor = connection.cursor()
        return connection, cursor

    #Function to execute sql query    
    def executeQuery(cursor, query):
        #Execute query    
        cursor.execute(query)
        queryResults = cursor.fetchall()
        return queryResults

    #Function to close connection    
    def closeConnectionToDb(cursor, connection):
        #Close connection to db
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

    #Get a list of rooms from building name
    def getRoomListFromFloor(buildingName, floorNumber):
        buildingId = getBuildingId(buildingName)
        floorId = getFloorId(floorNumber, buildingId)
        query = "select room_number from app_rooms where floor_id = " + str(floorId)
        roomsList = retrieveBuildingData(query)
        return roomsList

    #Get max room occupancy
    def getMaxRoomOccupancy(buildingName, floorNumber, roomNumber):
        buildingId = getBuildingId(buildingName)
        floorId = getFloorId(floorNumber, buildingId)
        query = "select max_occupancy from app_rooms where floor_id = " + str(floorId) \
            + "and room_number = " + str(roomNumber)
        maxOccupancy = retrieveBuildingData(query)
        return maxOccupancy[0][0]

    #Get room blueprints
    def getRoomBlueprints(buildingName, floorNumber, roomNumber):
        buildingId = getBuildingId(buildingName)
        floorId = getFloorId(floorNumber, buildingId)
        query = "select blueprint from app_rooms where floor_id = " + str(floorId) \
            + "and room_number = " + str(roomNumber)
        blueprintUrl = retrieveBuildingData(query)
        return blueprintUrl[0][0]

    #Get list of buildings
    def getBuildingsList():
        query = "select name from app_buildings"
        buildingList = retrieveBuildingData(query)
        return buildingList
    
    #Get building id
    def getBuildingId(buildingName):
        query = "select id from app_buildings where name = '" + buildingName + "'"
        buildingId = retrieveBuildingData(query)
        return buildingId[0][0]

    #Get list of floors
    def getFloorsList(buildingName):
        buildingId = getBuildingId(buildingName)
        query = "select number from app_floors where building_id = '" + str(buildingId) +"'"
        floorList = retrieveBuildingData(query)
        return floorList[0][0]

    #Get floor id
    def getFloorId(floorNumber, buildingId):
        query = "select id from app_floors where number = " + str(floorNumber) + \
            "and building_id = " + str(buildingId)
        floorId = retrieveBuildingData(query)
        return floorId[0][0]

    #Handle the different get requests
    if queryType == 0:
        result = getBuildingsList()
    elif queryType == 1:
        result = getFloorsList(info[0])
    elif queryType == 2:
        result = getRoomListFromFloor(info[0], info[1])
    elif queryType == 3:
        result = getMaxRoomOccupancy(info[0], info[1], info[2])
    elif queryType == 4:
        result = getRoomBlueprints(info[0], info[1], info[2])

    return result

#Uncomment next 2 lines for testing Only
#data = getBuildingData(4, "ICT", 2, 121)
#print(data)

