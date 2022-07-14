""" Problem Statement : """
"""
Problem
To access CRED programs, one needs to have a credit score of 750750 or more.
Given that the present credit score is XX, determine if one can access CRED programs or not.

If it is possible to access CRED programs, output \texttt{YES}YES, otherwise output \texttt{NO}NO.

Input Format
The first and only line of input contains a single integer XX, the credit score.

Output Format
Print \texttt{YES}YES if it is possible to access CRED programs. Otherwise, print \texttt{NO}NO.

You may print each character of the string in uppercase or lowercase (for example, the strings \texttt{YeS}YeS, \texttt{yEs}yEs, \texttt{yes}yes and \texttt{YES}YES will all be treated as identical).

Sample Input :
823

Sample Output :
YES

"""

""" Solution : """
# cook your dish here
cred_score = int(input())
if cred_score >= 750:
    print("YES")
else:
    print("NO")
