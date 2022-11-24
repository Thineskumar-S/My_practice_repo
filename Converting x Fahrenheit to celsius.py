def to_celsius(fahrenheit):
    b= (fahrenheit-32) * .5556
    return "{:.2f}".format(b)
a=float(input())
print(to_celsius(a))

