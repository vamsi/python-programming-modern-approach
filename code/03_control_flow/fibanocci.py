"""
def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)
"""
a, b = 1, 1
total = 0
while a <= 4000000:
    if a % 2 == 0:
        total += a
    a, b = b, a + b  # the real formula for Fibonacci sequence
print(total)
