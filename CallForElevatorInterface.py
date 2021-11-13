class CallForElevatorInterface:
    INIT = 0
    GOING2SRC = 1
    GOIND2DEST = 2
    DONE = 3
    UP = 1
    DOWN = -1
    def getState(self):
        pass

    def getTime(self):
        pass

    def getSrc(self):
        pass

    def getDest(self):
        pass

    def getType(self):
        pass

    def allocatedTo(self):
        pass