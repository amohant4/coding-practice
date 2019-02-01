# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Merge sort algorithm
# Author : Abinash Mohanty
# Date : 05/24/2017
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def merge(arr, l, m, r):
	"""
	sub routine to merge two sorted arrays
	left arr = arr[l:m]
	right arr = arr[m+1, r]
	"""
	n1 = m - l + 1
	n2 = r - m 

	# create dummy arrays to store data
	L = [0]*n1
	R = [0]*n2
	
	# copy data to local arrays
	for i in range(0, n1):
		L[i] = arr[l+i]
	for j in range(0, n2):
		print '{} {} {}'.format(n2,m, m+1+j)	
		R[j] = arr[m+1+j]		
	# Merge the two local arrays
	i = 0
	j = 0
	k = l
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1					
		k += 1
	# Copy the remaining elements if L if any
	while i < n1:
		arr[k] = L[i]
		k += 1
		i += 1
	# copy the remaining elements of R if any
	while j < n2:
		arr[k] = R[j]
		k += 1
		j += 1


def mergeSort(arr, l , r):
	"""
	mergeSort routine, which successive divides the array into smaller
	sub arrays.
	"""
	if l < r:
		m = l + (r - l - 1)/2 
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)

if __name__ == '__main__':
	arr = [10, 30, 4, 38, 99, 20, 1002, 11, 45, 83, 901]
	print arr
	mergeSort(arr, 0, len(arr)-1)
	print 'Doing merge sort ...'
	print arr


