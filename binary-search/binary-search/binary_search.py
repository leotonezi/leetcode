class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while(left <= right):
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
        


nums = [-1,0,3,5,9,12]

if __name__ == "__main__":
    solution = Solution()
    result = solution.search(nums, 2)
    print(result)