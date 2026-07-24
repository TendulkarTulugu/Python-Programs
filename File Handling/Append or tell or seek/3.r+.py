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

file = open("File Handling\Append or tell or seek\sampler+.txt", "r+")

print(file.read())

file.write(" AI")

file.close()


'''
here is the most important point.

r+ does not always add.

It writes wherever the cursor is currently positioned.
Remember:

The cursor starts at the beginning in "r+".
write() overwrites existing characters from the current cursor position.
It does not insert characters and shift everything to the right.
'''

file = open("File Handling\Append or tell or seek\sampler+.txt", "r+")
file.write('HI')
file.close()


'''
⭐ Important Rule

write() does not insert characters.

It overwrites characters starting from the current cursor position.
'''

