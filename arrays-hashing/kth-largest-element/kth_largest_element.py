import heapq

def findKthLargest(nums, k):
    # Step 1: Create min-heap with first k elements
    heap = nums[:k]
    heapq.heapify(heap)  # O(k)

    # Step 2: Process remaining elements
    for num in nums[k:]:
        # If current number is larger than smallest in heap
        if num > heap[0]:
            heapq.heappop(heap)    # Remove smallest
            heapq.heappush(heap, num)  # Add current number

    # Step 3: Root is kth largest
    return heap[0]



nums = [5, 3, 8, 1]
findKthLargest(nums, 2)
