# Problem 10 — Largest of Three Numbers
# Take 3 numbers from the user and print the largest number.


n1=int(input('1st num:'))
n2=int(input('2nd num:'))
n3=int(input('3rd num:'))

if n1>n2 and n1>n3:
    print('n1 is larger')
elif n2>n1 and n2>n3:
    print('n2 is larger')
elif n3>n1 and n3>n2:
    print('n3 is larger')
else:
    print('all are equal')
    
# max function
    
# we can do this using a built-in-function called 'max()'

print(max(n1,n2,n3))