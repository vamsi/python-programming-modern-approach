s = "hello"
print(s.capitalize())  # Capitalize a string prints, "Hello"
print(s.upper())       # Convert a string to uppercase, prints "HELLO"
print(s.rjust(7))
# Right-justify a string, padding with spaces; prints "  hello"
print(s.center(7))
# Center a string, padding with spaces; prints " hello "
print(s.replace('l', '(ell)'))
# Replace all instances of one substring with another.
# prints "he(ell)(ell)o"
print('  world '.strip())
# Strip leading and trailing whitespace; prints "world"

"""
Output
Hello
HELLO
  hello
 hello 
he(ell)(ell)o
world
"""