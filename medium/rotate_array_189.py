""" Problem: 189. Rotate Array
 Date: 14-11-2024
"""
from typing import List


class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]




s = Solution()

my_nums = [1, 2, 3, 4, 5, 6, 7]
s.rotate(my_nums, 3)
print(my_nums)  # Output: [5, 6, 7, 1, 2, 3, 4]