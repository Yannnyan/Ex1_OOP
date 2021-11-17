import json
import Elevator

class Building:
    def __init__(self, building):
        # minFloor
        # maxFloor
        # numberOfElevators
        # getElevator
        # getBuildingsname
        # building is a json file path representing Bi (Building i from input) as i ranges from 1 to 5
        with open(building, "r") as read_file:
            buildingDict = json.load(read_file)
        key_list = list(buildingDict.keys())
        value_list = list(buildingDict.values())

        self.maxfloor = value_list[key_list.index("_maxFloor")]
        self.minfloor = value_list[key_list.index("_minFloor")]
        self.Elevator = []
        indexelev = key_list.index("_elevators")
        elevators = value_list[indexelev]
        for i in range(elevators.__len__()):
            elevPropertiesDict = value_list[indexelev][i]
            elevpropertiesVal = list(elevPropertiesDict.values())
            elevi = Elevator.Elevator(elevpropertiesVal)
            self.Elevator.append(elevi)

    def getBuildingName(self):
        pass
        # ??

    def minFloor(self):
        return self.minfloor

    def maxFloor(self):
        return self.maxfloor

    def numberOfElevators(self):
        return self.Elevator.__len__()

    # check NullPointerException when used
    def getElevator(self, i):
        if i in range(self.Elevator.__len__()):
            return self.Elevator[i]
        else:
            return None
            
