# Sorting Algorithms
# Abinash Mohanty

import math

def selectionSort(arr):
    """
    In every iteration of selection sort:
    the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.
    Time complexity : O(n^2)
    Auxiliary space = O(1)
    The good thing about selection sort: 
    It never makes more than O(n) swaps and can be useful when memory write is a costly operation.
    """
    print 'Doing selection sort.'
    for i in range(0,len(arr)):
        minindex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minindex]:
                minindex = j
        arr[i], arr[minindex] = arr[minindex], arr[i]

def bubbleSort(arr):
    """
    Repeatedly swap the adjacent elements if they are in wrong order.
    Average and worst case time complexity : O(n^2)
    Best case time complexity : O(n) -- already sorted
    """
    print 'Doing bubble sort.'
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertionSort(arr):
    """
    Pick and element and put it in sorted sequence. 
    Time complexity : O(n^2)
    Buondary case: if the elements are all sort in reverse order
    """
    print 'Doing insertion sort.'
    if len(arr) == 0:
        print 'Invalid array.'
    if len(arr) == 1:
        return

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def merge(arr, l, m, r):
    """
    Merge sub-routine to merge two separately sorted array arrr[l:m] and arr[m+1:r]
    Its done in linear time.
    """
    n1 = m - l + 1
    n2 = r - m

    # L1 and L2 are blank placeholder arrays.
    L = [0] * n1
    R = [0] * n2

    # Copy the array data into Left and Right arrays.
    for i in range(0,n1):
        L[i] = arr[i+l]
    
    for j in range(0,n2):
        R[j] = arr[j+m+1]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        k += 1
        i += 1

    while j< n2:
        arr[k] = R[j]
        k += 1
        j += 1


def mergeSort(arr, l, r):
    """
    Divide the array into two parts constantly. 
    call the merge routine to merge the small sorted array
    Time complexity: O(nLog(n))
    """
    if l < r:
        m = (l+(r-1))/2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr,l,m,r)


def binaryInsertionSort(arr):
    """
    Do binary search in the sorted sequence for quick location of the insertion point.
    """
    print 'Doing binary insertion sort.'

if __name__ == '__main__':
    
    arr = [1, 4, 5, 2, 9, 3, 8, 4, 10]
    print arr
    mergeSort(arr, 0, len(arr)-1)
    print arr


