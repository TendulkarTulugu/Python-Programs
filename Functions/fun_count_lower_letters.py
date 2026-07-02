def count_lower(text):
    count=0
    for ch in text:
        if ch.islower():
           count+=1
    return count

print(count_lower('PyTHon')) 