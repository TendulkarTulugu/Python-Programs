def count_even(nums):
    count=0
    for n in nums:
        if n%2==0:
            count+=1
    return count

numbers = [10, 15, 8, 7, 2, 5]

print(count_even(numbers))