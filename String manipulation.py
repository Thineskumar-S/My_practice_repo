string=input()
string_list=[i for i in string]
string_org=[]
for i in string_list:
    if string_list.count(i)==1:
        string_org.append(i)
string_mod=''.join(string_org)
print(string_mod)

"""
Rahul is given a task to manipulate a string, He hired you as a developer your task is to delete all the repeating characters and print the result left.

Input Description:
You are given a string ‘s’

Output Description:
Print the remaining string

Sample Input :
mississipie
Sample Output :
mpe
"""
