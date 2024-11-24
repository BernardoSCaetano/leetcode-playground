""" Problem: 2563. Count the Number of Fair Pairs
 Date: 13-11-2024
"""

from typing import List


class Solution:
  def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
    """
    A pair (i, j) is fair if
     - 0 <= i < j < n
     - lower <= nums[i] + nums[j] <= upper

    :param nums: a list of integers
    :param lower: an integer representing the lower bound
    :param upper: an integer representing the upper bound

    :return: the number of fair pairs
    """
    fair_pair = set()
    n = len(nums)

    for i in range(n):
      for j in range (i + 1, n, 1):
        if lower <= nums[i] + nums[j] <= upper:
          fair_pair.add((i, j))
    return len(fair_pair)

s = Solution()
print(s.countFairPairs([0,1,7,4,4,5], 3, 6))  # Expected output: 6
