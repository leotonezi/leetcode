def longest_ones(nums: list[int], k: int) -> int:
    """
    Find the maximum number of consecutive 1's in the array
    if you can flip at most k 0's.

    Args:
        nums: Binary array containing only 0s and 1s
        k: Maximum number of 0s that can be flipped to 1s

    Returns:
        Maximum length of consecutive 1s possible
    """
    # Initialize variables
    left = 0               # Left pointer of the window
    max_length = 0         # Maximum length found so far
    zero_count = 0         # Count of zeros in the current window

    # Iterate through the array with the right pointer
    for right in range(len(nums)):
        # If the current element is 0, increment zero_count
        if nums[right] == 0:
            zero_count += 1

        # If we have too many zeros, shrink the window from the left
        # until we have at most k zeros
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # Update the maximum length
        # Current window size is (right - left + 1)
        max_length = max(max_length, right - left + 1)

    return max_length


# Test cases
if __name__ == "__main__":
    # Example 1
    nums1 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k1 = 2
    print(f"Example 1: {longest_ones(nums1, k1)}")  # Expected: 6

    # Example 2
    nums2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k2 = 3
    print(f"Example 2: {longest_ones(nums2, k2)}")  # Expected: 10

    # Additional test cases
    # All ones - no flips needed
    print(f"All ones: {longest_ones([1, 1, 1, 1, 1], 2)}")  # Expected: 5

    # All zeros - need to flip all
    print(f"All zeros (k=3): {longest_ones([0, 0, 0, 0, 0], 3)}")  # Expected: 3
    print(f"All zeros (k=5): {longest_ones([0, 0, 0, 0, 0], 5)}")  # Expected: 5

    # Edge case: k = 0 (can't flip any)
    print(f"k=0: {longest_ones([1, 1, 0, 1, 1, 0, 1], 0)}")  # Expected: 2
