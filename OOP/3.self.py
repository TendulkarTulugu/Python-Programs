'''
🚀 Now comes the topic that confuses 90% of beginners...
self

Look at this code:

class Student:

    def __init__(self):
        print("Constructor")
Question

Why did Python write:

def __init__(self):

instead of:

def __init__():

🤔

What do you think self might represent?

'''





'''
Imagine this:

class Student:

    def __init__(self):
        print("Constructor")

Now we create:

rahul = Student()
priya = Student()
amit = Student()

We now have:

Student Class

        │
        ├── rahul
        ├── priya
        └── amit
Here's the question.

When Python calls:

__init__()

Which object's constructor is it calling?

Rahul's?
Priya's?
Amit's?

🤔

Python needs some way to know:

"I'm currently working with Rahul."

or

"I'm currently working with Priya."

or

"I'm currently working with Amit."


How can Python know which object it's currently initializing?

Think of a classroom.

Suppose I'm a teacher.

I say:

"Come here."

Who should come?

Rahul?
Priya?
Amit?

Nobody knows.

Now I say:

"Rahul, come here."

Now it's clear.

Similarly, when Python is inside __init__, it needs to know:

Which object am I working with right now?

That is the job of self.
'''

# Look at this code:

class Student:

    def __init__(self):
        print(self)

rahul = Student()
priya = Student()

'''
Questions
Will self print the same thing for Rahul and Priya?
Or different things?
Why do you think that?
'''

# Different because the objects are different and stored at different locations.

'''
Step 1

Python creates:

rahul

at memory:

0xA123

Then Python automatically calls:

__init__(?)

Question:

What should Python pass?

It passes:

__init__(rahul)

So inside the constructor,

print(self)

prints:

<__main__.Student object at 0xA123>

Step 2

Now Python creates:

priya

at memory:

0xB456

Then Python automatically calls:

__init__(priya)

Now,

print(self)

prints:

<__main__.Student object at 0xB456>


Notice something amazing.

We never wrote:

__init__(rahul)

or

__init__(priya)

Python did it automatically.

🎯 So what is self?

Now you're ready for the real definition.

----------------------------------------------------------
# # # self is a reference to the current object.
----------------------------------------------------------
That's it.

If Rahul is being initialized:

self → rahul

If Priya is being initialized:

self → priya

If Amit is being initialized:

self → amit

So self changes depending on which object is currently using the class.

Visualize it
Student Class

       │
       ├───────────────┐
       │               │
    rahul           priya
  (0xA123)        (0xB456)

self = rahul      self = priya

The class is one.

The objects are many.

self simply points to the object that is currently executing the method.

⭐ Here's something important.

Many beginners think:

self

is a Python keyword.

❌ It is not.

You could technically write:

class Student:

    def __init__(abc):
        print(abc)

and it would still work.

But nobody does that.

The Python community follows the convention of always naming it self.
'''


class Student:

    def __init__(self):
        print("self =", self)

rahul = Student()
print("rahul =", rahul)

# # output

# self = <__main__.Student object at 0x0000020CCC136CF0>
# rahul = <__main__.Student object at 0x0000020CCC136CF0>


'''
Notice something?

The memory addresses are identical.

That proves:

self and rahul refer to the same object.
'''




'''
Many beginners think:

self

is another object.

❌ It is not.

It's simply another reference (another name) for the same object.

Think of it like this:

           Student Object
          (Memory: 0xA123)
              ▲       ▲
              │       │
           rahul    self

Both arrows point to the same object.

🚀 Now comes the most important line in OOP

Until now, we've had empty objects.

Now we'll finally store data inside them.

You'll see this line:

self.name = name

This line confuses almost every beginner.

But because you've understood self, it'll make perfect sense.

We'll learn:

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

And you'll understand:

Why are there two names?
Why self.name?
What is the difference between name and self.name?

These are the questions that unlock the rest of OOP.
'''




'''
Visualize it
Object Created        self refers to

rahul  ----------->   self = rahul

priya  ----------->   self = priya

amit   ----------->   self = amit

Notice something?

👉 self changes.

The constructor (__init__) is always the same.

The object changes.

So self changes.

Think of it like a teacher.

There is one teacher (the constructor).

Students come one by one.

Teacher: "Next student!"

Rahul comes.
Teacher talks to Rahul.

↓

Priya comes.
Teacher talks to Priya.

↓

Amit comes.
Teacher talks to Amit.

The teacher doesn't change.

The student changes.

self is like "the student currently standing in front of the teacher."

'''




'''
Visual Representation
                Student Class
                     │
                     │
         __init__(self)
                     │
     ┌───────────────┼───────────────┐
     │               │               │
  rahul          priya           amit
     │               │               │
self = rahul    self = priya    self = amit

One class.

Many objects.

self always points to the object currently using the class.

🚀 NOW...

We're finally ready for the line that confuses almost everyone.

self.name = name

Don't panic.

We'll break it into two parts.

Part 1
name

Where does this name come from?

Look carefully.

rahul = Student("Rahul", 20, "Python")

Python automatically calls:

__init__(rahul, "Rahul", 20, "Python")

So inside the constructor:

name = "Rahul"
age = 20
course = "Python"

These are temporary variables (parameters).

Part 2
self.name

Remember:

For Rahul,

self = rahul

So this becomes:

rahul.name

Python creates a new attribute called name inside the Rahul object.

Then:

self.name = name

becomes:

rahul.name = "Rahul"
Let's trace it.
class Student:

    def __init__(self, name):
        self.name = name

rahul = Student("Rahul")
Step 1

Python creates the object:

rahul
Step 2

Python automatically calls:

__init__(rahul, "Rahul")

Now inside the constructor:

self = rahul
name = "Rahul"
Step 3

Python executes:

self.name = name

Substitute the values:

rahul.name = "Rahul"

Now the object becomes:

rahul
└── name → Rahul

🎉 That's it!

⭐ Golden Rule

The right side:

name

is the parameter (temporary value received by the constructor).

The left side:

self.name

is the attribute stored permanently inside the object.

Think of it as:

Temporary value
      │
      ▼
name = "Rahul"
      │
      ▼
Stored permanently
      │
      ▼
self.name
'''



# class Student:

#     def __init__(self, name):
#         self.name = name
#         print("Inside:", name)

# rahul = Student("Rahul")

# print("Outside:", rahul.name)
# # print(name)




