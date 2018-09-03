##################################
# Implementation of merge sort.  #
# Runtime: O(nlogn).             #
#                                #
# Written by Lewis Kim.          #
##################################

from math import floor

"""Return a sorted list given an unsorted list of integers LST."""
def mergesort(lst):
	if len(lst) == 1:
		return lst

	middle = floor(len(lst)/2)

	left = mergesort(lst[:middle])
	right = mergesort(lst[middle:])

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

