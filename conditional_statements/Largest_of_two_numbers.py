# Problem 8 — Largest of Two Numbers
# Take two numbers from the user and print the larger number.

n1=int(input('Enter your 1st number:'))
n2=int(input('Enter your 2nd number:'))
if n1>n2:
    print('n1 is larger')
else:
    print('n2 is larger')
    
# comparing numbers

# if a=10 & b=10 then it shows b is larger, so we need to change the case using elif

if n1>n2:
    print('n1 is larger')
elif n1<n2:
    print('n2 is larger')
else:
    print('both are equal')