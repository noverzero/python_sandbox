# Python has functions for creating, reading, updating, and deleting files.

# open a file

my_file = open('myfile.txt', 'w')

#get some info on the file

print('Name: ', my_file.name)
print('is_closed: ', my_file.closed)
print('opening mode: ', my_file.mode)

#write to file
my_file.write('I love Python!')
my_file.close()

#append to a file

my_file = open('myfile.txt', 'a')
my_file.write('  I also like JavaScript')
my_file.close()

#read from a file
my_file = open('myfile.txt', 'r+')
text= my_file.read(100)
print(text)
