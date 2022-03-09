"""Insertion Sort

Insertion sort is the first algorithm in the series. It is an intuitive sorting
algorithm that reflects how one would naturally sort a hand of cards.

Iteratively sorting a subarray from the left-most element expanding towards the
right-most element in the input array. 'Inserting' an element from the unsorted
side into the sorted subarray by shifting all the larger elements one space
over.

Time Complexity
---------------
Best case: O(n)
Worst case: O(n^2)
Average Case: O(n^2)
"""


def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
    return array


def main():
    array = [5, 2, 4, 6, 1, 3]
    print(f"Input: {array}")
    insertion_sort(array)
    print(f"Output: {array}")


if __name__ == "__main__":
    main()
