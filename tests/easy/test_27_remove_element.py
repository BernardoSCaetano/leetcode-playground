from unittest import TestCase
from easy.remove_element_27 import Solution

class TestSolution(TestCase):
  def test_remove_element(self):
    # Test cases
    s = Solution()
    self.assertEqual(s.removeElement([3, 2, 2, 3], 3), (2, [2, 2]) )
    self.assertEqual(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2), (5, [0, 1, 3, 0, 4]) )
    self.assertEqual(s.removeElement([1], 1) , (0, []) )