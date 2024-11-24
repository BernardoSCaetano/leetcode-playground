""" Problem: 2070. Most Beautiful Item for Each Query
 Date: 12-11-2024
"""
from typing import List

class Solution:
  def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
    # Sort items by price (increasing order)
    items.sort()
    # Pair each query with its original index for output order preservation
    indexed_queries = sorted((q, i) for i, q in enumerate(queries))

    # Initialize variables
    results = [0] * len(queries)  # to store the final answers
    max_beauty = 0
    item_index = 0  # to track items in items list

    # Iterate through each query in sorted order
    for query_price, query_index in indexed_queries:
      # Update max_beauty to the highest beauty available for the current query price
      while item_index < len(items) and items[item_index][0] <= query_price:
        max_beauty = max(max_beauty, items[item_index][1])
        item_index += 1

      # Store the max beauty for this query
      results[query_index] = max_beauty

    return results

# Test example
s = Solution()
items = [[3, 4], [5, 2], [2, 3]]
queries = [4, 2, 3]
print(s.maximumBeauty(items, queries))  # Expected output: [4, 3, 4]


print(items)
print(queries)
indexed_queries = sorted((q, i) for i, q in enumerate(queries))
print(indexed_queries)