"""
Goal: Multiply all numbers from n down to 1. ( Factorial {!} )
"""
def factorial(n):
    if n==1 or n==0:
        return  1
    return n * factorial(n-1)

"""
Goal: Take an integer and add its digits together using % 10 and // 10
"""
def sum_digits(n):
    if len(str(n)) == 1:
        return n
    a = n % 10
    return a + sum_digits(n//10)

"""
Goal: Compute x^nwithout using loops or **.
"""
def power(a, b):
    if b == 1:
        return a
    if  b == 0:
        return 1  
    return a*power(a,b-1)
print(power(2,0))