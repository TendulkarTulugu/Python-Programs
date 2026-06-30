'''Small Exercise (Let's combine everything)

Write a function:

It should return the larger number.

Rules
Use if-else
Use return
Don't use max()

'''

def lar(a,b):
    if a>b:
        return a
    else:
        return b

res=lar(10,20)
print(res)
res=lar(50,12)
print(res)