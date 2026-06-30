'''
until before we are printing 5x5 stars

what if  i want 

***
***
***

or

********
********
********
********
********
********
********
********

her we don't want to create function everytime.

Insted we can pass a value into the function.

Let's work on this
'''




def square(n):
    for i in range(n):
        print('*'*n)

square(5)




'''
Here n is the parameter
'''


# 1 🎯 Your First Parameter Challenge
'''
Complete this code:

def greet(name):
    print("Hello", name)

# Call the function here



Requirements:

Call it with your name.
Then call it with "Python".

Expected Output:

Hello Tendul
Hello Python

'''


def greet(name):
    print('Hello',name)

greet('Tendul')
greet('Python')


# name → Parameter (receives a value)



# "Tendul" → Argument (the value you pass)

# A simple way to remember it:

# Parameter = variable in the function definition.
# Argument = actual value when calling the function.