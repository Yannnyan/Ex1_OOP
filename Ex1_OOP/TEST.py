def testAllocate():
    f = open('Ex1_out.csv', 'w', newline='')
    writer = csv.writer(f)
    time = 0
    source = 0
    dest = 0
    elev = 0
    end = 0
    # run the algorithm here:

    # get specific call
    x = callList  # getCallCase(3)

    # get specific building
    b = building1  # getBuildingCase(2)
    building = Building.Building(b)

    # initialize the calls in an object
    calls = Calls.Calls(x)
    # read the calls file
    file = open(x, 'r')
    reader = csv.reader(file)
    rows = []
    # just to check the jar file, gets random elev for call
    for i in range(calls.size()):
        r = random.randint(0, building.numberOfElevators() - 1)
        time = calls.getcalltime(i)
        source = calls.getSourceFloor(i)
        dest = calls.getDestFloor(i)
        elev = r
        header = ['Elevator Call', str(time), str(source), str(dest), str(3), str(elev), "Done", "dt", str(0)]
        writer.writerow(header)
    # enter results here:
    f.close()

