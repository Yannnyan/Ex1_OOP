import csv
import Call
class Calls:
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
