def pyramid_on_right(rows):
    if 1<=rows <=100:
        for i in range(rows):
            for j in range(i+1):
                print("* ",end='')
            print()
rows=int(input())
a=pyramid_on_right(rows)

"""
output :
if rows was given as 5 then, 

*
**
***
****
*****
"""
