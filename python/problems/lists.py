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


"""Check for duplicates in an unsorted array ARRAY in O(1) space."""
def find_duplicates(array):
   return


"""Given a sorted array LST that has been rotated at some value, find the value of rotation.

   e.g. input: [4, 5, 6, 1, 2, 3]
        output: 1"""
def find_rotated_pivot(lst):
   return


"""Given 2 sorted arrays, ARRAY1 and ARRAY2 ARRAY1 and ARRAY2 (size m, n respectively), find
   the k-th smallest element in the union of ARRAY1 and ARRAY2.

   Method: Merge 2 lists, sort, and return kth element.

   Complexity: O(n+m)"""
def kth_smallest_two_sorted_arrays1(array1, array2):
   return


"""Given 2 sorted arrays, ARRAY1 and ARRAY2 ARRAY1 and ARRAY2 (size m, n respectively), find
   the k-th smallest element in the union of ARRAY1 and ARRAY2.

   Method: Use a pointer and iterate through first k smallest elements in ARRAY1 and ARRAY2.

   Complexity: O(k)"""
def kth_smallest_two_sorted_arrays2(array1, array2):
   return


"""Given 2 sorted arrays, ARRAY1 and ARRAY2 ARRAY1 and ARRAY2 (size m, n respectively), find
   the k-th smallest element in the union of ARRAY1 and ARRAY2.

   Complexity: O(logk)"""
def kth_smallest_two_sorted_arrays3(array1, array2):
   return


"""Given 2 sorted arrays, ARRAY1 and ARRAY2 (size m, n respectively), find the median
   of the 2 sorted arrays. Assume ARRAY1, ARRAY2 are non-empty.

   Complexity: O(log (m+n)).
   LeetCode: Hard."""
def median_of_two_sorted_arrays(array1, array2):

	return


def merged_median(list_of_arrays):
   return





