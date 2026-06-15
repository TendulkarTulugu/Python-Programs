# count number of vowels in the give word

word=input().lower()
vowels=0
for ch in word:
    if ch.isalpha():
        if ch in 'aeiou':
            vowels+=1
print(vowels)