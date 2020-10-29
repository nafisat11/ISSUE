def printDbQueryResults(queryResults):
    for row in queryResults:
        print("Id = ", row[0], )
        print("Room Number = ", row[1])
        print("Max Occupancy = ", row[2])
        print("Blueprint URL = ", row[3])
        print("Floor Id  = ", row[4], "\n")
