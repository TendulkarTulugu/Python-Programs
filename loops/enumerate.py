# enumerate() gives you both index and value.

students = ["Alice", "Bob", "Clara", "Dave"]
for index, name in enumerate(students, start=1):
    print(f"{index}. {name}")

# here the names are printing with the index number.

#