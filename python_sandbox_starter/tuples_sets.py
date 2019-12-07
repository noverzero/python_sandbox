# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#create a tuple literal
fruits = ('apples', 'oranges', 'grapes')

#create a tuple using a contsructor
fruits2 = tuple(('apples', 'oranges', 'grapes'))
 
print('fruits: ', fruits, 'fruits2: ', fruits2)

#tuple with only 1 value needs a trailing comma to be interpreted as a tuple

fruits3 = ('apples',)
print('trailing comma for single item: ', fruits3, 'type', type(fruits3))

#get value
print('get value by index [0]', fruits[0])

#replace value at index doesn't work because tuples are immutable
#fruits[0] = 'Cherries'
#print('immutable (expect error:)', fruits)

#delete

del fruits2
#print('delete: ', fruits2)

#length
print('len', len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.
