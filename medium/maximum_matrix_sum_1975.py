""" Problem: 1975. Maximum Matrix Sum
 Date: 24-11-2024
"""
from typing import List


class Solution:
  def maxMatrixSum(self, matrix: List[List[int]]) -> int:
    negative_counter = 0
    max_sum = 0
    min_number = float('inf')

    for row in matrix:
      for element in row:
        if element < 0:
          negative_counter += 1

        positive_element = abs(element)
        max_sum += positive_element
        if positive_element < min_number:
          min_number = positive_element

    if negative_counter % 2 != 0:
      max_sum -= 2 * min_number

    return max_sum
