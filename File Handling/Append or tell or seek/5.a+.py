'''
🚀 Final Mode: a+

This is the last update mode.

You already know:

a → append only
+ → read + write

So let's see if you can predict a+ from your understanding.
'''

file = open("File Handling\Append or tell or seek\samplew+a+.txt", "a+")

file.write(" AI") # adds the text at the end of the line.

file.seek(0)  # moves the cursor to the 0 index 

print(file.read()) # reads the file from where the cursor placed.

file.close() # closes the file