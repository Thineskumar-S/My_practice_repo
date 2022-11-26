import math
def eq_triangle_area(a):
    Area=1/4*(math.sqrt(3))*a*a
    Area="{:.2f}".format(Area)
    return Area

a=int(input())
print(eq_triangle_area(a))
