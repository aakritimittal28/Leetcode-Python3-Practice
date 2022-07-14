""" Problem Statement : """
"""
Problem
There is a group of NN friends who wish to enroll in a course together. The course has a maximum capacity of MM students that can register for it. If there are KK other students who have already enrolled in the course, determine if it will still be possible for all the NN friends to do so or not.

Input Format
The first line contains a single integer TT - the number of test cases. Then the test cases follow.
Each test case consists of a single line containing three integers NN, MM and KK - the size of the friend group, the capacity of the course and the number of students already registered for the course.
Output Format
For each test case, output Yes if it will be possible for all the NN friends to register for the course. Otherwise output No.

You may print each character of Yes and No in uppercase or lowercase (for example, yes, yEs, YES will be considered identical).

Sample Input :
3
2 50 27
5 40 38
100 100 0

Sample Output :
Yes
No
Yes

"""

""" Solution : """
# cook your dish here
test_cases = int(input())
for i in range(test_cases):
    n_wish_to, m_capacity, k_enrolled = input().split()
    available = int(m_capacity) - int(k_enrolled)
    if available >= int(n_wish_to):
        print("Yes")
    else:
        print("No")
