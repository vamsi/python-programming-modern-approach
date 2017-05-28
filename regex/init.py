import re
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
# re.sub(pat, replacement, str) -- returns new string with all replacements,
# \1 is group(1), \2 group(2) in the replacement
print(re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))
# purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher
