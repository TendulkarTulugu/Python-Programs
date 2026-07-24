'''
Topic 1: with open(...) as file

This is the professional and most commonly used way to work with files.

Until now we've written:

file = open("sample.txt")

content = file.read()

file.close()

It works perfectly.

But there's one problem.

🤔 Think about this

Suppose we write:

file = open("sample.txt")

print(file.read())

10 / 0

file.close()
Question

What happens here?

Notice carefully:

10 / 0

comes before

file.close()

Think about it.
'''
