r=int(input())
if 1<=r<=100:
    for i in range(r,0,-1):
        for j in range(1,i+1):
            print(j,end='')
        print()
        
        
"""
Write a code to generate a half pyramid pattern using numbers.

Input Description:
Given an integer R indicates number of rows.

Where 1<=R<=100.

Output Description:
Print the number half pyramid pattern with the size R.

Sample Input :
5
Sample Output :
1
22
333
4444
55555
"""
