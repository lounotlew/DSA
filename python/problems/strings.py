######################################################
# Functions for various string manipulation methods. #
#                                                    #
# Written by Lewis Kim.                              #
######################################################


"""Remove all duplicate characters from any arbitrary STRING.
The returned string must maintain its order (i.e. "aaabccdee" becomes "abcde").

Notes: You're ordering the the unordered items of {} with the character order (i.e. index)
of STRING."""
def remove_duplicate_chars(string):
	return "".join(sorted({c for c in list(string)}, key=string.index))


"""Reverse a string input, STRING.

   e.g. input: 'hello, world'
        output: 'dlrow ,olleh'"""
def reverse_string(string):
	# "easy way": return string[::-1]
	if len(string) == 1:
		return string

	return string[-1] + reverse_string(string[:-1])

	# Iteratively:
	# reversed_str = ""
	# i = len(string)-1
	# while i >= 0:
	# 	reversed_str += string[i]
	# 	i -= 1

	# return reversed_str


"""Given an input string STRING, reverse the string word by word.

   e.g. input: 'the sky is blue'
        output: 'blue is sky the'"""
def reverse_str_words(string):
	words = string.split(" ")

	# Without using built-in methods:
	reversed_input = words[len(words)-1]
	i = len(words) - 2
	while i >= 0:
		reversed_input += " " + words[i]
		i -= 1

	return reversed_input

	# Better way using built-in methods:
	# reversed_words = words[-1::-1]
	# output = ' '.join(reversed_words)

	# return output


"""Given a string STRING, return the longest palindromic substring in STRING.

   e.g. input: 'babad'
        output: 'bab'"""
def longest_palindrome_substring(string):
	return






