""" Problem: 58. Length of Last Word
 Date: 20-11-2024

 Given a string s consisting of words and spaces, return the length of the last word in the string.

  A word is a maximal
  substring
   consisting of non-space characters only.
"""

class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    return len(s.split()[-1])
