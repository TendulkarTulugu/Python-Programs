'''
Now comes the question you've probably been thinking about:

How does Rahul actually get the values "Rahul", 20, and "Python"?

Right now we only have:

rahul = Student()

This creates an empty object.

We'll learn the constructor (__init__), which lets us create objects like this:

rahul = Student("Rahul", 20, "Python")

and later access:

rahul.name
rahul.age
rahul.course

This is where OOP starts to become really powerful.
'''



class Student:
    pass

rahul = Student()       #creating the object.

print(rahul)   


'''
Does Python know that:

Name = Rahul
Age = 20
Course = Python
'''

# No, because we've only created an empty object. We haven't given it any data yet.


'''
We only said:

"Create one Student object."

We never said:

Name = Rahul
Age = 20
Course = Python

So Python creates something like this:

rahul
├── Name   → ❓
├── Age    → ❓
└── Course → ❓

Everything is empty because we never initialized it.

Then how do we give values?

This is exactly why Python introduced constructors.

Instead of:

rahul = Student()

we'll soon write:

rahul = Student("Rahul", 20, "Python")

Now Python immediately knows:

rahul
├── Name   → Rahul
├── Age    → 20
└── Course → Python
'''

# from now lets learn about the constructor.

'''
Imagine this situation.

Suppose I give you a blank student form.

Student Form

Name : __________

Age : __________

Course : __________

It's empty.

Now Rahul comes and fills it.

Student Form

Name : Rahul

Age : 20

Course : Python

Now Priya comes.

Student Form

Name : Priya

Age : 21

Course : Java

Notice something.

The form never changes.

Only the values change.

Now think about Python.

We have:

rahul = Student()

But we never gave Rahul's information.

Wouldn't it be better if we could write:

rahul = Student("Rahul", 20, "Python")

so that at the moment the object is created, Python also receives all the required information?

🤔

'''






'''
Think about what happens.

When Python sees:

rahul = Student("Rahul", 20, "Python")

Python thinks:

"Okay, create a new Student object."

Then:

"Now I have three pieces of information."

Name   → Rahul
Age    → 20
Course → Python

Then Python stores them inside the object.

So after creation, the object looks like:

rahul
├── Name   → Rahul
├── Age    → 20
└── Course → Python

Exactly what you said.

But here's the next question...

How does Python know that:

"Rahul"

should go into Name?

How does Python know that:

20

should go into Age?

How does Python know that:

"Python"

should go into Course?

It doesn't.

We have to teach Python.

And that's exactly what a constructor does.

Meet the Constructor
'''


class Student:

    def __init__(self, name, age, course):
        print(name)
        print(age)
        print(course)

'''
Don't panic. 😄

I'm not explaining it yet.

We're going to predict it.

'''
