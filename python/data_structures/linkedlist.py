######################################################
# Implementation of a doubly linked list with nodes. #
#                                                    #
# Written by Lewis Kim.                              #
######################################################


# A Node class that makes up a single linked list.
class Node1:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next


# A Node class that makes up a double linked list.
class Node2:
	def __init__(self, value, prev = None, next = None):
		self.value = value
		self.prev = prev
		self.next = next


# A singly linked list.
class SingleLinkedList:

	"""."""
	def __init__(self):
		self.head = None


	"""Append a new node whose value is VALUE to this linked list."""
	def append(self, value):
		new node = Node1(value)

		if self.head == None:
			self.head = new_node

		else:
			self.tail.next = new_node


	"""Remove the first instance of the node whose vaue is VALUE from this linked list."""
	def remove(self, value):
		prev = None
		curr_node = self.head

		while curr_node != None:
			if curr_node.value == value:
				# If we're removing the head node:
				if prev == None:
					self.head = None
					return

				else:
					prev.next = curr_node.next
					return

			else:
				prev = curr_node
				curr_node = curr_node.next

		return


	"""Traverse this linked list forward from the head."""
	def traverse():
		values = []
		curr_node = self.head

		while curr_node != None:
			values.append(curr_node.value)
			curr_node = curr_node.next

		return values


# A doubly linked list.
class DoubleLinkedList:

	"""."""
	def __init__(self):
		self.head = None
		self.tail = None


	"""Append a new node whose value is VALUE to this instance of a linked list."""
	def append(self, value):
		new_node = Node2(value)

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
				# If the current node is the head node AND single node, i.e. previous is None:
				if curr_node.prev == None and curr_node.next == None:
					self.head = None
					self.tail = None
					#print("r1")
					return

				### Edge Cases ###

				# If we're removing the head node with a non-null next value:
				elif curr_node.prev == None and curr_node.next != None:
					curr_node.next.prev = curr_node.prev
					self.head = curr_node.next
					#print("r2")
					return

				# If we're removing a tail node with a non-null previous value:
				elif curr_node.prev != None and curr_node.next == None:
					curr_node.prev.next = curr_node.next
					self.tail = curr_node.prev
					#print("r2")
					return

				### End of Edge Cases ###

				# If we're removing every other type of node:
				else:
					curr_node.prev.next = curr_node.next
					curr_node.next.prev = curr_node.prev
					#print("r3")
					return

			else:
				curr_node = curr_node.next

		#print("rn")


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

	print("Test 1 Passed")


def test2():
	ll = LinkedList()
	ll.append(2)
	assert(ll.traverse_fw() == [2])

	ll.remove(2)
	assert(ll.traverse_fw() == [])

	print("Test 2 Passed")


def test3():
	ll = LinkedList()
	ll.append(2)
	assert(ll.traverse_fw() == [2])

	ll.append(3)
	assert(ll.traverse_fw() == [2, 3])

	ll.append(2)
	assert(ll.traverse_fw() == [2, 3, 2])

	ll.remove(3)
	assert(ll.traverse_fw() == [2, 2])

	print("Test 3 Passed")


def test4():
	ll = LinkedList()
	ll.append(2)
	assert(ll.traverse_fw() == [2])

	ll.append(3)
	assert(ll.traverse_fw() == [2, 3])

	ll.append(3)
	assert(ll.traverse_fw() == [2, 3, 3])

	ll.remove(2)
	assert(ll.traverse_fw() == [3, 3])

	print("Test 4 Passed")


def run_all_tests():
	test1()
	test2()
	test3()
	test4()

