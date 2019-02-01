# Searching algorithms.

import math

def binarySearch(arr, start, end, key):
    """
    Compare with mid element and decide if you want to look in upper/lower half of array.
    O(logn) complexity
    """
    if start > end:
        return -1
    mid = start + (end-start)/2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binarySearch(arr, mid+1, end, key)
    else:
        return binarySearch(arr, start, mid-1, key)

def jumpSearch(arr, key):
    """
    Keep jumping with step size of sqrt(n) till the interval 
    has the key in range
    Then do linear search.
    Its complexity is O(sqrt(n)). its between linear and binary search. 
    In systems where jumping back is difficult, jump search is better than binary search.
    """
    print '~~~ jump search ~~~'
    n = len(arr)
    step = int(math.sqrt(len(arr)))
    prev = 0
    while (arr[math.min(step,n)] < key):
        prev = step
        step = step + step
        if prev >= n:
            return -1
    # TODO

def interpolationSearch(arr, start, end, key):
    """
    Improvement over binary search. 
    Instead of starting in the mid, it looks at the interpolated location.
    This method works if the array contains numbers uniformly distributed.
    """
    if start > end:
        return -1
    loc = start + int((end - start)*(key - arr[start])/(arr[end]-arr[start]))
    if arr[loc] == key:
        return loc
    elif arr[loc] < key:
        return interpolationSearch(arr, loc+1, end, key)
    else:
        return interpolationSearch(arr, start, loc-1, key)

def exponentialSearch(arr, key):
    """
    look at positios 1,2,4,8,16,...
    then do binary search in the interval
    This is good when trying to find something in an un-ending list of sorted elements. 
    Ex. finding 0 crossing in an monotonic function.
    """
    #TODO

if __name__ == '__main__':
    arr = [1,2,3,4,7,9,9,10,12,18,24]
    key = 10
    idx = interpolationSearch(arr, 0, len(arr)-1, key)

    if idx == -1:
        print 'element not found'
    else:
        print  'element found at {}'.format(idx)


