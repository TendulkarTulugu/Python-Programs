def find_smallest(nums):
    small=nums[0]
    for n in nums:
        if n<small:
            small=n
    return small

numbers = [10, 45, 7, 92, 31,105,110]

print(find_smallest(numbers))