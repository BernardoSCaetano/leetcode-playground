""" Problem: 977. Squares of a Sorted Array
 Date: 22-11-2024
"""
from typing import List


class Solution:
  def sortedSquares(self, nums: List[int]) -> List[int]:
    left, right = 0, len(nums) - 1
    result = []

    for i in range(len(nums) - 1, -1, -1):
      if abs(nums[left]) > abs(nums[right]):
        result.insert(0, nums[left] ** 2)
        left += 1
      else:
        result.insert(0, nums[right] ** 2)
        right -= 1

    return result

if __name__ == '__main__':
  solution = Solution()
  print(solution.sortedSquares([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
  print(solution.sortedSquares([-7, -3, 2, 3, 11]))  # [4, 9, 9, 49, 121]
  print(solution.sortedSquares([-7, -3, 2, 3, 11, 12]))  # [4, 9, 9, 49, 121, 144]
  print(solution.sortedSquares([-7, -3, 2, 3, 11, 12, 13]))  # [4, 9, 9, 49, 121, 144, 169]
  print(solution.sortedSquares([-7, -3, 2, 3, 11, 12, 13, 14]))  # [4, 9, 9, 49, 121, 144, 169, 196]
  print(solution.sortedSquares([-7, -3, 2, 3, 11, 12, 13, 14, 15]))  # [4, 9, 9, 49, 121, 144, 169, 196, 225]
  print(solution.sortedSquares([-7, -3, 2, 3, 11, 12, 13, 14, 15, 16]))  # [4, 9, 9, 49, 121, 144, 169, 196, 225, 256]
  print(solution.sortedSquares([-7, -3, 2, 3, 11, 12, 13, 14, 15, 16, 17]))  # [4, 9, 9, 49, 121, 144, 169, 196, 225, 256, 289]
  print(solution.sortedSquares([-7, -3, 2, 3, 11, 12, 13, 14, 15, 16, 17, 18]))  # [4, 9, 9, 49, 121, 144, 169,