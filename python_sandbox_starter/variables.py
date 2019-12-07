# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
x = 1 #int
y = 2.5 #float
name = 'John' #str
is_cool = True #bool

# multiple assignments

a, b, first_name, is_smart = (1, 2.5, 'Dustin', True)

print('Hello')
print(x, y, a*b, first_name, is_smart)
print(type(x))

# casting 
x = str(x)
print(type(x))