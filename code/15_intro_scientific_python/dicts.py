d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data

print(d['cat'])       # Get an entry from a dictionary; prints "cute"

print('cat' in d)    # Check if a dictionary has a given key;prints "True"

d['fish'] = 'wet'    # Set an entry in a dictionary
print(d['fish'])     # Prints "wet"

# print(d['monkey'])  # KeyError: 'monkey' not a key of d

print(d.get('monkey', 'N/A'))  # Get an element with a default; prints "N/A"

print(d.get('fish', 'N/A'))    # Get an element with a default; prints "wet"

del d['fish']        # Remove an element from a dictionary

print(d.get('fish', 'N/A'))  # "fish" is no longer a key; prints "N/A"

"""
Output
cute
True
wet
N/A
wet
N/A
"""
