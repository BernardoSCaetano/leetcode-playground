""" Problem: 2064. Minimized Maximum of Products Distributed to Any Store
 Date: 14-11-2024
"""
from typing import List


class Solution:
  def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
    """
    You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.

    You need to distribute all products to the retail stores following these rules:

    A store can only be given at most one product type but can be given any amount of it.
    After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.
    Return the minimum possible x.

    :param n: number of retail stores
    :param quantities:
    :return:
    """
    m = len(quantities)

    print(m // (m - n))
    print(m // (m - n) + m /(m -n) % n)

    number_of_splits = m - n
    # We sort the quantities in descending order
    # We give each type a number of splits mod it's length.
    # E.g.:
    # quantities = [11, 5]
    # n = 6
    # Number of splits = 4
    # [6 5] [5] -> global_max = 6; Original = 11; Split = 2 (increments); Values [6 5]
    # [4 4 3] [5] -> global_max = 5; Original = 11; Split = 3 (increments); Values [4, 4, 3]; Max = 4
    # [4 4 3] [3 2] -> global_max = 4;
    # [3 3 3 2] [3 2] -> global_max = 3;

    # We always split the max. We select the original number and divide by i, starting it with 1




s = Solution()
s.minimizedMaximum(3, [2, 3, 5])  # Expected output: 5
s.minimizedMaximum(6, [11, 6])  # Expected output: 3
