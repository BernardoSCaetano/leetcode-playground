"""
The strange though was having the idea I am always buying.
But that's not we are doing, we are checking max profit if we
were to buy on specific days. So updating min_price


Find and return the maximum profit you can achieve.
 - We need to have some kind of carry on per index.
 - Understand if should have sold or should continue keeping it

"""
from typing import List


class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    min_price = prices[0]
    accumulated_profit = 0

    for price in prices[1:]:
      if price > min_price:
        accumulated_profit += price - min_price
        min_price = price
      else:
        min_price = price
    return accumulated_profit
