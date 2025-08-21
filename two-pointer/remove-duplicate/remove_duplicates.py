def removeDuplicates(nums):
    k = 0  # pointer for next position to place non-val element
    dup = set()
    for i in range(len(nums)):
        if nums[i] not in dup:
            dup.add(nums[i])
            nums[k] = nums[i]
            k += 1

    return k

nums = [0,1,2,2,3,0,4,2]

removeDuplicates(nums)