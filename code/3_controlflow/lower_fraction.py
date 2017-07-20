number1 = int(input())
number2 = int(input())


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


newNumber1 = number1 / gcd(number1, number2)
newNumber2 = number2 / gcd(number1, number2)
print(number1)
print(number2)
print(newNumber1)
print(newNumber2)
