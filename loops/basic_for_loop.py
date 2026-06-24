#print 'hello' 5 times using loop

for i in range(5):
    print('Hello')
    



# for (starting,ending)

#Starting: starting values
# ending: it excludes the upper boundary. if end is 10, it excludes 10 and takes upto 9.


# iterating over list

data=['a','b','c','d']
for d in data:
    print(d)


# iterate over string

for char in "python":
    print(char)

# it prints each letter in new line

# if we want to print in single line but iterate through each character

name="Tendulkar"
for n in name:
    print(n,end=" ")
print()

# here each character is iterating and end=" " is used to seperate each character by using space betweeen each character.

# here i want to iterate numbers from 1-5 in single line. so similarly we'll use end=" " 

for i in range(1,6):
    print(i,end=" ")
print()

