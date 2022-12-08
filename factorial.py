def factorial(n):
    if n>=1:
        if n==1:
            return 1
    return n*factorial(n-1)
n=int(input())
print(factorial(n))
"""
You are provided with a number, "N". Find its factorial.

Input Description:
A positive integer is provided as an input.

Output Description:
Print the factorial of the integer.

Sample Input :
2
Sample Output :
2
"""
