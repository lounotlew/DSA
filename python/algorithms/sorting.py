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
	if len(lst) <= 1:
		return

	pivot_index = random.choice(range(0, len(lst)))
	pivot = lst[pivot_index]

	indexFromLeft = 0
	indexFromRight = len(lst) - 1

	while #indexFromLeft < indexFromRight:
		if lst[indexFromLeft] <= pivot and lst[indexFromRight] >= pivot:
			indexFromLeft += 1
			indexFromRight -= 1

		elif lst[indexFromLeft] <= pivot and lst[indexFromRight] < pivot:
			indexFromLeft += 1

		elif lst[indexFromLeft] > pivot and lst[indexFromRight] < pivot:
			lst[indexFromLeft], lst[indexFromRight] = lst[indexFromRight], lst[indexFromLeft]
			indexFromLeft += 1
			indexFromRight -= 1

		elif lst[indexFromLeft] > pivot and lst[indexFromRight] >= pivot:
			indexFromRight -= 1

	#partition_index = min(indexFromLeft, indexFromRight)

	quickSort(lst[:partition_index])
	quickSort(lst[partition_index:])


### Heapsort. ###

""".

   Runtime: """
def heapSort(lst):
	return





### Tests. ###

def test_quicksort():
	lst = [4, 1, 3, 12, 8, 7, 2, 4]
	print(lst)
	quickSort(lst)
	print(lst)


