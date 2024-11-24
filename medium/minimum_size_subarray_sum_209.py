""" Problem: 209. Minimum Size Subarray Sum
 Date: 20-11-2024
"""
from typing import List


class Solution:
  def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    left = 0
    result = float('inf')
    array_sum = 0

    for right in range(len(nums)):
      array_sum += nums[right]

      while array_sum >= target:
        result = min(result, right - left + 1)
        array_sum -= nums[left]
        left += 1

    return 0 if result == float('inf') else result
