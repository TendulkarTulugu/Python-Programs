"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

"""

for i in range(1,6):
    for j in range(5-i):
        print(' ',end='')
    for k in range(2*i-1):
        print('*',end='')
    print()
for z in range(2,6):
    for x in range(z-1):
        print(' ',end='')
    for y in range(2*(5-z)+1):
        print('*',end='')
    print()

# it prints the diamond
#----------------------------------

# here the diamond is of static number we can made dynamic as taking input and performing on that.