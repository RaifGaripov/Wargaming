MIN_MERGE = 32


def calc_min_run(array_len):
    """Returns the minimum of array_len and MIN_MERGE
    """
    r = 0
    while array_len > MIN_MERGE:
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
    left, right = [], []
    for index in range(0, len_first):
        left.append(sorted_array[left + index])
    for index in range(0, len_second):
        right.append(sorted_array[mid + 1 + index])

    index, j, k = 0, 0, left

    # after comparing, we merge those two array
    # in larger sub array
    while index < len_first and j < len_second:
        if left[index] <= right[j]:
            sorted_array[k] = left[index]
            index += 1

        else:
            sorted_array[k] = right[j]
            j += 1

        k += 1

    # Copy remaining elements of left, if any
    while index < len_first:
        sorted_array[k] = left[index]
        k += 1
        index += 1

    # Copy remaining element of right, if any
    while j < len_second:
        sorted_array[k] = right[j]
        k += 1
        j += 1


# Iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def tim_sort(sorted_array):
    length = len(sorted_array)
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
    arr = [-2, 7, 15, -14, 0, 15, 0,
           7, -7, -4, -13, 5, 8, -14, 12]

    print("Given Array is")
    print(arr)

    tim_sort(arr)

    print("After Sorting Array is")
    print(arr)
