def threeSum(nums):
    sorted_array = sorted(nums)
    result = []
    for i, value in enumerate(sorted_array):
        # Skip duplicates for the first number
        if i > 0 and sorted_array[i] == sorted_array[i-1]:
            continue

        # Early termination
        if value > 0:
            break

        left = i + 1
        right = len(sorted_array) - 1

        while left < right:
            sum3 = value + sorted_array[left] + sorted_array[right]

            if sum3 == 0:
                result.append([value, sorted_array[left], sorted_array[right]])

                # Skip duplicates for left and right pointers
                while left < right and sorted_array[left] == sorted_array[left + 1]:
                    left += 1
                while left < right and sorted_array[right] == sorted_array[right - 1]:
                    right -= 1

                # Move both pointers after finding a triplet
                left += 1
                right -= 1

            elif sum3 < 0:
                left += 1
            else:
                right -= 1

    return result
nums = [-1,0,1,2,-1,-4]
# [-4, -1, -1, 0, 1 ,2]
print(threeSum(nums))
