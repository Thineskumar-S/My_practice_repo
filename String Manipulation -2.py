string=input()
vow="aeiouAEIOU"
vow_list=[i for i in vow]
yes=[]
for i in string:
    if i in vow_list:
        yes.append("True")
if len(yes)==0:
    print("no")
else:
    print('yes')
    '''
    Given a string S, print 'yes' if it has a vowel in it else print 'no'.
Sample Testcase :
INPUT
codekata
OUTPUT
yes


    '''
