"""Merge Sort

Merge sort utilises a divide and conquer approach to sort an array. The
auxiliary function combines two sorted arrays into a larger array that is also
sorted. The recursion bottoms-out when the array to be sorted is of length 1,
in which case no sorting needs to occur.

Time Complexity
---------------
Best case: O(n*log(n))
Worst case: O(n*log(n))
Average Case: O(n*log(n))
"""


def merge(array, p, q, r):
    left = array[p : q + 1]
    right = array[q + 1 : r + 1]
    left.append(float("inf"))
    right.append(float("inf"))
    i, j = 0, 0
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
    return array


def merge_sort(array, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)
    return array


def main():
    array = [5, 2, 4, 6, 1, 3]
    print(f"Input: {array}")
    merge_sort(array, 0, len(array) - 1)
    print(f"Output: {array}")


if __name__ == "__main__":
    main()
