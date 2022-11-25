mport math
def roots_quadratic_eq(A,B,C):
    if A!=0 and B !=0 and C!=0:
        d=(B**2) -(4*A*C)
        sqrt=d**0.5
        denom=2*A
        x=(-B+sqrt)/denom
        X=round(x,2)
        y=(-B-sqrt)/denom
        Y=round(y,2)
        print(X)
        print(Y)
        return 
A=float(input())
B=float(input())
C=float(input())

print(roots_quadratic_eq(A,B,C))
