import Building
import Sector
import math
import Calls
import Call
class Sectors:
    # This class represents the root of the algorithm
    # it needs to have a list of Sector which divide the work of the elevators to clear cuts
    # , a Calls object, numberOfElevators, callMinFloor, callMaxFloor
    # The main function here is the SectIDOfFloor() which is the idea behind the algorithm
    def __init__(self, numberOfElevators, calls):
        # receives a list of Calls.Calls
        self.calls = calls
        self.callMinFloor = 0
        self.callMaxFloor = 0
        self.numberOfElevators = numberOfElevators
        self.sector = []
        self.setCallsMinMax()
        self.setSectors()
        self.SortSectors()
    def setCallsMinMax(self):
        # set minimum and maximum for calls O(n)
        for call in self.calls.calls:
            # if the source is lower than the min floor then it cant be bigger than the max floor
            if call.source < self.callMinFloor:
                self.callMinFloor = call.source
            elif call.source > self.callMaxFloor:
                self.callMaxFloor = call.source
            # same for destination
            if call.destination < self.callMinFloor:
                self.callMinFloor = call.destination
            elif call.destination > self.callMaxFloor:
                self.callMaxFloor = call.destination
    def setSectors(self):
        numOfFloors = (self.callMaxFloor - self.callMinFloor)
        lowBoundry = self.callMinFloor
        highBoundry = self.callMinFloor
        x= numOfFloors / self.numberOfElevators
        secDiff = int(x)
        for i in range(self.numberOfElevators):
            lowBoundry = highBoundry
            highBoundry = highBoundry + secDiff
            sect = Sector.Sector(lowBoundry,highBoundry)
            self.sector.append(sect)

        # it can happen that the int parse ignores important decimal values so the last sector would be a little bit more coarse
        if highBoundry < self.callMaxFloor:
            highBoundry = self.callMaxFloor
            self.sector[len(self.sector)-1] = Sector.Sector(lowBoundry,highBoundry)
    # given a floor this function returns the ID of the unique sector which contains it
    # it is designed to be that the ID of the Sector is associated to the ID of the elevator handling this Sector
    def SectIDOfFloor(self, floor):
        for i in range(self.numberOfElevators):
            if self.sector[i].lowBoundry <= floor and self.sector[i].highBoundry >= floor:
                return i
        return -1
    # this function analizes the calls and sorts the sectors by how many calls per sector
    def SortSectors(self):
        bucket = [0]*(self.callMaxFloor - self.callMinFloor)
        for call in self.calls.calls:
            bucket[call.destination] +=1
        l = [0]*len(self.sector)
        for i in range(len(bucket)):
            id = self.SectIDOfFloor(i)
            l[id] += bucket[i]
        self.QuickSort(l,0,len(l)-1)
    def QuickSort(self,l, low,high):
        if low < high:
            p = self.Partition(l,low,high)
            self.QuickSort(l,low,p-1)
            self.QuickSort(l,p+1,high)
    def Partition(self,l,low,high):
        i = (low - 1)  # index of smaller element
        pivot = l[high]  # pivot
        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if l[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                self.sector[i], self.sector[j] = self.sector[j], self.sector[i]
                l[i], l[j] = l[j], l[i]
        self.sector[i+1], self.sector[high] = self.sector[high], self.sector[i+1]
        l[i + 1], l[high] = l[high], l[i + 1]
        return (i + 1)
        # this function is usefull in Tests
    # returns the range of the sector given a Sector ID
    def rangeBySector(self, SectorID):
        l = []
        numberOfFloors = self.callMaxFloor - self.callMinFloor
        low = int(numberOfFloors / self.numberOfElevators) * (SectorID) + self.callMinFloor
        high = int(numberOfFloors / self.numberOfElevators) * (SectorID + 1) + self.callMinFloor
        l.append(low)
        l.append(high)
        return l
    # toString of the object
    def __str__(self):
        s = ''
        for i in range(len(self.sector)):
            s = s +' '+self.sector[i].__str__()
        return s