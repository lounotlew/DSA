##########################################
# Implementation of sorting algorithms.  #
# Runtime: O(nlogn).                     #
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
	start_time = time.time()

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
	pivot_index = random.choice(range(0, len(lst)))
	pivot = lst[pivot_index]

	itemFromLeft = 0
	itemFromRight = len(lst) - 1

	if len(lst) == 1:
		return

	while itemFromLeft < itemFromRight:
		if lst[itemFromLeft] < pivot and lst[itemFromRight] < pivot:
			itemFromLeft += 1

		if lst[itemFromLeft] > pivot and lst[itemFromRight] > pivot:
			itemFromRight -= 1

		if lst[itemFromLeft] > pivot and lst[itemFromRight] < pivot:
			lst[itemFromLeft], lst[itemFromRight] = lst[itemFromRight], lst[itemFromLeft]
			itemFromLeft += 1
			itemFromRight -= 1

	quicksort(lst[:pivot_index])
	quicksort(lst[pivot_index+1:])



