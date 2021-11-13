class ElevatorInterface:
    UP = 1
    LEVEL = 0
    DOWN = -1
    ERROR = -2

    def getMinFloor(self):
        pass

    def getMaxFloor(self):
        pass

    def getTimeForOpen(self):
        pass

    def getTimeForClose(self):
        pass

    def getState(self):
        pass

    def getPos(self):
        pass

    def goTo(self):
        pass

    def stop(self):
        pass

    def getSpeed(self):
        pass

    def getStartTime(self):
        pass

    def getStopTime(self):
        pass
