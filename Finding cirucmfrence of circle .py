import math
def circumfrence(r):
    if r>=0:
        a=2*math.pi*r
        return '{:.2f}'.format(a)
    else:
        return "Error"
r=float(input())
print(circumfrence(r))
