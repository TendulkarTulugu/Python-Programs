'''
Custom exceptions
🚀 Let's start Custom Exceptions

Here's the question that leads into it.

Suppose you're writing a banking application.

balance = 500

withdraw = 1000

You can write:

raise ValueError("Insufficient Balance")

But think about it...

Is "Insufficient Balance" really a ValueError?

🤔 Not really.

It's a banking-specific error.

Wouldn't it be nice if Python allowed us to create our own exception called:

InsufficientBalanceError

instead of using ValueError?

👉 It does!

That's exactly what Custom Exceptions are for.

'''


'''
Suppose you're building an ATM application.

balance = 500
withdraw = 1000

What happens?

Obviously,

Insufficient Balance

Now tell me...

Which built-in exception should we use?

ValueError ❌
ZeroDivisionError ❌
TypeError ❌
IndexError ❌

None of them describe the actual problem.

This isn't a Python error.

It's our business rule.

Real Life Analogy

Imagine a hospital.

Python already has doctors for:

ValueError
TypeError
IndexError
KeyError
ZeroDivisionError

Now suppose a patient comes with:

Alien Virus

Does any doctor specialize in that?

❌ No.

So the hospital creates a new department.

Similarly,

Python allows us to create our own exception class.

First Custom Exception
class InsufficientBalanceError(Exception):
    pass

Don't worry about the syntax.

Let's understand it word by word.
'''

# wait to understand this we need to complete OOP so we'll complete it later.

