# the task is of about the functions

'''
🎯 Homework (5 Function Problems)

Try these without looking at today's code.

1. Sum of two numbers

Returns the sum.

2. Find the smaller number

Returns the smaller value.


3. Square of a number


4. Check palindrome number

Returns "Palindrome" or "Not Palindrome".


5. Prime number

Returns "Prime" or "Not Prime".

'''

#1 

def sum(a,b):
    return a+b

result=sum(10,20)
print(result)


#2 

def small(a,b):
    if a<b:
        return a
    else:
        return b

result=small(5,10)
print(result)

# 3 square of a number

def square(n):
    return n*n

result=square(9)
print(result)



# 4 Check the palindrome
def is_palindrome(n):
    num=0
    o=n
    while n>0:
        dig=n%10
        num=num*10+dig
        n=n//10
    if num==o:
        return 'Palindrom'
    else:
        return 'Not a Palindrome'
result=is_palindrome(323)
print(result)

#5 Prime number

def is_prime(n):
    fact=0
    for i in range(1,n+1):
        if n%i==0:
            fact+=1
    if fact==2:
        return 'Prime'
    else:
        return 'Not Prime'
    # return fact
result=is_prime(11)
print(result)
        

