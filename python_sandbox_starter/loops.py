# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
people = ['Tom', 'Susan', 'Dustin', 'Michael', 'Sara']

# simple for loop (for in loop)
for person in people:
    print(f'current person {person}' )

# Break

for person in people:
    if person == 'Dustin':
        break
    print(f'current person (break) {person}' )

# Continue

for person in people:
    if person == 'Dustin':
        continue
    print(f'current person (continue) {person}' )

# range

for i in range(len(people)):
    print(f'range:: {people[i]}')

for i in range(1, 24):
    print(f'custom range {i}')

count = 0
while count <= 10:
    print(f'count :: {count}')
    count += 1


# While loops execute a set of statements as long as a condition is true.
