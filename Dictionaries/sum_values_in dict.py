#11

'''
Without looking at your previous code, write this function:

def sum_values(dictionary):

Example:

marks = {
    "Math": 90,
    "Science": 85,
    "English": 95
}

print(sum_values(marks))

Expected output:

270
Rules
✅ Use a loop.
✅ Don't use sum().
✅ Return the total.
'''

marks = {
    "Math": 90,
    "Science": 85,
    "English": 95
}

def sum_values(dictionary):
    sum=0
    for key in dictionary:
        sum+=dictionary[key]
    return sum

print(sum_values(marks))