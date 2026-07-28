'''
Question

Suppose your program has 10,000 lines.

The error occurs on line 50.

Should Python stop the remaining 9,950 lines?

Usually...

❌ No.

We want to recover.

Why Python Created try

Python gives us a protected area.
'''


'''
What does try actually mean?

When Python sees

try:

It silently says:

"I'm about to execute code that might fail."

Notice something.

It doesn't assume failure.

It simply prepares for it.
'''

'''
Example

try:
    print("Hello")

Nothing dangerous here.

It still works.

Because try doesn't create errors.

It only protects code.

'''



'''
Important Rule 1

try doesn't fix errors.

Many beginners think this.

Wrong.

It only says

"Watch this code carefully."
'''





