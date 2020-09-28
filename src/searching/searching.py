def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # get the middle point
    # compare the value in the middle with target
    start = 0
    end = (len(arr)-1)

    found = False
    while end >= start and not found:
        middle_ind = (start + end) // 2
        if arr[middle_ind] == target:
            found = True
            return middle_ind
        else:
            if target < arr[middle_ind]:
                end = middle_ind - 1
            if target > arr[middle_ind]:
                start = middle_ind + 1

    return -1
