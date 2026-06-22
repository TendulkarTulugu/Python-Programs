# Python allows explicit type conversion (casting) between compatible types using built-in functions.
# Implicit conversion happens automatically in some cases.


'''
Implicit conversion happens automatically by the interpreter itself.

Explicit conversion requires manual coding using built in function

'''


print(int("100"))  # 100

print(float(1)) #1.0 

print(int(3.9)) #3 -- Truncates, not round the values

print(str(1)) # '1'

print(bool(0)) # False

print(bool('Hello')) # True

print(list("abc")) # ['a','b','c']

print(tuple([1,2,3])) #(1,2,3)

print(set([1,2,2,3])) #{1,2,3}