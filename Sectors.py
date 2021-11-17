import Building
import Sector
import math
import Calls
import Call
class Sectors:
    def __init__(self, numberOfElevators, calls):
        self.calls = calls
        self.callMinFloor = 0
        self.callMaxFloor = 0
        # this is the list of calls file
        self.numberOfElevators = numberOfElevators
        self.sector = []
        self.setCallsMinMax()
        self.setSectors()
    def setCallsMinMax(self):
        # set minimum and maximum for calls
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
        secDiff = int(numOfFloors / self.numberOfElevators)
        for i in range(self.numberOfElevators):
            highBoundry = highBoundry + secDiff
            sect = Sector.Sector(lowBoundry,highBoundry)
            self.sector.append(sect)
            lowBoundry = highBoundry

    def SectIDOfFloor(self, floor):
        for i in range(self.numberOfElevators):
            if self.sector[i].lowBoundry <= floor and self.sector[i].highBoundry >= floor:
                return i
        return -1
    def rangeBySector(self, SectorID):
        l = []
        numberOfFloors = self.callMaxFloor - self.callMinFloor
        low = int(numberOfFloors / self.numberOfElevators) * (SectorID) + self.callMinFloor
        high = int(numberOfFloors / self.numberOfElevators) * (SectorID + 1) + self.callMinFloor
        l.append(low)
        l.append(high)
        return l

