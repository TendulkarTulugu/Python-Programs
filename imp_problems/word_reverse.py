word=input().lower()
rev=''
for ch in word:
    rev=ch+rev
print(rev)

w='Hello'
print(w[::-1])