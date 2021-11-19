# Ex1_OOP
The purpose of this Excersice is to modulate and solve an Off-Line algorithm for the elevator allocation problem, and implement this algorithm in python.
Explanation of the elevator allocation problem:
We are given a several lists of calls. Each call contains three specifications. A source floor, a destination floor and time called.
Also, we are given a building (ref-t Bi.json) with a maximum floor and minimum floor values, a number of elevators which maintain several properties with varying values such as speed, time to open ,time to close time to stop , etc...
The purpose of this algorithm is to determine the best sequence of allocations for elevators to calls. Which is considered the one with the least average waiting time per call.

This project contains folders such as 'AnalizeCalls' which contains files written in excel which analize the lists of calls.
The excel sheets contain graphs used to visualize the problem.
And more generally those are created to estimate values like average seconds per call, and the distribution of the source and destination calls for different ranges of floors.
The files insidee 'AnalizeCalls' are not necessary to run the code.
The project contains a folder called 'input', this folder contains all the .json and .csv files received.
READ THE PDF NAMED 'Ex1_OOP.pdf. This pdf file is an extension of this readme. It contains all the details about the project. This pdf is located inside this branch. 

Our algorithm implements a Sectorization algorithm for the elevator allocation problem.
To run this project, you will need the output file of the project, the .json file representing the building used and the .jar simulator file.
Example of running the jar file in cmd: java -jar Ex1_checker_V1.2_obf.jar 111,222 B5.json Ex1_out.csv out.log ![image](https://user-images.githubusercontent.com/82415308/142551926-75b57adb-b242-4fa0-a0ee-3599cb8a3850.png)
The results of the simulator should be written in a out.log file. Example: ![image](https://user-images.githubusercontent.com/82415308/142552274-eeb7c6f2-76f1-428b-a970-9e2ec5acccef.png)


