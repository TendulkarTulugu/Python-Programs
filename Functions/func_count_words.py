'''
Count number of words in a sentance. 

requirement:

don't use:
split(), count() functions

Think about spaces
'''


def count_words(text):
    spaces=0
    for ch in text:
        if ch==' ':
            spaces+=1
    words=spaces+1
    return words
print(count_words("ChatGPT is amazing"))


'''

i wrote the code but it having bugs. if there is sentance ends with spaces like 'I ' then it shows like 2 words.


if the input is " Hello" it shows 2 instead of 1

"Hello   World"

it shows 4 rather than 2


One Solution

Remove extra spaces first.

text = text.strip()

'''


def count_words(text):
    spaces=0
    text=text.strip()
    for ch in text:
        if ch==' ':
            spaces+=1
    words=spaces+1
    return words
print(count_words(""))