""" Problem: 1652. Defuse the Bomb
 Date: 18-11-2024

You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.
- code : circular array
- n = length(code) small
- code[i] small
- key k

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
- Go through a copy of the list, not to change its values

If k > 0, replace the ith number with the sum of the next k numbers.

If k < 0, replace the ith number with the sum of the previous k numbers.

If k == 0, replace the ith number with 0.

As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
- Circular array, important to normalize K to n

Strategy:
- Brute force, keep going k times over each i, and sum.
- Sliding window with len k.
"""

from typing import List


class Solution:
  def decrypt(self, code: List[int], k: int) -> List[int]:
    n = len(code)
    decrypted_code = [0] * n

    if k == 0:
      return decrypted_code

    is_positive = k > 0

    # Normalize K, use abs() to make it positive
    k = abs(k) % n

    for i in range(n):
      for j in range(1, k + 1, 1):
        if is_positive:
          new_index = (i + j) % (n)
        else:
          new_index = i - j
        decrypted_code[i] += + code[new_index]

    return decrypted_code
