from typing import List


class Solution:

  def is_prime(n):
    if n <= 1:
      return False
    for i in range(2, int(n ** 0.5) + 1):
      if n % i == 0:
        return False
    return True

  def primeSubOperation(self, nums: List[int]) -> bool:
    """
        [1,1,4]
            False

        [2,2]
            True
        [0,2]

        [2,2,2]
            False
        [2,0,2]
        [0,0,2]

        [3,3,4]
            True
            diff = 0
            p = 2
        [1,3,4]

        [4,9,6,10]
        9-6 = 3 >>>> diff == 3 -> p > 3 -> p = 5. pick the first prime larger than diff
        9-5 = 4. Put 4 in the place of 9
        [4,4,6,10]
        4-4 = 0 >>>>> p

        [X,4,6,10]

        [2,3,5,7,11,13,19,23,29,31,37,41,43,47]
    """
    last_num = float('inf')
    n = len(nums)
    largest_num = max(nums)

    for i in range(n - 1, -1, -1):
      current_num = nums[i]
      if last_num > current_num:
        last_num = current_num
      else:
        # try fixing with prime decrement
        prime_to_check = nums[i] - last_num

        while True:
          prime_to_check += 1
          if current_num - prime_to_check <= 0:
            return False
          if self.is_prime(prime_to_check):
            nums[i] -= prime_to_check
            last_num = nums[i]

            break

    return True
