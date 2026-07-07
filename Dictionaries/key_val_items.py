#6

student = {
    "name": "Tendul",
    "age": 23,
    "branch": "AI & DS"
}

print(student.keys())
# it'll give all the keys of dict

print(student.values())
#it'll give all the values of dict

print(student.items())
# it 'll give all items. Each item is a (key, value) pair.

for key in student:
    print(key,':',student[key])
# it give the dict key:values

for key,value in student.items():
    print(key,':',value)

# But items() lets us get both the key and value directly.