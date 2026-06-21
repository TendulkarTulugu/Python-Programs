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































# content

data="""
thon
newline = "Line1\nLine2" 
# Outputs:
# Line1
# Line2
Literal Backslash (\\): Since a single backslash means "an escape sequence is starting," 
you must use two backslashes if you want just one actual backslash to show up (like in a file path).

Python
backslash = "C:\\Users\\Alice"  # Outputs: C:\Users\Alice
Literal Quote (\"): If your string is wrapped in double quotes, you can't just drop another 
double quote inside it without confusing the code. Escaping it tells the program it's part of the text, not the end of the string.

Python
quote = "She said \"hi\""  # Outputs: She said "hi"
2. Raw Strings (r"...")
If you have a string with a lot of backslashes (like a complicated Windows file path or a 
Regular Expression pattern), typing \\ every single time gets annoying.

Putting an r right before the opening quote tells the language to treat backslashes as
completely literal characters, ignoring any escape sequences.

(Note: There was a small typo in your snippet's variable syntax. Here is how 
they look fixed up):

Python
# The 'r' tells Python to ignore the backslashes inside
path = r"C:\Users\Alice\Documents" 

# Highly useful for regex patterns where backslashes are common
x = r"\d+\.\d+" 
3. String Functions & Operators
len() Function: Returns the total count of characters in a string (including spaces and punctuation).

Python
print(len("Hello"))  # Outputs: 5
Repetition (*): When you "multiply" a string by a number, it repeats that string that many times.

Python
print("Py" * 3)  # Outputs: PyPyPy
Concatenation (+): When you "add" two strings together, it glues them end-to-end into a single string.

Python
print("Py" + "thon")  # Outputs: Python

"""



#




