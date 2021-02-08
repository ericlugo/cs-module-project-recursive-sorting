import unittest
import random
from searching import *


class RecursiveSortingTests(unittest.TestCase):
    def test_binary_search(self):
        arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
        arr2 = []

        self.assertEqual(binary_search(arr1, -8, 0, len(arr1)-1), 1)
        self.assertEqual(binary_search(arr1, 0, 0, len(arr1)-1), 6)
        self.assertEqual(binary_search(arr2, 6, 0, len(arr2)-1), -1)
        self.assertEqual(binary_search(arr2, 0, 0, len(arr2)-1), -1)

    def test_recursive_agnostic_binary_search(self):
        ascending = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
        descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]
        
        self.assertEqual(recursive_agnostic_binary_search(ascending, 12, 0, len(ascending)-1), 2)
        self.assertEqual(recursive_agnostic_binary_search(ascending, 54, 0, len(ascending)-1), 9)
        self.assertEqual(recursive_agnostic_binary_search(ascending, 31, 0, len(ascending)-1), -1)

        self.assertEqual(recursive_agnostic_binary_search(descending, 49, 0, len(descending)-1), 3)
        self.assertEqual(recursive_agnostic_binary_search(descending, -17, 0, len(descending)-1), 7)
        self.assertEqual(recursive_agnostic_binary_search(descending, -1, 0, len(descending)-1), -1)

    def test_iterative_agnostic_binary_search(self):
        ascending = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
        descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]
        
        self.assertEqual(iterative_agnostic_binary_search(ascending, 12), 2)
        self.assertEqual(iterative_agnostic_binary_search(ascending, 54), 9)
        self.assertEqual(iterative_agnostic_binary_search(ascending, 31), -1)

        self.assertEqual(iterative_agnostic_binary_search(descending, 49), 3)
        self.assertEqual(iterative_agnostic_binary_search(descending, -17), 7)
        self.assertEqual(iterative_agnostic_binary_search(descending, -1), -1)


if __name__ == '__main__':
    unittest.main()
