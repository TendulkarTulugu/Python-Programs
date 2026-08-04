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
