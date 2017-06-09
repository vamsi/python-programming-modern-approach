hello = 'hello'   # String literals can use single quotes
world = "world"   # or double quotes; it does not matter.
print(hello)       # Prints "hello"
print(len(hello))  # Prints string length
message = hello + ' ' + world  # String concatenation
print(message)  # Prints "hello world"
message_format = '%s %s %d' % (hello, world, 12)
print(message_format)  # prints "hello world 12"

"""
Output
hello
5
hello world
hello world 12
"""
