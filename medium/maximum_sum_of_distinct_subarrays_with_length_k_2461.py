""" Problem: 2461. Maximum Sum of Distinct Subarrays With Length K
 Date: 19-11-2024

  You are given an integer array nums and an integer k.
  - len(nums) medium
  - k medium
  - k <= len(nums)
  - nums[i] medium
  - nums[i] integer

  - k

  Find the maximum subarray sum of all the subarrays of nums
  - create window
  - start = 0
  - end = k - 1

   that meet the following conditions:
   - The length of the subarray is k, and
      - end - start need to be k
   - All the elements of the subarray are distinct.
      - We use a dict for distinct
          - We save the index where we found each element; We replace the start with the index after occurence.
      - OR we check if in the list already
          - IF SO, we start removing the first element until we find the dupplicate one


  - sum initiate to 0
  - if valid sub-array and > 0, we replace sum value
"""
from typing import List


class Solution:
  def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    result: int = 0
    window: List[int] = []
    n = len(nums)

    for i in range(n):
      next_int: int = nums[i]

      if next_int in window:
        # We found a duplicate, reduce window to only have 1 occurance
        # of next_int
        window.append(next_int)
        print(f'Window when it found a duplicate: {window}')
        for previous_int in window:
          del window[0]  # delete first element until we find the duplicate
          if previous_int == next_int:
            break
        print(f'Window after del: {window}')
      else:
        window.append(next_int)
        if len(window) == k:
          print(f'Window when it is full: {window}')
          result = max(result, sum(window))
          del window[0]

    return result


if __name__ == '__main__':
  s = Solution()
  s.maximumSubarraySum([1, 2, 2, 2, 4, 5], 3)
