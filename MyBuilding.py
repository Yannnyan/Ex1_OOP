import Building
import Sectors
import Sector
import Calls
import csv
class MyBuilding:
    def __init__(self, sectors, building, calls):
        self.building = building
        self.sectors = sectors
        self.calls = calls

    def AllocateToCall(self,Call):
        elevID = self.sectors.SectIDOfFloor(Call.destination)
        # calculate the average of calls per elevator
        average =0
        for i in range(len(self.building.Elevator)):
            average = average + self.building.getElevator(i).callCounter
        average = average / self.building.numberOfElevators()
        for i in range(self.building.numberOfElevators()):
            nextID = (elevID + i) % self.building.numberOfElevators()
            if self.building.Elevator[nextID].callCounter < (average * 0.95):
                elevID = nextID
                break
        self.building.Elevator[elevID].callCounter+=1
        return elevID
    def createOut(self):
        f = open('Ex1_out.csv', 'w', newline='')
        writer = csv.writer(f)
        for call in self.calls.calls:
            alloc = self.AllocateToCall(call)
            row = ['Elevator Call', str(call.time), str(call.source), str(call.destination),str(10),str(alloc)]
            writer.writerow(row)
