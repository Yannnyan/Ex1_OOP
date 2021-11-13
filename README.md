# Ex1_OOP
The purpose of this Excersice is to modulate and solve an Off-Line algorithm for the elevator allocation problem, and implement this algorithm in python.
Explanation of the elevator allocation problem:
We are given a several lists of calls. Each call contains three specifications. A source floor, a destination floor and time called.
Also, we are given a building (ref-t Bi.json) with a maximum floor and minimum floor values, a number of elevators which maintain several properties with varying values such as speed, time to open ,time to close time to stop , etc...
The purpose of this algorithm is to determine the best sequence of allocations for elevators to calls. Which is considered the one with the least average waiting time per call.

This project contains folders such as 'AnalizeCalls' which contains files written in excel which analize the lists of calls.
The excel sheets contain graphs used to visualize the problem.
And more generally those are created to estimate values like average seconds per call, and the distribution of the source and destination calls for different ranges of floors.
We shall use this information to adjust our algorithm to match the calls given and make our algorithm more efficient.
It is preffered to use excel spreadsheet to open the files in 'AnalizeCalls' folder.

The algorithm is not yet written, because of a certain complexity which made our last algorithm not viable.
further discovery and research is needed to complete this project efficiently.
