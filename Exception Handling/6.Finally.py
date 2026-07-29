'''
⭐ What is finally?

The finally block executes whether an exception occurs or not.

Think of it as:

"No matter what happens, execute this block before leaving the try-except statement."

Easy Analogy 🎓

Imagine you're writing an exam.

Enter Exam Hall
      │
      ▼
Write Exam (try)
      │
      ▼
Did something go wrong?
   │          │
  Yes        No
   │          │
except     continue
      \     /
       \   /
      finally
         │
         ▼
Leave Hall

Whether your exam went well or badly, you must leave the exam hall.

That's what finally is for.

Common Real-World Uses

Suppose you open a file:

file = open("data.txt")

After using it, you must close it.

Even if an exception occurs, the file should still be closed.

That's why finally is commonly used for:

Closing files
Closing database connections
Releasing network connections
Cleaning up resources
'''


try:
    print("Start")
    print(10 / 0)

except:
    print("Handled")

finally:
    print("Finally")

print("End")



'''
🎯 The Golden Rule of finally

Memorize this one sentence:

A finally block executes whether an exception occurs or not.

Or in simple words:

✅ Exception? → finally executes.
✅ No exception? → finally executes.
✅ Exception handled? → finally executes.

That's why it's called finally—it's the last thing Python does before leaving the try-except-finally structure.
'''


try:
    print("A")
    return_value = 10

finally:
    print("Finally")

print("End")


print('-------')

def demo():
    try:
        print("A")
        return 10

    finally:
        print("Finally")

print(demo())

'''
Many people think:

"As soon as return is executed, the function ends."

❌ Not yet!

Before the function actually returns, Python asks:

"Is there a finally block?"

✅ Yes.

So Python pauses the return, executes the finally block, and only then returns the value.
'''


def demo():
    try:
        print("A")
        return 10

    finally:
        print("Finally")
        return 20

print(demo())

'''

return 20

This is the important part.

The return 20 inside the finally block overrides the earlier return 10.

So the pending return 10 is discarded.

The function finally returns:

20
'''



'''
⭐ Golden Rule

If both try and finally contain a return statement:

The return in the finally block wins.

The same idea applies if finally raises an exception—it can also override an earlier pending return or exception.
'''

