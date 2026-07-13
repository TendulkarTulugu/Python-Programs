'''
1. Find the Second Largest Number

Rules
Use loops.
Don't use sort().
Don't use max().
Don't convert to a set.

'''
def second_largest(nums):
    largest=nums[0]
    sec_largest=float('-inf')
    for num in nums:
        if num>largest:
            sec_largest=largest
            largest=num
        elif num>sec_largest and num!=largest:
            sec_largest=num
    return largest,sec_largest

numbers = [10, 45, 7, 92, 31]
print(second_largest(numbers))


'''
2. Count Words

Rules
Use loops.
Don't use split().
Ignore leading and trailing spaces.
'''

def count_words(text):
    spaces=0
    text=text.strip()
    for ch in text:
        if ch==' ':
            spaces+=1
    words=spaces+1
    return words

texts = "Python "

print(count_words(texts))


'''
3. Common Elements Between Two Sets

Rules
Use loops.
Don't use the & operator.
Use the in operator.
'''
# using set operations & we can find
def common_elements(A,B):
    return (A&B)

A = {10, 20, 30}
B = {20, 30, 40}

print(common_elements(A,B))

# but we need to use loops

def common_elements(A,B):
    common=set()
    for n in A:
        for m in B:
            if n==m:
                common.add(m)
    return common

A = {10, 20, 30}
B = {20, 30, 40}

print(common_elements(A,B))

'''
4. Sum of Dictionary Values

Rules
Use loops.
Don't use sum().

'''
marks = {
    "Math": 90,
    "Science": 85,
    "English": 95
}

def sum_values(dictionary):
    total=0
    for values in dictionary:
        total+=dictionary[values]
    return total


print(sum_values(marks))



'''
5. Character Frequency

Rules
Use a dictionary.
Don't use count().
'''

def char_frequency(text):
    freq={}
    for ch in text:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq

texts = "banana"
print(char_frequency(texts))


'''
6. Remove Duplicates
Rules
Use a set.
Return the set.
'''

def remove_dups(nums):
    num=set()
    for n in nums:
        num.add(n)
    return num

numbers = [10, 20, 10, 30, 20, 40]
print(remove_dups(numbers))


'''
7. Search a Key in a Dictionary

Rules
Don't use get().
Use the in operator.
'''

student = {
    "name": "Tendul",
    "age": 23,
    "branch": "AI & DS"
}

def search_key(dictionary,key):
    for k in dictionary:
        if k==key:
            return dictionary[key]
    return 'Key not found'
    

print(search_key(student, "age"))
print(search_key(student, "city"))       




'''
8. Count Even Numbers

Rules
Use loops.
Return the count.
'''

def count_even(nums):
    count=0
    for num in nums:
        if num%2==0:
            count+=1
    return count

numbers = [10, 15, 8, 7, 2, 5]
print(count_even(numbers))



'''
9. Reverse a List

Rules
Don't use reverse() or slicing ([::-1]).
Use loops.
'''
def reverse_list(nums):
    rev=[]
    for num in nums:
        rev.insert(0,num)
    return rev

numbers = [10, 20, 30, 40]
print(reverse_list(numbers))


'''
10. Check Prime Number

Rules
Use loops.
Return "Prime" or "Not Prime".
'''

def is_prime(n):
    fact=0
    for i in range(1,n+1):
        if n%i==0:
            fact+=1
    if fact==2:
        return "Prime"
    else:
        return "Not Prime"

print(is_prime(11))
print(is_prime(12))