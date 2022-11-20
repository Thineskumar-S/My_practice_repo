list1=[[1,2,3,4],[5,6,7,8,9]]

def de(n):
    for i in list1:
        for j in list1:
            j.remove(n)
n=int((input('enter a number:')))
de(n)