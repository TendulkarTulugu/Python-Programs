# Accumulation Pattern
# Sum of Numbers

# here i want to find sum of the consecutive values like i want sum of 1...5

s=0
for i in range(1,6):
    s+=i
print(s)

# this is called Accumulation Pattern----> continuously adding values into a variable.

#using a built in function

print(sum(range(1,6)))

# -------------------------------------------------------
# Sum of Even Numbers

total=0
for i in range(0,11,2):
    total+=i
print(total)



# ----------------------------------------------------------
# Sum of odd Numbers

t=0
for i in range(1,15,2):
    t+=i
print(t)