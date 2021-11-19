import csv
import Call
class Calls:
    # simple class which reads from csv file and converts the Strings to a Call objects and stores them
    # inside a list
    def __init__(self, callsListcsv):
        f = open(callsListcsv, 'r')
        reader = csv.reader(f)
        self.calls = []
        for call in reader:
            time = float(call[1])
            source = int(call[2])
            dest = int(call[3])
            c = Call.Call(time,source,dest)
            self.calls.append(c)
