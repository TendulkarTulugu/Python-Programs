cons=0
vow=0
word=input().lower()
for ch in word:
    if ch.isalpha():
        if ch in 'aeiou':
            vow+=1
        else:
            cons+=1
print(vow)
print(cons)
