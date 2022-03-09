import unittest

from insertion_sort import insertion_sort
from merge_sort import merge_sort


class TestCase(unittest.TestCase):
    def test_insertion_sort(self):
        array = [5, 2, 4, 6, 1, 3]
        self.assertEqual(insertion_sort(array), [1, 2, 3, 4, 5, 6])

    def test_merge_sort(self):
        array = [5, 2, 4, 6, 1, 3]
        self.assertEqual(merge_sort(array, 0, len(array) - 1), [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
