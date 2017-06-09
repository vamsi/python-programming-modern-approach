nums = [3, 1, 2]   # Create a list
print(nums, nums[2])  # Prints "[3, 1, 2] 2"
print(nums[-1])   # Negative indices count from the end of the list prints "2"
nums[2] = 'foo'    # Lists can contain elements of different types
print(nums)        # Prints "[3, 1, 'foo']"
nums.append('bar')  # Add a new element to the end of the list
print(nums)        # Prints "[3, 1, 'foo', 'bar']"
x = nums.pop()     # Remove and return the last element of the list
print(x, nums)     # Prints "bar [3, 1, 'foo']"

"""
Output
[3, 1, 2] 2
2
[3, 1, 'foo']
[3, 1, 'foo', 'bar']
bar [3, 1, 'foo']
"""
