# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Heap Data structure: Nearly complete binary tree.
# An array can be visualized as an heap.
# for node i: left child is 2i+1 and right child is 2i+2
# Max Heap : Key of the element at any node is >= keys of its child nodes.
# Supported functions: 
# - getMax(): Returns the root element of the heap. Time complexity is O(1)
# - extractMax(): Removes the maximum element from Max Heap. Time Complexity of this Operation is O(Logn)
# - increaseKey(): Increases value of key. Time complexity of this operation is O(Logn).
# - insert(): Inserting a new key takes O(Logn) time.
# - delete(): Deleting a key also takes O(Logn) time.
# Author : Abinash Mohanty
# Date : 05/24/2017
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# TODO : max heap datastructure implementation
class myMaxHeap(): 
	
	def __init__(self):
		"""
		Constructor
		"""	
		self.heap = []	

def max_heapify(arr,n, i):
	"""
	Routine to convery an un-ordered array into a max heap.
	list: arr = array to be sorted.
	int: l = length of array.
	int: i = is the index of the node to heapify
	"""
	largest = i	# Initialize largest as i
	l = 2*i + 1	# left node
	r = 2*i + 2	# right node
	
	if l < n and arr[l] > arr[largest]:
		largest = l
	if r < n and arr[r] > arr[largest]:
		largest = r

	if i != largest:
		arr[largest], arr[i] = arr[i], arr[largest]	# swap
		max_heapify(arr, n, largest)	# max-heapify the new subtree		
		
def heapSort(arr):
	"""
	1. creates a max heap 
	2. swaps heap head with last element
	3. reduces size of arr by 1 
	4. goes to step 1.
	"""		
	n = len(arr)
	# create a max heap for the array
	for i in range(n, -1 , -1):	
		max_heapify(arr,n,i)

	# swap max with the last element of array
	# decrement size of array and create a max-heap
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		max_heapify(arr, i, 0)

if __name__=='__main__':
	arr = [20, 30, 19, 2, 5, 38, 0, 44, 28, 10, 3, 4 ,5, 99]
	print arr
	heapSort(arr)
	print 'Doing Heapsort ... '
	print arr

