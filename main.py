import Building


def main():
    building = "input\B1.json"
    B1 = Building.Building(building)
    print(B1.minFloor())


if __name__ == '__main__':
    main()


def AllocateAnElevator():
    # say there are 1000 calls and 10 elevators so:
    # this algo waits for the time that 100 calls have been called and allocates an elevator to the furthest call
    # up of course the elevator picks up all the passengers that want to go up and then allocates that elevator to
    # the furthest call down.
    pass
