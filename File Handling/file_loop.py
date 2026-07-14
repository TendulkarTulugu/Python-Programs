# 3


'''
Python reads one line at a time.

This is memory-efficient and is commonly used for large files.
'''

# file = open(r"File Handling\sample.txt")
# for line in file:
#     print(line)
# file.close()



'''
🎯 Practice Questions

Question 1

Using readline():

Print only the second line from sample.txt.

Question 2

Using readlines():

Print only the last line of the file.

Question 3

Using a loop:

Print the file like this:

'''

file = open(r"File Handling\sample.txt")
lines=file.readlines()
print(lines[1])



'''
"strip is used to remove spaces."

That's partially correct, but let's make it more accurate.

strip() removes:
Leading spaces ✅
Trailing spaces ✅
Leading newlines (\n) ✅
Trailing newlines (\n) ✅
Leading tabs (\t) ✅
Trailing tabs (\t) ✅

It does not remove spaces in the middle of a string.
'''


file = open(r"File Handling\fruits.txt")

lines = file.readlines()

for line in lines:
    print(line.strip())

file.close()


# .strip() working

text = "   Hello Python   "

print(len(text))
print(text.strip())
print(len(text.strip()))


'''
Notice what strip() didn't remove.

Hello␠Python

The middle space is still there.

It only removed the spaces at the beginning and end.
'''

file=open(r"File Handling\sample.txt")
count=1
for line in file:
    if count==2:
        print(line.strip())
    count+=1

file.close()


# to print last line we can use 2 methods.


#1st

file=open(r"File Handling\sample.txt")
count=1
for line in file:
    if count==3:
        print(line.strip())
    count+=1

file.close()

#2nd method

file=open(r"File Handling\sample.txt")
last_line=''
for line in file:
    last_line=line

print(last_line)
file.close()



# printing line numbers

file = open(r"File Handling\sample.txt")

count = 1

for line in file:
    print("Line", count, ":", line.strip())
    count += 1

file.close()

