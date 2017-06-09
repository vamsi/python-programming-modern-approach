class Greeter(object):

    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable

    # Instance method
    def greet(self, loud=False):
        if loud:
            print('HELLO, {}!'.format(self.upper()))
        else:
            print('Hello, {}'.format(self))


g = Greeter('Stark')   # Construct an instance of the Greeter class
g.greet()              # Call an instance method; prints "Hello, Fred"
g.greet(loud=True)     # Call an instance method; prints "HELLO, STARK!"
