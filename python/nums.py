##################################################
# Functions for various string numeric problems. #
#                                                #
# Written by Lewis Kim.                          #
##################################################


"""Given a list of N lists (where each list is a length of 2 containing
   cartesian coordinates, e.g. [2, 2]), return the maximum number of points
   that lie on the same line.

   e.g. input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        output: 4"""
def maxPoints(coords):
	return



"""Given a list of integers A, return the length of the shortest, non-empty
   contiguous subarray of A with sum at least K.
   Returns NONE if there is no such subarray.


   e.g. input: A = [2, -1, 2], K = 3
        output: 3"""
def shortestSubarray(A, k):
	return




"""Reverse the digits of a number. Assume the number does not end with a 0.

   e.g. input: 9801
        output: 1089"""
def reverse_digits(num):
  reversed_num = 0

  while num > 0:
    reversed_num *= 10
    reversed_num += num % 10
    num = num // 10

  return reversed_num

  # # Using str()/int():

  # num = str(num)
  # return int(num[::-1])


"""."""
def closest_palindrome(num):
  return






