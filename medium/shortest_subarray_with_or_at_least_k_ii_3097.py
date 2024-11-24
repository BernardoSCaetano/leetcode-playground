from typing import List


class Solution:

  @staticmethod
  def is_special_sub_array(sub_array, k):
    bitwise_or = 0
    for num in sub_array:
      bitwise_or = bitwise_or | num

    if bitwise_or > k:
      return True
    else:
      return False

  def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
    """
        [1,2,3], k = 2 -> 1
        0001
        0010
        0011

        0011

        [2,1,8], k = 10 -> 3
        0010
        0001
        1000

        1011

        Check len 1
    """
    window_length = 1
    window = []
    while window_length <= len(nums):
      for num in nums:
        window.append(num)
        if len(window) == window_length:
          if self.is_special_sub_array(window, k):
            return window_length
          else:
            window.pop(0)

      window_length += 1

    return -1
