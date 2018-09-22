############################################
# Functions to do with list manipulations. #
#                                          #
# Written by Lewis Kim.                    #
############################################


"""Given a sorted array of integers, NUMS, remove the duplicates in-place such that each
   element appears only once, and return NUMS.

   Not in-place solution: sorted({n for n in nums}, key=nums.index)"""
def remove_duplicates_inplace(nums):
   for i in range(len(nums)-1):
      j = i + 1
      while j < len(nums):
         if nums[i] == nums[j]:
            del nums[j]

         j += 1


"""Given a sorted array LST that has been rotated at some value, find the value of rotation.

   e.g. input: [4, 5, 6, 1, 2, 3]
        output: 1.

   Assumes there are no duplicate elements.

   Complexity: """
def find_rotated_pivot(lst):
   if len(lst) == 1:
      return lst[0]

   middle = int(len(lst)/2)

   if lst[middle] < lst[middle-1] and lst[middle] < lst[middle+1]:
      return lst[middle]

   if lst[middle] < lst[0]:
      return find_rotated_pivot(lst[0:middle])

   elif lst[middle] > lst[-1]:
      return find_rotated_pivot(lst[middle+1:])


"""Given an array of integers NUMS, return the sum of the max. contiguous subarray.

   e.g. input: [−2, 1, −3, 4, −1, 2, 1, −5, 4]
        output: 6 (subarray: [4, −1, 2, 1]).

   Complexity: """
def sum_max_contig_subarray(nums):
   return


"""Given 2 sorted arrays, ARRAY1 and ARRAY2 (size m, n respectively), find
   the k-th smallest element in the union of ARRAY1 and ARRAY2.

   Method: Use a pointer and iterate through first k smallest elements in ARRAY1 and ARRAY2.

   Complexity: O(k)"""
def kth_smallest_elem1(array1, array2):
   # We use a pointer.
   i, j = 0
   counter = 0
   kth_elem = 0

   while counter < k:
      if array1[i] < array2[j]:
         kth_elem = array1[i]
         i += 1


      counter += 1

   return


"""Given 2 sorted arrays, ARRAY1 and ARRAY2 ARRAY1 and ARRAY2 (size m, n respectively), find
   the k-th smallest element in the union of ARRAY1 and ARRAY2.

   Complexity: O(logk)"""
def kth_smallest_elem2(array1, array2):
   return


"""Given 2 sorted arrays, ARRAY1 and ARRAY2 (size m, n respectively), find the median
   of the 2 sorted arrays. Assume ARRAY1, ARRAY2 are non-empty.

   Complexity: O(log (m+n)).
   LeetCode: Hard."""
def median_of_two_sorted_arrays(array1, array2):

	return

