'''
Let's recall.

"w"
✅ Creates the file if it doesn't exist.
✅ Deletes all existing content if the file exists.
✅ Can write.
❌ Cannot read.

Now Python gives us:

"w+"

Notice the +.

From r+ you already learned:

+ usually means both reading and writing.

So don't memorize. Predict.
'''



'''
Prediction Question 1 🎯

Suppose sample.txt contains:

Python Programming

Now execute:

file = open("sample.txt", "w+")

print(file.read())

file.close()
Questions
Does "w+" delete the existing file contents?
What does print(file.read()) output?
'''


'''
w+ is deletes the data in the file.


As soon as Python executes:

open("sample.txt", "w+")

the file is truncated (emptied) immediately.

So the file becomes:

(an empty file)
'''

'''
After write(), the cursor is at the end of the file. 
To read the data we just wrote, we move the cursor 
back to the beginning using seek(0) before calling read().

'''

