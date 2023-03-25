string=input()
string_list=[i for i in string]
vow='aeiouAEIOU'
vow_list=[i for i in vow]
string_org=[]
for i in string_list:
    if i in vow_list:
        string_org.append('')
    else:
        string_org.append(i)
string_mod=''.join(string_org)
print(string_mod)

"""
You are given a string.Your task is to print only the consonants present in the string without affecting the sentence spacings if present. If no consonants are present print -1

Input Description:
You are given a string ‘s’.

Output Description:
Print only consonants.

Sample Input :
I am shrey 
Sample Output :
 m shry

"""
