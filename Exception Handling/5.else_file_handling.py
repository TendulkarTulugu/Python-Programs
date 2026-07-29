'''
Now comes one of the most misunderstood keywords:

else

Many beginners think:

"else runs when an exception occurs."

❌ That's wrong.

The else block runs only if NO exception occurs in the try block.

Syntax
try:
    # Risky code

except:
    # Executes if an exception occurs

else:
    # Executes only if NO exception occurs

Think of it like an exam.

Take Exam
    │
    ▼
Passed?
   │
 Yes ─────► else 🎉
   │
 No
   ▼
except 🚑

example 1:

'''

try:
    print("A")
    print(10 / 2)

except:
    print("Error")

else:
    print("Success")

print("End")



'''
⭐ Golden Rule of else

else executes only when the try block completes successfully without any exception.

You can think of it like this:

            try
             │
     Exception?
      /      \
    Yes       No
     │         │
 except      else
     \         /
      \       /
       Continue
'''


try:
    print("Start")
    print(10 / 0)

except:
    print("Handled")

else:
    print("Success")

print("End")


