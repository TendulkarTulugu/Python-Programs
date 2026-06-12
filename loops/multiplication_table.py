# we all studied the table that is 2 x 1 = 2 ...... 2 x 10 = 20

# now we are going to print the multiplication table for the user input

n=int(input())
for i in range(1,11):
    print(n,'x',i,'=',n*i)
    
    # using string interpolation
    print(f'{n} x {i} = {n*i}')
