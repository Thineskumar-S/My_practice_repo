def to_farenheit(Celsius):
    b= (Celsius* 1.8) + 32
    return "{:.2f}".format(b)
Celsius =float(input())
print(to_farenheit(Celsius))
