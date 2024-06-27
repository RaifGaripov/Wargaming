MIN_MERGE = 32


def calc_min_run(array_len):
    """Returns the minimum of array_len and MIN_MERGE
    """
    r = 0
    while array_len >= MIN_MERGE:
        r |= array_len & 1
        array_len >>= 1
    return array_len + r


# This function sorts array from left index to
# to right index which is of size at most RUN
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# Merge function merges the sorted runs
def merge(sorted_array, left, mid, right):
    # original array is separated in two parts
    # left and right array
    len_first, len_second = mid - left + 1, right - mid
    left_part, right_part = [], []
    for index in range(0, len_first):
        left_part.append(sorted_array[left + index])
    for index in range(0, len_second):
        right_part.append(sorted_array[mid + 1 + index])

    index, j, k = 0, 0, left

    # after comparing, we merge those two array
    # in larger sub array
    while index < len_first and j < len_second:
        if left_part[index] <= right_part[j]:
            sorted_array[k] = left_part[index]
            index += 1

        else:
            sorted_array[k] = right_part[j]
            j += 1

        k += 1

    # Copy remaining elements of left, if any
    while index < len_first:
        sorted_array[k] = left_part[index]
        k += 1
        index += 1

    # Copy remaining element of right, if any
    while j < len_second:
        sorted_array[k] = right_part[j]
        k += 1
        j += 1


# Iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def tim_sort(sorted_array):
    length = len(sorted_array)
    if length == 0:
        return sorted_array
    min_run = calc_min_run(length)

    # Sort individual sub arrays of size RUN
    for start in range(0, length, min_run):
        end = min(start + min_run - 1, length - 1)
        insertion_sort(sorted_array, start, end)

    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = min_run
    while size < length:

        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, length, 2 * size):

            # Find ending point of left sub array
            # mid + 1 is starting point of right sub array
            mid = min(length - 1, left + size - 1)
            right = min((left + 2 * size - 1), (length - 1))

            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid < right:
                merge(sorted_array, left, mid, right)

        size = 2 * size


if __name__ == "__main__":
    test_cases = [
        ([2, 5, 8, -3, 0, 7], 0, 2, 5, [-3, 0, 2, 5, 7, 8]),
        ([1, 1, 1, 1, 1, 1], 0, 2, 5, [1, 1, 1, 1, 1, 1]),
        ([1, 2, 3, 4, 5, 6], 0, 2, 5, [1, 2, 3, 4, 5, 6]),
        ([6, 5, 4, 3, 2, 1], 0, 2, 5, [1, 2, 3, 4, 5, 6]),
        ([], 0, 0, 0, []),
        ([1], 0, 0, 0, [1]),
        ([4, 5, 6, 4, 5, 6], 0, 2, 5, [4, 4, 5, 5, 6, 6])
    ]

    for arr, l, m, r, expected in test_cases:
        tim_sort(arr)
        print(f"Sorted array: {arr}, expected: {expected}")
        assert arr == expected, f"Failed: {arr} != {expected}"
    print("All test cases passed!")