'''
🚀 Final Mode: a+

This is the last update mode.

You already know:

a → append only
+ → read + write

So let's see if you can predict a+ from your understanding.
'''

file = open("File Handling\Append or tell or seek\samplew+a+.txt", "a+")

file.write(" AI")

file.seek(0)

print(file.read())

file.close()