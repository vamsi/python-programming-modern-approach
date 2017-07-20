x = 3
print(type(x))  # Prints "<type 'int'>"
print(x)       # Prints "3"
print(x + 1)   # Addition; prints "4"
print(x - 1)   # Subtraction; prints "2"
print(x * 2)   # Multiplication; prints "6"
print(x ** 2)  # Exponentiation; prints "9"
x += 1
print(x)  # Prints "4"
x *= 2
print(x)  # Prints "8"
y = 2.5
print(type(y))  # Prints "<type 'float'>"
print(y, y + 1, y * 2, y ** 2)  # Prints "2.5 3.5 5.0 6.25"

"""
Output
<class 'int'>
3
4
2
6
9
4
8
<class 'float'>
2.5 3.5 5.0 6.25

"""
