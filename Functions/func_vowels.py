'''
🎯 Next Mission

We're now going to combine functions + strings.

Challenge 1

count number if vowels in the word

'''


def count_vowels(text):
    vowels='aeiouAEIOU'
    count=0
    for ch in text:
        if ch in vowels:
            count+=1
    return count
result=count_vowels('Education')
print(result)


# the better version

def count_vowels(text):
    text=text.lower()
    vowels='aeiou'
    count=0
    for ch in text:
        if ch in vowels:
            count+=1
    return count
result=count_vowels('Education')
print(result)