'''
In Python, the dictionary.pop(key, default) method removes a specified key from a dictionary 
and returns its associated value. It modifies the original dictionary in place.

Syntax

pythonvalue = dictionary.pop(key, default)
Use code with caution.How Parameters Behavekey: 
The specific key you want to remove and retrieve. 
This argument is required.default: An optional fallback value. 
It prevents errors if the key does not exist.Behavior and 

OutcomesKey exists: The method removes the key-value pair and returns the value.
Key missing (with default): The method leaves the dictionary untouched and returns 
the default value.Key missing (no default): The method raises a KeyError exception.
'''


student = {
    "name": "Tendul",
    "age": 23,
    "branch": "AI & DS"
}

print(student)

student.pop("age")

print(student)



'''
🎯 Your Turn

Create this dictionary:

student = {
    "name": "Tendul",
    "age": 23,
    "branch": "AI & DS",
    "cgpa": 8.04
}

Now:

Remove "cgpa" using pop().
Print the dictionary.
'''
students={
    'name':'Tendulkar',
    'age':22,
    'branch':'AI & ML',
    'cgpa':8.04
}

print(students)
students.pop('cgpa')
print(students)