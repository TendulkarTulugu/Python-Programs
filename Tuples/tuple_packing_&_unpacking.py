'''
Tuple packing: 

When you assign multiple comma-separated values to a single variable, 
Python implicitly packs them into a single tuple—even without parentheses.



2. Sequence Unpacking:
You can extract values from any iterable directly into multiple variables. 
The number of variables on the left must match the number of elements in the collection.



3. Extended Unpacking with * :
If you want to extract specific elements and capture the rest, use the asterisk (*) operator. 
Python will bundle all remaining values into a list.

'''



# Packing values into a single tuple
coordinates = 40.7128, -74.0060  
print(coordinates)  # Output: (40.7128, -74.0060)


# tuple unpacking

student=('Tendul',22,'AI & DS')

name,age,branch=student

print(name)
print(age)
print(branch)


'''
🧠 Rule to Remember

Number of variables = Number of tuple elements
'''

student = ("Tendul", 23, "AI & DS", 8.04)

name, *details = student # its the additional feature in python.

# where the name carries its values the * is used for extended unpacking.
# the *details carries all the values left behind the name.

print(name)
print(details)
