'''
🎯 Challenge 2: Add a New Key

Suppose we have:

student = {
    "name": "Tendul",
    "age": 22
}

Now add a new key:

college → JNTUK

Expected dictionary:

{
    "name": "Tendul",
    "age": 22,
    "college": "JNTUK"
}

Hint

Just like you access a key:

student["name"]

You can also create one using the same syntax.

Try it yourself and then print the whole dictionary.

'''
student={
    "name": "Tendul",
    "age": 22,
}

# adding new key
student["college"]="JNTUK"


print(student["college"])


'''
🎯 Mini Practice

Try this:

student = {
    "name": "Tendul",
    "age": 22
}

Now:

Add "branch" → "AI & DS"
Add "cgpa" → 8.04
Update "age" from 22 to 23
Print the dictionary

This exercise will teach you adding and updating in one go.
'''

student = {
    "name": "Tendul",
    "age": 22
}
student['branch']='AI & DS'
student['cgpa']=8.04
student['age']=23
print(student)

'''
🌟 Notice something?

Lists use methods like:

nums.append(10)

But dictionaries don't need append().

You simply write:

dictionary[key] = value

Python decides whether to add a new key or update an existing one.

'''

