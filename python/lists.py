############################################
# Functions to do with list manipulations. #
#                                          #
# Written by Lewis Kim.                    #
############################################

import math


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
def max_contig_subarray_sum(nums):
   max_so_far = 0

   for i in range(len(nums)):
      max_ending_at_i = max(nums[i], max_ending_at_i + nums[i])
      max_so_far = max(max_so_far, max_so_far+nums[i])

   return max_so_far


"""Given a sorted array of the form [1, 2, 3, .... n], find the value that's been skipped over.

   e.g. input: [1, 2, 3, 5, 6]
        output: 4
   Complexity: O(n log n)."""
def missing_number(L):
   m = int(len(L)/2)

   if len(L) == 2:
      return L[0]+1

   elif L[m] - L[m-1] > 1:
      return L[m-1]+1

   elif L[m+1] - L[m] > 1:
      return L[m]+1

   elif L[m] - L[0] != len(L[:m+1])-1:
      return missing_number(L[:m])

   else:
      return missing_number(L[m+1:])


"""Given a sorted array L, return the index of the first number that is strictly smaller than N.
   Assume no duplicates are in the list.

   e.g. input: [1, 2, 3, 5, 8, 12], 5
        output: 2 (index of 3)."""
def first_strictly_smaller(L, n):
   start = 0
   end = len(L) - 1

   index = -1

   while start <= end:
      m = int((end + start) / 2)

      if L[m] >= n:
         end = m-1

      else:
         index = m
         start = m + 1

   return index


"""Given a sorted array L, return the index of the first number that is strictly larger than N.
   Assume no duplicates are in the list.

   e.g. input: [1, 2, 3, 5, 8, 12], 5
        output: 4 (index of 8)."""
def first_strictly_greater(L, n):
   start = 0
   end = len(L) - 1

   index = -1

   while start <= end:
      m = int((end + start) / 2)

      if L[m] > n:
         index = m
         end = m-1

      else:
         start = m+1

   return index


"""Given a sorted array L, find the index of the first occurence of a number N.

   e.g. input: [2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5
        output: 2."""
def first_occurence_n(L, n):
   start = 0
   end = len(L) - 1

   index = -1

   while start <= end:
      m = int((end + start) / 2)

      if L[m] >= n:
         if L[m] == n:
            index = m

         end = m-1

      else: # if L[m] < n
         start = m+1

   return index



"""Given a sorted array L, find the index of the last occurence of a number N.

   e.g. input: [2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5
        output: 2."""
def last_occurence_n(L, n):
   return


"""Given 2 sorted arrays, ARRAY1 and ARRAY2 (size m, n respectively), find
   the k-th smallest element in the union of ARRAY1 and ARRAY2.

   Method: Use a pointer and iterate through first k smallest elements in ARRAY1 and ARRAY2.

   Complexity: O(k)."""
def kth_smallest_elem1(array1, array2):
   # We use a pointer.


   return


"""Given 2 sorted arrays, ARRAY1 and ARRAY2 ARRAY1 and ARRAY2 (size m, n respectively), find
   the k-th smallest element in the union of ARRAY1 and ARRAY2.

   Complexity: O(logk)."""
def kth_smallest_elem2(array1, array2):
   return


"""Given 2 sorted arrays, ARRAY1 and ARRAY2 (size m, n respectively), find the median
   of the 2 sorted arrays. Assume ARRAY1, ARRAY2 are non-empty.

   Complexity: O(log (m+n))."""
def median_of_two_sorted_arrays(array1, array2):

	return

