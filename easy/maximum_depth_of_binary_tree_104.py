""" Problem: 104. Maximum Depth of Binary Tree
 Date: 13-11-2024
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    """
        Input: root = [3,9,20,null,null,15,7]
        Output: 3

        I see that 3 will be the "current_node", while the next 2 will be the child.
        And this will occur to the power of 2. From this, I notice we might be able
        to have a guess based on the length of the graph. But that might not be true,
        as the graph can grow one side, and the length would still increase (I think).

        As we only need to check the length, the maxDepth is the maximum of depths
        between each branches
    """
    # We check empty root. This way we avoid checking this every iteration
    if root is None:
      return 0

    def max_depth_aux(root: Optional[TreeNode]) -> int:
      if root.left is None and root.right is None:
        return 1
      elif root.left is None and root.right is not None:
        return 1 + max_depth_aux(root.right)
      elif root.left is not None and root.right is None:
        return 1 + max_depth_aux(root.left)
      else:
        return max(1 + max_depth_aux(root.left), 1 + max_depth_aux(root.right))

    return max_depth_aux(root)
