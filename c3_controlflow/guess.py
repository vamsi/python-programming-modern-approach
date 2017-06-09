def greet(name, gender=''):
    if gender == 'm':
        print("Hello Mr. {}".format(name))
    elif gender == 'f':
        print("Hello Ms. {}".format(name))
    else:
        print("Hello {}".format(name))


# greet("Sandeep", 'm')
# greet('Latha', 'f')
# greet('Machine', '')
# greet('Machine')

def gather(name, **shekar):
    print(shekar)
