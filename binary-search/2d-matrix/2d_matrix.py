class Solution(object):
    def matrixSearch(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        left = 0
        n = len(matrix[0])
        right = len(matrix) * n - 1

        while(left <= right):
          mid = (left + right) // 2
          mid_element = matrix[mid // n][mid % n]

          if mid_element == target:
            return True
          if mid_element < target:
            left = mid + 1
          else:
            right = mid - 1

        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

if __name__ == "__main__":
    solution = Solution()
    result = solution.matrixSearch(matrix, 23)
    print(result)