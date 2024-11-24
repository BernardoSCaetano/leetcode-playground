""" Problem: 2405. Optimal Partition of String
 Date: 21-11-2024
"""
from typing import List


class Solution:
  def partitionString(self, s: str) -> int:
    s_aux = set()
    counter = 1

    for c in s:
      if c in s_aux:
        counter += 1
        s_aux = set(c)
      else:
        s_aux.add(c)
    return counter
