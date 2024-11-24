from typing import List


class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
      return n

    previous_index = n - 1
    for next_index in range(n - 2, -1, -1):
      if nums[next_index] == nums[previous_index]:
        del nums[previous_index]

      previous_index = next_index

    return len(nums)
