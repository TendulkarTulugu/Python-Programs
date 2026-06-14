"""
New Pattern ⭐

Now let's introduce spaces.

    *
   **
  ***
 ****
*****

"""
# 1st it take 4 spaces and 1 star- 3 spaces and 2 stars -- as incrementing spaces decreases and stars increases


for i in range(1,6):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i):
        print('*',end='')
    print()