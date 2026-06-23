# conditional statements are mainly for the decision making.

# If, If-Else, If-Else-If are the types


# If is executed whenever the statement or specific condition is True otherwise it exectue and doesn't print anything.

# If-Else are two seperate ones --> If executes when the specified condition is True
# Else block executes if the specified condition is false.


# if - else - if is simply 'elif' and it is used whenever there are multiple conditions are there.

# let's see each one seperately


# Let's see 'IF' here


age=20

if age>=18:
    print('major')

# here the condition is True so it prints Major if the age is lesser then the code executes but returns nothing.


#If-Else

n=100

if n==10:
    print('n is 10')
else:
    print('n is not 10')

# here the condition checks that n is equal to 100 or not.
# The if block is not executed bcz the condition is not true. 
# so, the else block is executed



#if-else-if  --> Simply, elif

# The elif is used wherever there are multiple conditions are there.

# if only one condition-> if
# if more than 1  conditions -> elif

# the remain block -> else

a=25
if a==35:
    print('a is 25')
elif a==30:
    print('a is 30')
elif a==35:
    print('a is 35')
else:
    print('a is not 30,25 or 35')