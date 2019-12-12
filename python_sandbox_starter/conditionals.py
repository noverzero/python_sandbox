# If/ Else conditions are used to decide to do something based on something being true or false

x = 15
y = 15

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
# Simple if
if x > y:
    print('x is greater than y')

# if else

if x > y:
    print('x is greater than y')
else: print ('x is not greater than y')

# else if

if x > y:
    print('x is greater than y')
elif x == y:
    print('x is equal to y')
else: print ('y is  greater than x')

# nested if statements
if x > 2:
    if x <= 15:
        print('x is greater than 2 and less than or equal to 15')

# Logical operators (and, or, not) - Used to combine conditional statements

if x > 2 and x <= 15:
    print('x is greater than 2 and less than or equal to 15 again!')

if x > 15 or x == 15:
    print('x is greater than 15 or equal to 15')

# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5,6,7]
if x not in numbers:
    print('x is not in numbers')

numbers.append(15)

if x in numbers:
    print('x is in numbers')



# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
  