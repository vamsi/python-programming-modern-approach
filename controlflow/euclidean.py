"""
def gcd(a, b):
    '''
    Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    '''
    if b > a:
        return gcd(b, a)

    if a % b == 0:
        return b

    return gcd(b, a % b)
"""

'''
a = int(input("Enter a number:"))
b = int(input("Enter another number"))
rem = a % b
while rem!=0 :
    a = b
    b = rem
    rem = a % b
print("GCD of given numbers is :{}".format(b))
'''
a = int(input())
b = int(input())
while b:
    a, b = b, a % b
print(a)
