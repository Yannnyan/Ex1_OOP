import Building
class Sector:
    def __init__(self, lowBoundry, highBoundry):
        self.lowBoundry = lowBoundry
        self.highBoundry = highBoundry
    def getlowBoundry(self):
        return self.lowBoundry
    def gethighBoundry(self):
        return self.highBoundry