""" Problem: 169. Majority Element
 Date: 13-11-2024
"""
from typing import List


class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    num_dict = {}
    for num in nums:
      if num in num_dict:
        num_dict[num] += 1
      else:
        num_dict[num] = 1

    majority_element = (-1, 0)
    for key, value in num_dict.items():
      if value > majority_element[1]:
        majority_element = (key, value)

    return majority_element[0]
