# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

#Create a function 
#pass in a default value by setting name = to "World"

def sayHello(name = "World"):
    print(f"Hello, {name}")

sayHello('Dustin Huth')

#Return Values

def getSum(num1, num2):
    total = num1 + num2
    return total

print('getSum(4, 3): ', getSum(4, 3))



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2
print('lambda getSum(10, 3): ', getSum(10, 3))
