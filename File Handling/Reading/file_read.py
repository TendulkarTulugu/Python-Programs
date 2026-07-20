#2

# read() 

file=open(r"File Handling\sample.txt")
content=file.read()
print(content)
print(type(content))
file.close()

print('---readline()---')

# readline()
#  It reads only the first line.

file = open(r"File Handling\sample.txt")
content=file.readline()
print(type(content))
file.close()

print('--------')

file = open(r"File Handling\sample.txt")
print(file.readline())
print(file.readline())
file.close()

'''

calling readline()- 2 times

Each call reads the next line.

Think of it like turning pages in a book.
'''


# readlines()

print('---readlines()---')

file = open(r"File Handling\sample.txt")

lines = file.readlines()
print(type(lines))
print(lines)

file.close()


'''
['Hello Tendul\n',
 'Welcome to Python\n',
 'Today is a good day.']
 

Notice the \n?

It represents a newline character.
 
'''

