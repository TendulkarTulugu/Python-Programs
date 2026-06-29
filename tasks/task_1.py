# Pyramid
# Reverse Pyramid
# Diamond
# 12345 pattern
# 54321 pattern
# ABCDE pattern
# EDCBA pattern
# 1 / 23 / 456 / 78910 pattern


# 1 pyramid

#     *
#    ***
#   *****
#  *******
# *********



for i in range(1,6):
    for j in range(5-i):
        print(' ',end='')
    for k in range(2*i-1):
        print('*',end='')
    print()

print('------------------')

#2 reverse pyramid

for i in range(1,6):
    for j in range(i-1):
        print(' ',end='')
    for k in range(2*(5-i)+1):
        print('*',end='')
    print()
print('-------------')

#3 Diamond

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



print('---------------------------------')



# 4 Number pattern

# 1
# 12
# 123
# 1234
# 12345


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()    

print('--------------------')

# 5 Reverse number patterns

# 1
# 21
# 321
# 4321
# 54321


for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end='')
    print()

print('-----------------')

#6 Alphabet patterns

# A
# AB
# ABC
# ABCD
# ABCDE

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end='')
    print()
print('----------------------------')


# 7 Reverse alphabet

# E
# ED
# EDC
# EDCB
# EDCBA

for i in range(69,64,-1):
    for j in range(69,i-1,-1):
        print(chr(j),end='')
    print()
print('---------------')

# 8  continous number pattern

# 1
# 23
# 456
# 78910

n=1
for i in range(1,5):
    for j in range(i):
        print(n,end='')
        n+=1
    print()
print('--------------------')


