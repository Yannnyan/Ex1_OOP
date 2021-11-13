import csv

import Building


def getCallCase(callCase):
    # Notice those files are on Yan's PC so this may not work for everyone with access to this github
    Calls_a = 'input\calls_a.csv'
    Calls_b = 'input\calls_b.csv'
    Calls_c = 'input\calls_c.csv'
    Calls_d = 'input\calls_d.csv'
    # CHOOSE WHICH CALL TO RUN WITH 'callCase'
    x = ''
    if callCase == 0:
        x = Calls_a
    elif callCase == 1:
        x = Calls_b
    elif callCase == 2:
        x = Calls_c
    elif callCase == 3:
        x = Calls_d
    return x


def getBuildingCase(buildingCase):
    B1 = 'input\B1'
    B2 = 'input\B1'
    B3 = 'input\B1'
    B4 = 'input\B1'
    B5 = 'input\B1'
    x = ''
    if buildingCase == 0:
        x = B1
    elif buildingCase == 1:
        x = B2
    elif buildingCase == 2:
        x = B3
    elif buildingCase == 3:
        x = B4
    elif buildingCase == 4:
        x = B5
    return x


def AllocateAnElevator():
    f = open('out.csv', 'w')
    writer = csv.writer(f)
    time = 0
    source = 0
    dest = 0
    elev = 0
    end = 0
    # run the algorithm here:
    # get specific call
    x = getCallCase(3)
    # get specific building
    b = getBuildingCase(2)
    # read the calls file
    file = open(x, 'r')
    reader = csv.reader(file)
    rows = []
    for row in reader:
        rows.append(row)
        print(format(row))

    # enter results here:
    header = ['Elevator Call', str(time), str(source), str(dest), str(3), str(elev), 'Done', 'dt', str(end)]
    writer.writerow(header)
    f.close()


def main():
    AllocateAnElevator()


if __name__ == '__main__':
    main()
