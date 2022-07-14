""" Problem Statement : """

"""
Problem
Chef has to travel to another place. For this, he can avail any one of two cab services.
The first cab service charges XX rupees.
The second cab service charges YY rupees.
Chef wants to spend the minimum amount of money. Which cab service should Chef take?

Input Format
The first line will contain TT - the number of test cases. Then the test cases follow.
The first and only line of each test case contains two integers XX and YY - the prices of first and second cab services respectively.
Output Format
For each test case, output FIRST if the first cab service is cheaper, output SECOND if the second cab service is cheaper, output ANY if both cab services have the same price.
You may print each character of FIRST, SECOND and ANY in uppercase or lowercase (for example, any, aNy, Any will be considered identical).


Sample input :
3
30 65
42 42
90 50

Sample Output :
FIRST
ANY
SECOND


"""

""" Solution : """

# cook your dish here
test_cases = int(input())
for i in range(1, test_cases+1) :
    x, y = input().split()
    if int(x) < int(y):
        print("FIRST")
    elif int(x) == int(y):
        print("ANY")
    else:
        print("SECOND")


