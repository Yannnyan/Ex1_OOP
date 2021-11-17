import math


class Elevator:
    def __init__(self, elev):
        self._id = elev[0]
        self._speed = elev[1]
        self._minFloor = elev[2]
        self._maxFloor = elev[3]
        self._closeTime = elev[4]
        self._openTime = elev[5]
        self._startTime = elev[6]
        self._stopTime = elev[7]
        self.callCounter = 0
    def getMinFloor(self):
        return self._minFloor
    def getMaxFloor(self):
        return self._maxFloor
    def getTimeForOpen(self):
        return self._openTime
    def getTimeForClose(self):
        return self._closeTime
    def getSpeed(self):
        return self._speed
    def getStartTime(self):
        return self._startTime
    def getStopTime(self):
        return self._stopTime
    def incrementCall(self):
        self.callCounter+=1