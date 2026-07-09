
#3

'''
🎯 Now the Most Powerful Part of Sets

These are used a lot in:

Data Science 📊
SQL
Database operations
Interview questions

There are 3 important operations:

1️⃣ Union (|)

Think of it as combine everything.

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)

Output:

{1, 2, 3, 4, 5}

Notice:

3 appears in both sets.
It appears only once in the result.
2️⃣ Intersection (&)

Think of it as common elements.

A = {1, 2, 3}
B = {3, 4, 5}

print(A & B)

Output:

{3}

Because 3 is common to both.

3️⃣ Difference (-)

Think of it as:

"Give me elements in A that are not in B."

A = {1, 2, 3}
B = {3, 4, 5}

print(A - B)

Output:

{1, 2}

Because:

3 is removed (it's in both).
1 and 2 remain.

'''

A = {1, 2, 3}
B = {3, 4, 5}
print(A|B)
print(A&B)
print(A - B)

'''
Real-world Examples


Imagine two cricket teams.

Team A
Virat
Rohit
Gill
Team B
Gill
Rahul
Pant

Using sets:

team_a = {"Virat", "Rohit", "Gill"}
team_b = {"Gill", "Rahul", "Pant"}


Union
Everyone:

Virat
Rohit
Gill
Rahul
Pant

Intersection
Players in both teams:

Gill

Difference
Players only in Team A:

Virat
Rohit

This is exactly why sets are useful in Data Science, SQL, and analytics. They make it easy to compare collections of values.
'''
