
'''
🚀 Next: Methods

We've learned how an object stores data.

But objects should also be able to do things.

Think about a student:

Student
├── name
├── age
├── course
│
└── Behaviors
    ├── study()
    ├── attend_class()
    └── introduce()

The data is called attributes.

The actions/functions belonging to an object are called methods.

For example:

class Student:


    def __init__(self, name):
        self.name = name


    def introduce(self):
        print("Hello, I am", self.name)

Then:

rahul = Student("Rahul")
rahul.introduce()

The interesting part is:

self.name

inside introduce().

You already understand self, so this should be much easier.
'''




