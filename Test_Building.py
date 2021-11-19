import unittest
import Building

class MyTestCase(unittest.TestCase):
    def test_QuickSort(self):
        b4 = 'input\B4.json'
        building1 = Building.Building(b4)
        self.assertEqual(building1.Elevator[0].getSpeed(),1)
        self.assertEqual(building1.Elevator[1].getSpeed(), 2)
        self.assertEqual(building1.Elevator[2].getSpeed(), 2)
        self.assertEqual(building1.Elevator[3].getSpeed(), 6)
        self.assertEqual(building1.Elevator[4].getSpeed(), 8)
        b5 = 'input\B5.json'
        building2 = Building.Building(b5)
        self.assertEqual((building2.Elevator[0].getSpeed()),1.5)
        self.assertEqual((building2.Elevator[1].getSpeed()),2)
        self.assertEqual((building2.Elevator[2].getSpeed()),3)
        self.assertEqual((building2.Elevator[3].getSpeed()),3)
        self.assertEqual((building2.Elevator[4].getSpeed()),5)
        self.assertEqual((building2.Elevator[5].getSpeed()),5)
        self.assertEqual((building2.Elevator[6].getSpeed()),7)
        self.assertEqual((building2.Elevator[7].getSpeed()),9)
        self.assertEqual((building2.Elevator[8].getSpeed()),9)
        self.assertEqual((building2.Elevator[9].getSpeed()),9)


if __name__ == '__main__':
    unittest.main()
