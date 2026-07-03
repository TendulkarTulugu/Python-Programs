def second_smallest(nums):
    small=nums[0]
    second_small=float('inf')
    for n in nums:
        if n<small:
            second_small=small
            small=n
        elif n<second_small and n!=small:
            second_small=n
    return small,second_small



numbers = [10, 45, 7, 92, 31,105,110]

print(second_smallest(numbers))
