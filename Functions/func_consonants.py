def count_consonants(text):
    text=text.lower()
    vowels='aeiou'
    vowels_count=0
    consontants_count=0
    for ch in text:
        if ch not in vowels:
            consontants_count+=1
        else:
            vowels_count+=1
    return consontants_count
print(count_consonants('Education'))


'''
The works better 
but when the input is Hello world

it counts the space also as a consonant.

if the text is 'Python123' the 123 also counts as a consonant.

to overcome this 

Before checking whether it's a vowel or consonant, make sure it's a letter.

ch.isalpha()


True for letters (A-Z, a-z)
False for numbers, spaces, and symbols

'''

def count_consonants(text):
    text = text.lower()
    vowels = 'aeiou'
    consonants_count = 0

    for ch in text:
        if ch.isalpha():
            if ch not in vowels:
                consonants_count += 1

    return consonants_count

print(count_consonants("Hello World 123"))