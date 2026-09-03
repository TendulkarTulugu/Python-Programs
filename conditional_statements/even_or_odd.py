# Problem 6 — Even or Odd
# Take a number from the user and check whether it is:
# Even
# Odd

num=int(input('enter a number:'))
if num%2==0:
    print('It is Even')
else:
    print('It is Odd')
#compressed version

print("even" if num%2==0 else "odd")

