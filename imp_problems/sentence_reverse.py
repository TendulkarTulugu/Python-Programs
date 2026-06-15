
# take a sentence and reverse each word in the sentence and print in the same format

s="Let's take LeetCode contest"
w=s.split(' ')
print(w)
wr=''

# here i'm reversing each word and storing using concatinating

rev=''
for ch in w:
    wr=ch+' '+wr
for w in wr:
    rev=w+rev
print(rev)