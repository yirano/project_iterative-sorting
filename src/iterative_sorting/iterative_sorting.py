# TO-DO: Complete the selection_sort() function below

def selection_sort(arr):
    # * In-place selection sort
    curr = 0
    while curr < len(arr):
        smallest = curr
        for i in range(curr, len(arr)):
            if (arr[smallest] > arr[i]):
                smallest = i
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
    # Your code here

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


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
