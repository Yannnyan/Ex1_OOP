class Call:
    # a simple class just organize a single call from the csv file received
    def __init__(self,time, source, destination):
        self.time = time
        self.source = source
        self.destination = destination
