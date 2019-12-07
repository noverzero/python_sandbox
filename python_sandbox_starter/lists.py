# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
numbers = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'grapes', 'pears']

# use a constructor
numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2)

# get a single value
print(fruits[1])

#length of array
print(len(fruits))

#append to the end
fruits.append('Mangoes'.lower())
print('append', fruits)

#remove maching item
fruits.remove('grapes')
print('remove', fruits)

#insert into a specific index
fruits.insert(2, 'strawberries')
print('insert', fruits)

#remove by position (pop method)
fruits.pop(2)
print('pop', fruits)

#reverse list
fruits.reverse()
print('reverse', fruits)

#sort (alphabetical)
fruits.sort()
print('sort', fruits)


#reverse Sort
fruits.sort(reverse = True)
print('reverse sort', fruits)

#change value
fruits[0] = 'monkeys'
print('change value', fruits)

