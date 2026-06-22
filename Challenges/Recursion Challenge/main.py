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

"""
Goal: Turn a string backward by taking the first letter and gluing it to the end of the rest of the reversed
"""
def reverse(a):
    if len(str(a)) == 1:
        return a
    b = a[:-1] 
    ans = a[-1] + reverse(b)
    return ans
print(reverse("Param"))

"""
Goal: Determine if a word reads the same backward and forward.
"""
def is_palindrome_V1(a):
    a == str(a)
    if  a == len(a):
        return True
    if reverse(a) == a:
        return True
    else :
        return False
def is_palindrome_V2(a):
    a == str(a)
    if  1 == len(a) or 0 == len(a):
        return True
    b = a[1:-1]
    if a[0] == a[-1] and is_palindrome_V2(b):
        return True
    else:
        return False

"""
Goal: Count how many times a target item appears in an array.
"""

"""
Goal: Find the n-th Fibonacci number, where each number is the sum of the two preceding ones.
"""
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1) + fib(n-2)

"""
Goal: You are climbing a staircase with n steps. You can climb 1 or 2 steps at a time. In how many distinct ways can you climb to the top?
"""
def stairs(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return stairs(n-1) + stairs(n-2)
print(stairs(40))