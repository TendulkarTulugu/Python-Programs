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
