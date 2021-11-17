import csv
import math
import random
import sys
import Building
import Calls
import Sectors
import MyBuilding
def main():
    b = sys.argv[1]
    c = sys.argv[2]
    calls = Calls.Calls(c)
    building = Building.Building(b)
    sectors = Sectors.Sectors(building.numberOfElevators(),calls)
    myBuilding = MyBuilding.MyBuilding(sectors,building,calls)

    myBuilding.createOut()
if __name__ == '__main__':
    main()
