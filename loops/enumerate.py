# enumerate() gives you both index and value.

students = ["Alice", "Bob", "Clara", "Dave"]
for index, name in enumerate(students, start=1):
    print(f"{index}. {name}")

# here the names are printing with the index number.


names = ["Alice", "Bob", "Clara"]
scores = [92, 85, 78]
for name, score in zip(names, scores):
 print(f"{name}: {score}/100")
 
 # here it give like 90/100 format.