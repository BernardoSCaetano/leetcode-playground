""" Problem: 151. Reverse Words in a String
 Date: 20-11-2024
"""
from typing import List


class Solution:
  def reverseWords(self, s: str) -> str:
    return " ".join(s.split()[::-1])

if __name__ == '__main__':
  s = Solution()
  print(s.reverseWords("the sky is blue"))  # Output: "blue is sky the"

  print(s.reverseWords("  hello world  "))  # Output: "world hello"

  print(s.reverseWords("a good   example"))  # Output: "example good a"

