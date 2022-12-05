"""Given a string 'S' print the sum of weight of the String. A weight of character is defined as the ASCII value of corresponding character.

Input Description:
You are given a string ‘s’

Output Description:
Print weight

Sample Input :
abc
Sample Output :
294
"""
def weighted_sum_String(string1):
    x=[]
    for l in string1:
        x.append(l)
    z=[]
    for i in x:
        y=ord(i)
        z.append(y)
    return(sum(z))

string1=input() 
print(weighted_sum_String(string1))
