######################################################
# Implementation of a doubly linked list with nodes. #
#                                                    #
# Written by Lewis Kim.                              #
######################################################


# A Node class that makes up a linked list.
class Node:
	def __init__(self, value, prev = None, next = None):
		self.value = value
		self.prev = prev
		self.next = next

	def __repr__(self):
		return f"Node(Value: {self.value}, Prev: {self.prev}, Next: {self.next})"


# A doubly linked list.
class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	"""Append a new node whose value is VALUE to this instance of a linked list."""
	def append(self, value):
		new_node = Node(value)

		# Check if the linked list is empty. If True, set this linked list's head and tail as the node to be appended.
		if self.head == None:
			self.head = new_node
			self.tail = new_node
		
		# Set the new node's previous node to this linked list's tail and set this linked list's tail's next node to the new node
		# so that the new node becomes the new tail, and this linked list's tail becomes the 2nd last element.
		# Finally, point this linked list's tail to the new node.
		else:
			new_node.prev = self.tail
			self.tail.next = new_node
			self.tail = new_node

	"""Remove the first Node whose value is VALUE from this linked list."""
	def remove(self, value):
		return

	"""Remove all Nodes whose value is VALUE from this linked list."""
	def remove_all(self, value):
		return

	"""Traverse through this linked list forward (rightward), from head to tail. Returns all values in a list.""" 
	def traverse_fw(self):
		values = []
		curr_node = self.head

		if self.head == None:
			return values

		while curr_node != None:
			values.append(curr_node.value)
			curr_node = curr_node.next

		return values

	"""Traverse through this linked list backwards (leftward), from tail to head. Returns all values in a list."""
	def traverse_bw(self):
		values = []
		curr_node = self.tail

		if self.tail == None:
			return values

		while curr_node != None:
			values.append(curr_node.value)
			curr_node = curr_node.prev

		return values

