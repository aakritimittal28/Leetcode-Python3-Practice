""" Problem Statement : """

"""
Problem
Chef is watching TV. The current volume of the TV is XX. Pressing the volume up button of the TV remote increases the volume by 11 while pressing the volume down button decreases the volume by 11. Chef wants to change the volume from XX to YY. Find the minimum number of button presses required to do so.

Input Format
The first line contains a single integer TT - the number of test cases. Then the test cases follow.
The first and only line of each test case contains two integers XX and YY - the initial volume and final volume of the TV.
Output Format
For each test case, output the minimum number of times Chef has to press a button to change the volume from XX to YY.

Sample input :
2
50 54
12 10

Sample Output :
4
2

"""

""" Solution : """

# cook your dish here
test_cases = int(input())
for i in range(1, test_cases+1) :
    up, down = input().split()
    vol = abs(int(up) - int(down))
    print(vol)



