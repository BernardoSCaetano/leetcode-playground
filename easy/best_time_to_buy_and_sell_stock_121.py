""" Problem: 121. Best Time to Buy and Sell Stock
 Date: 14-11-2024

 You are given an array prices where prices[i] is the price of a given stock on the ith day.
  - len(prices) high
  - prices[i] medium
  - prices are positive

  You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
  - 1 day to buy stock
  - 1 day to sell stock
  - buy_day and sell_day must be different
  - sell day must be to the right of buy day

  Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
  - max proffit = maximum_sell_day - maximum_buy_day
"""
from typing import List


class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    min_buy = prices[0]
    max_profit = 0

    for price in prices[1:]:
      if price < min_buy:
        min_buy = price
      elif price - min_buy > max_profit:
        max_profit = price - min_buy
    return max_profit
