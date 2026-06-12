# Problem 11 — Simple Calculator

# Take:

# two numbers
# one operator (+, -, *, /)

# and perform the operation.

n1=int(input('enter your 1st number:'))
n2=int(input('enter your 2nd number:'))
op=input()
if op=='+':
    print(n1+n2)
elif op=='-':
    print(n1-n2)
elif op=='*':
    print(n1*n2)
elif op=='/':
    if n2!=0:
        print(n1/n2)
    else:
        print('cannot divide')
else:
    print('Invalid input')