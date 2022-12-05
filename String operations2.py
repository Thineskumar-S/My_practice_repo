"""you are given a string made up of parenthesis only.Your task is to check whether parenthesis are balanced or not.If they are balanced print 1 else print 0

Input Description:
You are given a string ‘s’

Output Description:
Print 1 for balanced and 0 for imbalanced

Sample Input :
{({})}
Sample Output :
1
"""
string=input()
x=[]
for i in string:
    x.append(i)
n=len(x)
b1=x.count('[')
b2=x.count(']')
b3=x.count('{')
b4=x.count('}')
b5=x.count('(')
b6=x.count(')')

if b1 == b2 and b3==b4 and b5==b6:
    print(1)
else:
    print(0)
