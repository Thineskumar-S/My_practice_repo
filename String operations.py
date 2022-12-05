 """You are given a string. You have to print “Wonder” if the string is wonderful and -1 if it is not. A wonderful string is a string,which is made up of exactly 3 different characters.

Input Description:
You are given a string

Output Description:
Print “Wonder” if it is wonderful and -1 if it is not

Sample Input :
aabbcc
Sample Output :
Wonder
"""
  string=input()
lis=[]
lis1=[]
for a in string:
    lis.append(a)
for l in lis:
    m=lis.count(l)
    lis1.append(m)
dic=dict(zip(lis,lis1))

if len(dic.keys())==3:
        print('Wonder')
else:
    print(-1)
   
