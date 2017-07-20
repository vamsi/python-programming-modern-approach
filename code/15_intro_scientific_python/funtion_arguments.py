def hello(name, loud=True):
    if loud:
        print('HELLO, {}!'.format(name.upper()))
    else:
        print('Hello, {}'.format(name))


hello('Stark')            # Prints "Hello, Stark"
hello('Bond', loud=True)  # Prints "HELLO, BOND!"
