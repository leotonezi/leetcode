def containsDuplicate(nums):
    already_seen = set()
    for num in nums:
        if num in already_seen:
            return True
        already_seen.add(num)
    return False
