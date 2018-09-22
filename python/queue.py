##########################################
# Implementation of queues and stacks.   #
#                                        #
# Written by Lewis Kim.                  #
##########################################

from linkedlist import SinglyLinkedList


# LIFO Queue using a Singly Linked List.
# Tail treated as top of the stack.
class Stack:

	"""."""
	def __init__(self):
		self.data = SinglyLinkedList()


	"""Return True if this Stack is empty."""
	def is_empty(self):
		return self.data.head() == None


	"""Add VALUE to this Stack."""
	def add(self, value):
		self.data.append(value)


	"""Peek at the top value of this Stack, i.e. the tail of the linked list."""
	def peek(self):
		return self.data.tail.value


	"""Remove the top of this Stack and return it."""
	def pop(self):
		if self.data.head == None:
			return

		value = self.data.tail.value

		self.data.remove_tail()

		return value


	"""Return the size of this Stack."""
	def size(self):
		return self.data.length()


	"""Print the contents of this Stack, where the top element is the first element of a list."""
	def show(self):
		return self.data.traverse()[::-1]


# FIFO Queue.
class Queue:

	"""."""
	def __init__(self):
		self.data = SinglyLinkedList()


	"""Return True if this Queue is empty."""
	def is_empty(self):
		return self.data.head == None


	"""Add VALUE to this Queue."""
	def add(self, value):
		self.data.append(value)


	"""Peek at the top value of this Queue, i.e. the tail of the linked list."""
	def peek(self):
		return self.data.head.value


	"""Remove the top of this Queue and return it."""
	def pop(self):
		if self.data.head == None:
			return

		value = self.data.head.value

		self.data.remove_head()

		return value


	"""Return the size of this Queue."""
	def size(self):
		return self.data.length()


	"""Print the contents of this Queue, where the top element is the first element of a list."""
	def show(self):
		return self.data.traverse()


### Tests for Stack. ###

def test_stack1():
	s = Stack()

	s.add(1)
	s.add(2)
	s.add(3)

	assert(s.show() == [3, 2, 1])

	assert(s.pop() == 3)
	assert(s.show() == [2, 1])

	assert(s.peek() == 2)
	assert(s.show() == [2, 1])

	assert(s.pop() == 2)
	assert(s.show() == [1])

	assert(s.pop() == 1)
	assert(s.show() == [])

	assert(s.pop() == None)
	assert(s.show() == [])

	print("Test 1 Passed")


### Tests for Queue. ###

def test_queue1():
	s = Queue()

	s.add(1)
	s.add(2)
	s.add(3)

	assert(s.show() == [1, 2, 3])

	assert(s.pop() == 1)
	assert(s.show() == [2, 3])

	assert(s.peek() == 2)
	assert(s.show() == [2, 3])

	assert(s.pop() == 2)
	assert(s.show() == [3])

	assert(s.pop() == 3)
	assert(s.show() == [])

	assert(s.pop() == None)
	assert(s.show() == [])

	print("Test 1 Passed")

