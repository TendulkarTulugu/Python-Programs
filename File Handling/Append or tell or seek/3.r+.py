'''

Until now, we've used:

Mode	Can Read	Can Write	Deletes Existing Data
"r"	        ✅	        ❌	        ❌
"w"	        ❌	        ✅	        ✅
"a"     	❌	        ✅	        ❌

Now imagine this situation.

"I want to read a file and modify it."

Using "r" ❌ Can't write.

Using "w" ❌ Deletes everything.

Using "a" ❌ Writes only at the end.

So Python introduced another mode.

r+

'''

# file = open("File Handling\Append or tell or seek\sampler+.txt", "r+")

# print(file.read())

# file.write(" AI")

# file.close()


'''
here is the most important point.

r+ does not always add.

It writes wherever the cursor is currently positioned.
Remember:

The cursor starts at the beginning in "r+".
write() overwrites existing characters from the current cursor position.
It does not insert characters and shift everything to the right.
'''

# file = open("File Handling\Append or tell or seek\sampler+.txt", "r+")
# file.write('HI')
# file.close()


'''
⭐ Important Rule

write() does not insert characters.

It overwrites characters starting from the current cursor position.
'''

file = open("File Handling\Append or tell or seek\sampler+.txt", "r+")
file.read(3)

file.write("ABC")
file.close()


#output-- PythonABC
'''
Your file became:

PythonABC

instead of:

PytABC
Why did this happen?

This is one of those real-world details that many tutorials skip.

When a file is opened in text update mode ("r+"), after you perform a read, 
Python's text I/O buffering means you should reposition the cursor before writing.

The safe pattern is:

file = open("sampler+.txt", "r+")

file.read(3)
file.seek(file.tell())   # synchronize the stream position
file.write("ABC")

file.close()

or simply:

file.seek(3)
file.write("ABC")

Now you'll get:

PytABC
'''


'''
Why didn't my earlier example match your result?

Because I simplified the behavior to teach the cursor concept first.

In actual Python text files, switching from reading to writing in an update mode (r+, w+, a+) 
should be done with an intervening seek() (or tell() followed by seek()). Without that, 
the behavior isn't something you should rely on and can differ because of text buffering.

So your experiment revealed an important practical detail.
'''

file = open("File Handling\Append or tell or seek\sampler+.txt", "r+")

print(file.read(3))
print(file.tell())

file.seek(file.tell())
file.write("ABC")

file.close()

# output-- 
# Pyt
# 3
# in the file-- PytABC

'''
there is clear difference between the two codes and outputs because.

The answer is buffering.

When you read from a file in text mode, Python keeps an internal buffer. After a read, 
immediately writing without repositioning the file pointer is not something you should rely on.

'''

