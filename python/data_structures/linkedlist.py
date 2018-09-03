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
		curr_node = self.head

		if curr_node == None:
			print("The list is currently empty.")
			return

		while curr_node != None:

			if curr_node.value == value:

				# Check if current node's previous node is None. If True, then this means the current node is the head node,
				# and we simply point the new head node to be current node's next node.
				if curr_node.prev == None:
					self.head = curr_node.next
					self.head.prev = None

					print("Successfully deleted " + str(value) + " from the list.1")
					return

				# Check if the current node's next node is None. Then, we're at a tail node, so simply point the new tail node
				# to be the current node's previous node, and point the new tail node's next node to be None.
				if curr_node.next == None:
					self.tail = curr_node.prev
					self.tail.next = None

					print("Successfully deleted " + str(value) + " from the list.2")
					return

				# Disconnect the previous node from this node, and point this node's next node as the previous node's next node.
				curr_node.prev.next = curr_node.next
				curr_node.next.prev = curr_node.prev

				print("Successfully deleted " + str(value) + " from the list.3")
				return

			else:
				curr_node = curr_node.next

		print(str(value) + " is not in the list.")
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


### Tests for LinkedList implementation. ###

def test1():
	ll = LinkedList()
	ll.append(2)
	ll.append(2)

	assert(ll.traverse_fw() == [2, 2])

	ll.remove(2)
	assert(ll.traverse_fw() == [2])

	ll.remove(2)
	assert(ll.traverse_fw() == [])

