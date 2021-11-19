import unittest
import Sectors
import Building
import Calls
import Sector
from typing import List
class MyTestCase(unittest.TestCase):
    b1 = Building.Building('input\B1.json')
    b2 = Building.Building('input\B2.json')
    b3 = Building.Building('input\B3.json')
    b4 = Building.Building('input\B4.json')
    b5 = Building.Building('input\B5.json')
    calla = Calls.Calls('input\Calls_a.csv')
    callb = Calls.Calls('input\Calls_b.csv')
    callc = Calls.Calls('input\Calls_c.csv')
    calld = Calls.Calls('input\Calls_d.csv')
    noe = [b1.numberOfElevators(), b2.numberOfElevators(), b4.numberOfElevators()
            , b5.numberOfElevators()]
    calls = [calla, callb, callc, calld]
    sectors = []
    def declare(self):
        for j in range(len(self.calls)):
            for i in range(len(self.noe)):
                secTemp = Sectors.Sectors(self.noe[i], self.calls[j])
                self.sectors.append(secTemp)
    def test_setCallsMinMax(self):
        self.declare()
        min = [-2,-10]
        max = [10,100]
        for i in range(len(self.sectors)):
            if(i < 4):
                self.assertEqual(self.sectors[i].callMaxFloor, max[0])
                self.assertEqual(self.sectors[i].callMinFloor, min[0])
            else:
                self.assertEqual(self.sectors[i].callMaxFloor, max[1])
                self.assertEqual(self.sectors[i].callMinFloor, min[1])
    def test_setSectors(self):
        self.declare()
        for i in range(len(self.sectors)):
            print(self.sectors[i].__str__())
    def test_sectIDOfFloor(self):
        self.declare()
        for j in range(len(self.callb.calls)):
            print(str(self.callb.calls[j].destination) + ' : ' + str(self.sectors[6].SectIDOfFloor(self.callb.calls[j].destination)))
    def test_rangeBySector(self):
        pass
    def test_SortSectors(self):
        self.declare()
        # change the index from 0 - 15 as wanted
        sect = self.sectors[7]
        sect.SortSectors()
        print(sect.__str__())

if __name__ == '__main__':
    unittest.main()