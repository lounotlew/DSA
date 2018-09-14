##########################################
# Implementation of min and max heaps.   #
#                                        #
# Written by Lewis Kim.                  #
##########################################


# MinHeap using array implementation.
class MinHeap:

	""".""" 
	def __init__(self):
		self.data = []


	"""Return the array containing this instance of MinHeap."""
	def show(self):
		return self.data


	"""Add VALUE to the array, and bubble up to maintain MinHeap structure."""
	def add(self, value):
		if len(self.data) == 0:
			self.data.append(value)

		else:
			self.data.append(value)
			self.bubbleUp()


	"""Pop the first element of this MinHeap."""
	def pop(self):
		if len(self.data) == 0:
			return

		value = self.data[0]
		self.data[0] = self.data[-1]
		del self.data[-1]

		self.bubbleDown()

		return value


	"""Return the first element of self.data."""
	def peek(self):
		if len(self.data) == 0:
			return

		return self.data[0]


	### Bubble methods. ###

	"""Bubble up the last element of self.data."""
	def bubbleUp(self):
		index = len(self.data) - 1

		while self.has_parent(index) and self.get_parent(index) > self.data[index]:
			self.swap(self.get_parent_index(index), index)
			index = self.get_parent_index(index)


	"""Bubble down the first element of self.data."""
	def bubbleDown(self):
		index = 0

		while self.has_left_child(index):
			smallerChildIndex = self.get_left_child_index(index)
			
			if self.has_right_child(index) and self.get_right_child(index) < self.get_left_child(index):
				smallerChildIndex = self.get_right_child_index(index)

			if self.data[index] < self.data[smallerChildIndex]:
				return

			else:
				self.swap(index, smallerChildIndex)

			index = smallerChildIndex



	### Helpers. ###

	"""Return the value of the left child of the node at index INDEX."""
	def get_left_child(self, index):
		return self.data[index*2 + 1]


	"""Return the value of the right child of the node at index INDEX."""
	def get_right_child(self, index):
		return self.data[index*2 + 2]


	"""Return the value of the parent of the node at index INDEX."""
	def get_parent(self, index):
		return self.data[self.get_parent_index(index)]


	"""Return the left child index of the node at INDEX."""
	def get_left_child_index(self, index):
		return index*2 + 1


	"""Return the right child index of the node at INDEX."""
	def get_right_child_index(self, index):
		return index*2 + 2


	"""Return the index of the parent node of the child at index INDEX."""
	def get_parent_index(self, index):
		return (index-1)//2


	"""Return True if the node at index INDEX has a left child."""
	def has_left_child(self, index):
		return index*2 + 1 < len(self.data)


	"""Return True if the node at index INDEX has a right child."""
	def has_right_child(self, index):
		return index*2 + 2 < len(self.data)


	"""Return True if the node at index INDEX has a parent index."""
	def has_parent(self, index):
		return self.get_parent_index(index) >= 0


	"""Swap 2 values at index I and index J."""
	def swap(self, i, j):
		temp = self.data[i]
		self.data[i] = self.data[j]
		self.data[j] = temp





# #
# class MaxHeap:
