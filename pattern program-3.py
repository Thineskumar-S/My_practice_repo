"""Write a code to generate a half pyramid number pattern.

Input Description:
Given an even integer R indicates number of rows.

Where 1<=R<=100

Output Description:
Print the number pattern based on the given integer R.

Sample Input :
5
Sample Output :
12345
1234
123
12
1
"""
r=int(input())
if 1<=r<=100:
    for i in range(r,0,-1):
        for j in range(1,i+1):
            print(j,end='')
        print()
