import Building
import Sectors
import Sector
import Calls
import csv
class MyBuilding:
    # This class supposed to be the father of all other classes and to connect between them
    # This is where the implementation of the algorithm is expressed

    def __init__(self, sectors, building, calls):
        self.building = building
        self.sectors = sectors
        self.calls = calls
    # assignes an elevator to handle a call
    def AllocateToCall(self,Call):
        elevID = self.sectors.SectIDOfFloor(Call.destination)
        elevID = self.building.Elevator[elevID]._id
        # calculate the average of calls per elevator
        # if an elevator got more calls than average then send this call to other elevator
        # than has less than 0.95 average just to balance things if an elevator is spammed
        average =0
        for i in range(len(self.building.Elevator)):
            average = average + self.building.getElevator(i).callCounter
        average = average / self.building.numberOfElevators()
        if self.building.getElevator(elevID).callCounter > average:
            for i in range(self.building.numberOfElevators()):
                nextID = (elevID + i) % self.building.numberOfElevators()
                if self.building.Elevator[nextID].callCounter < (average * 0.95):
                    elevID = nextID
                    break
        self.building.Elevator[elevID].callCounter+=1
        return elevID
    # creates the out file Ex1_out.csv
    def createOut(self):
        f = open('Ex1_out.csv', 'w', newline='')
        writer = csv.writer(f)
        for call in self.calls.calls:
            alloc = self.AllocateToCall(call)
            row = ['Elevator Call', str(call.time), str(call.source), str(call.destination),str(10),str(alloc)]
            writer.writerow(row)
