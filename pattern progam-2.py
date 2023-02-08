"""Generate a half pyramid pattern using numbers.

Input Description:
Given an integer R indicates number of rows.

Where 1<=R<=100.

Output Description:
Print the half pyramid pattern based on the given integer R.

Sample Input :
5
Sample Output :
1
12
123
1234
12345
"""
r=int(input())
if 1<=r<=100:
    for i in range(1,r+1):
        for j in range(1,i+1):
            print(j,end='')
        print()
        
        
