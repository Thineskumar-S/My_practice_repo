def is_leap(year):
    if 1900<= year<10**5:
        a=year%4==0
        b=year%100==0 
        c=year%400==0
        if a and b and c:
            return True
        else:
            leap = False
    return leap

year = int(input())
print(is_leap(year))
#logic is, a leap year can be divible by 4,100, 200 and whose reminder is 0
