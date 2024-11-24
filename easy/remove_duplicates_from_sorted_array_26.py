from typing import List


class Solution():
  def removeDuplicates(self, nums: List[int]) -> int:

    # Initialize the array position marker k to 0.
    # This will keep track of the position in the array
    # where the next unique element should be placed.
    k = 0

    # Loop through each number in the nums array.
    for x in nums:
      # Check if k is 0, which means we're at the start of the array
      # or if the current number is not equal to the last unique number we've seen.
      # The condition k == 0 is true for the first element,
      # so we store it as the first unique element.
      if k == 0 or x != nums[k - 1]:
        # Place the current unique element at the k-th position in the array.
        nums[k] = x
        # Increment k to indicate that the next unique element should be placed in the next position.
        k += 1

    # Return the length of the array that contains all unique elements,
    # which is also the new length of the array without duplicates.
    return k
