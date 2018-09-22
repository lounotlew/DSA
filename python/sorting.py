##########################################
# Implementation of sorting algorithms.  #
#                                        #
# Written by Lewis Kim.                  #
##########################################

from math import floor
import random
import time


### Insertion Sort. ###

"""Sort LST in place, which is an unsorted list.

   Runtime: Omega(n) best, O(n^2) worst."""
def insertionSort(lst):
	# start_time = time.time()
	pointer = 1

	while pointer < len(lst):
		if lst[pointer] < lst[pointer-1]:
			i = pointer
			j = pointer-1
			while lst[i] < lst[j] and j >= 0:
				lst[i], lst[j] = lst[j], lst[i]
				i -= 1
				j -= 1

		pointer += 1

	# print("Sort Time: %s seconds" % (time.time() - start_time))


### Merge Sort. ###

"""Return a sorted list given an unsorted list of integers LST.

   Runtime: O(nlogn) average & worst case."""
def mergeSort(lst):
	if len(lst) == 1:
		return lst

	middle = floor(len(lst)/2)

	left = mergeSort(lst[:middle])
	right = mergeSort(lst[middle:])

	sorted_lst = merge(left, right)

	return sorted_lst


"""Merge two sorted lists, LEFT and RIGHT."""
def merge(left, right):
	i = 0
	j = 0
	merged_lst = []

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			merged_lst.append(left[i])
			i += 1

		else:
			merged_lst.append(right[j])
			j += 1

	merged_lst += left[i:]
	merged_lst += right[j:]

	return merged_lst


### Quicksort. ###

"""sort LST in place, which is an unsorted list.

   Runtime: O(nlogn) average, O(n^2) worst-case."""
def quickSort(lst):
	return


### Heapsort. ###

""".

   Runtime: """
def heapSort(lst):
	return



### Tests. ###

def test_insertionSort():
	lst = [4, 1, 3, 12, 8, 7, 2, 4]
	insertionSort(lst)
	
	assert(lst == [1, 2, 3, 4, 4, 7, 8, 12])


def test_mergeSort():
	lst = [4, 1, 3, 12, 8, 7, 2, 4]
	new_lst = mergeSort(lst)
	
	assert(new_lst == [1, 2, 3, 4, 4, 7, 8, 12])

