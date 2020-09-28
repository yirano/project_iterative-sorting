# TO-DO: Complete the selection_sort() function below

def selection_sort(arr):
    # * In-place selection sort
    curr = 0
    while curr < len(arr):
        smallest = curr
        for i in range(curr, len(arr)):
            if (arr[smallest] > arr[i]):
                smallest = i
                # arr[smallest], arr[i] = arr[i], arr[smallest]
        arr.insert(curr, arr.pop(smallest))
        curr += 1

    return arr

    '''
    limit = len(arr)
    queue = []
    # * Out-of-place selection sort
    while len(queue) < limit:
        curr_ind = 0
        smallest_ind = curr_ind
        for i in range(1, len(arr)):
            if arr[smallest_ind] > arr[i]:
                smallest_ind = i

        queue.append(arr[smallest_ind])
        arr.pop(smallest_ind)
    return queue
    '''
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Bubble sort is "bubbling up" the greater value
    # To solve this I'll want to compare two items
    # and continue iterating through to compare w/the higher value until the end
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''

# ! Runtime Complexity: O(n)


def counting_sort(arr, maximum=None):

    if maximum is None or len(arr) == 0:
        return []

    bucket = [0] * (maximum + 1)
    sort = []

    for i in range(0, len(arr)):
        ind = arr[i]
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"

        bucket[ind] += 1

    for j in range(0, len(bucket)):
        sort += ([j] * bucket[j])

    return sort


# ? Insertion Sorting (from lecture)

def insertion_sort(list_to_sort):
    # the first element is already in the 'sorted side'
    # for all other items, we should do things
    # starting at the second item, iterate until it reaches the end
    # the curr number at the index represents the value currently being sorted
    # move the current number back through the array
    # keep moving until it's greater than the number before it OR the index is zero
    # shift the current value and the one to left of it
    # set the avlue at the curr index to the current number

    for i in range(1, len(list_to_sort)):
        current_num = list_to_sort[i]
        j = i
        while j > 0 and current_num < list_to_sort[j-1]:
            list_to_sort[j] = list_to_sort[j-1]
            j -= 1
        list_to_sort[j] = current_num

    return list_to_sort
