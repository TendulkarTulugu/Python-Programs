#4 

# write a program to print the output exactly like this using loops

# name : Tendul
# age : 23
# branch : AI & DS
# cgpa : 8.04


student = {
    "name": "Tendul",
    "age": 23,
    "branch": "AI & DS",
    "cgpa": 8.04
}

for key in student:
    print(key)              # it only prints the keys

for v in student:
    print(student[v])       # it print the values without keys

for d in student:
    print(d,':',student[d]) # it prints the whole dictionary i.e, key and values.

