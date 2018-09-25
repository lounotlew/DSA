############################################
# Functions to do with list manipulations. #
#                                          #
# Written by Lewis Kim.                    #
############################################

import math
import statistics
from linkedlist import SinglyLinkedList


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


"""Given an unsorted array L, sort it so that all the odd numbers are in the first half, and
   all the even numbers are in the second half. The odd/even halves do not need to be sorted.

   e.g. input: [1, 2, 3, 4, 5, 1, 3, 2]
        output: [1, 3, 5, 1, 3, 2, 4, 2]."""
def odd_even_sort(L):

   """Even number checker."""
   def is_even(n):
      return n % 2 == 0

   """Odd number checker."""
   def is_odd(n):
      return n % 2 == 1


   i = 0
   j = len(L)-1

   while i <= j:
      # If i and j are odd/even respectively, i.e. they're in the right place:
      if is_odd(L[i]) and is_even(L[j]):
         i += 1
         j -= 1

      # If i is odd and j is odd, then j needs to be swapped.:
      elif is_odd(L[i]) and is_odd(L[j]):
         i += 1

      # If i is even and i is even, then i needs to be swapped:
      elif is_even(L[i]) and is_even(L[j]):
         j -= 1

      # If i is even and j is odd, then we swap both.:
      elif is_even(L[i]) and is_odd(L[j]):
         L[i], L[j] = L[j], L[i]
         i += 1
         j -= 1

   return L


"""Given 2 values A and B, and a linked list L, swap the first node with the value A and
   first node with value B. A and B may not be present in the linked list.
   Swap should be in place, and should involve links, not swapping data.

   e.g. input: 1 -> 2 -> 3 -> 4 -> 5, 1, 2
        output: 2 -> 1 -> 3 -> 4 -> 5

   Runtime: """
def swap_nodes(L, a, b):
   found_a = False
   found_b = False

   prev = None
   curr_node = L.head

   a_prev = None
   a_node = None
   b_prev = None
   b_node = None

   # Searching for A and B in 1 traversal to maintain O(n):
   while found_a == False or found_b == False:
      if curr_node == None:
         break

      if curr_node.value == a and curr_node.value == b:
         return

      elif curr_node.value == a and not found_a:
         found_a = True
         a_node = curr_node
         a_prev = prev

         prev = curr_node
         curr_node = curr_node.next

      elif curr_node.value == b and not found_b:
         found_b = True
         b_node = curr_node
         b_prev = prev

         prev = curr_node
         curr_node = curr_node.next

      else:
         prev = curr_node
         curr_node = curr_node.next

   if found_a == False or found_b == False:
      return

   # If A is the head
   if a_prev == None:
      L.head = b_node

   else:
      a_prev.next = b_node

   # If B is head
   if b_prev == None:
      L.head = a_node
  
   else:
      b_prev.next = a_node

   tmp = a_node.next
   a_node.next = b_node.next
   b_node.next = tmp


def test_swap_nodes():
   ll = SinglyLinkedList()
   ll.append(1)
   ll.append(2)
   ll.append(3)
   ll.append(4)
   ll.append(5)

   swap_nodes(ll, 2, 3)
   return ll.traverse()



"""Given an unsorted linked list, sort it so that all the odd numbers are in the first half, and
   all the even numbers are in the second half. The odd/even halves do not need to be sorted.

   e.g. input: 1->4->3->2->5
        output: 1->3->5->4->2."""
def odd_even_sort_ll(L):
   return


"""Given a linked list L, create an integer whose digits are the linked list in reverse.
   Assume there are no leading zeroes.

   e.g. input: 1->4->3->2->5
        output: 52341."""
def reverse_ll_integer(L):
   curr_node = L.head
   pwr = 0
   num = 0

   while curr_node != None:
      num += curr_node.value*(10**pwr)
      pwr += 1
      curr_node = curr_node.next

   return num


def test_reverse_ll_integer():
   ll = SinglyLinkedList()
   ll.append(1)
   ll.append(4)
   ll.append(3)
   ll.append(2)
   ll.append(5)

   assert(everse_ll_integer(ll) == 52341)


"""Given an unsorted array L, find the average of averages of contiguous subarrays of size N.
   Return -1 if there are no such subarrays.

   e.g. input: [1, 2, 3, 4, 5, 6, 7, 8, 9], 7
        output: [4, 5, 6]."""
def avg_of_avgs_subarray(L, n):
   if n > len(L):
      return []

   arr_sum = 0
   head = 0
   tail = 0
   results = []

   while tail < len(L):
      if tail < n:
         arr_sum += L[tail]
         tail += 1

      else:
         results.append(arr_sum/n)
         arr_sum = arr_sum - L[head] + L[tail]
         head += 1
         tail +=1

   results.append(arr_sum/n)

   return results


"""Given 2 sorted arrays, ARRAY1 and ARRAY2 (size m, n respectively), find
   the k-th smallest element in the union of ARRAY1 and ARRAY2.

   Method: Use a pointer and iterate through first k smallest elements in ARRAY1 and ARRAY2.

   Complexity: O(k)."""
def kth_smallest_elem1(array1, array2, k):
   # We use a pointer.


   return


"""Given 2 sorted arrays, ARRAY1 and ARRAY2 ARRAY1 and ARRAY2 (size m, n respectively), find
   the k-th smallest element in the union of ARRAY1 and ARRAY2.

   Complexity: O(logk)."""
def kth_smallest_elem2(array1, array2, k):
   return


"""Given 2 sorted arrays, ARRAY1 and ARRAY2 (size m, n respectively), find the median
   of the 2 sorted arrays. Assume ARRAY1, ARRAY2 are non-empty.

   Complexity: O(log (m+n))."""
def median_of_two_sorted_arrays(array1, array2):

	return

