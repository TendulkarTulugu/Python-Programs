# Next Small Loop Problem
# Count Even Numbers
# Print how many even numbers are between: 1 to 10

count=0
for i in range(1,11):
    if i%2==0:
        count+=1
print(count)

# counting number of odd numbers

total=0
for i in range(1,10):
    if i%2!=0:
        total+=1
print(total)