# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Dustin'
age = 40

# String Formatting

# Concatenating
print('Hello. My name is, ' + name + '. I am ' + str(age) + ' years old!')

#Arguments by position
print('My name is, {name}.  I am {age} years old.'.format(name= name, age=age))

#F-Strings (Python 3.6^)
print(f"My name is, {name}. I'm {age} years of age")

# String Methods

s = 'hello world'.upper()
print(s.capitalize())
print(s)

