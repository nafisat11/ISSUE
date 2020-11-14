#All necessary imports
import psycopg2
from app.models import Buildings, Floors, Rooms, Heatmaps

#queryType == 0 buildings list
#queryType == 1 list of floors from building name
#queryType == 2 room list from floor number and building name
#queryType == 3 max occupancy from floor and room number
#queryType == 4 max pandemic occupancy from floor and room number
#queryType == 5 blueprint from building id and room number

#Function to handle all data
def getBuildingData(queryType, *info):
    result = []

    #Get a list of rooms from building name and floor number
    def getRoomListFromFloor(buildingName, floorNumber):
        buildingId = getBuildingId(buildingName)
        floorId = getFloorId(floorNumber, buildingId)
        roomsList = Rooms.objects.filter(floor = floorId)
        roomList = []
        for room in roomsList:
            roomList.insert(room.get_room_number())
        return roomList

    #Get max room occupancy
    def getMaxRoomOccupancy(buildingName, floorNumber, roomNumber):
        buildingId = getBuildingId(buildingName)
        floorId = getFloorId(floorNumber, buildingId)
        roomObject = Rooms.objects.filter(floor_id = floorId, room_number = roomNumber)
        return roomObject.get_max_occupancy()

    #Get max pandemic room occupancy
    def getMaxPandemicRoomOccupancy(buildingName, floorNumber, roomNumber):
        buildingId = getBuildingId(buildingName)
        floorId = getFloorId(floorNumber, buildingId)
        roomObject = Rooms.objects.filter(floor_id = floorId, room_number = roomNumber)
        return roomObject.get_max_pandemic_occupancy()

    #Get room blueprints
    def getRoomBlueprints(buildingName, floorNumber, roomNumber):
        buildingId = getBuildingId(buildingName)
        floorId = getFloorId(floorNumber, buildingId)
        roomObject = Rooms.objects.filter(floor_id = floorId, room_number = roomNumber)
        return roomObject.get_blueprint()

    #Get list of buildings
    def getBuildingsList():
        allBuildings = Buildings.objects.all()
        buildingList = []
        for building in allBuildings:
            buildingList.insert(building.get_building_name())
        return buildingList
    
    #Get building id
    def getBuildingId(buildingName):
        buildingId = Buildings.objects.filter(name = buildingName)
        return buildingId.get_building_id()

    #Get list of floors
    def getFloorsList(buildingName):
        buildingId = getBuildingId(buildingName)
        floorList = Floors.objects.filter(building = buildingId)
        floorNumbers = []
        for floor in floorList:
            floorNumbers.insert(floor.get_floor_number())
        return floorNumbers

    #Get floor id
    def getFloorId(floorNumber, buildingId):
        floorId = Floors.objects.filter(number = floorNumber, building=buildingId)
        return floorId.get_floor_id()

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
        result = getMaxPandemicRoomOccupancy(info[0], info[1], info[2])
    elif queryType == 5:
        result = getRoomBlueprints(info[0], info[1], info[2])

    return result

