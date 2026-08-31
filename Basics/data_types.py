# int

k=42
print(k)
print(type(k))

big=1_00_00_000    # _ are used for readability purpose.
print(big)
print(type(big))

# for negative values

neg=-17
print(neg)
print(type(neg))      # since it's a negative value still it's an integer

# for binary numbers

bin=0b1010
print(bin)
print(type(bin))




# for octal values

oct=0o17
print(oct)
print(type(oct))


# for hex decimal valus

hex=0xFF
print(hex)
print(type(hex))





#==========================================================================================================================================

# Float

pi=3.14
print(pi)

avogadro=6.022e23
print(avogadro)
print(type(avogadro))

tiny=1.5e-10
print(tiny)
print(type(tiny))


#==========================================================================================================================================

# Boolean

# Boolean

a=True #1
b=False #0
print(type(a))
print(a)
print(type(b))
print(b)

print(a+5)

print(bool(0))

print(bool(""))
print(bool(None))
print(bool(False))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool('Hello'))
print(bool(1))
print(bool(-1))



#==========================================================================================================================

# String

# single quotes
a1='Hello'

# double quotes
a2="Tendul"

# triple single quotes for multiple lines or paras
a3=''' Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:

web development (server-side),
software development,
mathematics,
system scripting.
What can Python do?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.'''



# triple double quotes for multiple lines or paragraph
a4="""Why Python?
Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
Python has a simple syntax similar to the English language.
Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
Python can be treated in a procedural way, an object-oriented way or a functional way.
Good to know
The most recent major version of Python is Python 3, which we shall be using in this tutorial.
In this tutorial Python will be written in a text editor. It is possible to write Python in an Integrated Development Environment, such as Thonny,
Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files."""

print(type(a1))
print(a1)
print(type(a2))
print(a2)
print(type(a3))
print(a3)
print(type(a4))
print(a4)




























