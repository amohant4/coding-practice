# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Heap Data structure: Nearly complete binary tree.
# This implementation uses heap functions from python library
# An array can be visualized as an heap.
# for node i: left child is 2i+1 and right child is 2i+2
# Min Heap : Key of the element at any node is <= keys of its child nodes.
# Supported functions: 
# - getMin(): Returns the root element of the heap. Time complexity is O(1)
# - extractMin(): Removes the minimum element from Min Heap. Time Complexity of this Operation is O(Logn)
# - decreaseKey(): decreases value of key. Time complexity of this operation is O(Logn).
# - insert(): Inserting a new key takes O(Logn) time.
# - delete(): Deleting a key also takes O(Logn) time.
# Author : Abinash Mohanty
# Date : 05/24/2017
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from heapq import heappush, heappop, heapify

class MinHeap():
	
	def __init__(self):
		self.heap = []
	
	def parent(self, i):
		"""	
		return the index of the parent
		"""
		return (i-1)/2

	def insertKey(self, k):
		"""
		inserts a new key 'k'
		"""
		heappush(self.heap, k)

	def decreaseKey(self, i, new_value):
		"""
		Decrease value of key at index i. 
		It is assumed that the new key is smaller that heap[i]	
		"""
		self.heap[i] = new_value
		while( i != 0 and self.heap[self.parent(i)] > self.heap[i]):
			self.heap[i], self.heap[self.parent[i]] = \
				self.heap[self.parent[i]], self.heap[i]
	def extractMin(self):
		"""
		Method to remove min element from min heap
		"""	
		return heappop(self.heap)

	def deleteKey(self, i):
		"""
		This function deletes key at index i.
		First decrease key value at i to -inf
		Then extract min key. 	
		"""	
		self.decreaseKey(i, float("-inf"))
		self.extractMin()

	def getMin(self):
		"""
		returns the min element from the heap	
		"""
		return self.heap[0]			
