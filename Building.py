import json
import Elevator
import random
class Building:
    # simple class which reads from csv file and convers the Strings to a Building object
    # Each Building has a list of Elevators min floor and maximum floor
    # The purpose of the class is to have a simple representation of a buiilding
    def __init__(self, building):

        with open(building, "r") as read_file:
            buildingDict = json.load(read_file)
        key_list = list(buildingDict.keys())
        value_list = list(buildingDict.values())

        self.maxfloor = value_list[key_list.index("_maxFloor")]
        self.minfloor = value_list[key_list.index("_minFloor")]
        self.Elevator = []
        indexelev = key_list.index("_elevators")
        elevators = value_list[indexelev]
        # initialize the Elevator list
        for i in range(elevators.__len__()):
            elevPropertiesDict = value_list[indexelev][i]
            elevpropertiesVal = list(elevPropertiesDict.values())
            elevi = Elevator.Elevator(elevpropertiesVal)
            self.Elevator.append(elevi)
        self.SortElevators()

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
    def SortElevators(self):
        self.QuickSort(0,self.numberOfElevators()-1)
    def QuickSort(self,low,high):
        if low < high and low >= 0 and high >=0:
            p =  self.partition(low,high)
            self.QuickSort(low,p-1)
            self.QuickSort(p+1,high)

    def partition(self,start,end):
        i = (start - 1)  # index of smaller element
        pivot = self.Elevator[end].getSpeed()  # pivot

        for j in range(start, end):

            # If current element is smaller than or
            # equal to pivot
            if self.Elevator[j].getSpeed() <= pivot:
                # increment index of smaller element
                i = i + 1
                self.swap(j,i)
        self.swap(i+1,end)
        return (i + 1)
    def swap(self, left, right):
        temp = self.Elevator[left]
        self.Elevator[left] = self.Elevator[right]
        self.Elevator[right] = temp
