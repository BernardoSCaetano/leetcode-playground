""" Problem: 704. Binary Search
 Date: 13-11-2024
"""
from typing import List

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    """
        Example 1:

        Input: nums = [-1,0,3,5,9,12], target = 9
        0 5

        Output: 4
        Explanation: 9 exists in nums and its index is 4
    """

    left_pointer, right_pointer = 0, len(nums) - 1

    """ Check the middle value. 
        - If it is the target, return its index
        - If value is bigger than target, it means target is to the left
            - We adjust the upper limit, aka the right_pointer, to be the middle - 1
        - If value is smaller than target, it means target is to the right
            - We adjust the lower limit, aka the left_pointer, to be the middle + 1
        We re-run the algotithm with the updated left and right boundaries

        We return 0 when the left and right are the same or have crossed each other
            - In other words, when left_pointer > right_pointer
    """

    while left_pointer <= right_pointer:
      # Get the middle value.
      mid_pointer = left_pointer + (right_pointer - left_pointer) // 2

      if nums[mid_pointer] == target:
        return mid_pointer
      elif nums[mid_pointer] > target:
        right_pointer = mid_pointer - 1
      else:
        left_pointer = mid_pointer + 1

    return -1
