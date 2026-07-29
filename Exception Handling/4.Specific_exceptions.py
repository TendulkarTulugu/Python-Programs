'''
Until now, we've been using:

except:

This means:

"Catch any exception."

Sometimes that's okay.

But professional programmers usually ask:

"Which exception occurred?"

Why do we need specific exceptions?

Consider this program.

try:
    num = int(input("Enter a number: "))
    print(100 / num)

except:
    print("Something went wrong")
Case 1

Input:

abc

Output:

Something went wrong
Case 2

Input:

0

Output:

Something went wrong
Question

Did the same problem occur in both cases?

❌ No.

Case 1
int("abc")

Python cannot convert "abc" to an integer.

Exception:

ValueError
Case 2
100 / 0

Python cannot divide by zero.

Exception:

ZeroDivisionError

But our program tells the user the same thing.

Something went wrong

That's not very helpful.

Python's Solution

Instead of writing:

except:

Python allows us to specify which exception we want to handle.

Example:
'''

try:
    num = int(input("Enter Number: "))
    print(100 / num)

except ValueError:
    print("Please enter only numbers.")

except ZeroDivisionError:
    print("Number cannot be zero.")


'''
Look carefully.

We now have two different except blocks.

Each one handles a different exception.
'''


'''
Real-time example:


Think of it Like a Hospital 🏥

Imagine a hospital.

Patients arrive with different problems.

Patient 1

Broken leg.

Does he go to a dentist?

❌ No.

Patient 2

Tooth pain.

Does he go to an orthopedic doctor?

❌ No.

Every doctor has a specialty.

Python works exactly the same way.

'''



try:
    num = int(input("Enter Number: "))
    print(50 / num)

except ValueError:
    print("Value Error")

except ZeroDivisionError:
    print("Zero Error")

print("Program End")


'''
Types of error

int("abc")      # ValueError
10 / 0          # ZeroDivisionError
my_list[10]     # IndexError
my_dict["age"]  # KeyError

'''
